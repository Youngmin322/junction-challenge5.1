# junction-challenge5.1

Junction 해커톤에 참가하기 위해 모인 팀 저장소입니다. 팀 이름은 이 저장소 이름과 같은 **junction-challenge5.1**입니다.

## 팀 구성

| 역할 | 담당 |
| --- | --- |
| 기획 | 엔조, 사노 |
| 디자인 | 제이 |
| 개발 | 오웬 |

## 자료 관리

회의록, 조사 자료 같은 문서는 [GitHub 위키](https://github.com/Youngmin322/junction-challenge5.1/wiki)에 모아서 정리하기로 했습니다.

스킬 다운로드 하기 : https://gist.github.com/eunseo-com/5db07681ec25f6d8909d6e1c1fec0aec -> 링크 복붙해서 ai 에게 준 뒤 스킬로 만들어달라고 하면 됩니다.

위키에 새 자료를 넣을 때는 이 저장소의 [`wiki-organize.md`](./wiki-organize.md) Claude Code 스킬을 씁니다. AI에게 마크다운 파일이나 노션 페이지 URL을 주고 `/wiki-organize`를 실행하면, 알맞은 카테고리를 찾아 위키 페이지로 만들어주고 사이드바까지 자동으로 정리해줍니다.

**예시**

노션 페이지를 위키로 가져올 때:
```
/wiki-organize https://www.notion.so/우리팀/킥오프-회의록-abc123
```

문서를 바로 붙여넣을 때:
```
/wiki-organize
(여기에 회의록이나 조사 자료 텍스트를 그대로 붙여넣기)
```

위키 구조를 다시 정리하고 싶을 때는 인자 없이 그냥 `/wiki-organize`만 실행하면 됩니다.
