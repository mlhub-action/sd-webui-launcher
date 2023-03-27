# SD Web UI 런처
[코랩](https://colab.research.google.com) 또는 [런팟](https://www.runpod.io)에서 [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)을 실행 시켜주는 웹 앱([Gradio](https://gradio.app/))
> 확장 프로그램이 아니라 별개 프로그램 입니다.
> 베타 버전이라 기능이 완벽하지 않거나 버그가 있을 수 있습니다
</br>

| 노트북 이름 | 설명 | 링크 |
| --- | --- | --- | 
| [SD Web UI 런처](https://github.com/mlhub-action/sd-webui-launcher/blob/main/notebooks/SD-Web-UI-Launcher.ipynb) | Stable Diffusion Web UI 런처 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mlhub-action/sd-webui-launcher/blob/main/notebooks/SD-Web-UI-Launcher.ipynb) | 
</br>

## 기능
- 코랩 또는 런팟 노트북에서 실행
- 코랩 사용시 구글 드라이브 연결
- 런처 설정 초기화, 가져오기, 내보내기
- 저장소, 확장, 모델 등 다운로드
- 확장, 모델, 실행 인자, 커밋 해시 등 즐겨찾기
- TODO: 즐겨찾기 내보내기/가져오기, 컨트롤넷 모델 추가 다운로드, SD Web UI 설정 내보내기/가져오기
</br>

## 알려진 문제
 - [TypeError: unsupported operand type(s) for |: 'type' and 'type'](https://github.com/mlhub-action/sd-webui-launcher/issues/2)
 - [Unexpected token '<', "<html> <h"... is not valid JSON](https://github.com/mlhub-action/sd-webui-launcher/issues/1)
</br>

## 업데이트
### v0.1.6 (2023-03-27)
#### 변경 내역
> 기능 개선
 - SD Web UI 설정 파일(config.json, ui-config.json) 위치를 작업디렉터리에 지정
 - 전체 실행 인자 표시 기능 추가, 회색 테마 적용
 - 확장 설치시 SD Web UI의 Check for updates 확인 기능 지원
</br>

### v0.1.5 (2023-03-27)
#### 변경 내역
- 컨트롤넷 모델 다운로드 버그 수정
</br>

### v0.1.4 (2023-03-27)
#### 변경 내역
- 확장 인덱스 링크 추가
- 구글 드라이브 연결시 기존 디렉토리 체크 후 연결
- 기본 설정 편집이 쉽도록 포맷팅
</br>

### v0.1.3 (2023-03-27)
#### 변경 내역
- 컨트롤넷 모델 다운로드 기능 추가
- 설정 내보내기시 한글 인코딩 문제 수정
</br>

### v0.1.2 (2023-03-26)
#### 변경 내역
- 커밋 해시 설정이 적용안되는 문제 수정
- 마지막 gradio==3.16.2 커밋 해시 즐겨찾기 추가
</br>

### v0.1.1 (2023-03-26)
#### 변경 내역
- 한글 패치 확장 즐겨찾기 추가
</br>

### v0.1.0 (2023-03-26)
#### 변경 내역
- 최초 릴리즈
</br>


## Credits
코랩 tcmalloc 관련 이슈 우회, https://github.com/toriato/easy-stable-diffusion