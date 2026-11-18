# SHORTS DELIVERY — 11/18 외국인 현·선물·옵션 수급 (3회차 · 외국인 수급 편)

## 산출물
| 항목 | 경로 |
| --- | --- |
| 유튜브 쇼츠 MP4 | `downloads/Stock2_1118_외국인_현선물옵션_수급_칠판드로잉_쇼츠.mp4` (저장소 사본 `content/2026-11-18/04_shorts_foreign_flow/stock_chalkboard/chalkboard_shorts_video.mp4`) |
| 움직이는 미리보기 GIF | `downloads/Stock2_1118_미리보기.gif` (사본 `preview/moving_preview.gif`) |
| 씬 캡처 3장 | `downloads/Stock2_1118_scene_1~3.png` (사본 `preview/scene{1,2,3}_preview.png`) |
| 대본 | `content/2026-11-18/04_shorts_foreign_flow/stock_chalkboard/shorts_script.md` |
| 생성 스크립트 | `scripts/generate_stock_1118_foreign_flow_shorts.py` + `engine/stock_chalkboard_engine.py` |
| 칠판 드로잉 원본 6장 | `assets/chalkboard/stock1118/v2_scene1~6_*.png` |
| 검증 리포트 | `content/2026-11-18/04_shorts_foreign_flow/stock_chalkboard/render_report.json` |

## 규격 (ffmpeg 검증)
- 1080x1920 (SAR 1:1, DAR 9:16 세로), H.264 High, **25.00 fps CFR (57.65초)**
- 오디오 AAC LC 44.1kHz 모노, Edge-TTS `ko-KR-InJoonNeural` (+5%)
- 용량 3.71MB, mean_volume -20.5dB / max -3.8dB

## 구성 (6씬 · 58초)
| 씬 | 배지 | 노란 키워드 | 수치 카드 | 겅태 |
| --- | --- | --- | --- | --- |
| 1 | 현·선물 엇갈린 하루 | S = 0 혼조 | 현물 -3,338억 / 선물 -323계약 / 8766 S=0 (15:43 -40) | 놀람 |
| 2 | 장중엔 2,145계약 | 마감에 -1,920 | 14:27 +2,145계약 / 15:25 +1,597계약 / 15:45 -323계약 | 걱정 |
| 3 | 미결제도 줄었다 | 762계약 청산 | 미결제 166,759 → 165,997 / 762계약 감소 / 현물 종가 +878억 | 설명 |
| 4 | 베이시스 괴리 축소 | -5.15 → -2.84pt | 시장 -1.26pt / 이론 +1.58pt / 전일 -5.15pt | 가리키기 |
| 5 | 감마 +1,793억 | 위클리 콜이 130% | 총 GEX +1,793억 / 위클리(목) +2,336억 / 월물 -547억 | 놀람 |
| 6 | 완충은 하루짜리 | 792.5~795 콜 벽 | 792.5 +912억 / 795 +734억 / 만기 뒤 -543억 | 인사 |

## 업로드 문구안
- 제목: 장중에 산 선물 2,145계약, 종가에 다 되팔았습니다 (11/18 외국인 수급)
- 설명 첫 줄: 외국인 현물 -3,338억(4일째), 선물 장중 +2,145계약 → 종가 -323계약. 감마 +1,793억의 130%가 11/19 만기 위클리 콜입니다.
- 고지: 본 영상은 투자 권유가 아닌 시장 기록 및 정보 정리입니다.

## 고지
전 씬 하단 고정: "본 영상은 투자 권유가 아닌 시장 기록 및 정보 정리입니다."

## 출처
`content/2026-11-18/02_foreign_flow_analysis.md` (8766 KIS 실측, 18901 감마 프록시, 한국거래소 집계)
자매 저장소의 시황 편: `kst104/stock-analysis` `content/2026-11-18/03_shorts_market/`
