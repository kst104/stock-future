#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-11-16 (월) 외국인 현·선물·옵션 수급 쇼츠 생성기 (1회차 · 외국인 수급 전용)
- 1편: 외국인 현·선물·옵션 수급 심화 (장중 투기적 숏 → 종가 헷지, 18901 감마 플립 793.01)
- 칠판 분필 드로잉 특강 스타일 / 겅태 캐릭터 감정 매핑 / 투자 면책 고지 상시 노출
- 실행: python scripts/generate_stock_1116_foreign_flow_shorts.py
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

# 결과물 mp4 출력 위치 (기본: 저장소 output/, 환경변수로 바꿀 수 있음)
DOWNLOADS = Path(os.environ.get("STOCK_SHORTS_OUTPUT", str(REPO_ROOT / "output")))
DOWNLOADS.mkdir(parents=True, exist_ok=True)

# 칠판 드로잉 원본 이미지 (저장소 assets/chalkboard/<회차>)
ART = Path(os.environ.get("STOCK_CHALK_ART_DIR", str(REPO_ROOT / "assets" / "chalkboard" / "stock1116")))

FLOW_DIR = REPO_ROOT / "content" / "2026-11-16" / "04_shorts_foreign_flow" / "stock_chalkboard"

HEADER = ("외국인 수급 심화 특강", "2026.11.16 (월) 장마감")

VIDEO = {
    "id": "Stock2_1116",
    "title": "11/16 외국인 현·선물·옵션 수급 — 장중 투기적 숏, 종가는 헷지",
    "header": HEADER,
    "out": DOWNLOADS / "Stock2_1116_외국인_현선물옵션_수급_칠판드로잉_쇼츠.mp4",
    "archive_dir": FLOW_DIR,
    "scenes": [
        {
            "badge": "현·선물 역방향",
            "keyword": "정반대 조합",
            "chalk_img": str(ART / "v2_scene1_balance_scale.png"),
            "stats": [
                {"label": "코스피 현물", "value": "-1조3,769억", "delta": "거래소 집계 -1조3,838억", "color": "down"},
                {"label": "코스피200 선물", "value": "+1,620계약", "delta": "+3,239억 순매수", "color": "up"},
                {"label": "8766 투기지수", "value": "S = -60", "delta": "헷지·차익성 매수", "color": "neutral"},
            ],
            "main_text": "현물은 1조3,769억 팔고\n선물은 1,620계약 샀습니다",
            "sub_text": "방향이 정반대인 하루, 역방향 조합",
            "voice": "현물은 일조 삼천칠백육십구억 팔고, 선물은 천육백이십 계약 샀습니다. 방향이 정반대인 하루였습니다.",
            "character": "expr_surprise",
            "character_label": "",
        },
        {
            "badge": "장중 궤적은 달랐습니다",
            "keyword": "동시호가 반전",
            "chalk_img": str(ART / "v2_scene2_intraday_reversal.png"),
            "stats": [
                {"label": "오전 10:15", "value": "+653계약", "delta": "누적 순매수", "color": "up"},
                {"label": "오후 15:44", "value": "-584계약", "delta": "누적 순매도", "color": "down"},
                {"label": "오후 15:45", "value": "+1,620계약", "delta": "마감 동시호가 단일가", "color": "up"},
            ],
            "main_text": "장중은 매도, 마감에 매수\n성격이 바뀐 하루",
            "sub_text": "오후 2시 31분부터 순매도 300계약을 넘었습니다",
            "voice": "그런데 그 선물 매수는 마감 동시호가에서 나왔습니다. 오후 두 시 반부터는 순매도가 삼백 계약을 넘었습니다.",
            "character": "expr_explain",
            "character_label": "",
        },
        {
            "badge": "8766 수급 판정",
            "keyword": "투기적 숏 4/4",
            "chalk_img": str(ART / "v2_scene3_four_conditions.png"),
            "stats": [
                {"label": "14:31~15:16", "value": "S = +100", "delta": "투기적 숏 (4/4)", "color": "down"},
                {"label": "15:31~15:44", "value": "S = +100", "delta": "투기적 숏 (4/4)", "color": "down"},
                {"label": "종가 15:45", "value": "S = -60", "delta": "헷지·차익성 매수", "color": "neutral"},
            ],
            "main_text": "장중 내내 투기적 숏\n종가엔 헷지·차익성 매수",
            "sub_text": "네 조건 전부 정렬 60분, 마감에 성격이 바뀌었습니다",
            "voice": "장중 두 구간은 투기적 숏, 네 조건 전부 정렬이었습니다. 종가 판정은 헷지·차익성 매수입니다.",
            "character": "expr_worried",
            "character_label": "",
        },
        {
            "badge": "베이시스가 말해줍니다",
            "keyword": "괴리 -3.69pt",
            "chalk_img": str(ART / "v2_scene4_basis_gap.png"),
            "stats": [
                {"label": "시장 베이시스", "value": "-2.21pt", "delta": "선물 789.35 / 현물 791.56", "color": "down"},
                {"label": "이론 베이시스", "value": "+1.48pt", "delta": "장중 괴리 -4.44pt까지", "color": "up"},
                {"label": "괴리", "value": "-3.69pt", "delta": "선물 저평가", "color": "down"},
            ],
            "main_text": "매수세가 끌어올린 게 아니라\n매도가 선물을 할인시켰습니다",
            "sub_text": "선물이 이론가보다 3.69포인트 싸게 거래됐습니다",
            "voice": "선물은 이론가보다 삼 점 육구 포인트 싸게 거래됐습니다. 매수세가 아니라 매도가 선물을 할인시킨 하루입니다.",
            "character": "pose_point",
            "character_label": "",
        },
        {
            "badge": "18901 감마",
            "keyword": "플립 793.01",
            "chalk_img": str(ART / "v2_scene5_gamma_flip.png"),
            "stats": [
                {"label": "딜러 감마", "value": "-2,373.6억", "delta": "1% 변동당 프록시", "color": "down"},
                {"label": "감마 플립", "value": "793.01", "delta": "종가 791.56, 플립 아래", "color": "neutral"},
                {"label": "딜러 헤지", "value": "1,101계약", "delta": "2사분면 강도 (강)", "color": "down"},
            ],
            "main_text": "플립 793.01 아래\n2사분면 충돌과 챕",
            "sub_text": "이 구간에서 딜러는 내리면 팔고 올리면 삽니다",
            "voice": "감마는 마이너스 이천삼백칠십삼억. 플립 칠백구십삼 점 영일 아래, 충돌과 챕이 겹치는 이사분면입니다.",
            "character": "expr_surprise",
            "character_label": "",
        },
        {
            "badge": "전환 기준 하나",
            "keyword": "793.01 회복",
            "chalk_img": str(ART / "v2_scene6_flip_recovery.png"),
            "stats": [
                {"label": "코스피200", "value": "791.56", "delta": "플립 아래 -0.18%", "color": "down"},
                {"label": "전환선", "value": "793.01", "delta": "위로 올라서면 감마 양전", "color": "neutral"},
                {"label": "다음 참고점", "value": "800.0", "delta": "콜 미결제 최대 행사가", "color": "up"},
            ],
            "main_text": "반등은 반도체 외국인\n순매수 전환에서 시작됩니다",
            "sub_text": "플립 회복 전까지는 하락 시 딜러 매도 구간",
            "voice": "플립을 되찾기 전까지는 내리면 딜러 매도가 붙습니다. 반등은 반도체 외국인 순매수에서 시작됩니다.",
            "character": "pose_cheer",
            "character_label": "",
        },
    ],
}


