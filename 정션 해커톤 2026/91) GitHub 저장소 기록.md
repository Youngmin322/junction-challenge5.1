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
- 현재 로컬 경로: `/Users/e.j.l/Documents/정션2026/junction-challenge5.1`
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

### 작업 문서 공유

- 브랜치: `DocsShare`
- 커밋: `7e382f9 정션 해커톤 작업 문서 공유`
- 정션 작업 산출물 7개를 `정션 해커톤 2026/` 폴더에 공유
- 저장소가 공개 상태이므로 개인 프로필·지원서·팀 갈등 회고가 포함된 `시작전/` 문서는 제외

### 트랙 변경에 따른 로컬 정리

- 팀 결정에 따라 활성 트랙을 Microsoft Korea × 경상북도 공공데이터 트랙으로 변경
- Lablup 전용 브리프·근거·자동 전사는 로컬 `DocsShare` 작업 트리에서 제거 대상으로 정리
- 공공데이터 트랙 브리프·근거·트래커·허브·로그를 추가 또는 갱신
- 이후 사용자 요청에 따라 `DocsShare` 브랜치에 커밋·원격 반영 진행

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
