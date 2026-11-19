# SHORTS DELIVERY — 11/19 외국인 현·선물·옵션 수급 (4회차 · 수급 편)

## 산출물
| 항목 | 경로 |
| --- | --- |
| 유튜브 쇼츠 MP4 | `downloads/Stock2_1119_외국인_현선물옵션_수급_칠판드로잉_쇼츠.mp4` (저장소 사본 `content/2026-11-19/04_shorts_foreign_flow/stock_chalkboard/chalkboard_shorts_video.mp4`) |
| 움직이는 미리보기 GIF | `downloads/Stock2_1119_미리보기.gif` (사본 `preview/moving_preview.gif`) |
| 씬 캡처 3장 | `downloads/Stock2_1119_scene_1~3.png` (사본 `preview/scene{1,2,3}_preview.png`) |
| 대본 | `content/2026-11-19/04_shorts_foreign_flow/stock_chalkboard/shorts_script.md` |
| 생성 스크립트 | `scripts/generate_stock_1119_foreign_flow_shorts.py` + `engine/stock_chalkboard_engine.py` |
| 칠판 드로잉 원본 6장 | `assets/chalkboard/stock1119/v2_scene1~6_*.png` |
| 검증 리포트 | `content/2026-11-19/04_shorts_foreign_flow/stock_chalkboard/render_report.json` |

## 규격 (ffmpeg 검증)
- 1080x1920 (SAR 1:1, DAR 9:16 세로), H.264 High, **25.00 fps CFR (49.10초)**
- 오디오 AAC LC 44.1kHz 모노, Edge-TTS `ko-KR-InJoonNeural` (+5%)
- 용량 3.01MB

## 구성 (6씬 · 49초)
| 씬 | 배지 | 노란 키워드 | 수치 카드 | 겅태 |
| --- | --- | --- | --- | --- |
| 1 | 현물은 팔고 선물은 샀다 | 현물 -4,036억 | 현물 -4,036억 / 선물 +342계약 / S = 0 혼조 | 걱정 |
| 2 | 장중엔 1,243계약 | 낮에 산 걸 되돌림 | 13:21 +1,243 / 15:15 +329 / 종가 +342 | 놀람 |
| 3 | 미결제 1.39% 증가 | 신규 구축 | 184,104계약 / +2,521 / 5일 전 대비 +10.82% | 가리키기 |
| 4 | 베이시스 할인 유지 | -3.10pt | 시장 -1.59pt / 이론 +1.51pt / 괴리 -3.10pt | 설명 |
| 5 | 만기 감마 1조 3,080억 | 795 콜 +1조 1,183억 | 총 감마 +1조 3,080억 / 위클리 +1조 3,130억 / 월물 -166억 | 가리키기 |
| 6 | 만기 뒤 플립 799.5 | -50억 숏감마 | 만기 후 -50억 / 플립 799.5 / 오전 최저 -1,899억 | 인사 |

## 업로드 문구안
- 제목: 낮에 산 선물을 종가에 되돌렸습니다 (11/19 외국인 수급)
- 설명 첫 줄: 외국인 현물 -4,036억(5일째), 선물 장중 +1,243계약에서 종가 +342계약. 만기 콜 감마 1조 3,080억은 오늘로 사라졌습니다.
- 고지: 본 영상은 투자 권유가 아닌 시장 기록 및 정보 정리입니다.

## 고지
전 씬 하단 고정: "본 영상은 투자 권유가 아닌 시장 기록 및 정보 정리입니다."

## 출처
`content/2026-11-19/02_foreign_flow_analysis.md` (8766 5대 변수, 18901 감마·베이시스, 한국거래소 집계)
자매 저장소의 시황 편: `kst104/stock-analysis` `content/2026-11-19/03_shorts_market/`
