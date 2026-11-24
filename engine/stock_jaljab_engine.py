# -*- coding: utf-8 -*-
"""올.주.선.이 3단 레이아웃 칠판 쇼츠 엔진 (주식·선물옵션 채널 전용)

- 상단 0~540px 흰 배경: 1줄 굵은 검정 '올바른 주식·선물 이해하기' + 2줄 네이비 박스 '올.주.선.이 · <주제>'
- 중단 540~1400px: 칠판 아트 1080x860 좌우 꽉 차게 + 하단 중앙 검정 외곽선 흰 한 줄 자막
- 하단 1400~1920px 흰 배경: y=1422 작은 회색 안내문, 아래는 유튜브 UI 여백
- 영상 시작 0.0~2.0초에만 '구독·알림·좋아요는 힘이 됩니다' 배지 오버레이
- 1080x1920 25fps, 실명 없음, 투자 면책 문구는 하단 안내문으로 대체
"""

import asyncio
import os
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

try:
    import imageio_ffmpeg

    FFMPEG_PATH = imageio_ffmpeg.get_ffmpeg_exe()
except Exception:
    FFMPEG_PATH = "ffmpeg"

BASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR.parent
FONT_BOLD = os.environ.get("STOCK_FONT_BOLD", str(REPO_ROOT / "fonts" / "NanumGothic-Bold.ttf"))

# ---- 올.주.선.이 규격 ----
TOP_LINE = "올바른 주식·선물 이해하기"
BRAND = "올.주.선.이"
FOOTER = "올.주.선.이 · 투자 참고용 정보 정리"
POINT = (30, 58, 138)            # #1E3A8A 네이비
TEXT_DARK = (20, 20, 20)
FOOTER_GRAY = (105, 105, 105)
TOP_BAND = (0, 540)
VIDEO_BAND = (540, 1400)
FOOTER_Y = 1422
CAPTION_FILL = (255, 255, 255)
CAPTION_OUTLINE = (10, 10, 10)

# ---- 첫 2초 구독 배지 ----
BADGE_TEXT = "구독·알림·좋아요는 힘이 됩니다"
BADGE_TOP = 565
BADGE_FONT = 36
BADGE_PAD_X = 34
BADGE_PAD_Y = 15
BADGE_FILL = (238, 108, 30, 235)
BADGE_EDGE = (255, 255, 255, 215)
BADGE_WINDOW = (0.0, 2.0)
BADGE_FADE_OUT = 0.45

DISCLAIMER = "본 영상은 투자 권유가 아닌 시장 기록 및 정보 정리입니다."


def _fit_font_width(text, max_w, start_size, min_size=24):
    size = start_size
    while size > min_size:
        font = ImageFont.truetype(FONT_BOLD, size)
        bbox = font.getbbox(text)
        if bbox[2] - bbox[0] <= max_w:
            return font, bbox
        size -= 2
    font = ImageFont.truetype(FONT_BOLD, size)
    return font, font.getbbox(text)


def _outlined_text(draw, center, text, font, fill=CAPTION_FILL, outline=CAPTION_OUTLINE, width=4):
    x, y = center
    for dx in range(-width, width + 1):
        for dy in range(-width, width + 1):
            if dx * dx + dy * dy <= width * width + 2 and (dx or dy):
                draw.text((x + dx, y + dy), text, font=font, fill=outline, anchor="mm")
    draw.text((x, y), text, font=font, fill=fill, anchor="mm")


def _cover_crop(src: Image.Image, target_w: int, target_h: int, bias: float = 0.5) -> Image.Image:
    ratio = src.width / src.height
    target = target_w / target_h
    if ratio > target:
        new_h = target_h
        new_w = int(round(new_h * ratio))
    else:
        new_w = target_w
        new_h = int(round(new_w / ratio))
    resized = src.resize((new_w, new_h), Image.Resampling.LANCZOS)
    extra_x, extra_y = new_w - target_w, new_h - target_h
    cx = int(round(extra_x * 0.5))
    cy = int(round(extra_y * bias))
    return resized.crop((cx, cy, cx + target_w, cy + target_h))


def subscribe_badge_geometry(width: int = 1080):
    font, bb = _fit_font_width(BADGE_TEXT, width - 120, BADGE_FONT, 26)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    box_w = tw + BADGE_PAD_X * 2
    box_h = th + BADGE_PAD_Y * 2
    x1 = (width - box_w) // 2
    y1 = BADGE_TOP
    return font, (x1, y1, x1 + box_w, y1 + box_h), th


