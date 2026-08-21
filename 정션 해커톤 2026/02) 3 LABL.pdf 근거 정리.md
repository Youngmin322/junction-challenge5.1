---
title: "3 LABL.pdf 근거 정리"
date: 2026-08-21
updated: 2026-08-21
status: tracking
tags:
  - project/junction-2026
  - track/lablup-furiosaai
  - evidence/pdf
related:
  - "[[00) 정션 해커톤 2026 - 프로젝트 허브]]"
  - "[[01) Lablup·FuriosaAI 트랙 브리프]]"
  - "[[01-1) 트랙 사실·추측·미확정 트래커]]"
source: "https://notebook.google.com/notebook/5c56229a-4ca6-4d1c-ba52-d0721c9a41a7"
---

# 3 LABL.pdf 근거 정리

## 조사 범위와 신뢰도

- 원문: Lablup 제공 자료 `3 LABL.pdf`
- 접근 경로: [팀 NotebookLM](https://notebook.google.com/notebook/5c56229a-4ca6-4d1c-ba52-d0721c9a41a7)
- 조사 방법: NotebookLM에 PDF만 근거로 답하도록 요청하고, 핵심 답변의 PDF 인용 세부정보와 화면 캡처 문구를 재검증함
- `확인`: PDF 본문 또는 캡처에 문구가 직접 표시됨
- `미확정`: PDF에 규칙이 없거나 화면 판독만으로 확정할 수 없음

> [!warning] 근거 사용 원칙
> NotebookLM의 해석 자체는 원문이 아니다. 아래에서 `확인`으로 표시한 내용도 실제 대회 포털이나 운영진 공지가 바뀌면 최신 안내를 우선한다.

## 즉시 적용할 확인 사실

| 항목 | 확인 내용 | 근거 |
| --- | --- | --- |
| 필수 결과물 | 문제 해결형 AI 에이전트 스쿼드와 Trace 기반 인터랙티브 시각화 | PDF Slide 87 |
| 평가 배점 | 벤치마크 40점, 시각화 30점, 토큰 효율성 30점 | PDF Slide 96 |
| 시각화 기준 | observability, interpretability, traceability, explainability, clarity, insightfulness | PDF Slide 96 인용 세부정보 |
| 제출 구성 | Squad Template JSON 1개와 트랙별 one-shot prompt 1개 | PDF Slide 83 캡처 |
| 템플릿 Checking | 무료이며 반복 횟수 제한 없음. Queue 제출 전에는 대기열에 들어가지 않음 | PDF Slide 83 캡처 |
| 제출 Queue | 팀당 동시 실행 1개, 대기 3개 | PDF Slide 83 캡처 |
| 제출 포털 | `https://submission.jxc.events.lablup.ai:8444` | PDF Slide 90 |
| 정식 평가 제출 비용 | 모델별 기준 단가의 100% 반영, 모든 제출 누적 | PDF Slide 96 |
| AI:GO Test Run 비용 | 모델별 기준 단가의 20%만 반영 | PDF Slide 96 |
| 제출 횟수 | 복수 제출 가능하지만 모든 제출 비용이 누적됨 | PDF Slide 96 인용 세부정보 |
| 공개 정보 | 실시간 리더보드, 실행별 점수, 모델별 토큰 수 | PDF Slide 96 |

정규화 사용 비용의 문서상 구조는 다음과 같다.

$$
\text{normalized cost} = \text{submission cost} \times 1.0 + \text{test run cost} \times 0.2
$$

단, 이 비용이나 순위를 실제 30점으로 변환하는 정확한 산식은 PDF에 없다.

## 제공 모델로 확인된 항목

| 모델 | PDF에 표시된 크기 | 근거 | 상태 |
| --- | --- | --- | --- |
| Qwen3.5 4B GGUF | 다운로드 약 2.6 GB, VRAM/Context 약 4.2 GB | Slide 86 | 확인 |
| Qwen3 4B (MLX) | 다운로드 약 2.1 GB, VRAM/Context 약 4.2 GB | Slide 86 | 확인 |
| Phi-3.5 Mini GGUF | 다운로드 약 2.2 GB, VRAM/Context 약 3.7 GB | Slide 86 | 확인 |
| Phi-3.5 Mini (MLX) | 다운로드 약 2.0 GB, VRAM/Context 약 3.7 GB | Slide 86 | 확인 |
| Gemma 3n E4B Instruct | 다운로드/가동 약 4.2/4.4 GB, `gemma-3n-E4B-it-Q4_K_M` | Slide 74 | 확인 |
| Qwen3-4B-Thinking-2507-Q4_K_M | 가동 약 2.3 GB | Slide 72 | 확인 |
| Qwen3-30B-A3B-Instruct-2507-FP8 | 모델명만 확인, 크기 불명 | Slide 84 | 부분 확인 |

> [!note] 모델 해석 주의
> `Qwen3-30B-A3B-Instruct-2507-FP8`이 원격 shared serving stack이라는 설명은 화면 정황에서 나온 추정이다. 실제 제공 방식과 역할별 사용 제한은 운영진 확인이 필요하다.

## PDF에서 확인되지 않은 핵심 규칙

- 벤치마크의 정확한 입력·출력 JSON 스키마와 예제
- 평가 문제·테스트 케이스의 사전 공개 여부
- 에이전트 수의 최소·최대 제한
- 에이전트별 역할과 모델의 매핑 제한
- 외부 API, 인터넷 검색, MCP 사용 가능 여부
- 코드 실행 환경, 지원 언어, 라이브러리, 파일 접근 범위
- 단일 실행의 시간 제한과 무한 루프 처리
- 실패·오류·타임아웃 시 0점 또는 부분 점수 규칙
- 토큰 효율성 비용/순위를 30점으로 바꾸는 정확한 산식
- 시각화 결과물의 최종 제출 형식과 호스팅 요구
- 최종 제출 마감 시각

## 자료 간 표현 차이

- PDF Slide 87은 시각화를 두 번째 결과물로 제시하므로 **필수로 취급**한다.
- 발표 자동 전사에는 시각화를 “recommend”한다고 기록되어 있다.
- 30점 배점까지 있으므로 구현 계획에서는 필수 결과물로 두되, 현장에서 제출 형식만 재확인한다.
- Slide 96은 Trace 시각화 평가 문구와 배점 헤더의 배치가 혼동될 수 있으나, 배점 자체는 40/30/30으로 표시된다.

## 운영진에게 우선 물을 질문

1. 벤치마크 입력·출력 스키마와 예제 문제를 받을 수 있는가?
2. 토큰 효율성 30점은 단순 비용 순위인가, 벤치마크 성능 대비 비용까지 반영하는가?
3. 한 Run의 시간 제한과 실패·예외·타임아웃의 채점 규칙은 무엇인가?
4. 외부 API·인터넷·코드 실행기·로컬 파일·추가 라이브러리는 어디까지 허용되는가?
5. 시각화는 GitHub 소스, 배포 URL, 발표 데모 중 무엇을 제출해야 하는가?
6. 최종 제출 마감 시각은 언제인가?

## 일정과 보상

- AI:GO 온보딩: 21:00–21:30, 21:30–22:00 — Slide 97
- 1위: 200만 원과 인당 5만 원 상당 굿즈
- 2위: 100만 원과 인당 5만 원 상당 굿즈
- 기업 탐방 및 현직자 커피챗·커리어챗 기회 — Slides 101–105

