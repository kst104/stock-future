#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-24 (화) 외국인 수급 쇼츠 생성기 (7회차 · 올.주.선.이 3단 레이아웃)
- 5씬 + 마지막 방향성 컷(오늘의 방향 ▲ 강위 / 내일의 예상 ▲ 강위, 우측 상단 11/23~ 집계 대상 없음)
- 실행: STOCK_SHORTS_OUTPUT=/workspace/downloads python scripts/generate_stock_1124_foreign_flow_shorts.py
"""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR.parent
sys.path.insert(0, str(REPO_ROOT))

from engine.stock_jaljab_engine import render_shorts, FFMPEG_PATH, FOOTER, TOP_LINE

DOWNLOADS = Path(os.environ.get("STOCK_SHORTS_OUTPUT", str(REPO_ROOT / "output")))
DOWNLOADS.mkdir(parents=True, exist_ok=True)
ART = Path(os.environ.get("STOCK_CHALK_ART_DIR", str(REPO_ROOT / "assets" / "chalkboard" / "stock1124")))
ARCHIVE = REPO_ROOT / "content" / "2026-11-24" / "04_shorts_foreign_flow" / "stock_chalkboard"

VIDEO = {
    "id": "Stock2_1124",
    "title": "11/24 외국인 수급 — 마지막 한 시간에 선물 5,281계약을 덜어냈다",
    "out": DOWNLOADS / "Stock2_1124_외국인_현선물옵션_수급_칠판드로잉_쇼츠.mp4",
    "scenes": [
        {
            "topic": "외국인 vs 기관",
            "caption": "선물 외국인 +3,604 · 기관 -3,786계약",
            "chalk_img": str(ART / "v2_scene1_tug.png"),
            "voice": "이십사일 선물 시장은 외국인과 기관의 정면 대결. 외국인 삼천육백사 계약 매수, 기관 삼천칠백팔십육 계약 매도입니다.",
        },
        {
            "topic": "미결제 +646계약",
            "caption": "173,213계약 · 7% 상승에 증가는 적다",
            "chalk_img": str(ART / "v2_scene2_oi_stack.png"),
            "voice": "미결제는 십칠만 삼천이백십삼 계약. 전일보다 육백사십육 계약만 늘었습니다. 칠 퍼센트 오른 날치고 적습니다.",
        },
        {
            "topic": "누적 +3,604 · 막판 -5,281",
            "caption": "당일 누적 +3,604 · 막판 1시간 -5,281",
            "chalk_img": str(ART / "v2_scene3_last_hour.png"),
            "voice": "외국인은 열네 시 사십사 분 구천삼십오 계약까지 쌓았다가 종가 삼천육백사 계약. 마지막 한 시간에만 오천이백팔십일 계약을 팔았습니다. 누적은 매수, 막판은 매도로 따로 봐야 합니다.",
        },
        {
            "topic": "콜 +4,135 · 풋 +1,289",
            "caption": "P/C Ratio 0.79 · 콜 우세",
            "chalk_img": str(ART / "v2_scene4_options.png"),
            "voice": "옵션은 콜 사천백삼십오 계약, 풋 천이백팔십구 계약 매수. 콜 우세, 피씨 비율 영 점 칠구입니다.",
        },
        {
            "topic": "감마 플립 770.83",
            "caption": "순감마 +91억 · 종가는 플립 위",
            "chalk_img": str(ART / "v2_scene5_gamma.png"),
            "voice": "감마는 플러스로 돌아섰고 플립은 칠백칠십 점 팔삼. 종가 칠백칠십팔 점 육팔은 플립 위입니다.",
        },
        {
            "type": "direction",
            "topic": "오늘·내일 방향",
            "today_label": "강위",
            "tomorrow_label": "강위",
            "today_arrow": "▲",
            "tomorrow_arrow": "▲",
            "accuracy_text": "11/23~ 집계 대상 없음",
            "hold": 2.0,
            "voice": "오늘도 내일도 강한 상방으로 봅니다. 장 막판 선물 매도가 이어지는지만 확인하면 됩니다.",
        },
    ],
}


def ffprobe_meta(path: Path) -> dict:
    import re as _re
    p = subprocess.run([FFMPEG_PATH, "-i", str(path)], capture_output=True, text=True)
    info = {"duration": 0.0, "size": path.stat().st_size, "streams": []}
    for line in p.stderr.split("\n"):
        if "Duration:" in line:
            h, m, s = line.split("Duration:")[1].split(",")[0].strip().split(":")
            info["duration"] = round(float(h) * 3600 + float(m) * 60 + float(s), 2)
        if "Stream" in line and "Video:" in line:
            wh = _re.search(r"(\d{2,5})x(\d{2,5})", line)
            fp = _re.search(r"([\d.]+)\s*fps", line)
            info["streams"].append({"type": "video", "w": int(wh.group(1)) if wh else None,
                                    "h": int(wh.group(2)) if wh else None, "fps": fp.group(1) if fp else None})
        if "Stream" in line and "Audio:" in line:
            info["streams"].append({"type": "audio"})
    return info


def _show(p: Path) -> str:
    try:
        return str(p.resolve().relative_to(Path("/workspace")))
    except Exception:
        try:
            return str(p.resolve().relative_to(REPO_ROOT))
        except Exception:
            return str(p)


def write_script(video: dict):
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    chars = sum(len(s["voice"]) for s in video["scenes"])
    lines = [
        f"# {video['title']} — 유튜브 쇼츠 대본 (올.주.선.이 · 7회차)",
        "",
        f"- 상단 훅: {TOP_LINE} / 네이비 박스: 올.주.선.이 · <주제>",
        f"- 규격: 1080x1920 세로형 9:16, 25fps, 3단 레이아웃(상단 흰색·중단 칠판 1080x860·하단 흰색), {len(video['scenes'])}개 씬",
        "- 음성: Edge-TTS ko-KR-SunHiNeural, 속도 +5%",
        f"- 대본 분량: {chars}자",
        "- 시작 0.0~2.0초: '구독·알림·좋아요는 힘이 됩니다' 배지 오버레이",
        "- 마지막 컷: 오늘의 방향 ▲ 강위 / 내일의 예상 ▲ 강위 + 우측 상단 '11/23~ 집계 대상 없음'",
        f"- 하단 안내문: {FOOTER}",
        "",
        "| 씬 | 주제 | 자막 | 내레이션 |",
        "| :--- | :--- | :--- | :--- |",
    ]
    for i, s in enumerate(video["scenes"], 1):
        cap = s.get("caption") or f"오늘의 방향: {s.get('today_label')} / 내일의 예상: {s.get('tomorrow_label')}"
        lines.append(f"| {i} | {s['topic']} | {cap} | {s['voice']} |")
    lines.append("")
    (ARCHIVE / "shorts_script.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"✅ 대본 저장 ({chars}자)")


def make_preview(video: dict):
    src = video["out"]
    gif = DOWNLOADS / f"{video['id']}_미리보기.gif"
    total = ffprobe_meta(src)["duration"]
    subprocess.run([FFMPEG_PATH, "-y", "-i", str(src), "-vf",
                    "fps=1.6,scale=420:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=192[p];[s1][p]paletteuse=dither=bayer",
                    "-loop", "0", str(gif)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    caps = []
    for idx, ts in enumerate([0.5, total * 0.30, total - 1.2], 1):
        cap = DOWNLOADS / f"{video['id']}_scene_{idx}.png"
        subprocess.run([FFMPEG_PATH, "-y", "-ss", f"{ts:.2f}", "-i", str(src),
                        "-frames:v", "1", str(cap)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        caps.append(cap)
    return gif, caps


def build(video: dict):
    write_script(video)
    timings = render_shorts(video["scenes"], str(video["out"]), temp_dir=f"/tmp/{video['id']}_build")
    shutil.copy(video["out"], ARCHIVE / "chalkboard_shorts_video.mp4")
    gif, caps = make_preview(video)
    pdir = ARCHIVE / "preview"
    pdir.mkdir(parents=True, exist_ok=True)
    shutil.copy(gif, pdir / "moving_preview.gif")
    for i, c in enumerate(caps, 1):
        shutil.copy(c, pdir / f"scene{i}_preview.png")
    meta = ffprobe_meta(video["out"])
    last_cut = DOWNLOADS / f"{video['id']}_마지막2초컷.png"
    subprocess.run([FFMPEG_PATH, "-y", "-ss", f"{max(meta['duration'] - 1.5, 0):.2f}", "-i", str(video["out"]),
                    "-frames:v", "1", str(last_cut)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    shutil.copy(last_cut, pdir / "last_cut.png")
    report = {"file": _show(video["out"]), "duration": round(meta["duration"], 2),
              "size_mb": round(meta["size"] / 1024 / 1024, 2), "streams": meta["streams"],
              "gif": _show(gif), "captures": [_show(c) for c in caps], "last_cut": _show(last_cut),
              "timings": timings,
              "layout": "jaljab(올.주.선.이 3단)", "subscribe_badge": "0.0~2.0s",
              "direction_cut": "last scene (오늘의 방향 ▲ 강위 / 내일의 예상 ▲ 강위 / 11/23~ 집계 대상 없음)"}
    (ARCHIVE / "render_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report


if __name__ == "__main__":
    build(VIDEO)
