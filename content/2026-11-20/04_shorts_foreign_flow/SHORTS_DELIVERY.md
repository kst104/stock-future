# SHORTS DELIVERY — 11/20 외국인 수급 (5회차 · 외국인 수급 편 · 올.주.선.이 3단 레이아웃)

## 산출물
| 항목 | 경로 |
| --- | --- |
| 유튜브 쇼츠 MP4 | `downloads/Stock2_1120_외국인_현선물옵션_수급_칠판드로잉_쇼츠.mp4` (저장소 사본 `content/2026-11-20/04_shorts_foreign_flow/stock_chalkboard/chalkboard_shorts_video.mp4`) |
| 움직이는 미리보기 GIF | `downloads/Stock2_1120_미리보기.gif` (사본 `preview/moving_preview.gif`) |
| 씬 캡처 3장 | `downloads/Stock2_1120_scene_1~3.png` (사본 `preview/scene{1,2,3}_preview.png`) |
| 대본 | `content/2026-11-20/04_shorts_foreign_flow/stock_chalkboard/shorts_script.md` |
| 생성 스크립트 | `scripts/generate_stock_1120_foreign_flow_shorts.py` + `engine/stock_jaljab_engine.py` |
| 칠판 드로잉 원본 6장 | `assets/chalkboard/stock1120/v2_scene1~6_*.png` |
| 검증 리포트 | `content/2026-11-20/04_shorts_foreign_flow/stock_chalkboard/render_report.json` |

## 규격 (ffmpeg 검증)
- 1080x1920 (세로 9:16), H.264, 25.00 fps, 55.97초, 3.29MB
- 오디오 AAC 44.1kHz, Edge-TTS `ko-KR-InJoonNeural` (+5%)
- 상단 0~540px 흰 배경: `올바른 주식·선물 이해하기` + 네이비(#1E3A8A) 박스 `올.주.선.이 · <주제>`
- 중단 540~1400px: 칠판 아트 1080x860, 하단 중앙 한 줄 자막(흰 글씨·검정 외곽선)
- 하단 1400~1920px 흰 배경: y=1422 `올.주.선.이 · 투자 참고용 정보 정리`
- 시작 0.0~2.0초 `구독·알림·좋아요는 힘이 됩니다` 배지

## 구성 (6씬 · 56초)
| 씬 | 주제 | 자막 |
| --- | --- | --- |
| 1 | 장중 S=+80 | 장중 판정 · 투기적 숏 |
| 2 | 동방향 매도 | 현물 -1조2,682억 · 선물 -3,297계약 |
| 3 | 베이시스 괴리 | 시장 -1.79pt · 이론 +1.36pt · 괴리 -3.15pt |
| 4 | 숏 되사기 | 15:30 -3,297 · 15:45 +504계약 |
| 5 | 미결제 감소 | 169,223 · 168,696계약 |
| 6 | 최종 S=-40 | 헷지·차익성 매수 · 선물 +923억 |

## 업로드 문구안
- 제목: 외국인은 장중 투기적 숏, 마감 뒤 숏을 닫았다 (11/20 수급)
- 설명 첫 줄: 장중 외국인 선물 -3,297계약, 투기지수 +80. 시간외 단일가에서 3,568계약을 되사 +504계약, 미결제 527계약 감소. 최종 판정 S -40.
- 고지: 본 영상은 투자 권유가 아닌 시장 기록 및 정보 정리입니다.

## 유튜브 업로드 (2026-11-21 완료)
| 항목 | 값 |
| --- | --- |
| 채널 | 올바른 주식·선물 이해하기(올.주.선.이) `@oljusuni` (`UC7yGPQdpVraizH7ANQ--voQ`) |
| URL | https://youtube.com/shorts/PojPw9YQgG0 |
| 제목 | [11/20 수급] 외국인, 장중 투기적 숏 쌓고 마감 뒤 되샀다 #선물옵션 #올주선이 #Shorts |
| 공개 상태 | 공개(Public) · 아동용 아님 · 0:56 · 2026. 11. 21. 게시 |

## 출처
`content/2026-11-20/02_foreign_flow_analysis.md` (8766 KIS 분 단위 표본, 18901 감마·나침반)
자매 저장소의 시장 마감 편: `kst104/stock-analysis` `content/2026-11-20/03_shorts_market/`
