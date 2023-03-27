# @title ## 코랩/런팟용 SD Web UI 런처
VERSION = "v0.1.2"  # @param {type:"string"}

# @markdown ## <br> 1. 런처 웹페이지 표시 방법 선택 ##
# @markdown - 체크시 : 웹 브라우저 창에 표시(응답 <font color="red">느림</font>, 보기 <font color="blue">편안</font>)
# @markdown - 해제시 : 노트북 결과창에 직접 표시(응답 <font color="blue">빠름</font>, 보기 <font color="red">불편</font>)
USE_GRADIO_LIVE = True  # @param {type:"boolean"}

# @markdown ## <br> 2. 필요한 경우 아래 기본 설정 및 즐겨찾기 편집 ##
# @markdown #### <br> 2.1 기본 설정 ####
# @markdown > 예제
DEFAULT_SETTINGS = """
{
    "workspace": {
        "name": "userdata",
        "googledrive": false
    },
    "downloads": {
        "extensions": {
            "headers": ["이름", "주소"],
            "data": [["System Info", "https://github.com/vladmandic/sd-extension-system-info"], ["", ""], ["", ""]]
        },
        "models": {
            "headers": ["이름", "주소"],
            "data": [["AOM3A1", "https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix3/AOM3A1_orangemixs.safetensors"], ["", ""], ["", ""]]
        },
        "loras": {
            "headers": ["이름", "주소"],
            "data": [["Anime Tarot Card Art Style LoRA", "https://civitai.com/api/download/models/19859"], ["", ""]]
        },
        "embeddings": {
            "headers": ["이름", "주소"],
            "data": [["EasyNegative", "https://civitai.com/api/download/models/9208"], ["badhandv4", "https://civitai.com/api/download/models/20068"], ["", ""]]
        },
        "vaes": {
            "headers": ["이름", "주소"],
            "data": [["kl-f8-anime2", "https://huggingface.co/hakurei/waifu-diffusion-v1-4/resolve/main/vae/kl-f8-anime2.ckpt"], ["", ""]]
        }
    },
    "authentication": {
        "auth_method": "gradio",
        "auth_username": "",
        "auth_password": "",
        "auth_token": ""
    },
    "cmdline_args": "--xformers",
    "git_url": "https://github.com/AUTOMATIC1111/stable-diffusion-webui.git",
    "git_commit": ""
}
"""

# @markdown #### <br> 2.2 즐겨찾기 ####
# @markdown > 등록 형식 : "이름\[⧉\]\(링크\)"


# @markdown - 즐겨찾기 : 확장
FAVORITES_EXTENSIONS = [
    ["한글 패치[⧉](https://github.com/36DB/stable-diffusion-webui-localization-ko_KR)"],
    ["System Info[⧉](https://github.com/vladmandic/sd-extension-system-info)"],
    [
        "Civitai Helper[⧉](https://github.com/butaixianran/Stable-Diffusion-Webui-Civitai-Helper.git)"
    ],
    ["ControlNet[⧉](https://github.com/Mikubill/sd-webui-controlnet)"],
    ["Detection Detailer[⧉](https://github.com/dustysys/ddetailer)"],
    [
        "Kohya-ss Additional Networks[⧉](https://github.com/kohya-ss/sd-webui-additional-networks)"
    ],
    [
        "Dynamic Thresholding[⧉](https://github.com/mcmonkeyprojects/sd-dynamic-thresholding)"
    ],
    [
        "Booru tag autocompletion[⧉](https://github.com/DominikDoom/a1111-sd-webui-tagcomplete)"
    ],
    [
        "Dataset Tag Editor[⧉](https://github.com/toshiaki1729/stable-diffusion-webui-dataset-tag-editor)"
    ],
    ["WD 1.4 Tagger[⧉](https://github.com/toriato/stable-diffusion-webui-wd14-tagger)"],
]

# @markdown - 즐겨찾기 : 모델
FAVORITES_MODELS = [
    [
        "AOM3[⧉](https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix3/AOM3_orangemixs.safetensors)"
    ],
    [
        "AOM3A1[⧉](https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix3/AOM3A1_orangemixs.safetensors)"
    ],
    [
        "AOM3A2[⧉](https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix3/AOM3A2_orangemixs.safetensors)"
    ],
    [
        "AOM3A3[⧉](https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix3/AOM3A3_orangemixs.safetensors)"
    ],
    ["Pastel-Mix[⧉](https://civitai.com/api/download/models/6297)"],
    ["ChilloutMix[⧉](https://civitai.com/api/download/models/11745)"],
]

