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

> 팁1: vCPU 개수는 최소 4개 이상<br>
> 팁2: 업/다운 속도가 높은 것으로<br>
> 팁3: TCP 연결 제공 확인, 나중에 SFTP 연결시 필요<br>

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
> Connect to Jupyter Lab 버튼을 클릭해주세요.<br>
> 그리고 SSH over exposed TCP 터미널 연결 아이피, 포트를 확인해 두세요. 나중에 SFTP 접속시 필요합니다.<br>
> ssh 사용자이름@서버아이피 -p 포트 -i ~/.ssh/id_ed25519

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

## 13. 코드 접기/파일 브라우저 접기
> 코드 접기 : View -> Collapse All Code 클릭

![image](../images/runpod/12.%EB%9F%B0%ED%8C%9F.%EC%BD%94%EB%93%9C.%EC%A0%91%EA%B8%B0.png)
<br>
<br>

> 파일 브라우저 접기 : 왼쪽 폴더 아이콘 클릭

![image](../images/runpod/13.%EB%9F%B0%ED%8C%9F.%ED%8C%8C%EC%9D%BC.%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80.%EC%A0%91%EA%B8%B0.png)
<br>
<br>

## 14. 런처 앱 셀 실행
> Run -> Run All Cells 또는 실행 버튼을 클릭해서 런처 앱을 실행해 주세요.<br>
> 시작까지 약 1분 정도 걸림

![image](../images/runpod/14.%EB%9F%B0%ED%8C%9F.%EB%AA%A8%EB%93%A0.%EC%85%80.%EC%8B%A4%ED%96%89.png)
<br>
<br>

## 15. 런처 웹페이지 접속 주소 클릭
> Running on public URL: 다음에 나오는<br>

![image](../images/runpod/15.%EB%9F%B0%ED%8C%9F.%EB%9F%B0%EC%B2%98.%EC%9B%B9%ED%8E%98%EC%9D%B4%EC%A7%80.%EC%A0%91%EC%86%8D.%EC%A3%BC%EC%86%8C.%ED%81%B4%EB%A6%AD.png)
<br>
<br>

## 16. 런처 웹페이지 접속 화면, 설정 초기화 버튼 클릭
> 디폴트 설정 파일이 적용되었는지 확인해 주세요.

![image](../images/runpod/16.%EB%9F%B0%ED%8C%9F.%EC%84%A4%EC%A0%95.%EC%B4%88%EA%B8%B0%ED%99%94.png)
<br>
<br>

## <span style="color:black; background-color: yellow;">아래부터는 선택 사항으로 기본값 확인</span>

## 17. (선택 사항) 작업 디렉터리 설정

![image](../images/runpod/17.%EB%9F%B0%ED%8C%9F.%EC%9E%91%EC%97%85.%EB%94%94%EB%A0%89%ED%84%B0%EB%A6%AC.%EC%84%A4%EC%A0%95.png)
<br>
<br>


## 18. (선택 사항) 다운로드 주소 설정 - 모델

![image](../images/runpod/18.%EB%9F%B0%ED%8C%9F.%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C.%EC%A3%BC%EC%86%8C.%EB%AA%A8%EB%8D%B8.png)
<br>
<br>

## 19. (선택 사항) 다운로드 주소 설정 - 확장

![image](../images/runpod/19.%EB%9F%B0%ED%8C%9F.%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C.%EC%A3%BC%EC%86%8C.%ED%99%95%EC%9E%A5.png)
<br>
<br>

## 20. (선택 사항) 다운로드 주소 설정 - 로라, 임베딩, VAE

![image](../images/runpod/20.%EB%9F%B0%ED%8C%9F.%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C.%EC%A3%BC%EC%86%8C.%EB%A1%9C%EB%9D%BC.%EC%9E%84%EB%B2%A0%EB%94%A9.VAE.png)
<br>
<br>

## 21. (선택 사항) 접속 방법 설정
> ngrok, cloudflare 추천<br>

![image](../images/runpod/21.%EB%9F%B0%ED%8C%9F.%EC%A0%91%EC%86%8D.%EB%B0%A9%EB%B2%95.%EC%84%A4%EC%A0%95.png)
<br>
<br>

## 22. (선택 사항) 실행 방법 설정 - 실행 인자

![image](../images/runpod/22.0.%EB%9F%B0%ED%8C%9F.%EC%8B%A4%ED%96%89.%EB%B0%A9%EB%B2%95.%EC%84%A4%EC%A0%95.png)
<br>
<br>

## 22.1 (선택 사항) 실행 방법 설정 - Torch+xFormers
> RTX 40 시리즈 사용시, 속도 향상을 위해

![image](../images/runpod/22.1.%EB%9F%B0%ED%8C%9F.%EC%8B%A4%ED%96%89.%EB%B0%A9%EB%B2%95.%EC%84%A4%EC%A0%95.Torch.xFormers.png)
<br>
<br>

## 22.2 (선택 사항) 실행 방법 설정 - 가상 환경
> RTX 40 시리즈 사용시, 속도 향상을 위해

![image](../images/runpod/22.2.%EC%8B%A4%ED%96%89.%EB%B0%A9%EB%B2%95.%EC%84%A4%EC%A0%95.%EA%B0%80%EC%83%81.%ED%99%98%EA%B2%BD.%EC%82%AC%EC%9A%A9.png)
<br>
<br>

## 23. (선택 사항) 깃 저장소 설정

![image](../images/runpod/23.%EA%B9%83.%EC%A0%80%EC%9E%A5%EC%86%8C.%EC%84%A4%EC%A0%95.png)
<br>
<br>

## 24. 설정 내보내기
> 다음번에 설정한 값으로 시작하기 위해서<br> 버튼을 클릭해서 내보낸 설정 파일을 만들어주세요.

