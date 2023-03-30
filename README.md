# SD Web UI 런처
로컬(Windows), [코랩](https://colab.research.google.com) 또는 [런팟](https://www.runpod.io)에서 [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)을 실행 시켜주는 웹 앱([Gradio](https://gradio.app/))
> 확장 프로그램이 아니라 별개 프로그램 입니다.
> 기능이 완벽하지 않거나 버그가 있을 수 있습니다
</br>

| 노트북 이름 | 설명 | 링크 |
| --- | --- | --- | 
| [SD Web UI 런처](https://github.com/mlhub-action/sd-webui-launcher/blob/main/notebooks/SD-Web-UI-Launcher.ipynb) | Stable Diffusion Web UI 런처 | [![코랩에서 열기](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mlhub-action/sd-webui-launcher/blob/main/notebooks/SD-Web-UI-Launcher.ipynb) | 
</br>


## 제공 기능
- 코랩 또는 런팟 노트북으로 실행
- 코랩 사용시 구글 드라이브 연결해서 모델, 설정 파일 저장
- 작업 디렉터리, 확장, 모델, 접속 방법, 실행 인자, 저장소를 런처에서 설정
- 런처에서 설정한 파일 - 설정 초기화, 가져오기, 내보내기
- 확장, 모델, 저장소 등 자동 다운로드
- 확장, 모델, 실행 인자, 커밋 해시 등 즐겨찾기
</br>

## [원클릭 코랩](https://github.com/toriato/easy-stable-diffusion) 사용자 호환성
 - 작업 디렉터리 이름을 같게(예, SD) 하면
 - 모델, 로라, VAE를 그대로 사용할 수 있음
 - 설정 파일도 그대로 사용(config.json, ui-config.json)
 - 단, 확장은 지원 안함(일부 확장에서 구글 드라이브 경로 문제로 실행이 안되는 문제가 있어서 제외)
</br>

## 제한 사항
- 설정한 확장은 구글 드라이브에 저장 안됨. gradio 보안상 이유로 SD Web UI 앱 이외의 경로 접근 제한
- 기본값으로 런처는 gradio.live로 연결되는데 gradio.live가 응답이 느린 경우 USE_GRADIO_LIVE 체크 해제하고 사용 권장
- 코랩 사용 환경 : ubuntu 20.04, python 3.9, venv 가상 환경
- 런팟 사용 환경 : runpod/pytorch:3.10-1.13.1-116 템플릿, ubuntu 20.04, python 3.10, venv 가상 환경
- 로컬 사용 환경 : Windows 10, python 3.10, git
</br>

## 알려진 문제
 - [Unexpected token '<', "<html> <h"... is not valid JSON](https://github.com/mlhub-action/sd-webui-launcher/issues/1)
</br>

## 업데이트
### v0.2.5 (2023-03-29)
#### 변경 내역
 - 가상 환경 venv 사용 여부 선택 기능 추가, 기본값 미사용
 - 마지막 설정 다운로드 기능 추가
 - ddetailer 확장 설치시 미리 빌드된 패키지 설치 선택 기능 추가, 기본값 사용
</br>

### v0.2.4 (2023-03-29)
#### 변경 내역
 - 로컬(Windows) 설치 지원(테스트 중)
 - 컨트롤넷 다운로드 주소 검사
 - 실행 중 UI 상태 표시
</br>

### v0.2.3 (2023-03-28)
#### 변경 내역
 - 총 진행 단계 수 올바르게 계산하도록 수정
 - 실행까지 걸린 시간 출력
 - 코랩 구글 드라이브 연결시 작업 디렉토리 이름을 입력했는지 확인후 진행
 - 원클릭 코랩 사용자 호환성 설명 추가
</br>

### v0.2.2 (2023-03-28)
#### 변경 내역
- 작업 디렉터리 이름을 루트로 시작할 수 없도록 안내
- 커밋 해시 즐겨찾기 추가 "2023-03-27 gradio==3.23[⧉](https://github.com/AUTOMATIC1111/stable-diffusion-webui/commit/955df7751eef11bb7697e2d77f6b8a6226b21e13)"
</br>

### v0.2.1 (2023-03-28)
#### 변경 내역
- 실행 인자 즐겨 찾기 추가 : --no-gradio-queue, SD Web UI 응답이 느린 경우 사용
</br>

### v0.2.0 (2023-03-28)
#### 변경 내역
- 파일 탐색기 기능 추가
- 실행 인자 덮어 쓰기 기능 추가
- 노트북에 제공 기능, 제한 사항 설명 추가
</br>

### v0.1.9 (2023-03-28)
#### 변경 내역
- v0.1.8에서 코랩 tcmalloc 관련 이슈 우회 적용 안되는 문제 수정 
- ngrok 연결 주소 알기 쉽도록 한번 더 출력
- ngrok 인증 토큰? 설명 웹 주소 변경
- 즐겨찾기 편집 쉽도록 줄 바꿈
</br>

### v0.1.8 (2023-03-28)
#### 변경 내역
 - ngrok로 연결이 안되는 문제 수정
</br>

### v0.1.7 (2023-03-27)
#### 변경 내역
 - 코랩 tcmalloc 관련 이슈 [우회](https://github.com/toriato/easy-stable-diffusion/blob/1cb87d815dae953cbf7bb8c6df386f9e8b388b06/easy-stable-diffusion.py#L325), https://github.com/toriato/easy-stable-diffusion
 - 확장 즐겨찾기 목록 추가
</br>

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
코랩 tcmalloc 관련 이슈 [우회](https://github.com/toriato/easy-stable-diffusion/blob/1cb87d815dae953cbf7bb8c6df386f9e8b388b06/easy-stable-diffusion.py#L325), https://github.com/toriato/easy-stable-diffusion

파일 탐색기 [앱](https://github.com/Linaqruf/kohya-trainer/blob/main/kohya-LoRA-finetuner.ipynb), https://github.com/Linaqruf/kohya-trainer
