# stock-future — 외국인 현·선물·옵션 수급 분석 & 쇼츠 엔진

김승태 님의 **외국인 현물·선물·옵션 수급** 콘텐츠를 매일 같은 형식으로 만들어 내보내는 저장소입니다.
현물/선물/옵션 수급 원고 → 쇼츠 대본 → 칠판 분필 드로잉 영상(1080×1920)까지 한 흐름으로 나오고, 원천 수치는 실측 데이터 저장소 두 곳에서 가져옵니다.

- **8766** `kst104/futureoption` — 외국인 현물·선물 수급과 5대 변수 합산 투기지수 S (투기적 숏 / 헷지·차익성 매수 / 숏커버 판정)
- **18901** `kst104/futureoption1` — KOSPI200 옵션 딜러 감마(GEX)·바나(VEX), 감마 플립 레벨, 4사분면 방향성

> 이 저장소는 **외국인 수급 전용**입니다. 주식시장 마감(데일리 인사이트)은 자매 저장소 **`kst104/stock-analysis`** 에서 다룹니다.
> 본 저장소의 모든 영상·원고에는 투자 권유가 아닌 시장 기록·정보 정리라는 고지가 붙습니다.

---

## 1. 전체 구조

```
kst104/futureoption   (8766)  ─┐  외국인 현물·선물 수급 · 투기지수 S
kst104/futureoption1  (18901) ─┼─▶  stock-future  ──▶  수급 원고 1건 (블로그·노션)
                               │    (이 저장소)     └─▶  쇼츠 1편 (mp4·gif·씬 이미지·대본)
kst104/github.com-new  ────────┘  통합 콘텐츠 허브 ──▶  Notion 콘텐츠 보드
```

| 연결 대상 | 역할 | 저장 위치 / 포트 |
| --- | --- | --- |
| `kst104/futureoption` | 8766 투기지수(S) 엔진. 코스피 현물 외국인 누적, 선물 순매수 계약, 5대 변수 합산 판정(투기적 숏 / 헷지·차익성 매수) | 로컬 8766, private 저장소 |
| `kst104/futureoption1` | 18901 감마·GEX/VEX 프록시. 딜러 감마, 감마 플립 레벨, 4사분면 판정 | 로컬 18901, private 저장소 |
| `kst104/stock-analysis` | 자매 저장소 — **주식시장 마감 데일리 인사이트** 전용 | public 저장소 |
| `kst104/github.com-new` | 통합 콘텐츠 자동화 허브(로컬 8787 칸반·편집기). 이 저장소는 **외국인 수급 전용 트랙**으로 연결 | public 저장소 |
| Notion `[🚀 블로그 & 마케팅 콘텐츠 자동화 허브]` | 콘텐츠 기획·상태 관리 페이지 | `413cac32-3750-818b-b53a-c5048fdd8bb0` |
| Notion `📋 콘텐츠 보드` | 회차별 콘텐츠 행(상태·채널·GitHub 링크) | DB `2365fe4b-b1c3-40ba-9f89-089c01fc2c4a` (data source `32dd0b24-1e9a-4f85-8277-3dfee488a423`) |

### 데이터 → 콘텐츠 흐름

1. **수집(장마감 직후)** — 8766에서 외국인 현물 순매수(코스피·코스닥), 코스피200 선물 계약·금액, 미결제약정, 베이시스·프로그램 매매, 5대 변수 합산 투기지수 S를, 18901에서 딜러 감마·감마 플립·4사분면 판정을 읽습니다. 8766과 거래소 집계가 어긋나면(예: 11/16 외국인 현물 -13,769억 vs 집계 -13,838억) 두 값을 함께 적고 방향 일치 여부로 판단합니다.
2. **원고** — `content/YYYY-MM-DD/02_foreign_flow_analysis.md`(현·선물·옵션 수급 심층)를 작성하고 Notion 콘텐츠 보드에 행을 만듭니다.
3. **쇼츠** — 대본(`shorts_script.md`) 확정 후 `scripts/`의 생성기로 칠판 드로잉 영상을 렌더링합니다. 수치는 화면에 아라비아 숫자, 내레이션은 한글 발음(예: "일조 삼천칠백육십구억").
4. **검증·보관** — `render_report.json`(길이·해상도·코덱·용량), 움직이는 GIF 미리보기, 씬 캡처를 회차 폴더에 함께 남깁니다.
5. **발행** — 블로그는 16:10 이후, 쇼츠·릴스는 20:00. 발행 후 Notion 행의 `발행 URL`을 채웁니다.

