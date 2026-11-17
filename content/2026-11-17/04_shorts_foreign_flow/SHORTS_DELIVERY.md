# SHORTS DELIVERY — 11/17 외국인 현·선물·옵션 수급 (2회차 · 외국인 수급 편)

## 산출물
| 항목 | 경로 |
| --- | --- |
| 유튜브 쇼츠 MP4 | `downloads/Stock2_1117_외국인_현선물옵션_수급_칠판드로잉_쇼츠.mp4` (저장소 사본 `content/2026-11-17/04_shorts_foreign_flow/stock_chalkboard/chalkboard_shorts_video.mp4`) |
| 움직이는 미리보기 GIF | `downloads/Stock2_1117_미리보기.gif` (사본 `preview/moving_preview.gif`) |
| 씬 캡처 3장 | `downloads/Stock2_1117_scene_1~3.png` (사본 `preview/scene{1,2,3}_preview.png`) |
| 대본 | `content/2026-11-17/04_shorts_foreign_flow/stock_chalkboard/shorts_script.md` |
| 생성 스크립트 | `scripts/generate_stock_1117_foreign_flow_shorts.py` + `engine/stock_chalkboard_engine.py` |
| 칠판 드로잉 원본 6장 | `assets/chalkboard/stock1117/v2_scene1~6_*.png` |
| 검증 리포트 | `content/2026-11-17/04_shorts_foreign_flow/stock_chalkboard/render_report.json` |

## 규격 (ffmpeg 검증)
- 1080x1920 (SAR 1:1, DAR 9:16 세로), H.264 High, **25.00 fps CFR (1,498프레임 = 59.95초)**
- 오디오 AAC LC 44.1kHz 모노, Edge-TTS `ko-KR-InJoonNeural` (+5%)
- 용량 4.05MB, mean_volume -20.5dB / max -3.6dB

## 구성 (6씬 · 60초)
| 씬 | 배지 | 노란 키워드 | 수치 카드 | 겅태 |
| --- | --- | --- | --- | --- |
| 1 | 현·선물 역방향 3일째 | 헷지·차익성 매수 | 현물 -1조4,459억 / 선물 +1,582계약(+3,037억) / 8766 S=-60 | 놀람 |
| 2 | 장중 궤적이 달랐습니다 | 투기적 숏 0회 | 09:32 +59계약 / 11:38 +1,562계약 / 15:45 +1,582계약 | 가리키기 |
| 3 | 베이시스가 말해줍니다 | 괴리 -5.15pt | 미결제 179,208계약(+8,140) / 시장 베이시스 -3.54pt / 괴리 -5.15pt | 설명 |
| 4 | 옵션은 반대 방향 | 풋 +3,794계약 | 콜 -19.9억(-2,578계약) / 풋 +3.19억(+3,794계약) / 콜-풋 차 -23.1억 | 걱정 |
| 5 | 18901 감마 전환 | 플립 760.63 | 딜러 감마 +230.8억 / 플립 760.63 / 헤지 강도 83.7계약 | 놀람 |
| 6 | 만기가 지나면 사라집니다 | 11/19 위클리 만기 | 위클리(목) +977.3억 / 월물 202612 -742.6억 / 확인 조건 현물 순매수 | 인사 |

## 업로드 문구안
- 제목: 현물은 팔고 선물은 사흘째 샀습니다 (11/17 외국인 수급)
- 설명 첫 줄: 현물 -1조4,459억, 선물 +1,582계약. 장중 한 번도 마이너스로 가지 않은 하루였습니다.
- 고지: 본 영상은 투자 권유가 아닌 시장 기록 및 정보 정리입니다.

## 고지
전 씬 하단 고정: "본 영상은 투자 권유가 아닌 시장 기록 및 정보 정리입니다."

## 출처
`content/2026-11-17/02_foreign_flow_analysis.md` (8766 KIS 조회, 한국거래소 집계, 18901 감마·GEX/VEX)
시황 편: `kst104/stock-analysis` `content/2026-11-17/03_shorts_market/`