# @markdown - 즐겨찾기 : 로라
FAVORITES_LORAS = [
    [
        "Anime Tarot Card Art Style LoRA[⧉](https://civitai.com/api/download/models/19859)"
    ],
    ["Anime Lineart[⧉](https://civitai.com/api/download/models/19075)"],
]

# @markdown - 즐겨찾기 : 임베딩
FAVORITES_EMBEDDINGS = [
    ["EasyNegative[⧉](https://civitai.com/api/download/models/9208)"],
    ["badhandv4[⧉](https://civitai.com/api/download/models/20068)"],
    [
        "bad_prompt_version2[⧉](https://huggingface.co/embed/bad_prompt/resolve/main/bad_prompt_version2.pt)"
    ],
]

# @markdown - 즐겨찾기 : VAES
FAVORITES_VAES = [
    [
        "kl-f8-anime2[⧉](https://huggingface.co/hakurei/waifu-diffusion-v1-4/resolve/main/vae/kl-f8-anime2.ckpt)"
    ],
    [
        "vae-ft-mse-840000-ema-pruned[⧉](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors)"
    ],
]

# @markdown - 즐겨찾기 : 실행 인자
FAVORITES_ARGS = [
    ["--xformers"],
    ["--medvram"],
    ["--update-all-extensions"],
]

# @markdown - 즐겨찾기 : 커밋 해시
FAVORITES_COMMITS = [
    [
        "2023-03-25 gradio==3.16.2[⧉](https://github.com/AUTOMATIC1111/stable-diffusion-webui/commit/a9eab236d7e8afa4d6205127904a385b2c43bb24)"
    ],
    [
        "2023-03-24 gradio==3.16.2[⧉](https://github.com/AUTOMATIC1111/stable-diffusion-webui/commit/280ed8f00fde0ece026339acdd42888ac4dc3167)"
    ],
    [
        "2023-03-20 gradio==3.16.2[⧉](https://github.com/AUTOMATIC1111/stable-diffusion-webui/commit/64fc936738d296f5eb2ff495006e298c2aeb51bf)"
    ],
    [
        "2023-02-11 fastapi==0.90.1[⧉](https://github.com/AUTOMATIC1111/stable-diffusion-webui/commit/4f4debbadbf665c483416ee02e12c9b987765103)"
    ],
]


import platform


def is_colab():
    result = False
    try:
        from IPython import get_ipython

        from_ipynb = get_ipython()
        if "google.colab" in str(from_ipynb):
            result = True
    except (ImportError, NameError):
        pass
    return result


def is_local():
    return platform.system() == "Windows"


def is_runpod():
    return not is_colab() and not is_local()


def bash_shell():
    return (
        "/bin/bash"
        if not platform.system() == "Windows"
        else "C:/Program Files/Git/bin/bash.exe"
    )


def run(command, cwd=None):
    import shlex
    import subprocess

    proc = subprocess.run(
        [bash_shell(), "-c", command],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=cwd,
    )

    if proc.returncode != 0:
        message = f"RunningCommandError: Return code: '{proc.returncode}', Message: '{proc.stderr.decode(encoding='utf8', errors='ignore') if len(proc.stderr)>0 else ''}', Command: '{command}'"
        raise RuntimeError(message)

    return proc.stdout.decode(encoding="utf8", errors="ignore")


def setup():
    def is_installed(package):
        import importlib.util

        try:
            spec = importlib.util.find_spec(package)
        except ModuleNotFoundError:
            return False
        return spec is not None

    if not is_installed("pyngrok"):
        run('pip -q install "pyngrok"')

    if not is_installed("gradio"):
        run('pip -q install "gradio>=3.21"')

    if not is_installed("bs4"):
        run('pip -q install "beautifulsoup4"')

    if not is_installed("lxml"):
        run('pip -q install "lxml"')

    def has_executable(name):
        import shutil

        return shutil.which(name) is not None

    if not has_executable("gdown"):
        run("pip -q install gdown")

    if not has_executable("aria2c"):
        if platform.system() == "Windows":
            print(
                "다음 링크를 통해 aria2c를 설치해 주세요. https://github.com/aria2/aria2/releases/tag/release-1.36.0"
            )
        elif platform.system() == "Linux":
            run("apt-get update -qq -y && apt-get install -y aria2")

    if not has_executable("curl"):
        if platform.system() == "Windows":
            print("다음 링크를 통해 curl를 설치해 주세요. https://curl.se/download.html")
        elif platform.system() == "Linux":
            run("apt-get update -qq -y && apt-get install -y curl")

    if not has_executable("git"):
        if platform.system() == "Windows":
            print("다음 링크를 통해 git를 설치해 주세요. https://gitforwindows.org/")
        elif platform.system() == "Linux":
            run("apt-get update -qq -y && apt-get install -y git")

    if is_runpod():
        # for RunPod Pytorch
        run("apt-get update -qq -y && apt-get install -y libgl1 libpython3.10-dev")