def ffprobe_meta(path: Path) -> dict:
    """ffmpeg 스트림 정보 파싱 (ffprobe 미설치 환경)."""
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


def write_screenplay(video: dict):
    d = video["archive_dir"]
    d.mkdir(parents=True, exist_ok=True)
    chars = sum(len(s["voice"]) for s in video["scenes"])
    lines = [
        f"# {video['title']} — 유튜브 쇼츠 대본 (칠판 특강 · 1회차)",
        "",
        f"- 헤더: {video['header'][0]} / {video['header'][1]}",
        "- 규격: 1080x1920 세로형 9:16, 25fps, 칠판 분필 드로잉 시장 특강 스타일, 6개 씬",
        "- 음성: Edge-TTS ko-KR-InJoonNeural, 속도 +5% (차분한 남성 톤)",
        f"- 대본 분량: {chars}자",
        "- 수치 표기: 화면은 아라비아 숫자, 내레이션은 한글 발음(예: 일조 삼천팔백삼십팔억)",
        f"- 하단 고지: {DISCLAIMER}",
        "",
        "| 씬 | 배지 | 키워드 | 수치 카드 | 화면 문구 | 내레이션 | 겅태 |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for i, s in enumerate(video["scenes"], 1):
        cards = " / ".join(f"{c['label']} {c['value']}" for c in s["stats"])
        main = s["main_text"].replace("\n", " ")
        lines.append(f"| {i} | {s['badge']} | {s['keyword']} | {cards} | {main} | {s['voice']} | {s['character']} |")
    lines += ["", "## 연출 메모", "- 겅태 감정 매핑: 급락·반전 훅은 놀람/걱정, 수치 설명은 가리키기·설명, 마무리는 환호·인사.", ""]
    (d / "shorts_script.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"✅ 대본 저장: {d / 'shorts_script.md'} ({chars}자)")


def make_preview(video: dict):
    src = video["out"]
    gif = DOWNLOADS / f"{video['id']}_칠판쇼츠_움직이는미리보기.gif"
    total = ffprobe_meta(src)["duration"]
    subprocess.run([
        FFMPEG_PATH, "-y", "-i", str(src),
        "-vf", "fps=1.6,scale=420:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=192[p];[s1][p]paletteuse=dither=bayer",
        "-loop", "0", str(gif),
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    caps = []
    for idx, frac in enumerate([0.10, 0.42, 0.74], 1):
        cap = DOWNLOADS / f"{video['id']}_씬{idx}_미리보기.png"
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
    meta = ffprobe_meta(video["out"])
    report = {
        "file": str(video["out"]),
        "duration": round(meta["duration"], 2),
        "size_mb": round(meta["size"] / 1024 / 1024, 2),
        "streams": meta["streams"],
        "gif": str(gif),
        "captures": [str(c) for c in caps],
    }
    (video["archive_dir"] / "render_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report


def main():
    build(VIDEO)


if __name__ == "__main__":
    main()