def draw_subscribe_badge(layer: Image.Image, width: int = 1080):
    font, box, _ = subscribe_badge_geometry(width)
    x1, y1, x2, y2 = box
    d = ImageDraw.Draw(layer)
    radius = (y2 - y1) // 2
    d.rounded_rectangle([x1 + 3, y1 + 6, x2 + 3, y2 + 6], radius=radius, fill=(0, 0, 0, 95))
    d.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=BADGE_FILL, outline=BADGE_EDGE, width=3)
    d.text((width // 2, (y1 + y2) // 2 - 1), BADGE_TEXT, font=font, fill=(255, 255, 255, 255),
           anchor="mm", stroke_width=2, stroke_fill=(255, 255, 255, 255))


def create_subscribe_badge_png(out_png: str, width: int = 1080, height: int = 1920) -> str:
    layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw_subscribe_badge(layer, width)
    layer.save(out_png)
    return out_png


def create_scene_frame(*, chalk_img_path: str, out_img: str, topic: str = "", caption: str = "",
                       top_line: str = TOP_LINE, footer: str = FOOTER, width: int = 1080,
                       height: int = 1920, crop_bias: float = 0.5, show_badge: bool = False):
    img = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # 1. 상단 훅 (y=244 중심)
    top_line = (top_line or TOP_LINE).strip()
    f_top, bb = _fit_font_width(top_line, width - 100, 62, 38)
    top_h = bb[3] - bb[1]
    line1_cy = 244 + top_h // 2
    draw.text((width // 2, line1_cy), top_line, font=f_top, fill=TEXT_DARK,
              anchor="mm", stroke_width=2, stroke_fill=TEXT_DARK)

    # 2. 네이비 주제 박스
    box_line = BRAND if not topic else f"{BRAND} · {topic}"
    box_line = box_line.strip()
    f_box, bb2 = _fit_font_width(box_line, width - 140, 64, 34)
    tw2, th2 = bb2[2] - bb2[0], bb2[3] - bb2[1]
    pad_x, pad_y = 32, 16
    box_y1 = max(line1_cy + top_h // 2 + 24, 366)
    box_y2 = box_y1 + th2 + pad_y * 2 + 12
    if box_y2 > TOP_BAND[1] - 14:
        box_y1 = TOP_BAND[1] - 14 - (box_y2 - box_y1)
        box_y2 = TOP_BAND[1] - 14
    box_x1 = (width - tw2) // 2 - pad_x
    box_x2 = (width + tw2) // 2 + pad_x
    draw.rectangle([box_x1, box_y1, box_x2, box_y2], fill=POINT)
    draw.text((width // 2, (box_y1 + box_y2) // 2), box_line, font=f_box, fill=(255, 255, 255),
              anchor="mm", stroke_width=2, stroke_fill=(255, 255, 255))

    # 3. 중단 칠판 아트 1080x860
    vid_y1, vid_y2 = VIDEO_BAND
    vid_h = vid_y2 - vid_y1
    if chalk_img_path and os.path.exists(chalk_img_path):
        art = _cover_crop(Image.open(chalk_img_path).convert("RGB"), width, vid_h, bias=crop_bias)
        img.paste(art, (0, vid_y1))
    else:
        draw.rectangle([0, vid_y1, width, vid_y2], fill=(22, 38, 30))

    # 4. 한 줄 자막 (중단 하단 중앙)
    cap = (caption or "").strip()
    if cap:
        f_cap, bb_cap = _fit_font_width(cap, width - 80, 52, 30)
        cap_w = bb_cap[2] - bb_cap[0]
        if cap_w > width - 80 and " · " in cap:
            head, tail = cap.split(" · ", 1)
            f_cap = ImageFont.truetype(FONT_BOLD, 42)
            _outlined_text(draw, (width // 2, vid_y1 + vid_h - 122), head, f_cap, width=4)
            _outlined_text(draw, (width // 2, vid_y1 + vid_h - 58), tail, f_cap, width=4)
        else:
            _outlined_text(draw, (width // 2, vid_y1 + vid_h - 92), cap, f_cap, width=4)

    # 5. 하단 안내문
    if footer:
        f_foot, bb_f = _fit_font_width(footer, width - 80, 28, 22)
        draw.text(((width - (bb_f[2] - bb_f[0])) // 2, FOOTER_Y), footer, font=f_foot, fill=FOOTER_GRAY)

    # 6. 배지 (정지 프레임 확인용)
    if show_badge:
        layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw_subscribe_badge(layer, width)
        img.paste(layer, (0, 0), layer)

    img.save(out_img, quality=95)
    return out_img


def create_direction_frame(*, out_img: str, topic: str = "오늘과 내일의 방향",
                           today_label: str = "중간하방", tomorrow_label: str = "약간 상방 또는 횡보",
                           today_arrow: str = "▼", tomorrow_arrow: str = "▲",
                           accuracy_text: str = "11/23~ 집계 시작",
                           top_line: str = TOP_LINE, footer: str = FOOTER,
                           width: int = 1080, height: int = 1920) -> str:
    """마지막 방향성 컷: 오늘의 방향 / 내일의 예상 + 우측 상단 누적 적중률 시작 표시"""
    create_scene_frame(chalk_img_path="", out_img=out_img, topic=topic, caption="",
                       top_line=top_line, footer=footer, width=width, height=height)
    img = Image.open(out_img).convert("RGB")
    d = ImageDraw.Draw(img)
    vid_y1, vid_y2 = VIDEO_BAND

    # 우측 상단 누적 집계 배지
    f_b, bb_b = _fit_font_width(accuracy_text, width - 260, 34, 22)
    tw_b, th_b = bb_b[2] - bb_b[0], bb_b[3] - bb_b[1]
    pad_x, pad_y = 20, 10
    bx2 = width - 36
    bx1 = bx2 - tw_b - pad_x * 2
    by1 = vid_y1 + 26
    by2 = by1 + th_b + pad_y * 2
    d.rounded_rectangle([bx1, by1, bx2, by2], radius=(by2 - by1) // 2, fill=(245, 245, 245), outline=(120, 120, 120), width=2)
    d.text(((bx1 + bx2) // 2, (by1 + by2) // 2 - 1), accuracy_text, font=f_b, fill=(30, 30, 30), anchor="mm")

    # 오늘의 방향
    f_lab, bb_lab = _fit_font_width("오늘의 방향", width - 160, 42, 30)
    d.text((width // 2, vid_y1 + 150), "오늘의 방향", font=f_lab, fill=(190, 190, 190), anchor="mm")
    today_text = f"{today_arrow} {today_label}"
    f_t, bb_t = _fit_font_width(today_text, width - 120, 82, 44)
    d.text((width // 2, vid_y1 + 258), today_text, font=f_t, fill=(255, 138, 128), anchor="mm")

    # 구분선
    d.line([(120, vid_y1 + 360), (width - 120, vid_y1 + 360)], fill=(120, 140, 125), width=3)

    # 내일의 예상
    d.text((width // 2, vid_y1 + 470), "내일의 예상", font=f_lab, fill=(190, 190, 190), anchor="mm")
    tomorrow_text = f"{tomorrow_arrow} {tomorrow_label}"
    f_m, bb_m = _fit_font_width(tomorrow_text, width - 100, 70, 38)
    d.text((width // 2, vid_y1 + 578), tomorrow_text, font=f_m, fill=(255, 235, 140), anchor="mm")

    # 하단 보조 문구
    f_s, bb_s = _fit_font_width("방향은 참고 기록이며 투자 판단의 근거가 아닙니다", width - 120, 30, 22)
    d.text((width // 2, vid_y1 + 710), "방향은 참고 기록이며 투자 판단의 근거가 아닙니다", font=f_s, fill=(165, 165, 165), anchor="mm")
    img.save(out_img, quality=95)
    return out_img


async def _tts(text: str, out_mp3: str, voice: str = "ko-KR-SunHiNeural", rate: str = "+5%"):
    import edge_tts
    await edge_tts.Communicate(text, voice, rate=rate).save(out_mp3)


def get_audio_duration(path: str) -> float:
    p = subprocess.run([FFMPEG_PATH, "-i", path], capture_output=True, text=True)
    for line in p.stderr.split("\n"):
        if "Duration:" in line:
            h, m, s = line.split("Duration:")[1].split(",")[0].strip().split(":")
            return float(h) * 3600 + float(m) * 60 + float(s)
    return 3.0


def render_scene(frame: str, audio: str, out_mp4: str, duration: float, badge_png: str = None, fps: int = 25):
    if badge_png and os.path.exists(badge_png):
        start, end = BADGE_WINDOW
        end = min(end, max(duration, 0.1))
        fade_start = max(start, end - BADGE_FADE_OUT)
        fade_len = max(end - fade_start, 0.05)
        graph = (
            f"[1:v]format=rgba,fade=t=out:st={fade_start:.2f}:d={fade_len:.2f}:alpha=1[badge];"
            f"[0:v][badge]overlay=0:0:enable='between(t,{start:.2f},{end:.2f})',fps={fps}[v]"
        )
        cmd = [FFMPEG_PATH, "-y", "-loop", "1", "-i", frame, "-loop", "1", "-i", badge_png, "-i", audio,
               "-filter_complex", graph, "-map", "[v]", "-map", "2:a",
               "-c:v", "libx264", "-tune", "stillimage", "-preset", "veryfast", "-threads", "1",
               "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-pix_fmt", "yuv420p",
               "-t", f"{duration + 0.3:.2f}", "-shortest", out_mp4]
    else:
        cmd = [FFMPEG_PATH, "-y", "-loop", "1", "-i", frame, "-i", audio,
               "-c:v", "libx264", "-tune", "stillimage", "-preset", "veryfast", "-threads", "1",
               "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-pix_fmt", "yuv420p",
               "-t", f"{duration + 0.3:.2f}", "-shortest", out_mp4]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)


def render_shorts(scenes: list, output_mp4: str, temp_dir: str = "/tmp/stock_jaljab", fps: int = 25,
                  top_line: str = TOP_LINE, footer: str = FOOTER, subscribe_badge: bool = True):
    os.makedirs(temp_dir, exist_ok=True)
    parts, total = [], 0.0
    timings = []
    print(f"[올.주.선.이 엔진] {len(scenes)}씬 렌더링 시작")
    for idx, sc in enumerate(scenes, 1):
        audio = os.path.join(temp_dir, f"audio_{idx}.mp3")
        frame = os.path.join(temp_dir, f"frame_{idx}.jpg")
        part = os.path.join(temp_dir, f"scene_{idx}.mp4")
        asyncio.run(_tts(sc["voice"], audio))
        dur = get_audio_duration(audio)
        total += dur + 0.3
        if sc.get("type") == "direction":
            create_direction_frame(out_img=frame, topic=sc.get("topic", "오늘과 내일의 방향"),
                                   today_label=sc.get("today_label", "중간하방"),
                                   tomorrow_label=sc.get("tomorrow_label", "약간 상방 또는 횡보"),
                                   today_arrow=sc.get("today_arrow", "▼"),
                                   tomorrow_arrow=sc.get("tomorrow_arrow", "▲"),
                                   accuracy_text=sc.get("accuracy_text", "11/23~ 집계 시작"),
                                   top_line=sc.get("top_line") or top_line, footer=sc.get("footer") or footer)
        else:
            create_scene_frame(chalk_img_path=sc.get("chalk_img", ""), out_img=frame,
                               topic=sc.get("topic", ""), caption=sc.get("caption", ""),
                               top_line=sc.get("top_line") or top_line, footer=sc.get("footer") or footer,
                               crop_bias=sc.get("crop_bias", 0.5))
        badge = None
        if subscribe_badge and idx == 1:
            badge = create_subscribe_badge_png(os.path.join(temp_dir, "badge.png"))
        render_scene(frame, audio, part, dur, badge_png=badge, fps=fps)
        parts.append(part)
        scene_start = total - (dur + 0.3)
        timings.append({"scene": idx, "topic": sc.get("topic", ""), "start": round(scene_start, 2),
                        "end": round(total, 2), "seconds": round(dur + 0.3, 2)})
        print(f"  - 씬 {idx}/{len(scenes)} {dur:.1f}초 {sc.get('topic', '')}")
        hold = float(sc.get("hold") or 0)
        if hold > 0:
            silent = os.path.join(temp_dir, f"silence_{idx}.mp3")
            subprocess.run([FFMPEG_PATH, "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
                            "-t", f"{hold:.2f}", silent], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            hpart = os.path.join(temp_dir, f"scene_{idx}_hold.mp4")
            render_scene(frame, silent, hpart, hold, badge_png=None, fps=fps)
            parts.append(hpart)
            timings[-1]["end"] = round(total + hold, 2)
            timings[-1]["hold"] = round(hold, 2)
            total += hold
            print(f"    · 방향 컷 {hold:.1f}초 정지 유지")

    concat = os.path.join(temp_dir, "concat.txt")
    with open(concat, "w") as f:
        for p in parts:
            f.write(f"file '{p}'\n")
    raw = os.path.join(temp_dir, "concat_raw.mp4")
    subprocess.run([FFMPEG_PATH, "-y", "-f", "concat", "-safe", "0", "-i", concat, "-c", "copy", raw],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    subprocess.run([FFMPEG_PATH, "-y", "-i", raw, "-r", str(fps), "-fps_mode", "cfr",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
                    "-colorspace", "bt709", "-c:a", "aac", "-b:a", "192k", "-ar", "44100",
                    "-movflags", "+faststart", output_mp4],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    print(f"✅ 완성 {output_mp4} (약 {total:.1f}초)")
    return timings
