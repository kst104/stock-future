#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-11-19 (목) 외국인 현·선물·옵션 수급 쇼츠 생성기 (4회차 · 외국인 수급 전용)
- 2편: 수급 심화 (현물 -4,036억 5일째 · 선물 장중 +1,243 → 종가 +342 · S 0 혼조 · 베이시스 괴리 -3.10pt · 위클리 만기 감마 1조 3,080억 · 만기 후 플립 799.5)
- 칠판 분필 드로잉 특강 스타일 / 겅태 캐릭터 감정 매핑 / 투자 면책 고지 상시 노출
- 실행: STOCK_SHORTS_OUTPUT=/workspace/downloads python scripts/generate_stock_1119_foreign_flow_shorts.py
"""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent      # scripts/
REPO_ROOT = BASE_DIR.parent                    # 저장소 루트

sys.path.insert(0, str(REPO_ROOT))

from engine.stock_chalkboard_engine import render_stock_shorts, FFMPEG_PATH, DISCLAIMER

DOWNLOADS = Path(os.environ.get("STOCK_SHORTS_OUTPUT", str(REPO_ROOT / "output")))
DOWNLOADS.mkdir(parents=True, exist_ok=True)

ART = Path(os.environ.get("STOCK_CHALK_ART_DIR", str(REPO_ROOT / "assets" / "chalkboard" / "stock1119")))

FLOW_DIR = REPO_ROOT / "content" / "2026-11-19" / "04_shorts_foreign_flow" / "stock_chalkboard"

HEADER = ("외국인 수급 심화 특강", "2026.11.19 (목) 장마감")

VIDEO = {
    "id": "Stock2_1119",
    "title": "11/19 외국인 현·선물·옵션 수급 — 낮에 산 선물을 종가에 되돌리고, 만기 감마는 사라졌다",
    "header": HEADER,
    "out": DOWNLOADS / "Stock2_1119_외국인_현선물옵션_수급_칠판드로잉_쇼츠.mp4",
    "archive_dir": FLOW_DIR,
    "scenes": [
        {
            "badge": "현물은 팔고 선물은 샀다",
            "keyword": "현물 -4,036억",
            "chalk_img": str(ART / "v2_scene1_spot_vs_futures.png"),
            "stats": [
                {"label": "코스피 현물", "value": "-4,036억", "delta": "5거래일 연속 매도", "color": "down"},
                {"label": "코스피200 선물", "value": "+342계약", "delta": "+680억 순매수", "color": "up"},
                {"label": "8766 판정", "value": "S = 0", "delta": "혼조 (장중 -40)", "color": "neutral"},
            ],
            "main_text": "현물은 닷새째 팔고\n선물은 조금 샀습니다",
            "sub_text": "닷새 누적 선물 +7,816계약, 버티는 자세",
            "voice": "외국인은 코스피 현물 사천삼십육억을 닷새째 팔았고, 선물은 삼백사십이 계약 순매수였습니다.",
            "character": "expr_worried",
            "character_label": "",
        },
        {
            "badge": "장중엔 1,243계약",
            "keyword": "낮에 산 걸 되돌림",
            "chalk_img": str(ART / "v2_scene2_hill_lockin.png"),
            "stats": [
                {"label": "13:21 최대", "value": "+1,243계약", "delta": "장중 누적", "color": "up"},
                {"label": "15:15", "value": "+329계약", "delta": "오후 반락", "color": "down"},
                {"label": "15:45 종가", "value": "+342계약", "delta": "약 900계약 되돌림", "color": "neutral"},
            ],
            "main_text": "낮에 산 선물을\n종가에 되돌렸습니다",
            "sub_text": "오전 10시 38분엔 -309계약까지 밀렸습니다",
            "voice": "선물은 오후 한 시 이십일 분 천이백사십삼 계약까지 갔다가 종가에 삼백사십이 계약으로 줄었습니다.",
            "character": "expr_surprise",
            "character_label": "",
        },
        {
            "badge": "미결제 1.39% 증가",
            "keyword": "신규 구축",
            "chalk_img": str(ART / "v2_scene3_oi_stack.png"),
            "stats": [
                {"label": "미결제", "value": "184,104", "delta": "15:46 KIS 집계", "color": "neutral"},
                {"label": "전일 대비", "value": "+2,521", "delta": "+1.39%", "color": "up"},
                {"label": "5일 전 대비", "value": "+17,972", "delta": "+10.82%", "color": "up"},
            ],
            "main_text": "오후에 새 포지션이\n쌓였습니다",
            "sub_text": "14시를 지나며 8766 기준 +1%를 넘었습니다",
            "voice": "미결제약정은 십팔만 사천백사 계약, 전일보다 일 점 삼구 퍼센트 늘었습니다.",
            "character": "pose_point",
            "character_label": "",
        },
        {
            "badge": "베이시스 할인 유지",
            "keyword": "-3.10pt",
            "chalk_img": str(ART / "v2_scene4_basis_wedge.png"),
            "stats": [
                {"label": "시장 베이시스", "value": "-1.59pt", "delta": "선물 794.75 · 현물 796.34", "color": "down"},
                {"label": "이론 베이시스", "value": "+1.51pt", "delta": "괴리 -3.10pt", "color": "neutral"},
                {"label": "전일 괴리", "value": "-2.84pt", "delta": "0.26pt 확대", "color": "down"},
            ],
            "main_text": "선물이 올랐는데도\n할인이 남았습니다",
            "sub_text": "선물 +1.06%, 현물 +1.10%로 현물이 조금 더 올랐습니다",
            "voice": "베이시스 괴리는 마이너스 삼 점 일영 포인트로, 어제보다 조금 더 벌어졌습니다.",
            "character": "expr_explain",
            "character_label": "",
        },
        {
            "badge": "만기 감마 1조 3,080억",
            "keyword": "795 콜 +1조 1,183억",
            "chalk_img": str(ART / "v2_scene5_expiry_hourglass.png"),
            "stats": [
                {"label": "총 감마", "value": "+1조 3,080억", "delta": "1% 변동당", "color": "up"},
                {"label": "위클리(목)", "value": "+1조 3,130억", "delta": "오늘 만기", "color": "up"},
                {"label": "월물 202612", "value": "-166억", "delta": "만기 뒤 남는 값", "color": "down"},
            ],
            "main_text": "플러스 감마는\n오늘 만기에서 나왔습니다",
            "sub_text": "잔존시간 한 시간, 감마가 기계적으로 커진 값입니다",
            "voice": "총 감마 일조 삼천억의 대부분이 오늘 만기되는 위클리에서 나왔습니다. 월물은 마이너스 백육십육억입니다.",
            "character": "pose_point",
            "character_label": "",
        },
        {
            "badge": "만기 뒤 플립 799.5",
            "keyword": "-50억 숏감마",
            "chalk_img": str(ART / "v2_scene6_post_expiry_balance.png"),
            "stats": [
                {"label": "만기 후 감마", "value": "-50억", "delta": "종가 796.34 기준", "color": "down"},
                {"label": "만기 후 플립", "value": "799.5", "delta": "종가는 플립 아래", "color": "neutral"},
                {"label": "오전 최저", "value": "-1,899억", "delta": "12:15, 지수 773.7", "color": "down"},
            ],
            "main_text": "완충이 사라지고\n부호가 바뀌는 자리입니다",
            "sub_text": "내일 799.5 위 출발 여부와 현물 순매수 전환을 봅니다",
            "voice": "만기 뒤 남는 감마는 마이너스 오십억, 플립은 칠백구십구 포인트 오로 올라섭니다. 종가는 그 아래입니다.",
            "character": "pose_wave",
            "character_label": "",
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
            m = _re.search(r"Video:\s*([^,\s]+)", line)
            wh = _re.search(r"(\d{2,5})x(\d{2,5})", line)
            fp = _re.search(r"([\d.]+)\s*fps", line)
            info["streams"].append({
                "type": "video", "codec": m.group(1) if m else None,
                "w": int(wh.group(1)) if wh else None,
                "h": int(wh.group(2)) if wh else None,
                "fps": fp.group(1) if fp else None,
            })
        if "Stream" in line and "Audio:" in line:
            m = _re.search(r"Audio:\s*([^,\s]+)", line)
            info["streams"].append({"type": "audio", "codec": m.group(1) if m else None,
                                    "w": None, "h": None, "fps": None})
    return info


def _show(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(Path("/workspace")))
    except Exception:
        try:
            return str(path.resolve().relative_to(REPO_ROOT))
        except Exception:
            return str(path)


def write_screenplay(video: dict):
    d = video["archive_dir"]
    d.mkdir(parents=True, exist_ok=True)
    chars = sum(len(s["voice"]) for s in video["scenes"])
    lines = [
        f"# {video['title']} — 유튜브 쇼츠 대본 (칠판 특강 · 4회차)",
        "",
        f"- 헤더: {video['header'][0]} / {video['header'][1]}",
        f"- 규격: 1080x1920 세로형 9:16, 25fps, 칠판 분필 드로잉 시장 특강 스타일, {len(video['scenes'])}개 씬",
        "- 음성: Edge-TTS ko-KR-InJoonNeural, 속도 +5% (차분한 남성 톤)",
        f"- 대본 분량: {chars}자",
        "- 수치 표기: 화면은 아라비아 숫자, 내레이션은 한글 발음(예: 천이백사십삼 계약)",
        f"- 하단 고지: {DISCLAIMER}",
        "",
        "| 씬 | 배지 | 키워드 | 수치 카드 | 화면 문구 | 내레이션 | 겅태 |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for i, s in enumerate(video["scenes"], 1):
        cards = " / ".join(f"{c['label']} {c['value']}" for c in s["stats"])
        main = s["main_text"].replace("\n", " ")
        lines.append(f"| {i} | {s['badge']} | {s['keyword']} | {cards} | {main} | {s['voice']} | {s['character']} |")
    lines += ["", "## 연출 메모", "- 겅태 감정 매핑: 수급 훅은 걱정/놀람, 구조 설명은 가리키기·설명, 마무리는 인사.", ""]
    (d / "shorts_script.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"✅ 대본 저장: {d / 'shorts_script.md'} ({chars}자)")


def make_preview(video: dict):
    src = video["out"]
    gif = DOWNLOADS / f"{video['id']}_미리보기.gif"
    total = ffprobe_meta(src)["duration"]
    subprocess.run([
        FFMPEG_PATH, "-y", "-i", str(src),
        "-vf", "fps=1.6,scale=420:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=192[p];[s1][p]paletteuse=dither=bayer",
        "-loop", "0", str(gif),
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    caps = []
    for idx, frac in enumerate([0.10, 0.42, 0.74], 1):
        cap = DOWNLOADS / f"{video['id']}_scene_{idx}.png"
        subprocess.run([FFMPEG_PATH, "-y", "-ss", f"{total * frac:.2f}", "-i", str(src),
                        "-frames:v", "1", str(cap)], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        caps.append(cap)
    return gif, caps


def build(video: dict):
    write_screenplay(video)
    render_stock_shorts(
        video["scenes"], str(video["out"]),
        header_title=video["header"][0], header_meta=video["header"][1],
        temp_dir=f"/tmp/{video['id']}_build",
    )
    shutil.copy(video["out"], video["archive_dir"] / "chalkboard_shorts_video.mp4")
    gif, caps = make_preview(video)
    preview_dir = video["archive_dir"] / "preview"
    preview_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(gif, preview_dir / "moving_preview.gif")
    for i, c in enumerate(caps, 1):
        shutil.copy(c, preview_dir / f"scene{i}_preview.png")
    meta = ffprobe_meta(video["out"])
    report = {
        "file": _show(video["out"]),
        "duration": round(meta["duration"], 2),
        "size_mb": round(meta["size"] / 1024 / 1024, 2),
        "streams": meta["streams"],
        "gif": _show(gif),
        "captures": [_show(c) for c in caps],
    }
    (video["archive_dir"] / "render_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report


def main():
    build(VIDEO)


if __name__ == "__main__":
    main()