---

## 2. 폴더 구조

```
stock-future/
├── content/
│   ├── 2026-11-16/                       # 1회차 (2026-11-16 월 장마감)
│   │   ├── 02_foreign_flow_analysis.md   # 외국인 현·선물·옵션 수급 심층 원고
│   │   └── 04_shorts_foreign_flow/       # 쇼츠 1편 (외국인 수급 심화)
│   ├── 2026-11-17/                       # 2회차 (2026-11-17 화 장마감)
│   ├── 2026-11-18/                       # 3회차 (2026-11-18 수 장마감)
│       ├── 02_foreign_flow_analysis.md   # 외국인 현·선물·옵션 수급 심층 원고
│       └── 04_shorts_foreign_flow/       # 쇼츠 1편 (외국인 수급 심화)
├── engine/
│   └── stock_chalkboard_engine.py        # 칠판 분필 드로잉 쇼츠 렌더 엔진
├── scripts/
│   ├── generate_stock_1116_foreign_flow_shorts.py  # 1회차 수급 쇼츠 생성 스크립트(씬 정의·렌더·리포트)
│   ├── generate_stock_1117_foreign_flow_shorts.py  # 2회차 수급 쇼츠 생성 스크립트
│   └── generate_stock_1118_foreign_flow_shorts.py  # 3회차 수급 쇼츠 생성 스크립트
├── assets/
│   ├── character/geongtae/               # 겅태 공식 3D 에셋 15종(감정·포즈·회전)
│   ├── chalkboard/stock1116/             # 1회차 수급 칠판 드로잉 원본 6장(v2)
│   ├── chalkboard/stock1117/             # 2회차 수급 칠판 드로잉 원본 6장(v2)
│   └── chalkboard/stock1118/             # 3회차 수급 칠판 드로잉 원본 6장(v2)
├── fonts/NanumGothic-Bold.ttf            # 렌더링 폰트 (OFL)
├── requirements.txt
└── .gitignore
```

회차 폴더 안의 구성(쇼츠):

| 파일 | 설명 |
| --- | --- |
| `stock_chalkboard/chalkboard_shorts_video.mp4` | 완성본 1080×1920, 25fps |
| `stock_chalkboard/preview/moving_preview.gif` | 움직이는 미리보기 |
| `stock_chalkboard/preview/scene{1,2,3}_preview.png` | 주요 장면 캡처 |
| `stock_chalkboard/scene{1..6}_*.png` | 씬별 칠판 드로잉 원본 |
| `stock_chalkboard/shorts_script.md` | 씬·배지·수치카드·내레이션·겅태 연기 대본 |
| `stock_chalkboard/render_report.json` | 길이·용량·스트림 검증 리포트 |
| `SHORTS_DELIVERY.md` | 납품 요약(규격·씬 흐름·업로드 문구) |

---

## 3. 다시 만들기 (단독 실행)

```bash
git clone https://github.com/kst104/stock-future.git
cd stock-future
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/generate_stock_1116_foreign_flow_shorts.py
```

- 렌더 결과 mp4는 기본으로 `output/` 에 저장되고, 회차 폴더(`content/2026-11-16/04_shorts_foreign_flow/`)로 사본이 들어갑니다.
- 경로는 모두 **저장소 루트 기준 상대경로**입니다. 환경변수로 바꿀 수 있습니다.
  - `STOCK_SHORTS_OUTPUT` : mp4 출력 폴더
  - `STOCK_CHALK_ART_DIR` : 칠판 드로잉 원본 폴더
  - `GEONGTAE_ASSET_DIR` : 겅태 캐릭터 PNG 폴더
  - `STOCK_FONT_BOLD` : 폰트 파일 경로
- 음성은 Edge-TTS `ko-KR-InJoonNeural`(+5%)를 쓰므로 인터넷 연결이 필요합니다. ffmpeg는 `imageio-ffmpeg` 동봉 바이너리를 우선 사용하고, 없으면 시스템 `ffmpeg`를 씁니다.
- 새 회차는 `scripts/generate_stock_1116_foreign_flow_shorts.py`를 복사해 `VIDEO`의 씬 정의(배지·키워드·수치카드·내레이션·겅태 감정)를 그날 수치로 바꾸고, `content/YYYY-MM-DD/` 폴더를 새로 만듭니다.

