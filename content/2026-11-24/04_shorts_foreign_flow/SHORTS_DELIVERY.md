# SHORTS DELIVERY — 11/24 외국인 수급 (7회차 · 수급 편 · 올.주.선.이 3단 레이아웃)

## 산출물
| 항목 | 경로 |
| --- | --- |
| 유튜브 쇼츠 MP4 | `downloads/Stock2_1124_외국인_현선물옵션_수급_칠판드로잉_쇼츠.mp4` (저장소 사본 `content/2026-11-24/04_shorts_foreign_flow/stock_chalkboard/chalkboard_shorts_video.mp4`) |
| 마지막 2초 컷 PNG | `downloads/Stock2_1124_마지막2초컷.png` (사본 `preview/last_cut.png`) |
| 움직이는 미리보기 GIF | `downloads/Stock2_1124_미리보기.gif` (사본 `preview/moving_preview.gif`) |
| 씬 캡처 3장 | `downloads/Stock2_1124_scene_1~3.png` (사본 `preview/scene{1,2,3}_preview.png`) |
| 대본 | `content/2026-11-24/04_shorts_foreign_flow/stock_chalkboard/shorts_script.md` |
| 생성 스크립트 | `scripts/generate_stock_1124_foreign_flow_shorts.py` + `engine/stock_jaljab_engine.py` |
| 칠판 드로잉 원본 5장 | `assets/chalkboard/stock1124/v2_scene1~5_*.png` |
| 방향성 누적 기록 | `direction_accuracy.json` (11/24 적중 1/1, 100.0%) |
| 검증 리포트 | `content/2026-11-24/04_shorts_foreign_flow/stock_chalkboard/render_report.json` |

## 규격 (ffprobe 검증)
- 1080x1920 (세로 9:16), H.264, 25.00 fps, **58.12초**, 2.94MB
- 오디오 AAC 44.1kHz, Edge-TTS `ko-KR-SunHiNeural` (+5%)
- 3단 레이아웃(상단 흰색·중단 칠판 1080x860·하단 흰색), 시작 0.0~2.0초 구독 배지
- 마지막 컷: `오늘의 방향 ▲ 강위` / `내일의 예상 ▲ 강위`, 우측 상단 `11/23~ 적중률 100.0% (1/1)`, 마지막 2초 정지 유지

## 타임스탬프 목차 (실제 씬 시작 시각, MM:SS)
| 시각 | 구간 | 내용 |
| --- | --- | --- |
| 00:00 | 외국인 vs 기관 | 선물 외국인 +3,604계약, 기관 -3,786계약 |
| 00:10 | 미결제 +646계약 | 173,213계약, 7% 상승에 증가는 작다 |
| 00:21 | 마지막 1시간 -5,281 | 14:44 +9,035계약 → 종가 +3,604계약 |
| 00:32 | 콜 +4,135 · 풋 +1,289 | P/C Ratio 0.79, 콜 우세 |
| 00:42 | 감마 플립 770.83 | 순감마 +91억, 종가 778.68은 플립 위 |
| 00:50 | 오늘·내일 방향 | ▲ 강위 / ▲ 강위 + 적중률 100.0% (1/1), 2초 정지 |

## 업로드 문구안
- 제목: [11/24 수급] 선물 +3,604계약, 그런데 마지막 1시간에 5,281계약을 팔았다
- 설명 첫 줄: 외국인 선물 누적은 +3,604계약인데, 14시 44분 고점 +9,035계약에서 5,431계약을 덜어냈습니다. 미결제는 646계약만 늘었고 베이시스는 -0.58입니다.
- 고지: 본 영상은 투자 권유가 아닌 시장 기록 및 정보 정리입니다.

## 해시태그 (13개 · #Shorts 뒤 앞 5개 4글자 이내)
`#Shorts #선물 #수급 #옵션 #감마 #외국인 #미결제약정 #베이시스 #숏커버 #프로그램매매 #코스피200 #수급분석 #올주선이`

## 출처
`content/2026-11-24/02_foreign_flow_analysis.md` (signals.kr 16:10 집계, KRX·한국투자증권 시세 기반)
