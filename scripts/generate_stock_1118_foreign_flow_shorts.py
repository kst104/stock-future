#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-11-18 (수) 외국인 현·선물·옵션 수급 쇼츠 생성기 (3회차 · 외국인 수급 전용)
- 2편: 수급 심화 (현물 -3,338억 4일째 · 선물 장중 +2,145 → 종가 -323 · S 0 혼조 · 베이시스 괴리 -2.84pt · 감마 +1,793억 · 11/19 위클리 만기)
- 칠판 분필 드로잉 특강 스타일 / 겅태 캐릭터 감정 매핑 / 투자 면책 고지 상시 노출
- 실행: STOCK_SHORTS_OUTPUT=/workspace/downloads python scripts/generate_stock_1118_foreign_flow_shorts.py
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
ART = Path(os.environ.get("STOCK_CHALK_ART_DIR", str(REPO_ROOT / "assets" / "chalkboard" / "stock1118")))

FLOW_DIR = REPO_ROOT / "content" / "2026-11-18" / "04_shorts_foreign_flow" / "stock_chalkboard"

HEADER = ("외국인 수급 심화 특강", "2026.11.18 (수) 장마감")

VIDEO = {
    "id": "Stock2_1118",
    "title": "11/18 외국인 현·선물·옵션 수급 — 장중에 산 선물을 종가에 다 되팔았다",
    "header": HEADER,
    "out": DOWNLOADS / "Stock2_1118_외국인_현선물옵션_수급_칠판드로잉_쇼츠.mp4",
    "archive_dir": FLOW_DIR,
    "scenes": [
        {
            "badge": "현·선물 엇갈린 하루",
            "keyword": "S = 0 혼조",
            "chalk_img": str(ART / "v2_scene1_spot_vs_futures.png"),
            "stats": [
                {"label": "코스피 현물", "value": "-3,338억", "delta": "4거래일 연속 매도", "color": "down"},
                {"label": "코스피200 선물", "value": "-323계약", "delta": "-681억 순매도", "color": "down"},
                {"label": "8766 판정", "value": "S = 0", "delta": "혼조 (15:43은 -40)", "color": "neutral"},
            ],
            "main_text": "현물은 나흘째 팔고\n선물은 마감에 뒤집혔습니다",
            "sub_text": "사흘째 이어지던 현물 매도·선물 매수 조합이 깨진 날",
            "voice": "외국인은 코스피 현물 삼천삼백삼십팔억을 나흘째 팔았고, 선물은 삼백이십삼 계약 순매도로 마감했습니다.",
            "character": "expr_surprise",
            "character_label": "",
        },
        {
            "badge": "장중엔 2,145계약",
            "keyword": "마감에 -1,920",
            "chalk_img": str(ART / "v2_scene2_auction_cliff.png"),
            "stats": [
                {"label": "14:27 최대", "value": "+2,145계약", "delta": "장중 누적", "color": "up"},
                {"label": "15:25", "value": "+1,597계약", "delta": "동시호가 진입", "color": "up"},
                {"label": "15:45 종가", "value": "-323계약", "delta": "20분 새 1,920계약", "color": "down"},
            ],
            "main_text": "마지막 20분에\n1,920계약이 뒤집혔습니다",
            "sub_text": "정오까지 현물도 함께 샀고, 10시 34분엔 투기적 롱 판정",
            "voice": "선물 누적은 오후 두 시 이십칠 분 이천백사십오 계약까지 갔습니다. 그런데 마지막 이십 분에 천구백이십 계약이 매도로 바뀌었습니다.",
            "character": "expr_worried",
            "character_label": "",
        },
        {
            "badge": "미결제도 줄었다",
            "keyword": "762계약 청산",
            "chalk_img": str(ART / "v2_scene3_basis_wedge.png"),
            "stats": [
                {"label": "15:25 미결제", "value": "166,759", "delta": "계약", "color": "neutral"},
                {"label": "15:45 미결제", "value": "165,997", "delta": "762계약 감소", "color": "down"},
                {"label": "현물 종가", "value": "+878억", "delta": "동시호가 순매수", "color": "up"},
            ],
            "main_text": "새로 판 것보다\n갖고 있던 것을 정리했습니다",
            "sub_text": "현물은 사고 선물은 파는, 차익 청산 쪽 조합",
            "voice": "같은 시간 미결제약정은 칠백육십이 계약 줄었습니다. 새로 판 것보다 갖고 있던 선물을 정리한 쪽입니다.",
            "character": "expr_explain",
            "character_label": "",
        },
        {
            "badge": "베이시스 괴리 축소",
            "keyword": "-5.15 → -2.84pt",
            "chalk_img": str(ART / "v2_scene4_gamma_spike.png"),
            "stats": [
                {"label": "시장 베이시스", "value": "-1.26pt", "delta": "선물 786.45 · 현물 787.71", "color": "down"},
                {"label": "이론 베이시스", "value": "+1.58pt", "delta": "괴리 -2.84pt", "color": "neutral"},
                {"label": "전일 괴리", "value": "-5.15pt", "delta": "2.31pt 축소", "color": "up"},
            ],
            "main_text": "사흘 벌어지던 할인이\n처음 줄었습니다",
            "sub_text": "현물 2.20% 오를 때 선물은 2.41% 올랐습니다",
            "voice": "베이시스 괴리는 마이너스 이 점 팔사 포인트로, 어제 마이너스 오 점 일오에서 크게 줄었습니다.",
            "character": "pose_point",
            "character_label": "",
        },
        {
            "badge": "감마 +1,793억",
            "keyword": "위클리 콜이 130%",
            "chalk_img": str(ART / "v2_scene5_expiry_hourglass.png"),
            "stats": [
                {"label": "총 GEX", "value": "+1,793억", "delta": "전일 +163억", "color": "up"},
                {"label": "위클리(목) 만기", "value": "+2,336억", "delta": "11월 19일", "color": "up"},
                {"label": "월물 202612", "value": "-547억", "delta": "만기 뒤 남는 값", "color": "down"},
            ],
            "main_text": "플러스 감마의 출처는\n내일 만기되는 콜입니다",
            "sub_text": "감마 플립 761.59 위, 4사분면 1, 강도 554계약",
            "voice": "감마는 천칠백구십삼억원으로 하루 만에 열 배 넘게 커졌습니다. 그 백삼십 퍼센트가 내일 만기되는 위클리 콜입니다.",
            "character": "expr_surprise",
            "character_label": "",
        },
        {
            "badge": "완충은 하루짜리",
            "keyword": "792.5~795 콜 벽",
            "chalk_img": str(ART / "v2_scene6_pin_walls.png"),
            "stats": [
                {"label": "792.5 감마", "value": "+912억", "delta": "콜 3,840계약", "color": "up"},
                {"label": "795 감마", "value": "+734억", "delta": "콜 3,393계약", "color": "up"},
                {"label": "만기 뒤 완충", "value": "-543억", "delta": "월물+위클리(월)", "color": "down"},
            ],
            "main_text": "지수는 761과 795 사이에\n갇혀 있습니다",
            "sub_text": "내일 만기가 끝나면 완충은 사라집니다",
            "voice": "만기 콜이 칠백구십이 점 오와 칠백구십오에 칠천이백삼십 계약 몰려 있습니다. 내일 만기가 끝나면 이 완충은 사라집니다.",
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
        f"# {video['title']} — 유튜브 쇼츠 대본 (칠판 특강 · 3회차)",
        "",
        f"- 헤더: {video['header'][0]} / {video['header'][1]}",
        f"- 규격: 1080x1920 세로형 9:16, 25fps, 칠판 분필 드로잉 시장 특강 스타일, {len(video['scenes'])}개 씬",
        "- 음성: Edge-TTS ko-KR-InJoonNeural, 속도 +5% (차분한 남성 톤)",
        f"- 대본 분량: {chars}자",
        "- 수치 표기: 화면은 아라비아 숫자, 내레이션은 한글 발음(예: 천칠백구십삼억)",
        f"- 하단 고지: {DISCLAIMER}",
        "",
        "| 씬 | 배지 | 키워드 | 수치 카드 | 화면 문구 | 내레이션 | 겅태 |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for i, s in enumerate(video["scenes"], 1):
        cards = " / ".join(f"{c['label']} {c['value']}" for c in s["stats"])
        main = s["main_text"].replace("\n", " ")
        lines.append(f"| {i} | {s['badge']} | {s['keyword']} | {cards} | {main} | {s['voice']} | {s['character']} |")
    lines += ["", "## 연출 메모", "- 겅태 감정 매핑: 수급 반전 훅은 놀람/걱정, 수치 설명은 가리키기·설명, 마무리는 인사.", ""]
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
