# SD Web UI 런처 사용법 - 런팟(RunPod)

## 1. 선결 조건 : 런팟 가입 및 10달러 결제
> 가입 및 결제까지 완료해 주세요.
<br>

## 2. 메뉴에서 서버 찾기
> 런팟 홈페이지 Browse Servers 버튼을 클릭해 주세요.

![image](../images/runpod/01.%EB%9F%B0%ED%8C%9F.png)
<br>
<br>

## 3. 업로드 속도가 높은 순으로 정렬
> 서버 기준 업로드 속도가 내 컴퓨터로 다운로드 속도입니다.

![image](../images/runpod/02.%EB%9F%B0%ED%8C%9F.png)
<br>
<br>

## 4. 사용할 GPU와 시간당 달러 확인 후 more 버튼 클릭
> 팁: 가성비가 좋은 3070, 3080, 3090 중에서 선택하세요.

![image](../images/runpod/03.%EB%9F%B0%ED%8C%9F.png)
<br>
<br>

## 5. 대여할 수 있는 서버 목록 확인
> Quadro RTX 5000은 2개 중 1개만 대여 가능 확인 후<br>
> Deploy 버튼을 클릭해 주세요.

![image](../images/runpod/04.%EB%9F%B0%ED%8C%9F.png)
<br>
<br>

## 6. RunPod Pytorch 템플릿 선택
> 선택 : runpod/pytorch:3.10-1.13.1-116 또는 runpod/pytorch:3.10-2.0.0-117<br>
> 체크 : Start Jupyter Notebook<br>
> 하고 Deploy 버튼을 클릭해 주세요.

![image](../images/runpod/05.%EB%9F%B0%ED%8C%9F.png)
<br>
<br>

## 7. My Pods로 가기

![image](../images/runpod/06.%EB%9F%B0%ED%8C%9F.png)
<br>
<br>

## 8. Connect 버튼 클릭
> Pods 상태가 Running인지 확인해 주세요.

![image](../images/runpod/07.%EB%9F%B0%ED%8C%9F.png)
<br>
<br>

## 9. 주피터 노트북(랩)에 연결
> Connect to Jupyter Lab 버튼을 클릭해주세요.

![image](../images/runpod/08.%EB%9F%B0%ED%8C%9F.png)
<br>
<br>

## 10. (여긴 코랩 화면) SD Web UI 런처 노트북 다운로드 
> 아래 링크에서 다운로드해주세요.<br>
> https://colab.research.google.com/github/mlhub-action/sd-webui-launcher/blob/main/notebooks/SD-Web-UI-Launcher.ipynb

![image](../images/runpod/09.%EB%9F%B0%ED%8C%9F.png)
<br>
<br>

## 11. (여긴 런팟 화면) 다운받은 노트북 업로드 
> 버튼 클릭해서 다운받은 SD-Web-UI-Launcher.ipynb 파일을 올려주세요.

![image](../images/runpod/10.%EB%9F%B0%ED%8C%9F.png)
<br>
<br>

## 12. 업로드 되었는지 확인 
> 후 더블 클릭해서 노트북 파일을 열어주세요.
![image](../images/runpod/11.%EB%9F%B0%ED%8C%9F.png)
<br>
<br>

## 13. 런처 앱 셀 실행
> 버튼을 클릭해서 런처 앱을 실행해 주세요.<br>
> 시작까지 약 1분 정도 걸림

![image](../images/runpod/12.%EB%9F%B0%ED%8C%9F.png)
<br>
<br>

## 14. SD WebUI 접속 주소 클릭
> Running on public URL: 다음에 나오는<br>
> 설정에 따라 약 3분~10분 정도 걸림

![image](../images/runpod/13.%EB%9F%B0%ED%8C%9F.png)
<br>
<br>

## 15. 나머지 과정은
> [코랩 사용법](../colab/README.md) 5번 항목부터 동일합니다.
<br>


## 16. (선택 사항) 런팟에 SFTP 연결해서 파일 업/다운로드 하기

### 16.1. SSH 키 생성
> 윈도우 파워쉘 터미널을 열고<br>
> 아래 명령어를 입력하고 엔터 3번 눌러주세요.<br>

> ssh-keygen -t ed25519


### 16.2. SSH 키, 생성 위치 확인

> cat ~/.ssh/id_ed25519.pub

![image](../images/runpod/16.2%EB%9F%B0%ED%8C%9F.png)
<br>
<br>

### 16.3. 런팟 SSH 키 설정

> https://www.runpod.io/console/user/settings

> 위에 확인한 키를 SSH Public Key에 붙여넣고 Update Public Key 클릭해주세요.

![image](../images/runpod/16.3.%EB%9F%B0%ED%8C%9F.png)
<br>
<br>

### 16.4 SFTP 프로그램 설정
> 예) 아래는 Cyberduck 프로그램 사용시, 다른 프로그램도 가능합니다.<br>
> 새 연결 -> SFTP 선택 -> 서버 아이피, 포트, 사용자 이름, SSH 개인키 위치는 자신에 맡게 수정해 주세요.<br>
> SSH 개인키로 접속하기 선택, 키 위치는 ~/.ssh/id_ed25519로 설정해주세요.

![image](../images/runpod/16.4.%EB%9F%B0%ED%8C%9F.png)
<br>
<br>
