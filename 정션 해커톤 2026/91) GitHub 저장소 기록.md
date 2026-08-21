---
title: "정션 해커톤 2026 GitHub 저장소 기록"
date: 2026-08-21
updated: 2026-08-21
status: active
tags:
  - project/junction-2026
  - github
  - repository
related:
  - "[[00) 정션 해커톤 2026 - 프로젝트 허브]]"
  - "[[90) 작업 로그]]"
---

# GitHub 저장소 기록

## 위치

- 원격 저장소: [Youngmin322/junction-challenge5.1](https://github.com/Youngmin322/junction-challenge5.1)
- GitHub Wiki: [junction-challenge5.1 Wiki](https://github.com/Youngmin322/junction-challenge5.1/wiki)
- 로컬 경로: `/Users/e.j.l/Documents/Codex/정션2026/junction-challenge5.1`
- 기본 브랜치: `main`

## 팀 구성

| 역할 | 담당 |
| --- | --- |
| 기획 | 엔조, 사노 |
| 디자인 | 제이 |
| 개발 | 오웬 |

## 현재 저장소 성격

- 해커톤 준비 및 지식 관리용 문서 중심 저장소
- CBL 학습 문서 10개 포함
- README와 SwiftUI 개발 컨벤션 포함
- 세부 제품 주제와 구현 코드는 해커톤 진행 중 추가 예정
- Wiki는 문제 → 해결 → 검증 → 임팩트 → 피칭 순서의 뼈대를 제공

## 주요 변경 이력

### 한글 파일명 정규화

- 문제: macOS에서 새 클론 직후 CBL 문서 10개가 `untracked`로 표시됨
- 원인: 저장소 경로의 NFD/NFC Unicode 정규화 혼합
- 수정: 파일 본문은 유지하고 파일명만 NFC로 통일
- 브랜치: `fix/normalize-korean-filenames`
- 커밋: `5ba4112`
- PR: [#1](https://github.com/Youngmin322/junction-challenge5.1/pull/1)
- 병합: 2026-08-21 20:23 KST
- 병합 커밋: `f8dcec6`

## 연결 상태

- GitHub CLI 설치 및 계정 연결 완료
- Git HTTPS 인증을 GitHub CLI 자격 증명 공급자와 연결
- 인증 토큰 값은 이 노트에 기록하지 않음

## 저장소 운영 원칙

- 해커톤 주제 확정 전에는 컨벤션의 제품·API 관련 빈칸을 억지로 채우지 않는다.
- 팀 공유 저장소에 push하기 전 변경 범위와 diff를 확인한다.
- 의료·개인정보 또는 인증 정보는 공개 저장소에 올리지 않는다.
- 사실, 실험 결과, 검증 수치를 Wiki의 문제·해결·검증·임팩트 구조에 맞춰 누적한다.

