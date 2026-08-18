# 프로젝트 규칙

> 이 파일은 AI(코드 생성/수정 담당)를 위한 규칙입니다.
> 코드를 생성하거나 수정할 때 아래 규칙을 예외 없이 따르세요.
> 사용 위치: `CLAUDE.md`(Claude Code) / `.cursorrules`(Cursor) / 매 프롬프트 앞에 그대로 붙여넣기(ChatGPT 등)

---

## 프로젝트 개요
- 앱 종류: (예: iOS 네이티브 앱)
- 목적: (해커톤 데모용 — 1줄로 프로젝트가 무엇을 하는지 채워넣기)
- 대상 플랫폼: iOS, SwiftUI
- 백엔드/API: (사용 중이면 base URL, 인증 방식 채워넣기)

---

## 기술 스택 (고정값 — 임의로 바꾸지 말 것)
- 언어: Swift
- UI 프레임워크: SwiftUI
- 아키텍처: MVVM
- 최소 지원 버전: (iOS 버전 명시, 예: iOS 17+)
- 의존성 관리: Swift Package Manager (다른 방식 제안 금지)
- 비동기 처리: async/await 사용 (completion handler, Combine 새로 도입 금지 — 기존 코드에 이미 있는 경우만 유지)

**새 라이브러리를 추가해야 한다고 판단되면, 임의로 추가하지 말고 "이런 라이브러리가 필요해 보입니다"라고 먼저 알릴 것.**

---

## 아키텍처 규칙 (필수)

코드 생성/수정 시 반드시 아래 3계층을 분리한다.

1. **View** (`SwiftUI View`)
   - UI 렌더링과 사용자 입력 전달만 담당
   - 비즈니스 로직, API 호출, 데이터 가공 절대 포함 금지
2. **ViewModel** (`ObservableObject`)
   - `@Published` 프로퍼티로 상태 노출
   - API 호출, 데이터 변환, 유효성 검사 등 로직 담당
   - UI(SwiftUI import) 관련 코드 포함 금지
3. **Model** (`struct`, `Codable` 준수)
   - 순수 데이터 구조체
   - 로직 없음

새 화면을 만들 때는 항상 `View + ViewModel + Model` 세트로 생성한다. View 하나만 만들고 로직을 그 안에 넣지 않는다.

---

## 파일/폴더 구조 (반드시 준수)

```
Features/<화면명>/
  ├── <화면명>View.swift
  ├── <화면명>ViewModel.swift
  └── <화면명>Model.swift
Common/Components/     ← 2곳 이상에서 쓰이는 UI는 여기로 분리
Common/Extensions/
Network/
```

- 새 파일은 반드시 위 구조에 맞는 위치에 생성한다.
- 파일명은 타입명과 100% 동일하게 한다 (`LoginView.swift` 안에 `struct LoginView`).

---

## 네이밍 규칙 (필수)

| 대상 | 규칙 |
|---|---|
| 타입 (struct/class/enum/protocol) | UpperCamelCase |
| 변수, 함수, 프로퍼티 | lowerCamelCase |
| Bool 변수 | `is`, `has`, `should` 접두사 필수 |
| 약어(URL, ID, API) | 항상 대문자로 (`userID`, not `userId`) |

- 변수명을 줄이지 말 것 (`vm`, `d`, `tmp` 같은 축약 금지). 단, 클로저의 `$0` 등 관례적 표현은 허용.

---

## 코딩 규칙 (필수 — 위반 시 코드 반려됨)

1. **강제 언래핑(`!`) 금지.** 항상 `guard let` / `if let` / `??` 사용.
2. **강제 캐스팅(`as!`) 금지.** `as?` + 옵셔널 처리 사용.
3. **매직 넘버/문자열 금지.** 상수로 분리 (`let maxRetryCount = 3`).
4. 함수는 **하나의 책임만** 수행. 한 함수가 너무 길어지면(대략 40줄 이상) 분리 제안.
5. 에러 처리는 `try/catch` 또는 `Result` 타입으로 명시적으로 한다. 에러를 조용히 무시하지 않는다.
6. 네트워크 호출은 `async/await` + `Network/` 폴더의 클라이언트를 통해서만 한다. View나 ViewModel에서 `URLSession`을 직접 호출하지 않는다.
7. 접근 제어자는 기본적으로 필요한 최소 범위로 (`private`, `fileprivate` 적극 사용, 불필요한 `public` 지양).

---

## 코드 생성 시 항상 지킬 것

- 기존 코드 스타일이 컨벤션과 다르게 보여도, **새로 작성하는 코드는 이 문서 기준을 따른다.** (기존 코드를 기준으로 스타일을 따라가지 말 것)
- 요청받지 않은 리팩토링/구조 변경을 마음대로 하지 않는다. 필요하다고 판단되면 "~하는 게 좋아 보이는데 반영할까요?"로 먼저 물어본다.
- 코드만 요청받았을 때, 장황한 설명 없이 코드 위주로 응답한다. 설명은 꼭 필요한 경우 3줄 이내로.
- 주석은 "왜"를 설명할 때만 작성한다. 코드를 그대로 말로 옮기는 주석(`// i를 1 증가시킨다`) 금지.
- 더미 데이터/Mock이 필요하면 명확히 `// TODO: Mock 데이터, 실제 API 연동 필요`로 표시한다.

---

## 하지 말아야 할 것 (Do NOT)

- View 안에서 직접 API 호출하지 않기
- 강제 언래핑(`!`) 사용하지 않기
- 팀 컨벤션에 없는 새 아키텍처 패턴(예: TCA, VIPER) 임의 도입하지 않기
- 이미 있는 공용 컴포넌트(`Common/Components/`)를 확인 안 하고 중복 생성하지 않기
- Info.plist, 프로젝트 설정 파일을 요청 없이 수정하지 않기

---

## 이 프로젝트에서 자주 쓰는 패턴 (예시 템플릿)

```swift
// ViewModel 템플릿
@MainActor
final class ExampleViewModel: ObservableObject {
    @Published var isLoading = false
    @Published var items: [ExampleModel] = []
    @Published var errorMessage: String?

    private let apiClient: APIClient

    init(apiClient: APIClient = .shared) {
        self.apiClient = apiClient
    }

    func fetchItems() async {
        isLoading = true
        defer { isLoading = false }
        do {
            items = try await apiClient.fetchItems()
        } catch {
            errorMessage = error.localizedDescription
        }
    }
}
```

새 화면의 ViewModel을 만들 때 위 템플릿 구조(로딩 상태, 에러 상태, async 함수)를 기본값으로 따른다.

---

## 마지막 체크 (코드 제출 전 스스로 확인)

- [ ] View / ViewModel / Model 분리했는가
- [ ] 강제 언래핑, 강제 캐스팅 없는가
- [ ] 폴더 위치, 파일명이 규칙과 맞는가
- [ ] 네이밍 규칙을 따랐는가
- [ ] 에러 처리를 빼먹지 않았는가