---

## 4. 회차별 결과물

### 2026-11-16 (월) 1회차

| 구분 | 파일 | 내용 |
| --- | --- | --- |
| 원고 | `content/2026-11-16/02_foreign_flow_analysis.md` | 현물 -1조3,769억(집계 -1조3,838억) / 선물 +1,620계약(+3,239억), 마감 동시호가 반전, 8766 S=-60(헷지·차익성 매수), 18901 감마 플립 793.01 아래 2사분면 |
| 쇼츠 | `content/2026-11-16/04_shorts_foreign_flow/stock_chalkboard/` | "장중 투기적 숏, 종가는 헷지" — 6씬, 수급 심화 |
| 엔진 | `engine/stock_chalkboard_engine.py` | 칠판 보드·수치 카드·겅태 인서트·면책 고지 상시 노출 |
| 생성기 | `scripts/generate_stock_1116_foreign_flow_shorts.py` | 씬 정의 + 렌더 + 검증 리포트 자동 생성 |

### 2026-11-17 (화) 2회차

| 구분 | 파일 | 내용 |
| --- | --- | --- |
| 원고 | `content/2026-11-17/02_foreign_flow_analysis.md` | 현물 -1조4,459억(집계 -1조4,430억) / 선물 +1,582계약(+3,037억), 장중 한 번도 마이너스 없음·투기적 숏 0회, 미결제 +8,140계약, 베이시스 괴리 -5.15pt, 콜 -19.9억·풋 +3.19억, 18901 감마 +230.8억(플립 760.63 위, 1사분면 약) |
| 쇼츠 | `content/2026-11-17/04_shorts_foreign_flow/stock_chalkboard/` | "현물은 팔고 선물은 사흘째 샀다" — 6씬 60.0초, 수급 심화 |
| 생성기 | `scripts/generate_stock_1117_foreign_flow_shorts.py` | 2회차 씬 정의 + 렌더 + 검증 리포트 |
| 엔진 | `engine/stock_chalkboard_engine.py` | 칠판 보드·수치 카드·겅태 인서트·면책 고지 상시 노출(공용) |

### 2026-11-18 (수) 3회차

| 구분 | 파일 | 내용 |
| --- | --- | --- |
| 원고 | `content/2026-11-18/02_foreign_flow_analysis.md` | 현물 -3,338억(8766 -3,339억, 4일째) / 선물 장중 +2,145 → 종가 -323계약(-681억), 마지막 20분 1,920계약 반전·미결제 -762계약, 8766 S 0 혼조(15:43 -40, 투기적 롱 4표본·숏 0표본), 베이시스 괴리 -2.84pt(전일 -5.15), 콜 +3.21억·풋 -10.44억, 18901 감마 +1,793억(플립 761.59 위, 1사분면 강도 554계약, 위클리(목) +2,336억이 130%) |
| 쇼츠 | `content/2026-11-18/04_shorts_foreign_flow/stock_chalkboard/` | "장중에 산 선물을 종가에 다 되팔았다" — 6씬 57.7초, 수급 심화 |
| 생성기 | `scripts/generate_stock_1118_foreign_flow_shorts.py` | 3회차 씬 정의 + 렌더 + 검증 리포트 |

---

## 5. 표기·검수 규칙

- 하단 면책 고지 상시 노출: **"본 영상은 투자 권유가 아닌 시장 기록 및 정보 정리입니다."**
- 8766 수급 수치와 거래소 집계가 다르면 **두 값 모두** 표기하고 차이(집계 시점·결제 기준)를 밝힙니다.
- 확인되지 않은 종목별 수급은 "확인 안 됨"으로 남기고 추정으로 채우지 않습니다.
- 내레이션 숫자는 한글 발음, 화면 숫자는 아라비아 숫자.
- 겅태 연기: 급락·반전 훅은 놀람/걱정, 수치 설명은 가리키기·설명, 마무리는 환호·인사.

---

## 6. 관련 저장소

- 자매 저장소(주식시장 마감): <https://github.com/kst104/stock-analysis>
- 통합 콘텐츠 허브: <https://github.com/kst104/github.com-new>
- 8766 투기지수 엔진: `kst104/futureoption` (private)
- 18901 감마 프록시: `kst104/futureoption1` (private)
