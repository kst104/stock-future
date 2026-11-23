# SHORTS DELIVERY — 11/23 외국인 수급 (6회차 · 수급 편 · 올.주.선.이 3단 레이아웃)

## 산출물
| 항목 | 경로 |
| --- | --- |
| 유튜브 쇼츠 MP4 | `downloads/Stock2_1123_외국인_현선물옵션_수급_칠판드로잉_쇼츠.mp4` (저장소 사본 `content/2026-11-23/04_shorts_foreign_flow/stock_chalkboard/chalkboard_shorts_video.mp4`) |
| 움직이는 미리보기 GIF | `downloads/Stock2_1123_미리보기.gif` (사본 `preview/moving_preview.gif`) |
| 씬 캡처 3장 | `downloads/Stock2_1123_scene_1~3.png` (사본 `preview/scene{1,2,3}_preview.png`) |
| 대본 | `content/2026-11-23/04_shorts_foreign_flow/stock_chalkboard/shorts_script.md` |
| 생성 스크립트 | `scripts/generate_stock_1123_foreign_flow_shorts.py` + `engine/stock_jaljab_engine.py` |
| 칠판 드로잉 원본 6장 | `assets/chalkboard/stock1123/v2_scene1~6_*.png` |
| 방향성 누적 기록 | `direction_accuracy.json` (11/23 첫 기록) |
| 검증 리포트 | `content/2026-11-23/04_shorts_foreign_flow/stock_chalkboard/render_report.json` |

## 규격 (ffmpeg 검증)
- 1080x1920 (세로 9:16), H.264, 25.00 fps, 59.00초, 2.72MB
- 오디오 AAC 44.1kHz, Edge-TTS `ko-KR-SunHiNeural` (+5%)
- 3단 레이아웃(상단 흰색·중단 칠판 1080x860·하단 흰색), 시작 0~2초 구독 배지
- 마지막 컷: `오늘의 방향: 중간하방` / `내일의 예상: 약간 상방 또는 횡보`, 우측 상단 `11/23~ 집계 시작`, 마지막 2초 정지 유지

## 구성 (6씬 + 방향 컷)
| 씬 | 주제 | 자막 |
| --- | --- | --- |
| 1 | 투기지수 -20 | 혼조·헷지 · 투기 4조건 중 1개 |
| 2 | 현물 매도·선물 매수 | 현물 -2,472억 · 선물 +1,681계약 |
| 3 | 괴리 -5.32pt | 시장 -4.18pt · 이론 +1.14pt |
| 4 | 3시 숏 → 3시 30분 롱 | 15:20 -657계약 · 15:45 +1,681계약 |
| 5 | 미결제 +3,871 | 172,567계약 · 최근 30분 -1,638계약 |
| 6 | 콜 매도·플립 732.12 | 콜 -88.8억 · ATM IV 66.9% |
| 7 | 오늘·내일 방향 | 오늘의 방향: 중간하방 / 내일의 예상: 약간 상방 또는 횡보 |

## 업로드 문구안
- 제목: 장 막판 30분에 선물 2,338계약 매수 (11/23 수급)
- 설명 첫 줄: 외국인 투기지수 -20 혼조·헷지. 현물 -2,472억, 선물 +1,681계약, 괴리 -5.32pt. 15시 20분 -657계약에서 15시 45분 +1,681계약으로 뒤집혔습니다.
- 고지: 본 영상은 투자 권유가 아닌 시장 기록 및 정보 정리입니다.

## 출처
`content/2026-11-23/02_foreign_flow_analysis.md` (8766 KIS 실측, 18901 감마)
