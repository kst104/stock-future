#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-11-17 (화) 외국인 현·선물·옵션 수급 쇼츠 생성기 (2회차 · 외국인 수급 전용)
- 2편: 수급 심화 (현물 -1조4,459억 · 선물 +1,582계약 · 투기적 숏 0회 · 베이시스 -5.15pt · 감마 플립 760.63)
- 칠판 분필 드로잉 특강 스타일 / 겅태 캐릭터 감정 매핑 / 투자 면책 고지 상시 노출
- 실행: STOCK_SHORTS_OUTPUT=/workspace/downloads python scripts/generate_stock_1117_foreign_flow_shorts.py
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
ART = Path(os.environ.get("STOCK_CHALK_ART_DIR", str(REPO_ROOT / "assets" / "chalkboard" / "stock1117")))

FLOW_DIR = REPO_ROOT / "content" / "2026-11-17" / "04_shorts_foreign_flow" / "stock_chalkboard"

HEADER = ("외국인 수급 심화 특강", "2026.11.17 (화) 장마감")

VIDEO = {
    "id": "Stock2_1117",
    "title": "11/17 외국인 현·선물·옵션 수급 — 현물은 팔고 선물은 사흘째 샀다",
    "header": HEADER,
    "out": DOWNLOADS / "Stock2_1117_외국인_현선물옵션_수급_칠판드로잉_쇼츠.mp4",
    "archive_dir": FLOW_DIR,
    "scenes": [
        {
            "badge": "현·선물 역방향 3일째",
            "keyword": "헷지·차익성 매수",
            "chalk_img": str(ART / "v2_scene1_spot_sell_futures_buy.png"),
            "stats": [
                {"label": "코스피 현물", "value": "-1조4,459억", "delta": "거래소 집계 -1조4,430억", "color": "down"},
                {"label": "코스피200 선물", "value": "+1,582계약", "delta": "+3,037억 순매수", "color": "up"},
                {"label": "8766 판정", "value": "S = -60", "delta": "헷지·차익성 매수", "color": "neutral"},
            ],
            "main_text": "현물은 1조4,459억 팔고\n선물은 1,582계약 샀습니다",
            "sub_text": "현물 매도·선물 매수, 사흘째 이어진 조합입니다",
            "voice": "외국인은 코스피 현물을 일조 사천사백오십구억 팔고, 코스피이백 선물은 천오백팔십이 계약 샀습니다. 사흘째 같은 조합입니다.",
            "character": "expr_surprise",
            "character_label": "",
        },
        {
            "badge": "장중 궤적이 달랐습니다",
            "keyword": "투기적 숏 0회",
            "chalk_img": str(ART / "v2_scene2_never_negative.png"),
            "stats": [
                {"label": "09:32 최소", "value": "+59계약", "delta": "하루 중 가장 낮은 값", "color": "up"},
                {"label": "11:38 정점", "value": "+1,562계약", "delta": "오전 누적 순매수", "color": "up"},
                {"label": "15:45 마감", "value": "+1,582계약", "delta": "동시호가 +1,410계약", "color": "up"},
            ],
            "main_text": "장중에 한 번도\n마이너스로 가지 않았습니다",
            "sub_text": "어제 두 차례 나왔던 투기적 숏 신호는 오늘 0회",
            "voice": "오늘은 장중 내내 선물 누적이 마이너스로 간 적이 없습니다. 어제 두 차례 나왔던 투기적 숏 신호도 없었습니다.",
            "character": "pose_point",
            "character_label": "",
        },
        {
            "badge": "베이시스가 말해줍니다",
            "keyword": "괴리 -5.15pt",
            "chalk_img": str(ART / "v2_scene3_basis_wedge.png"),
            "stats": [
                {"label": "미결제약정", "value": "179,208계약", "delta": "+8,140 (+4.76%)", "color": "up"},
                {"label": "시장 베이시스", "value": "-3.54pt", "delta": "이론 +1.61pt", "color": "down"},
                {"label": "괴리", "value": "-5.15pt", "delta": "전일 -3.69pt에서 확대", "color": "down"},
            ],
            "main_text": "미결제는 늘고 선물은 할인됐습니다\n단순 차익 청산이 아닙니다",
            "sub_text": "새로 쌓인 계약은 하방 헷지로 읽힙니다",
            "voice": "미결제약정은 팔천백사십 계약 늘었는데, 선물은 이론가보다 오 점 일오 포인트 싸게 마감했습니다.",
            "character": "expr_explain",
            "character_label": "",
        },
        {
            "badge": "옵션은 반대 방향",
            "keyword": "풋 +3,794계약",
            "chalk_img": str(ART / "v2_scene4_put_insurance.png"),
            "stats": [
                {"label": "콜", "value": "-19.9억", "delta": "-2,578계약", "color": "down"},
                {"label": "풋", "value": "+3.19억", "delta": "+3,794계약 (+68%)", "color": "up"},
                {"label": "콜-풋 차", "value": "-23.1억", "delta": "선물 롱과 반대", "color": "down"},
            ],
            "main_text": "콜을 팔고 풋을 샀습니다\n옵션은 상승 베팅이 아닙니다",
            "sub_text": "프리미엄은 방어 쪽에 썼습니다",
            "voice": "옵션에서는 콜을 팔고 풋을 샀습니다. 풋 순매수 계약은 삼천칠백구십사로 육십팔 퍼센트 늘었습니다.",
            "character": "expr_worried",
            "character_label": "",
        },
        {
            "badge": "18901 감마 전환",
            "keyword": "플립 760.63",
            "chalk_img": str(ART / "v2_scene5_gamma_flip_line.png"),
            "stats": [
                {"label": "딜러 감마", "value": "+230.8억", "delta": "1% 변동당 프록시", "color": "up"},
                {"label": "감마 플립", "value": "760.63", "delta": "종가 770.74, 플립 위", "color": "neutral"},
                {"label": "헤지 강도", "value": "83.7계약", "delta": "1사분면 (약)", "color": "neutral"},
            ],
            "main_text": "플러스로 돌아섰지만\n강도는 84계약뿐입니다",
            "sub_text": "오르면 조금 팔고 내리면 조금 사는 구조",
            "voice": "감마는 플러스로 돌아섰지만 강도는 팔십사 계약으로 약합니다. 종가는 플립 칠백육십 점 육삼 위입니다.",
            "character": "expr_surprise",
            "character_label": "",
        },
        {
            "badge": "만기가 지나면 사라집니다",
            "keyword": "11/19 위클리 만기",
            "chalk_img": str(ART / "v2_scene6_expiry_clock.png"),
            "stats": [
                {"label": "위클리(목)", "value": "+977.3억", "delta": "11월 19일 만기", "color": "up"},
                {"label": "월물 202612", "value": "-742.6억", "delta": "만기 후 남는 감마", "color": "down"},
                {"label": "확인 조건", "value": "현물 순매수", "delta": "전환 전에는 추세 아님", "color": "neutral"},
            ],
            "main_text": "완충의 수명은 이틀입니다",
            "sub_text": "반등의 시작은 반도체 외국인 순매수 전환",
            "voice": "다만 이 플러스는 목요일 만기 위클리가 만든 것입니다. 만기가 지나면 완충도 사라집니다. 방향 전환은 현물 순매수에서 확인하십시오.",
            "character": "pose_wave",
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


def _show(path: Path) -> str:
    """리포트 표기용 경로 (워크스페이스 기준 상대 경로)."""
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
        f"# {video['title']} — 유튜브 쇼츠 대본 (칠판 특강 · 2회차)",
        "",
        f"- 헤더: {video['header'][0]} / {video['header'][1]}",
        f"- 규격: 1080x1920 세로형 9:16, 25fps, 칠판 분필 드로잉 외국인 수급 특강 스타일, {len(video['scenes'])}개 씬",
        "- 음성: Edge-TTS ko-KR-InJoonNeural, 속도 +5% (차분한 남성 톤)",
        f"- 대본 분량: {chars}자",
        "- 수치 표기: 화면은 아라비아 숫자, 내레이션은 한글 발음(예: 일조 사천사백오십구억)",
        f"- 하단 고지: {DISCLAIMER}",
        "",
        "| 씬 | 배지 | 키워드 | 수치 카드 | 화면 문구 | 내레이션 | 겅태 |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for i, s in enumerate(video["scenes"], 1):
        cards = " / ".join(f"{c['label']} {c['value']}" for c in s["stats"])
        main = s["main_text"].replace("\n", " ")
        lines.append(f"| {i} | {s['badge']} | {s['keyword']} | {cards} | {main} | {s['voice']} | {s['character']} |")
    lines += ["", "## 연출 메모", "- 겅태 감정 매핑: 수급 반전 훅은 놀람, 판정 근거는 가리키기·설명, 리스크 경고는 걱정, 마무리 조건 제시는 인사.", ""]
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
