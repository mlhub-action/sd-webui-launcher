# SD Web UI 런처
로컬(Windows), [코랩](https://colab.research.google.com) 또는 [런팟](https://www.runpod.io)에서 [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)을 실행 시켜주는 웹 앱([Gradio](https://gradio.app/))
> 확장 프로그램이 아니라 별개 프로그램 입니다.
> 기능이 완벽하지 않거나 버그가 있을 수 있습니다
</br>

## 코랩 이용 제한사항
무료 이용시 SD Web UI 사용이 제한될 수 있습니다[[1]](https://research.google.com/colaboratory/faq.html#limitations-and-restrictions).

"Colab 리소스는 상호작용 사용 사례에 우선 할당됩니다. 일괄 연산, 다른 사용자에게 부정적인 영향을 줄 수 있는 작업, 정책을 우회하는 작업 등은 금지됩니다. 다음은 Colab 런타임에서 허용되지 않는 사항입니다."
</br>

| 노트북 이름 | 설명 | 코랩 링크 |
| --- | --- | --- | 
| [SD Web UI 런처](https://github.com/mlhub-action/sd-webui-launcher/blob/main/notebooks/SD-Web-UI-Launcher.ipynb) | Stable Diffusion Web UI 런처 | [![코랩에서 열기](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mlhub-action/sd-webui-launcher/blob/main/notebooks/SD-Web-UI-Launcher.ipynb) | 
</br>

## 사용법
- [코랩(Colab)](docs/colab/README.md)
- [런팟(RunPod)](docs/runpod/README.md)
- [로컬(Windows)](docs/local/README.md)
</br>

## 제공 기능
- 로컬, 코랩 또는 런팟 노트북으로 실행
- 코랩 사용시 구글 드라이브 연결해서 모델, 설정 파일 저장, 확장 설정 파일 복사
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
- 설정한 확장은 구글 드라이브에 저장 안됨. 확장 호환성을 위한 선택.
- 기본값으로 런처는 gradio.live로 연결되는데 웹 응답이 느린 경우 USE_GRADIO_LIVE 체크 해제하고 사용 권장
- 코랩 사용 환경 : ubuntu 20.04, python 3.9
- 런팟 사용 환경 : ubuntu 20.04, python 3.10, [runpod/pytorch 템플릿](https://hub.docker.com/r/runpod/pytorch/tags), venv 가상 환경
  > runpod/pytorch:3.10-1.13.1-116 <br> runpod/pytorch:3.10-2.0.0-117
- 로컬 사용 환경 : Windows 10, python 3.10, git, venv 가상 환경(강제)
</br>

## 알려진 문제
 - [Unexpected token '<', "<html> <h"... is not valid JSON](https://github.com/mlhub-action/sd-webui-launcher/issues/1)</br>
 - [DiffusionMapper has 859.52 M params](https://github.com/mlhub-action/sd-webui-launcher/issues/4)</br>
 - [PyTorch has CUDA Version=11.7 and torchvision has CUDA Version=11.8](https://github.com/mlhub-action/sd-webui-launcher/issues/5)</br>
 

## 업데이트
### v0.4.2 (2023-04-21)
#### 변경 내역
 - 코랩 무료 이용시 SD Web UI [사용이 제한](https://research.google.com/colaboratory/faq.html#limitations-and-restrictions)될 수 있습니다.
 - 파일 탐색기 앱(코랩 전용) 삭제 : 코랩 자체 파일 탐색기로 대체
</br>

### v0.4.1 (2023-04-17)
#### 변경 내역
 - 컨트롤넷 모델 이름과 설정 파일 이름이 같도록 수정
 - 임베딩 즐겨찾기 주소 변경 : 잦은 civitai.com 접속 장애 때문에 huggingface.co로
</br>

### v0.4.0 (2023-04-16)
#### 변경 내역
 - ControlNet v1.0/v1.1 모델 즐겨찾기 추가
 - RTX 40 시리즈 사용시, 속도 향상 안내 문구 추가
 - 확장 즐겨찾기 추가 : 3D Openpose Editor, LyCORIS, Regional Prompter, Segment Anything
</br>

### v0.3.9 (2023-04-08)
#### 변경 내역
 - 코랩/런팟 노트북 출력창에 표시되는 줄 수 제한, 기본값 40줄
</br>

### v0.3.8 (2023-04-06)
#### 변경 내역
 - mmcv 패키지 버전 업데이트로 ddetailer 확장 설치 안되는 문제 수정
 - ddetailer 의존 패키지 버전 명시 : openmim==0.3.7, mmcv-full==1.7.1, mmdet==2.28.2
</br>

### v0.3.7 (2023-04-06)
#### 변경 내역
 - 확장 탭에서 확장이 설치 안되는 문제 수정
 - [SD Web UI 경로 설정 예시](./docs/settings/README.md) 문서 추가
 - 구글 드라이브 연결시 style.cv 설정 파일 동기화
 - 확장별 설정 파일 위치 정확하게 설명
 - 확장 즐겨찾기 추가 : - Image browser
</br>

### v0.3.6 (2023-04-04)
#### 변경 내역
 - 가상 환경 사용 여부 기본값을 사용으로 변경, 호환성을 위해
 - 접속 방법 : cloudflare 추가
 - 시작시 CPU 정보 출력
 - 실행 인자 즐겨찾기 추가 : --reinstall-torch --reinstall-xformers
</br>

### v0.3.5 (2023-04-03)
#### 변경 내역
 - 사용법 문서 추가
 - ddetailer 확장 Torch 2 이상 버전에서 호환성 경고
</br>

### v0.3.4 (2023-04-02)
#### 변경 내역
 - 런팟 템플릿 업데이트로, 가상 환경 사용 강제
 - 즐겨찾기 실행 인자 추가: --disable-console-progressbars
</br>

### v0.3.3 (2023-04-02)
#### 변경 내역
 - 초보가 사용이 쉽도록, 코랩/런팟 노트북 실행해야 할 탐색기/런처 앱 넘버링, 과도한 정보 숨김
 - 코랩 런타임 연결 끊기 항목 추가
</br>

### v0.3.2 (2023-04-02)
#### 변경 내역
 - 확장이 설치되지 않았을 때, 구글 드라이브 확장 설정 파일을 복사 하지 않도록 수정
 - 마지막 설정 불러오기 기능 로컬일 때만 동작하도록 수정
 - 시작시 플랫폼, 그래픽 카드 정보 출력하도록 수정
</br>

### v0.3.1 (2023-04-01)
#### 변경 내역
 - 파일 로깅 기능 추가
 - pip 모듈 설치 개선
</br>

### v0.3.0 (2023-04-01)
#### 변경 내역
 - curl로 pip 모듈을 설치할 수 없는 문제 수정(SSL certificate 문제)
</br>

### v0.2.9 (2023-04-01)
#### 변경 내역
 - 확장 설정 파일이 여러번 복사되는 문제 수정
</br>

### v0.2.8 (2023-04-01)
#### 변경 내역
 - 구글 드라이브 연결시 확장 설정 파일 복사 기능 추가, (\*.json|extensions/sd-dynamic-prompts/wildcards/\*.txt)
   => \[작업 디렉터리 이름\]/extensions 아래 확장 폴더 구조를 유지해서 복사할 설정 파일 위치시켜 주세요
 - 로컬 터미널 빠른 편집 모드 설정 레지스트리 파일 추가
</br>

### v0.2.7 (2023-03-30)
#### 변경 내역
 - 설정 파일(config.json)이 구글 드라이브 연동와 안되는 문제 수정
 - 커밋 해시 즐겨찾기에 최근 5일간 변경 내역 자동 등록 기능 추가(두번째 실행 부터 저장소를 다운 받은 후)
</br>

### v0.2.6 (2023-03-30)
#### 변경 내역
 - 로컬(Windows) 설치 지원, 런처로-SD-Web-UI-실행.bat 배치 파일로 실행
 - Torch+xFormers 버전 선택 기능 추가, 기본값 빈칸
 - --no-gradio-queue 실행 인자를 기본 설정값으로 추가(현재 SD Web UI 로딩 문제로)
 - ddetailer 확장 설치시 미리 빌드된 패키지 설치 선택 기능 제거, 확인해 보니 불필요한 기능
 - ddetailer 확장 패치 적용 선택 기능 추가, No module named 'lib2to3' 문제 해결, 기본값 사용
 - 작업 디렉토리 이름 기본값 수정, 기본값 이름 없음
 - 마지막 설정 자동 불러오기 기능 추가(로컬만 지원)
 - 설정 내보내기 할 때, 편집이 쉽도록 들여쓰도록 수정
</br>

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

[pycloudflared](https://github.com/Bing-su/pycloudflared)
