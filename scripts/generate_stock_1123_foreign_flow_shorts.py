#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-23 (월) 외국인 수급 쇼츠 생성기 (6회차 · 올.주.선.이 3단 레이아웃)
- 6씬 + 마지막 방향성 컷(오늘의 방향 / 내일의 예상, 우측 상단 11/23~ 집계 시작)
- 실행: STOCK_SHORTS_OUTPUT=/workspace/downloads python scripts/generate_stock_1123_foreign_flow_shorts.py
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
ART = Path(os.environ.get("STOCK_CHALK_ART_DIR", str(REPO_ROOT / "assets" / "chalkboard" / "stock1123")))
ARCHIVE = REPO_ROOT / "content" / "2026-11-23" / "04_shorts_foreign_flow" / "stock_chalkboard"

VIDEO = {
    "id": "Stock2_1123",
    "title": "11/23 외국인 수급 — 장 막판 30분에 선물 2,338계약을 되샀다",
    "out": DOWNLOADS / "Stock2_1123_외국인_현선물옵션_수급_칠판드로잉_쇼츠.mp4",
    "scenes": [
        {
            "topic": "투기지수 -20",
            "caption": "혼조·헷지 · 투기 4조건 중 1개",
            "chalk_img": str(ART / "v2_scene1_hedge.png"),
            "voice": "이십삼일 외국인 판정은 투기지수 마이너스 이십, 혼조와 헷지입니다.",
        },
        {
            "topic": "현물 매도·선물 매수",
            "caption": "현물 -2,472억 · 선물 +1,681계약",
            "chalk_img": str(ART / "v2_scene2_futspot.png"),
            "voice": "현물은 이천사백칠십억을 팔고, 선물은 천육백팔십일 계약을 샀습니다. 방향이 반대입니다.",
        },
        {
            "topic": "괴리 -5.32pt",
            "caption": "시장 -4.18pt · 이론 +1.14pt",
            "chalk_img": str(ART / "v2_scene3_basis.png"),
            "voice": "선물이 이론가보다 오 포인트 넘게 싸게 끝났습니다. 전일 마이너스 삼 점 구오에서 더 벌어졌습니다.",
        },
        {
            "topic": "3시 숏 → 3시 30분 롱",
            "caption": "15:20 -657계약 · 15:45 +1,681계약",
            "chalk_img": str(ART / "v2_scene4_flip.png"),
            "voice": "오후 세 시 이십 분까지 육백오십칠 계약 매도였는데, 동시호가 뒤에 천육백팔십일 계약 매수로 뒤집혔습니다.",
        },
        {
            "topic": "미결제 +3,871",
            "caption": "172,567계약 · 최근 30분 -1,638계약",
            "chalk_img": str(ART / "v2_scene5_oi.png"),
            "voice": "최근 삼십 분에 이천삼백삼십팔 계약을 되샀고, 미결제는 천육백삼십팔 계약 줄었습니다.",
        },
        {
            "topic": "콜 매도·플립 732.12",
            "caption": "콜 -88.8억 · ATM IV 66.9%",
            "chalk_img": str(ART / "v2_scene6_gex.png"),
            "voice": "콜은 팔았고 변동성은 육십육 퍼센트. 감마 플립 칠백삼십이 포인트 일에 붙어 마감했습니다.",
        },
        {
            "type": "direction",
            "topic": "오늘·내일 방향",
            "today_label": "중간하방",
            "tomorrow_label": "약간 상방 또는 횡보",
            "accuracy_text": "11/23~ 집계 시작",
            "hold": 2.0,
            "voice": "오늘의 방향은 중간 하방이었습니다. 내일은 약간 상방 또는 횡보로 봅니다. 단기 바닥은 사천이백에서 사천오백 사이입니다.",
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
        f"# {video['title']} — 유튜브 쇼츠 대본 (올.주.선.이 · 6회차)",
        "",
        f"- 상단 훅: {TOP_LINE} / 네이비 박스: 올.주.선.이 · <주제>",
        f"- 규격: 1080x1920 세로형 9:16, 25fps, 3단 레이아웃(상단 흰색·중단 칠판 1080x860·하단 흰색), {len(video['scenes'])}개 씬",
        "- 음성: Edge-TTS ko-KR-SunHiNeural, 속도 +5%",
        f"- 대본 분량: {chars}자",
        "- 시작 0.0~2.0초: '구독·알림·좋아요는 힘이 됩니다' 배지 오버레이",
        "- 마지막 컷: 오늘의 방향 / 내일의 예상 + 우측 상단 '11/23~ 집계 시작'",
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
    render_shorts(video["scenes"], str(video["out"]), temp_dir=f"/tmp/{video['id']}_build")
    shutil.copy(video["out"], ARCHIVE / "chalkboard_shorts_video.mp4")
    gif, caps = make_preview(video)
    pdir = ARCHIVE / "preview"
    pdir.mkdir(parents=True, exist_ok=True)
    shutil.copy(gif, pdir / "moving_preview.gif")
    for i, c in enumerate(caps, 1):
        shutil.copy(c, pdir / f"scene{i}_preview.png")
    meta = ffprobe_meta(video["out"])
    report = {"file": _show(video["out"]), "duration": round(meta["duration"], 2),
              "size_mb": round(meta["size"] / 1024 / 1024, 2), "streams": meta["streams"],
              "gif": _show(gif), "captures": [_show(c) for c in caps],
              "layout": "jaljab(올.주.선.이 3단)", "subscribe_badge": "0.0~2.0s",
              "direction_cut": "last scene (오늘의 방향 / 내일의 예상 / 11/23~ 집계 시작)"}
    (ARCHIVE / "render_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report


if __name__ == "__main__":
    build(VIDEO)
