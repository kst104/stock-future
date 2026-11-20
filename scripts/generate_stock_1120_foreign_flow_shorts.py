#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-20 (금) 외국인 수급 쇼츠 생성기 (5회차 · 올.주.선.이 3단 레이아웃)
- 2편: 장중 투기적 숏 S=+80 → 시간외 단일가 숏 되사기 → 종가 S=-40, 감마 플립 764.55
- 실행: STOCK_SHORTS_OUTPUT=/workspace/downloads python scripts/generate_stock_1120_foreign_flow_shorts.py
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
ART = Path(os.environ.get("STOCK_CHALK_ART_DIR", str(REPO_ROOT / "assets" / "chalkboard" / "stock1120")))
ARCHIVE = REPO_ROOT / "content" / "2026-11-20" / "04_shorts_foreign_flow" / "stock_chalkboard"

VIDEO = {
    "id": "Stock2_1120",
    "title": "11/20 외국인 수급 — 장중 투기적 숏, 마지막 5분에 숏을 닫았다",
    "out": DOWNLOADS / "Stock2_1120_외국인_현선물옵션_수급_칠판드로잉_쇼츠.mp4",
    "scenes": [
        {
            "topic": "장중 S=+80",
            "caption": "장중 판정 · 투기적 숏",
            "chalk_img": str(ART / "v2_scene1_short.png"),
            "voice": "장중 외국인은 현물과 선물을 함께 팔았습니다. 투기지수는 플러스 팔십까지 올라갔고, 판정은 투기적 숏이었습니다.",
        },
        {
            "topic": "동방향 매도",
            "caption": "현물 -1조2,682억 · 선물 -3,297계약",
            "chalk_img": str(ART / "v2_scene2_oi.png"),
            "voice": "현물 일조 이천육백팔십이억, 선물 삼천이백구십칠 계약, 프로그램 비차익 일조 이천백십이억이 같은 방향으로 나왔습니다.",
        },
        {
            "topic": "베이시스 괴리",
            "caption": "시장 -1.79pt · 이론 +1.36pt · 괴리 -3.15pt",
            "chalk_img": str(ART / "v2_scene3_basis.png"),
            "voice": "선물이 이론가보다 삼 포인트 넘게 싸게 거래됐습니다. 베이시스가 무너진 자리입니다.",
        },
        {
            "topic": "숏 되사기",
            "caption": "15:30 -3,297 · 15:45 +504계약",
            "chalk_img": str(ART / "v2_scene4_buyback.png"),
            "voice": "정규장 마감까지 삼천이백구십칠 계약 매도였는데, 시간외 단일가에서 삼천오백육십팔 계약을 되샀습니다.",
        },
        {
            "topic": "미결제 감소",
            "caption": "169,223 · 168,696계약",
            "chalk_img": str(ART / "v2_scene5_decline.png"),
            "voice": "되사는 동안 미결제는 오백이십칠 계약 줄었습니다. 새로 산 것이 아니라 숏을 닫은 것입니다.",
        },
        {
            "topic": "최종 S=-40",
            "caption": "헷지·차익성 매수 · 선물 +923억",
            "chalk_img": str(ART / "v2_scene6_compass.png"),
            "voice": "하루 최종 판정은 마이너스 사십, 헷지와 차익성 매수입니다. 외국인 선물은 구백이십삼억 순매수로 마감했습니다.",
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
        f"# {video['title']} — 유튜브 쇼츠 대본 (올.주.선.이 · 5회차)",
        "",
        f"- 상단 훅: {TOP_LINE} / 네이비 박스: 올.주.선.이 · <주제>",
        f"- 규격: 1080x1920 세로형 9:16, 25fps, 3단 레이아웃(상단 흰색·중단 칠판 1080x860·하단 흰색), {len(video['scenes'])}개 씬",
        "- 음성: Edge-TTS ko-KR-InJoonNeural, 속도 +5%",
        f"- 대본 분량: {chars}자",
        "- 시작 0.0~2.0초: '구독·알림·좋아요는 힘이 됩니다' 배지 오버레이",
        f"- 하단 안내문: {FOOTER}",
        "",
        "| 씬 | 주제 | 자막 | 내레이션 |",
        "| :--- | :--- | :--- | :--- |",
    ]
    for i, s in enumerate(video["scenes"], 1):
        lines.append(f"| {i} | {s['topic']} | {s['caption']} | {s['voice']} |")
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
    for idx, ts in enumerate([0.5, total * 0.30, total * 0.62], 1):
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
              "layout": "jaljab(올.주.선.이 3단)", "subscribe_badge": "0.0~2.0s"}
    (ARCHIVE / "render_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report


if __name__ == "__main__":
    build(VIDEO)