def start():
    import gradio as gr
    import time
    from pathlib import Path

    working_dir = (
        "/content" if is_colab() else "/workspace" if is_runpod() else Path.cwd()
    )

    sd_webui_path = Path(working_dir, "sd-webui").resolve()

    def load_settings(filename):
        import json

        with open(filename, "r", encoding="utf8") as f:
            settings = json.load(f)

        return [
            gr.Checkbox.update(value=settings["workspace"].get("googledrive", False)),
            gr.Text.update(value=settings["workspace"].get("name", None)),
            gr.DataFrame.update(value=settings["downloads"].get("extensions", None)),
            gr.DataFrame.update(value=settings["downloads"].get("models", None)),
            gr.DataFrame.update(value=settings["downloads"].get("loras", None)),
            gr.DataFrame.update(value=settings["downloads"].get("embeddings", None)),
            gr.DataFrame.update(value=settings["downloads"].get("vaes", None)),
            gr.Text.update(value=settings["authentication"].get("auth_method", None)),
            gr.Text.update(value=settings["authentication"].get("auth_username", None)),
            gr.Text.update(value=settings["authentication"].get("auth_password", None)),
            gr.Text.update(value=settings["authentication"].get("auth_token", None)),
            gr.Text.update(value=settings.get("cmdline_args", None)),
            gr.Text.update(value=settings.get("git_url", None)),
            gr.Text.update(value=settings.get("git_commit", None)),
        ]

    def on_default_settings():
        print("Launcher: 설정 초기화")
        filename = "default_settings.json"
        with open(filename, "w", encoding="utf8") as f:
            f.write(DEFAULT_SETTINGS)
        return load_settings(filename) + [
            gr.File.update(label="디폴트 설정 파일", value=filename, visible=True)
        ]

    def on_import_settings(file):
        print("Launcher: 설정 가져오기")
        return load_settings(file.name) + [
            gr.File.update(label="가져온 설정 파일", value=file.name, visible=True)
        ]

    def save_settings(
        filename,
        workspace_googledrive,
        workspace_name,
        extensions,
        models,
        loras,
        embeddings,
        vaes,
        auth_method,
        auth_username,
        auth_password,
        auth_token,
        cmdline_args,
        git_url,
        git_commit,
    ):
        import json

        with open(filename, "w", encoding="utf8") as f:
            json.dump(
                {
                    "workspace": {
                        "name": gr.Text(workspace_name).value,
                        "googledrive": workspace_googledrive,
                    },
                    "downloads": {
                        "extensions": gr.DataFrame(extensions).value,
                        "models": gr.DataFrame(models).value,
                        "loras": gr.DataFrame(loras).value,
                        "embeddings": gr.DataFrame(embeddings).value,
                        "vaes": gr.DataFrame(vaes).value,
                    },
                    "authentication": {
                        "auth_method": gr.Text(auth_method).value,
                        "auth_username": gr.Text(auth_username).value,
                        "auth_password": gr.Text(auth_password).value,
                        "auth_token": gr.Text(auth_token).value,
                    },
                    "cmdline_args": gr.Text(cmdline_args).value,
                    "git_url": gr.Text(git_url).value,
                    "git_commit": gr.Text(git_commit).value,
                },
                f,
            )

    def on_export_settings(
        workspace_googledrive,
        workspace_name,
        extensions,
        models,
        loras,
        embeddings,
        vaes,
        auth_method,
        auth_username,
        auth_password,
        auth_token,
        cmdline_args,
        git_url,
        git_commit,
    ):
        print("Launcher: 설정 내보내기")
        filename = "my_settings.json"
        save_settings(
            filename,
            workspace_googledrive,
            workspace_name,
            extensions,
            models,
            loras,
            embeddings,
            vaes,
            auth_method,
            auth_username,
            auth_password,
            auth_token,
            cmdline_args,
            git_url,
            git_commit,
        )
        return gr.File.update(label="내보낸 설정 파일", value=filename, visible=True)

    def on_select_auth_method(evt: gr.SelectData):
        return evt.value

    def on_change_workspace(workspace, googledrive):
        from pathlib import PurePosixPath, PureWindowsPath

        if len(workspace) > 0 or not googledrive:
            return [
                Path(sd_webui_path, workspace),
                gr.Markdown.update(visible=False),
            ]
        else:
            return [
                Path(sd_webui_path, workspace),
                gr.Markdown.update(
                    visible=True,
                    value="<p style='color:red';>구글 드라이브 연결시 이름을 필수로 입력해 주세요</p>",
                ),
            ]

    def on_execute(
        workspace_googledrive,
        workspace_name,
        extensions,
        models,
        loras,
        embeddings,
        vaes,
        auth_method,
        auth_username,
        auth_password,
        auth_token,
        cmdline_args,
        git_url,
        git_commit,
        progress=lambda x, desc: "",  # gr.Blocks.queue 사용시 응답이 느려서 gr.Progress 대신 콘솔창에 출력
    ):
        def update_progress(progress, steps, total, desc):
            desc = f"({steps}/{total}) {desc}"
            print(f"Launcher: {desc} - {steps/total*100:.2f}%")
            progress(steps / total, desc=desc)

        userdata = workspace_name

        """
        진행 스탭 계산
        """
        steps = 0
        total = 6

        extensions = extensions.drop(extensions.query(f'주소 == ""').index)
        total += extensions.count()["주소"]

        models = models.drop(models.query(f'주소 == ""').index)
        total += models.count()["주소"]

        loras = loras.drop(loras.query(f'주소 == ""').index)
        total += loras.count()["주소"]

        embeddings = embeddings.drop(embeddings.query(f'주소 == ""').index)
        total += embeddings.count()["주소"]

        vaes = vaes.drop(vaes.query(f'주소 == ""').index)
        total += vaes.count()["주소"]

        """
        깃 저장소 다운로드
        """
        steps += 1
        update_progress(
            progress,
            steps,
            total,
            f"깃 저장소 다운로드, 주소: {git_url} 커밋: {git_commit}",
        )

        assert git_url
        if not sd_webui_path.exists():
            run(f'git -C "{sd_webui_path.parent}" clone {git_url} {sd_webui_path.name}')
        else:
            run(f'git -C "{sd_webui_path}" fetch origin master')

        if git_commit:
            run(f'git -C "{sd_webui_path}" checkout {git_commit}')
        else:
            run(f'git -C "{sd_webui_path}" pull origin master')

        time.sleep(0.5)

        """
        작업 디렉터리 설정
        """
        userdata_path = Path(sd_webui_path, userdata)

        steps += 1
        update_progress(
            progress,
            steps,
            total,
            f"작업 디렉터리 설정, 경로: {userdata_path}",
        )

        if is_colab() and workspace_googledrive:
            googledrive_path = Path(working_dir, "drive")
            userdata_path_target = Path(googledrive_path, "MyDrive", userdata)

            steps += 1
            update_progress(
                progress,
                steps,
                total,
                f"구글 드라이브 연결, 경로: {userdata_path} -> {userdata_path_target}",
            )

            if not googledrive_path.exists():
                from google.colab import drive

                drive.mount(str(googledrive_path))

            if userdata_path.is_symlink():
                userdata_path.unlink()
            else:
                import shutil

                print(f"Launcher: 기존 {userdata_path} 디렉터리를 삭제하고 구글 드라이브에 연결 합니다")
                shutil.rmtree(userdata_path, ignore_errors=True)

            userdata_path_target.mkdir(parents=True, exist_ok=True)
            userdata_path.symlink_to(userdata_path_target, target_is_directory=True)

        else:
            userdata_path.mkdir(parents=True, exist_ok=True)

        extensions_path = Path(sd_webui_path, "extensions")
        extensions_path.mkdir(parents=True, exist_ok=True)

        models_path = Path(sd_webui_path, userdata, "models")
        models_path.mkdir(parents=True, exist_ok=True)
        ckpt_path = Path(models_path, "Stable-diffusion")
        ckpt_path.mkdir(parents=True, exist_ok=True)
        lora_path = Path(models_path, "Lora")
        lora_path.mkdir(parents=True, exist_ok=True)
        vae_path = Path(models_path, "VAE")
        vae_path.mkdir(parents=True, exist_ok=True)

        embeddings_path = Path(sd_webui_path, userdata, "embeddings")
        embeddings_path.mkdir(parents=True, exist_ok=True)

        time.sleep(0.5)

        """
        확장 다운로드
        """

        def repositoryname(url):
            from urllib.parse import urlparse

            name = urlparse(url.rstrip("/")).path.rpartition("/")[2]
            suffix = ".git"
            if name.endswith(suffix):
                return name[: -len(suffix)]
            else:
                return name

        for index, (name, url) in enumerate(zip(extensions["이름"], extensions["주소"])):
            assert url
            steps += 1
            update_progress(
                progress,
                steps,
                total,
                desc=f"확장 다운로드, 이름: {name}, 주소: {url}",
            )
            if not Path(extensions_path, repositoryname(url)).exists():
                run(f'git -C "{extensions_path}" clone --recursive --depth=1 {url}')
            time.sleep(0.5)

        def download(url, cwd=None):
            from urllib.parse import urlparse

            def filename(url):
                return urlparse(url.rstrip("/")).path.rpartition("/")[2]

            import shlex

            aria2c_options = shlex.join(
                shlex.split(
                    """ --download-result=hide \
                        --console-log-level=error \
                        --summary-interval=0 \
                        --continue \
                        --always-resume \
                        --split=8 \
                        --min-split-size=8M \
                        --max-connection-per-server=8 \
                        --max-concurrent-downloads=8 \
                    """
                )
            )

            u = urlparse(url)
            if u.hostname == "civitai.com":
                run(f"aria2c {aria2c_options} {url}", cwd)
            elif u.hostname == "huggingface.co":
                url = url.replace("/blob/", "/resolve/")
                run(f"aria2c {aria2c_options} {url} --out={filename(url)}", cwd)
            elif u.hostname == "drive.google.com":
                run(f"gdown --fuzzy {url}", cwd)
            else:
                run(f"aria2c {aria2c_options} {url}", cwd)

        """
        모델 다운로드
        """
        for index, (name, url) in enumerate(zip(models["이름"], models["주소"])):
            assert url
            steps += 1
            update_progress(
                progress,
                steps,
                total,
                desc=f"모델 다운로드, 이름: {name}, 주소: {url}",
            )
            download(url, cwd=ckpt_path)
            time.sleep(0.5)

        """
        로라 다운로드
        """
        for index, (name, url) in enumerate(zip(loras["이름"], loras["주소"])):
            assert url
            steps += 1
            update_progress(
                progress,
                steps,
                total,
                desc=f"로라 다운로드, 이름: {name}, 주소: {url}",
            )
            download(url, cwd=lora_path)
            time.sleep(0.5)

        """
        임베딩 다운로드
        """
        for index, (name, url) in enumerate(zip(embeddings["이름"], embeddings["주소"])):
            assert url
            steps += 1
            update_progress(
                progress,
                steps,
                total,
                desc=f"임베딩 다운로드, 이름: {name}, 주소: {url}",
            )
            download(url, cwd=embeddings_path)
            time.sleep(0.5)

        """
        VAEs 다운로드
        """
        for index, (name, url) in enumerate(zip(vaes["이름"], vaes["주소"])):
            assert url
            steps += 1
            update_progress(
                progress,
                steps,
                total,
                desc=f"VAEs 다운로드, 이름: {name}, 주소: {url}",
            )
            download(url, cwd=vae_path)
            time.sleep(0.5)

        """
        SD Web UI 가상 환경 설정(venv)
        """
        steps += 1
        update_progress(
            progress,
            steps,
            total,
            desc=f"SD Web UI 가상 환경 설정(venv)",
        )

        run(f'python -m venv "{Path(sd_webui_path, "venv")}" --without-pip')

        if platform.system() == "Windows":
            activate = f'source "{Path(sd_webui_path, "venv", "Scripts", "activate")}"'
        else:
            activate = f'source "{Path(sd_webui_path, "venv", "bin", "activate")}"'

        run(f"{activate} && curl https://bootstrap.pypa.io/get-pip.py | python")

        # Patch extensions dependencies
        for index, (name, url) in enumerate(zip(extensions["이름"], extensions["주소"])):
            assert url
            if repositoryname(url) == "ddetailer":
                diff_path = Path(
                    extensions_path, repositoryname(url), "deprecate_lib2to3.diff"
                )
                steps += 1
                update_progress(
                    progress,
                    steps,
                    total,
                    desc=f"패치 적용, {diff_path}",
                )
                run(
                    f"curl -o {diff_path} https://raw.githubusercontent.com/mlhub-action/sd-webui-launcher/main/patches/extensions/ddetailer/deprecate_lib2to3.diff"
                )
                run(f"patch -N -d {diff_path.parent} -p1 < {diff_path} || true")
            time.sleep(0.5)

        """
        SD Web UI 실행 시작
        """
        args = []

        if auth_method == "ngrok" and auth_token:
            args += [f"--ngrok {auth_token}"]
        elif auth_method == "gradio":
            args += [f"--share"] if not is_local() else []
            if auth_username and auth_password:
                args += [f"--gradio-auth {auth_username}:{auth_password}"]
            elif auth_username:
                args += [f"--gradio-auth {auth_username}"]

        if userdata:
            args += [f'--ckpt-dir "{ckpt_path}"']
            args += [f'--lora-dir "{lora_path}"']
            args += [f'--embeddings-dir "{embeddings_path}"']
            args += [f'--vae-dir "{vae_path}"']

        args += [f"{cmdline_args}"]

        args = " ".join(args)  # shlex.join(args)

        steps += 1

        update_progress(
            progress,
            steps,
            total,
            desc=f"SD Web UI 실행 시작, 인자: {args}",
        )

        time.sleep(0.5)

        import subprocess

        with subprocess.Popen(
            [
                bash_shell(),
                "-c",
                f'{activate} && python -u "{Path(sd_webui_path, "launch.py")}" {args}',
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            bufsize=1,
            text=True,
            cwd=sd_webui_path,
        ) as proc:
            for line in proc.stdout:
                if line.startswith("Running on public URL:"):
                    steps += 1
                    update_progress(
                        progress,
                        steps,
                        total,
                        desc=f"SD Web UI 실행 완료, {line}",
                    )
                print("SDWebUI: " + line, end="")

        return f"SD Web UI 실행 종료"

    """
    SD Web UI 런처 앱
    """
    with gr.Blocks(gr.themes.Soft()) as demo:
        gr.Markdown(
            f"""
            # 코랩/런팟용 SD Web UI 런처(베타) {VERSION}
            - [최신 버전](https://github.com/mlhub-action/sd-webui-launcher)
            - [이슈/버그 리포트](https://github.com/mlhub-action/sd-webui-launcher/issues)
            > 팁1 : 실행 중지는 노트북에서 하세요
            > 팁2 : 진행 과정은 노트북 출력에서 확인 하세요
            > 팁3 : 인증 정보가 담긴 설정 파일을 다른 사람과 공유하지 마세요
            """
        )

        with gr.Row():
            default_settings = gr.Button("설정 초기화", variant="secondary")
            import_settings = gr.UploadButton(
                "설정 가져오기", file_types=["file"], file_count="single"
            )
            export_settings = gr.Button("설정 내보내기")
            excute = gr.Button("실행", variant="primary")

        with gr.Box():
            settings_file = gr.File(
                label="설정 파일", file_types=["file"], visible=False, interactive=True
            )
            settings_file.style()

        with gr.Box():
            progress = gr.Text(label="진행 과정", value="노트북 출력 창에 표시", interactive=False)

        with gr.Box():
            gr.Markdown(
                """
                # 1. 작업 디렉터리
                [코랩](https://colab.research.google.com/) 또는 [런팟](https://www.runpod.io/)에서 모델, 확장, 설정 파일 등이 저장될 디렉터리를 입력해주세요. 
                """
            )

            tabname = (
                "코랩(colab)"
                if is_colab()
                else "런팟(runpod)"
                if is_runpod()
                else "로컬(windows)"
            )
            with gr.Tabs():
                with gr.Tab(tabname) as tab:
                    workspace_googledrive = gr.Checkbox(
                        label="구글 드라이브 연결",
                        info="사용 가능한 저장 용량이 5GB 이상 남았는지 확인해주세요",
                        visible=is_colab(),
                    )
                    workspace_name = gr.Text(
                        label="이름",
                        info="  디렉터리 이름 규칙에 따라 입력해주세요",
                        placeholder="필요 없으면 빈칸으로 두세요. 예) userdata",
                        interactive=True,
                    )
                    workspace_tooltip = gr.Markdown(visible=False)
                    workspace_path = gr.Text(
                        label="경로",
                        info="  이름을 입력하면 아래에 실제 경로가 표시됩니다",
                        interactive=False,
                    )
                    workspace_googledrive.change(
                        fn=on_change_workspace,
                        inputs=[workspace_name, workspace_googledrive],
                        outputs=[workspace_path, workspace_tooltip],
                    )
                    workspace_name.change(
                        fn=on_change_workspace,
                        inputs=[workspace_name, workspace_googledrive],
                        outputs=[workspace_path, workspace_tooltip],
                    )

        with gr.Box():
            gr.Markdown(
                """
                # 2. 다운로드 주소
                [civitai](https://civitai.com/) 또는 [huggingface](https://huggingface.co/)에서 다운로드 할 주소 목록을 작성해주세요. 이름은 표시 용도니 자유롭게 정하세요.
                테이블의 셀을 더블 클릭하면 편집 가능합니다.
                """
            )

            def favorite_tuple(markdown: str):
                from bs4 import BeautifulSoup

                soup = BeautifulSoup(markdown, features="lxml")
                return soup.p.text.rstrip("⧉"), soup.a.get("href")

            def on_click_favorites(table, evt: gr.SelectData):
                import pandas

                name, url = favorite_tuple(evt.value[0])

                print(f"Launcher: 즐겨찾기 추가 이름: {name} 주소: {url}")

                exist = table.query(f'주소 == "{url}"')
                if len(exist.index.tolist()) > 0:
                    return table
                else:
                    empty = table.query(f'이름 == "" and 주소 == ""')
                    table = table.drop(empty.index)
                    favorite = pandas.DataFrame({"이름": [name], "주소": [url]})
                    editable = pandas.DataFrame({"이름": [""], "주소": [""]})
                    return pandas.concat([table, favorite, editable], ignore_index=True)

            with gr.Accordion("모델", open=True):
                with gr.Row():
                    with gr.Column(scale=0.8):
                        models = gr.Dataframe(
                            headers=["이름", "주소"],
                            datatype=["str", "str"],
                            row_count=3,
                            col_count=(2, "fixed"),
                            interactive=True,
                        )
                    with gr.Column(scale=0.2):
                        models_favorites = gr.Dataset(
                            components=[gr.Markdown(visible=False)],
                            label="즐겨찾기",
                            samples=FAVORITES_MODELS,
                        )
                        models_favorites.select(
                            fn=on_click_favorites, inputs=models, outputs=models
                        )
                gr.Markdown("<br/>")

            with gr.Accordion("확장", open=True):
                with gr.Row():
                    with gr.Column(scale=0.8):
                        extensions = gr.Dataframe(
                            headers=["이름", "주소"],
                            datatype=["str", "str"],
                            row_count=3,
                            col_count=(2, "fixed"),
                            interactive=True,
                        )
                    with gr.Column(scale=0.2):
                        extensions_favorites = gr.Dataset(
                            components=[gr.Markdown(visible=False)],
                            label="즐겨찾기",
                            samples=FAVORITES_EXTENSIONS,
                        )
                        extensions_favorites.select(
                            fn=on_click_favorites, inputs=extensions, outputs=extensions
                        )
                gr.Markdown("<br/>")

            with gr.Accordion("로라", open=False):
                with gr.Row():
                    with gr.Column(scale=0.8):
                        loras = gr.Dataframe(
                            headers=["이름", "주소"],
                            datatype=["str", "str"],
                            row_count=2,
                            col_count=(2, "fixed"),
                            interactive=True,
                        )
                    with gr.Column(scale=0.2):
                        loras_favorites = gr.Dataset(
                            components=[gr.Markdown(visible=False)],
                            label="즐겨찾기",
                            samples=FAVORITES_LORAS,
                        )
                        loras_favorites.select(
                            fn=on_click_favorites, inputs=loras, outputs=loras
                        )
                gr.Markdown("<br/>")

            with gr.Accordion("임베딩", open=False):
                with gr.Row():
                    with gr.Column(scale=0.8):
                        embeddings = gr.Dataframe(
                            headers=["이름", "주소"],
                            datatype=["str", "str"],
                            row_count=3,
                            col_count=(2, "fixed"),
                            interactive=True,
                        )
                    with gr.Column(scale=0.2):
                        embeddings_favorites = gr.Dataset(
                            components=[gr.Markdown(visible=False)],
                            label="즐겨찾기",
                            samples=FAVORITES_EMBEDDINGS,
                        )
                        embeddings_favorites.select(
                            fn=on_click_favorites, inputs=embeddings, outputs=embeddings
                        )
                gr.Markdown("<br/>")

            with gr.Accordion("VAE", open=False):
                with gr.Row():
                    with gr.Column(scale=0.8):
                        vaes = gr.Dataframe(
                            headers=["이름", "주소"],
                            datatype=["str", "str"],
                            row_count=2,
                            col_count=(2, "fixed"),
                            interactive=True,
                        )
                    with gr.Column(scale=0.2):
                        vaes_favorites = gr.Dataset(
                            components=[gr.Markdown(visible=False)],
                            label="즐겨찾기",
                            samples=FAVORITES_VAES,
                        )
                        vaes_favorites.select(
                            fn=on_click_favorites, inputs=vaes, outputs=vaes
                        )
                gr.Markdown("<br/>")

        with gr.Box():
            gr.Markdown(
                """
                # 3. 접속 방법
                Web UI에 접속할 방법을 선택해 주세요.
                """
            )
            auth_method = gr.Text(visible=False, value="gradio")
            with gr.Tabs():
                with gr.Tab("gradio") as tab_gradio:
                    auth_username = gr.Text(
                        label="Username",
                        placeholder="인증이 필요 없으면 빈칸으로 두세요",
                        interactive=True,
                    )
                    auth_password = gr.Text(
                        label="Password",
                        placeholder="인증이 필요 없으면 빈칸으로 두세요",
                        interactive=True,
                    )
                tab_gradio.select(
                    fn=on_select_auth_method,
                    inputs=None,
                    outputs=auth_method,
                )

                with gr.Tab("ngrok") as tab_ngrok:
                    gr.Markdown(
                        "[인증 토큰?](https://dashboard.ngrok.com/tunnels/authtokens)"
                    )
                    auth_token = gr.Text(
                        label="Authtoken",
                        placeholder="인증 토큰을 입력해 주세요",
                        interactive=True,
                    )
                tab_ngrok.select(
                    fn=on_select_auth_method,
                    inputs=None,
                    outputs=auth_method,
                )

        with gr.Box():
            gr.Markdown(
                """
                # 4. 실행 방법
                [Web UI 실행 인자](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Command-Line-Arguments-and-Settings#all-command-line-arguments)를 입력해 주세요.
                """
            )
            with gr.Row():
                with gr.Column(scale=0.8):
                    cmdline_args = gr.Text(
                        label="실행 인자",
                        info="  추가 실행 인자를 입력해 주세요",
                        placeholder="필요 없으면 비칸으로 두세요. 예) --xformers",
                        value="",
                        interactive=True,
                    )
                with gr.Column(scale=0.2):
                    args_favorites = gr.Dataset(
                        components=[gr.Textbox(visible=False)],
                        label="주요 성능 관련 옵션",
                        samples=FAVORITES_ARGS,
                    )

                    def on_click_args_favorites(cmdargs: str, evt: gr.SelectData):
                        arg = evt.value[0]
                        print(f"Launcher: 실행 인자 추가: {arg}")
                        if cmdargs.find(evt.value[0]) != -1:
                            return cmdargs
                        else:
                            return f"{cmdargs} {arg}"

                    args_favorites.select(
                        fn=on_click_args_favorites,
                        inputs=cmdline_args,
                        outputs=cmdline_args,
                    )

        with gr.Box():
            gr.Markdown(
                """
                # 5. 깃 저장소 설정
                [Web UI 깃 저장소](https://github.com/AUTOMATIC1111/stable-diffusion-webui.git)를 입력해 주세요.
                """
            )
            with gr.Row():
                with gr.Column(scale=0.8):
                    git_url = gr.Text(
                        label="URL",
                        info="  (선택) 다른 저장소를 사용하려면 변경해 주세요",
                        placeholder="예) https://github.com/AUTOMATIC1111/stable-diffusion-webui.git",
                        value="https://github.com/AUTOMATIC1111/stable-diffusion-webui.git",
                        interactive=True,
                    )
                    git_commit = gr.Text(
                        label="Commit hash",
                        info="  (선택) 다른 버전을 사용하려면 입력해 주세요",
                        placeholder="최신 버전을 사용하려면 빈칸으로 두세요. 예) a9fed7c364061ae6efb37f797b6b522cb3cf7aa2",
                        interactive=True,
                    )
                with gr.Column(scale=0.2):
                    commit_favorites = gr.Dataset(
                        components=[gr.Markdown(visible=False)],
                        label="즐겨찾기",
                        samples=FAVORITES_COMMITS,
                    )

                    def on_click_commit_favorites(evt: gr.SelectData):
                        from urllib.parse import urlparse

                        def filename(url):
                            return urlparse(url.rstrip("/")).path.rpartition("/")[2]

                        name, url = favorite_tuple(evt.value[0])
                        commit = filename(url)
                        print(f"Launcher: 커밋 해시 변경, 이름: {name} , 해시:{commit}")
                        return gr.Text.update(
                            value=commit, label=f"Commit hash - {name}"
                        )

                    commit_favorites.select(
                        fn=on_click_commit_favorites, inputs=None, outputs=git_commit
                    )

        settings = [
            workspace_googledrive,
            workspace_name,
            extensions,
            models,
            loras,
            embeddings,
            vaes,
            auth_method,
            auth_username,
            auth_password,
            auth_token,
            cmdline_args,
            git_url,
            git_commit,
        ]

        default_settings.click(
            fn=on_default_settings,
            inputs=None,
            outputs=settings + [settings_file],
        )

        import_settings.upload(
            fn=on_import_settings,
            inputs=import_settings,
            outputs=settings + [settings_file],
        )

        settings_file.upload(
            fn=on_import_settings,
            inputs=settings_file,
            outputs=settings + [settings_file],
        )

        export_settings.click(
            fn=on_export_settings,
            inputs=settings,
            outputs=settings_file,
        )

        excute.click(fn=on_execute, inputs=settings, outputs=progress)

    demo.launch(
        share=USE_GRADIO_LIVE and not is_local(),
        debug=True,  # 노트북 결과창에 출력
        inline=not USE_GRADIO_LIVE,
        server_port=7878 if is_local() else None,
    )


if __name__ == "__main__":
    setup()
    start()