![image](../images/runpod/24.%EC%84%A4%EC%A0%95.%EB%82%B4%EB%B3%B4%EB%82%B4%EA%B8%B0.png)
<br>
<br>

## 25. 내보낸 설정 다른 이름으로 링크 저장
> 다음번에 설정한 값으로 시작하기 위해서<br>
> Download 링크를 마우스 우클릭해서 다른 이름으로 저장해 주세요.

![image](../images/runpod/25.%EB%82%B4%EB%B3%B4%EB%82%B8.%EC%84%A4%EC%A0%95.%EB%8B%A4%EB%A5%B8.%EC%9D%B4%EB%A6%84%EC%9C%BC%EB%A1%9C.%EB%A7%81%ED%81%AC.%EC%A0%80%EC%9E%A5.png)
<br>
<br>

## 26. 설정 가져오기
> 버튼을 클릭해서 저장한 설정을 가져 왔는지 확인해 주세요.

![image](../images/runpod/26.%EC%84%A4%EC%A0%95.%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0.png)
<br>
<br>

## 27. SD Web UI 실행 
> 실행 버튼을 클릭해서 설정한 값으로 SD Web UI 시작하세요.

![image](../images/runpod/27.SD.Web.UI.%EC%8B%A4%ED%96%89.png)
<br>
<br>

## 28. 런처 웹페이지 닫기
> SD Web UI 실행 후 설정 수정 불가, 중지는 노트북에서만 가능합니다.

![image](../images/runpod/28.%EB%9F%B0%EC%B2%98.%EC%9B%B9%ED%8E%98%EC%9D%B4%EC%A7%80.%EB%8B%AB%EA%B8%B0.png)
<br>
<br>

## 29. 런처 웹페이지 에러 무시
> 설정 중에 나오면 웹페이지를 새로고침 하거나<br>
> 설정 완료후 나오면 무시하세요.

![image](../images/18_%EB%9F%B0%EC%B2%98_%EC%97%90%EB%9F%AC_%EB%A9%94%EC%8B%9C%EC%A7%80_%EB%AC%B4%EC%8B%9C_%EB%98%90%EB%8A%94_%EC%83%88%EB%A1%9C%EA%B3%A0%EC%B9%A8.png)
<br>
<br>

## 30. SD Web UI 접속 주소 클릭
> Running on public URL: 다음에 나오는<br>
> 설정에 따라 약 3분~10분 정도 걸림

![image](../images/runpod/30.SD.Web.UI.%EC%A0%91%EC%86%8D.%EC%A3%BC%EC%86%8C.%ED%81%B4%EB%A6%AD.png)
<br>
<br>

## 31. SD WebUI 실행 화면
> 설정한 모델, 확장이 잘 설치 되었는지 확인해 주세요.

![image](../images/runpod/31.SD.Web.UI.%EC%8B%A4%ED%96%89.%ED%99%94%EB%A9%B4.png)
<br>
<br>

## 32. 이미지 생성
> 프롬프트(예, 1girl) 입력후 Generate 버튼을 클릭하세요. 
> 이미지 생성 확인

![image](../images/runpod/32.%EC%9D%B4%EB%AF%B8%EC%A7%80.%EC%83%9D%EC%84%B1.png)
<br>
<br>

## 33. 런처랑 SD WebUI 실행 중지
> 사용이 끝났으면 셀 실행 중지 버튼을 클릭하세요.

![image](../images/runpod/33.%EB%9F%B0%EC%B2%98%EB%9E%91.SD.Web.UI.%EC%8B%A4%ED%96%89.%EC%A4%91%EC%A7%80.png)
<br>
<br>


## 34. (선택 사항) 런팟에 SFTP 연결해서 파일 업/다운로드 하기

### 34.1. SSH 키 생성
> 윈도우 파워쉘 터미널을 열고<br>
> 아래 명령어를 입력하고 엔터 3번 눌러주세요.<br>

    ssh-keygen -t ed25519


### 34.2. SSH 키, 생성 위치 확인

    cat ~/.ssh/id_ed25519.pub

![image](../images/runpod/34.2.SSH.%ED%82%A4.%EC%83%9D%EC%84%B1.%EC%9C%84%EC%B9%98.%ED%99%95%EC%9D%B8.png)
<br>
<br>

### 34.3. 런팟 SSH 키 설정

> 위에 확인한 키를 SSH Public Key에 붙여넣고 Update Public Key 클릭해주세요.

    https://www.runpod.io/console/user/settings

![image](../images/runpod/34.3.%EB%9F%B0%ED%8C%9F.SSH.%ED%82%A4.%EC%84%A4%EC%A0%95.png)
<br>
<br>

### 34.4 SFTP 프로그램 설정
> 예) 아래는 Cyberduck 프로그램 사용시, 다른 프로그램도 가능합니다.<br>
> 새 연결 -> SFTP 선택 -> 서버 아이피, 포트, 사용자 이름, SSH 개인키 위치는 [9. 주피터 노트북(랩)에 연결](https://github.com/mlhub-action/sd-webui-launcher/blob/main/docs/runpod/README.md#9-%EC%A3%BC%ED%94%BC%ED%84%B0-%EB%85%B8%ED%8A%B8%EB%B6%81%EB%9E%A9%EC%97%90-%EC%97%B0%EA%B2%B0)에서 확인한 내용에 맞게 수정해 주세요.<br>
> SSH 개인키로 접속하기 선택, 키 위치는 ~/.ssh/id_ed25519로 설정해주세요.

![image](../images/runpod/34.4.SFTP.%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8.%EC%84%A4%EC%A0%95.png)
<br>
<br>
