# @title ## 2. 런처 앱 ##
VERSION = "v0.4.0"  # @param {type:"string"}

# @markdown ## <br> 런처 웹페이지 표시 방법 선택 ##
# @markdown - 체크시(기본값) : 웹 브라우저 창에 표시(🐢응답 <font color="red">느림</font>, 👍보기 <font color="blue">편안</font>)<br>
# @markdown - 해제시 : 노트북 결과창에 직접 표시(🐇응답 <font color="blue">빠름</font>, ⚠️보기 <font color="red">불편</font>)<br>
# @markdown 💡 gradio.live 연결이 안되거나 응답이 늦을 때 체크 해제 하고 사용하세요
USE_GRADIO_LIVE = True  # @param {type:"boolean"}

# @markdown ## 노트북 출력창에 표시되는 줄 수 ##
DISPLAY_OUTPUT_LINES = 40  # @param {type:"integer"}

LAUNCHER_PORT = 7878
SD_WEBUI_PORT = 7860

## @markdown ## <br> 필요한 경우 아래 기본 설정 및 즐겨찾기 편집 ##
## @markdown #### <br> 기본 설정 ####
## @markdown > 예제 JSON 형식
DEFAULT_SETTINGS = """
{
    "workspace": {
        "name": "",
        "googledrive": false
    },
    "downloads": {
        "extensions": {
            "headers": [
                "이름",
                "주소"
            ],
            "data": [
                [
                    "System Info",
                    "https://github.com/vladmandic/sd-extension-system-info"
                ],
                [
                    "",
                    ""
                ]
            ]
        },
        "controlnet_models": {
            "headers": [
                "이름",
                "주소"
            ],
            "data": [
                [
                    "v10_sd15_openpose",
                    "https://huggingface.co/webui/ControlNet-modules-safetensors/blob/main/control_openpose-fp16.safetensors"
                ],
                [
                    "v10_sd15_canny",
                    "https://huggingface.co/webui/ControlNet-modules-safetensors/blob/main/control_canny-fp16.safetensors"
                ],
                [
                    "v10_sd15_hed",
                    "https://huggingface.co/webui/ControlNet-modules-safetensors/blob/main/control_hed-fp16.safetensors"
                ],
                [
                    "v10_sd15_depth",
                    "https://huggingface.co/webui/ControlNet-modules-safetensors/blob/main/control_depth-fp16.safetensors"
                ],
                [
                    "",
                    ""
                ]
            ]
        },
        "models": {
            "headers": [
                "이름",
                "주소"
            ],
            "data": [
                [
                    "AOM3A1",
                    "https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix3/AOM3A1_orangemixs.safetensors"
                ],
                [
                    "",
                    ""
                ]
            ]
        },
        "loras": {
            "headers": [
                "이름",
                "주소"
            ],
            "data": [
                [
                    "Anime Tarot Card Art Style LoRA",
                    "https://civitai.com/api/download/models/19859"
                ],
                [
                    "",
                    ""
                ]
            ]
        },
        "embeddings": {
            "headers": [
                "이름",
                "주소"
            ],
            "data": [
                [
                    "EasyNegative",
                    "https://civitai.com/api/download/models/9208"
                ],
                [
                    "badhandv4",
                    "https://civitai.com/api/download/models/20068"
                ],
                [
                    "",
                    ""
                ]
            ]
        },
        "vaes": {
            "headers": [
                "이름",
                "주소"
            ],
            "data": [
                [
                    "kl-f8-anime2",
                    "https://huggingface.co/hakurei/waifu-diffusion-v1-4/resolve/main/vae/kl-f8-anime2.ckpt"
                ],
                [
                    "",
                    ""
                ]
            ]
        }
    },
    "authentication": {
        "auth_method": "gradio",
        "auth_username": "",
        "auth_password": "",
        "auth_token": ""
    },
    "cmdline_args": "--xformers --no-gradio-queue",
    "git_url": "https://github.com/AUTOMATIC1111/stable-diffusion-webui.git",
    "git_commit": "",
    "use_virtualenv": true,
    "apply_ddetailer_patches": true,
    "copy_extensions_config": true
}
"""

## @markdown #### <br> 즐겨찾기 ####
## @markdown > 등록 형식 : "이름\[⧉\]\(링크\)"

# fmt: off
## @markdown - 즐겨찾기 : 확장
FAVORITES_EXTENSIONS = [
    ["한글 패치[⧉](https://github.com/36DB/stable-diffusion-webui-localization-ko_KR)"],
    ["3D Openpose Editor[⧉](https://github.com/nonnonstop/sd-webui-3d-open-pose-editor)"],
    ["Bilingual Localization[⧉](https://github.com/journey-ad/sd-webui-bilingual-localization)"],
    ["Booru tag autocompletion[⧉](https://github.com/DominikDoom/a1111-sd-webui-tagcomplete)"],
    ["Civitai Helper[⧉](https://github.com/butaixianran/Stable-Diffusion-Webui-Civitai-Helper.git)"],
    ["Composable LoRA[⧉](https://github.com/opparco/stable-diffusion-webui-composable-lora.git)"],
    ["ControlNet[⧉](https://github.com/Mikubill/sd-webui-controlnet)"],
    ["Cutoff[⧉](https://github.com/hnmr293/sd-webui-cutoff.git)"],
    ["Dataset Tag Editor[⧉](https://github.com/toshiaki1729/stable-diffusion-webui-dataset-tag-editor)"],
    ["Detection Detailer[⧉](https://github.com/dustysys/ddetailer)"],
    ["Dump U-Net[⧉](https://github.com/hnmr293/stable-diffusion-webui-dumpunet.git)"],
    ["Dynamic Prompts[⧉](https://github.com/adieyal/sd-dynamic-prompts.git)"],
    ["Dynamic Thresholding[⧉](https://github.com/mcmonkeyprojects/sd-dynamic-thresholding)"],
    ["Image browser[⧉](https://github.com/AlUlkesh/stable-diffusion-webui-images-browser.git)"],
    ["Kohya-ss Additional Networks[⧉](https://github.com/kohya-ss/sd-webui-additional-networks)"],
    ["Latent Couple[⧉](https://github.com/ashen-sensored/stable-diffusion-webui-two-shot.git)"],
    ["Locon[⧉](https://github.com/KohakuBlueleaf/a1111-sd-webui-locon.git)"],
    ["LyCORIS[⧉](https://github.com/KohakuBlueleaf/a1111-sd-webui-lycoris.git)"],
    ["Preset Utilities[⧉](https://github.com/Gerschel/sd_web_ui_preset_utils.git)"],
    ["Regional Prompter[⧉](https://github.com/hako-mikan/sd-webui-regional-prompter.git)"],
    ["Segment Anything[⧉](https://github.com/continue-revolution/sd-webui-segment-anything.git)"],
    ["stable-diffusion-webui-state[⧉](https://github.com/ilian6806/stable-diffusion-webui-state.git)"],
    ["System Info[⧉](https://github.com/vladmandic/sd-extension-system-info)"],
    ["WD 1.4 Tagger[⧉](https://github.com/toriato/stable-diffusion-webui-wd14-tagger)"],
]

## @markdown - 즐겨찾기 : ControlNet 모델
FAVORITES_CONTROLNET_V10_MODELS = [
    ["v10_sd15_openpose[⧉](https://huggingface.co/webui/ControlNet-modules-safetensors/blob/main/control_openpose-fp16.safetensors)"],
    ["v10_sd15_canny[⧉](https://huggingface.co/webui/ControlNet-modules-safetensors/blob/main/control_canny-fp16.safetensors)"],
    ["v10_sd15_hed[⧉](https://huggingface.co/webui/ControlNet-modules-safetensors/blob/main/control_hed-fp16.safetensors)"],
    ["v10_sd15_depth[⧉](https://huggingface.co/webui/ControlNet-modules-safetensors/blob/main/control_depth-fp16.safetensors)"],
    ["v10_sd15_normal[⧉](https://huggingface.co/webui/ControlNet-modules-safetensors/blob/main/control_normal-fp16.safetensors)"],
    ["v10_sd15_mlsd[⧉](https://huggingface.co/webui/ControlNet-modules-safetensors/blob/main/control_mlsd-fp16.safetensors)"],
    ["v10_sd15_scribble[⧉](https://huggingface.co/webui/ControlNet-modules-safetensors/blob/main/control_scribble-fp16.safetensors)"],
    ["v10_sd15_seg[⧉](https://huggingface.co/webui/ControlNet-modules-safetensors/blob/main/control_seg-fp16.safetensors)"],
]

FAVORITES_CONTROLNET_V11_MODELS = [
    ["v11p_sd15_openpose[⧉](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/blob/main/control_v11p_sd15_openpose_fp16.safetensors)"],
    ["v11p_sd15_canny[⧉](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/blob/main/control_v11p_sd15_canny_fp16.safetensors)"],
    ["v11f1p_sd15_depth[⧉](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/blob/main/control_v11f1p_sd15_depth_fp16.safetensors)"],
    ["v11p_sd15_normalbae[⧉](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/blob/main/control_v11p_sd15_normalbae_fp16.safetensors)"],
    ["v11p_sd15_mlsd[⧉](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/blob/main/control_v11p_sd15_mlsd_fp16.safetensors)"],
    ["v11p_sd15_scribble[⧉](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/blob/main/control_v11p_sd15_scribble_fp16.safetensors)"],
    ["v11p_sd15_seg[⧉](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/blob/main/control_v11p_sd15_seg_fp16.safetensors)"],
    ["v11p_sd15_softedge[⧉](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/blob/main/control_v11p_sd15_softedge_fp16.safetensors)"],
    ["v11p_sd15_lineart[⧉](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/blob/main/control_v11p_sd15_lineart_fp16.safetensors)"],
    ["v11p_sd15s2_lineart_anime[⧉](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/blob/main/control_v11p_sd15s2_lineart_anime_fp16.safetensors)"],
    ["v11p_sd15_inpaint[⧉](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/blob/main/control_v11p_sd15_inpaint_fp16.safetensors)"],
    ["v11u_sd15_tile[⧉](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/blob/main/control_v11u_sd15_tile_fp16.safetensors)"],
    ["v11e_sd15_ip2p[⧉](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/blob/main/control_v11e_sd15_ip2p_fp16.safetensors)"],
    ["v11e_sd15_shuffle[⧉](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/blob/main/control_v11e_sd15_shuffle_fp16.safetensors)"],
]

## @markdown - 즐겨찾기 : 모델
FAVORITES_MODELS = [
    ["AOM3[⧉](https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix3/AOM3_orangemixs.safetensors)"],
    ["AOM3A1[⧉](https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix3/AOM3A1_orangemixs.safetensors)"],
    ["AOM3A2[⧉](https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix3/AOM3A2_orangemixs.safetensors)"],
    ["AOM3A3[⧉](https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix3/AOM3A3_orangemixs.safetensors)"],
    ["Anything V5[⧉](https://civitai.com/api/download/models/30163)"],
    ["Pastel-Mix[⧉](https://civitai.com/api/download/models/6297)"],
    ["ChilloutMix[⧉](https://civitai.com/api/download/models/11745)"],
]

## @markdown - 즐겨찾기 : 로라
FAVORITES_LORAS = [
    ["Anime Tarot Card Art Style LoRA[⧉](https://civitai.com/api/download/models/19859)"],
    ["Anime Lineart[⧉](https://civitai.com/api/download/models/28907)"],
]

## @markdown - 즐겨찾기 : 임베딩
FAVORITES_EMBEDDINGS = [
    ["EasyNegative[⧉](https://civitai.com/api/download/models/9208)"],
    ["badhandv4[⧉](https://civitai.com/api/download/models/20068)"],
    ["bad_prompt_version2[⧉](https://huggingface.co/embed/bad_prompt/resolve/main/bad_prompt_version2.pt)"],
]

## @markdown - 즐겨찾기 : VAES
FAVORITES_VAES = [
    [
        "kl-f8-anime2[⧉](https://huggingface.co/hakurei/waifu-diffusion-v1-4/resolve/main/vae/kl-f8-anime2.ckpt)"
    ],
    [
        "vae-ft-mse-840000-ema-pruned[⧉](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors)"
    ],
]

## @markdown - 즐겨찾기 : 실행 인자
FAVORITES_ARGS = [
    ["--xformers"],
    ["--medvram"],
    ["--no-gradio-queue"],
    ["--no-hashing"],
    ["--disable-console-progressbars"],
    ["--update-all-extensions"],
    ["--reinstall-torch"],
    ["--reinstall-xformers"],
]

## @markdown - 즐겨찾기 : 커밋 해시
FAVORITES_COMMITS = [
    [
        "2023-03-29 gradio==3.23[⧉](https://github.com/AUTOMATIC1111/stable-diffusion-webui/commit/22bcc7be428c94e9408f589966c2040187245d81)"
    ],
    [
        "2023-03-27 gradio==3.23[⧉](https://github.com/AUTOMATIC1111/stable-diffusion-webui/commit/955df7751eef11bb7697e2d77f6b8a6226b21e13)"
    ],
    [
        "2023-03-25 gradio==3.16.2[⧉](https://github.com/AUTOMATIC1111/stable-diffusion-webui/commit/a9eab236d7e8afa4d6205127904a385b2c43bb24)"
    ],
    [
        "2023-02-11 fastapi==0.90.1[⧉](https://github.com/AUTOMATIC1111/stable-diffusion-webui/commit/4f4debbadbf665c483416ee02e12c9b987765103)"
    ],
]
# fmt: on

import os
import sys
import shutil
from pathlib import Path, PurePath
from abc import ABC, abstractmethod

import logging
import logging.handlers

logger = logging.getLogger("Launcher")
logger.setLevel(logging.INFO)


def run(shell, command, cwd=None, check=False, live=False, env=None):
    import shlex
    import subprocess

    if live:
        logger.info(f"Launcher: {command}")
        proc = subprocess.run(
            [shell, "-c", command],
            encoding="utf8",
            errors="ignore",
            cwd=cwd,
            env=env,
        )
        if proc.returncode != 0:
            message = f"RunningCommandError: Return code: '{proc.returncode}', Command: '{command}'"
            if check:
                raise RuntimeError(message)
            else:
                logger.info(f"Launcher: {message}")

        return ""
    else:
        logger.debug(f"Launcher: {command}")
        proc = subprocess.run(
            [shell, "-c", command],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf8",
            errors="ignore",
            cwd=cwd,
            env=env,
        )

        if proc.returncode != 0:
            message = f"RunningCommandError: Return code: '{proc.returncode}', Message: '{proc.stderr if len(proc.stderr)>0 else ''}', Command: '{command}'"
            if check:
                raise RuntimeError(message)
            else:
                logger.warning(f"Launcher: {message}")

        return proc.stdout


class Launcher(ABC):
    import platform

    def __init__(self):
        self.shell = self.bash_path()
        self.environ = os.environ.copy()

    def cmd(self, command, cwd=None, check=False, live=False, env=None):
        return run(
            self.shell,
            command=command,
            cwd=cwd,
            check=check,
            live=live,
            env=env if env else self.environ,
        )

    def setup(self):
        global logger
        try:
            console_log_lvl = logging.INFO
            console_log_fmt = "%(message)s"
            if not logger.handlers:
                if self.service_type() != "노트북":
                    # 노트북에서는 콘솔 로그가 두번 출력되지 않도록 핸들러를 등록하지 않음
                    console_handler = logging.StreamHandler(sys.stdout)
                    console_handler.setLevel(console_log_lvl)
                    console_handler.setFormatter(logging.Formatter(console_log_fmt))
                    logger.addHandler(console_handler)
                else:
                    root_logger = logging.getLogger()
                    root_logger.setLevel(console_log_lvl)
                    root_handler = root_logger.handlers[0]
                    root_handler.setFormatter(logging.Formatter(console_log_fmt))

                log_filename = Path("log", "launcher.log")
                log_filename.parent.mkdir(parents=True, exist_ok=True)
                file_handler = logging.handlers.RotatingFileHandler(
                    log_filename, maxBytes=(1024 * 512), backupCount=3, encoding="utf8"
                )
                file_handler.setFormatter(
                    logging.Formatter(
                        "%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s",
                        datefmt="%Y-%m-%dT%H:%M:%S",
                    )
                )
                file_handler.setLevel(logging.DEBUG)
                logger.addHandler(file_handler)

            # 노트북 재실행할 경우 terminator 복구
            for handler in (
                logging.getLogger("Launcher").handlers + logging.getLogger().handlers
            ):
                handler.terminator = "\n"

        except IndexError:
            logging.basicConfig(
                level=console_log_lvl, format=console_log_fmt, encoding="utf8"
            )

        try:
            if SUPPORT_LAUNCHER_NGROK and not self.is_installed("pyngrok"):
                self.cmd('pip -q install "pyngrok"', check=True, live=True)
        except NameError:
            pass

        logger.info(f"Launcher: 시작, 버전: {VERSION}")

        def info2list(info: dict):
            return [
                "{key}: {val}".format(key=key, val=info[key])
                for i, key in enumerate(info)
                if info[key]
            ]

        for info in info2list(self.system_info()):
            logger.info(f"Launcher: {info}")

        # Suppress pip version upgrade warning
        self.cmd("python -m pip -q install --upgrade pip", check=False, live=True)

        if not self.is_installed("gradio"):
            self.cmd('pip -q install "gradio>=3.21"', check=True, live=True)
        else:
            from importlib.metadata import version

            versioning = ["major", "minor", "patch"]
            gradio_version = dict(
                zip(versioning, map(int, version("gradio").split(".", maxsplit=2)))
            )
            # SD Web UI와 Python 환경을 같이 써서 SD Web UI에서 gradio 버전을 다운그레이드한 경우
            if gradio_version["major"] != 3 or gradio_version["minor"] < 21:
                logger.warning("Launcher: gradio 버전이 낮아 재설치 합니다.")
                self.cmd(
                    'pip -q install --upgrade --force-reinstall "gradio>=3.21"',
                    check=True,
                    live=True,
                )

        if not self.is_installed("bs4"):
            self.cmd('pip -q install "beautifulsoup4"', check=True, live=True)

        if not self.is_installed("lxml"):
            self.cmd('pip -q install "lxml"', check=True, live=True)

        if not self.has_executable("gdown"):
            self.cmd('pip -q install "gdown"', check=True, live=True)

    @staticmethod
    def is_interactive():
        return hasattr(sys, "ps1")

    @staticmethod
    def is_installed(package):
        import importlib.util

        try:
            spec = importlib.util.find_spec(package)
        except ModuleNotFoundError:
            return False
        return spec is not None

    @staticmethod
    def has_executable(name, path=None):
        import shutil

        return shutil.which(cmd=name, path=path) is not None

    @staticmethod
    @abstractmethod
    def bash_path():
        pass

    @staticmethod
    @abstractmethod
    def python_path(venv_path=None):
        pass

    @staticmethod
    def system_info():
        pass

    @staticmethod
    @abstractmethod
    def working_dir():
        pass

    @staticmethod
    @abstractmethod
    def service_name():
        pass

    @staticmethod
    def service_type():
        pass

    @staticmethod
    @abstractmethod
    def is_support_googledrive():
        pass

    @staticmethod
    @abstractmethod
    def is_support_share():
        pass

    @staticmethod
    @abstractmethod
    def is_support_load():
        pass

    @staticmethod
    def force_virtualenv():
        pass

    def start(self, inbrowser=False):
        import gradio as gr
        import time

        service_type = self.service_type()
        sd_webui_path = Path(self.working_dir(), "sd-webui").resolve()

        def load_settings(filename):
            import json

            with open(filename, "r", encoding="utf8") as f:
                settings = json.load(f)

            return {
                workspace_googledrive: gr.Checkbox.update(
                    value=settings["workspace"].get("googledrive", False),
                ),
                workspace_name: gr.Text.update(
                    value=settings["workspace"].get("name", None),
                ),
                extensions: gr.DataFrame.update(
                    value=settings["downloads"].get("extensions", None),
                ),
                controlnet_models: gr.DataFrame.update(
                    value=settings["downloads"].get("controlnet_models", None),
                ),
                models: gr.DataFrame.update(
                    value=settings["downloads"].get("models", None),
                ),
                loras: gr.DataFrame.update(
                    value=settings["downloads"].get("loras", None),
                ),
                embeddings: gr.DataFrame.update(
                    value=settings["downloads"].get("embeddings", None),
                ),
                vaes: gr.DataFrame.update(
                    value=settings["downloads"].get("vaes", None),
                ),
                auth_method: gr.Text.update(
                    value=settings["authentication"].get("auth_method", None),
                ),
                auth_username: gr.Text.update(
                    value=settings["authentication"].get("auth_username", None),
                ),
                auth_password: gr.Text.update(
                    value=settings["authentication"].get("auth_password", None),
                ),
                auth_token: gr.Text.update(
                    value=settings["authentication"].get("auth_token", None),
                ),
                extra_cmdline_args: gr.Text.update(
                    value=settings.get("cmdline_args", None),
                ),
                torch_command: gr.Text.update(
                    value=settings.get("torch_command", None),
                ),
                xformers_package: gr.Text.update(
                    value=settings.get("xformers_package", None),
                ),
                use_virtualenv: gr.Checkbox.update(
                    value=settings.get("use_virtualenv", True),
                ),
                git_url: gr.Text.update(
                    value=settings.get("git_url", None),
                ),
                git_commit: gr.Text.update(
                    value=settings.get("git_commit", None),
                ),
                apply_ddetailer_patches: gr.Checkbox.update(
                    value=settings.get("apply_ddetailer_patches", True),
                ),
                copy_extensions_config: gr.Checkbox.update(
                    value=settings.get("copy_extensions_config", True),
                ),
            }

        def on_default_settings():
            filepath = Path("settings", "default_settings.json")
            logger.info(f'Launcher: 설정 초기화, "{filepath}"')
            if not filepath.exists():
                filepath.parent.mkdir(parents=True, exist_ok=True)
                with open(filepath, "w", encoding="utf8") as f:
                    f.write(DEFAULT_SETTINGS)

            return {
                **load_settings(filepath),
                settings_file: gr.File.update(
                    label="디폴트 설정 파일", value=filepath, visible=True
                ),
            }

        def on_import_settings(filewrap):
            filepath = filewrap.name
            logger.info(f'Launcher: 설정 가져오기, "{filepath}"')

            return {
                **load_settings(filepath),
                settings_file: gr.File.update(
                    label="가져온 설정 파일", value=filepath, visible=True
                ),
            }

        def on_load_last_settings():
            filepath = Path("settings", "last_settings.json")
            if not filepath.exists():
                return {settings_file: gr.File.update(visible=False)}

            logger.info(f'Launcher: 마지막 실행한 설정 불러오기, "{filepath}"')

            return {
                **load_settings(filepath),
                settings_file: gr.File.update(
                    label="불러온 설정 파일", value=filepath, visible=True
                ),
            }

        def save_settings(
            filepath,
            workspace_googledrive,
            workspace_name,
            extensions,
            controlnet_models,
            models,
            loras,
            embeddings,
            vaes,
            auth_method,
            auth_username,
            auth_password,
            auth_token,
            extra_cmdline_args,
            torch_command,
            xformers_package,
            use_virtualenv,
            git_url,
            git_commit,
            apply_ddetailer_patches,
            copy_extensions_config,
        ):
            import json

            with open(filepath, "w", encoding="utf8") as f:
                json.dump(
                    {
                        "workspace": {
                            "name": gr.Text(workspace_name).value,
                            "googledrive": workspace_googledrive,
                        },
                        "downloads": {
                            "extensions": gr.DataFrame(extensions).value,
                            "controlnet_models": gr.DataFrame(controlnet_models).value,
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
                        "cmdline_args": gr.Text(extra_cmdline_args).value,
                        "torch_command": gr.Text(torch_command).value,
                        "xformers_package": gr.Text(xformers_package).value,
                        "use_virtualenv": use_virtualenv,
                        "git_url": gr.Text(git_url).value,
                        "git_commit": gr.Text(git_commit).value,
                        "apply_ddetailer_patches": apply_ddetailer_patches,
                        "copy_extensions_config": copy_extensions_config,
                    },
                    f,
                    ensure_ascii=False,
                    indent=4,
                )

        def on_export_settings(*settings):
            filepath = Path("settings", "my_settings.json")
            logger.info(f'Launcher: 설정 내보내기, "{filepath}"')
            filepath.parent.mkdir(parents=True, exist_ok=True)
            save_settings(filepath, *settings)
            return gr.File.update(label="내보낸 설정 파일", value=filepath, visible=True)

        def on_execute_settings(*settings):
            filepath = Path("settings", "last_settings.json")
            logger.info(f'Launcher: 설정 내보내기, "{filepath}"')
            filepath.parent.mkdir(parents=True, exist_ok=True)
            save_settings(filepath, *settings)
            return gr.File.update(label="마지막 설정 파일", value=filepath, visible=True)

        def on_change_workspace(workspace, googledrive):
            from pathlib import PurePosixPath, PureWindowsPath

            if PurePath(workspace).anchor:
                return [
                    PurePath(sd_webui_path, ""),
                    gr.Markdown.update(
                        visible=True,
                        value="<p style='color:red';>이름은 루트 디렉터리로 시작할 수 없습니다</p>",
                    ),
                ]

            if not workspace and googledrive and self.is_support_googledrive():
                return [
                    PurePath(sd_webui_path, workspace),
                    gr.Markdown.update(
                        visible=True,
                        value="<p style='color:red';>구글 드라이브 연결시 이름을 필수로 입력해 주세요</p>",
                    ),
                ]

            return [
                PurePath(sd_webui_path, workspace),
                gr.Markdown.update(visible=False),
            ]

        def build_cmdline_args(
            workspace_name,
            auth_method,
            auth_username,
            auth_password,
            auth_token,
            extra_args,
        ):
            cmdline_args = []

            import shlex

            override_args = shlex.split(extra_args)  # allow override

            if not "--enable-insecure-extension-access" in override_args:
                cmdline_args += [f"--enable-insecure-extension-access"]

            if not "--autolaunch" in override_args:
                if inbrowser:
                    cmdline_args += [f"--autolaunch"]

            if not "--ngrok" in override_args:
                if auth_method == "ngrok" and auth_token:
                    cmdline_args += [f"--ngrok {auth_token}"]
                    if not "--ngrok-region" in override_args:
                        cmdline_args += [f"--ngrok-region jp"]

            if not "--gradio-auth" in override_args:
                if auth_method == "gradio":
                    cmdline_args += [f"--share"] if self.is_support_share() else []
                    if auth_username and auth_password:
                        cmdline_args += [
                            f"--gradio-auth {auth_username}:{auth_password}"
                        ]
                    elif auth_username:
                        cmdline_args += [f"--gradio-auth {auth_username}"]

            userdata = workspace_name
            if userdata:
                ckpt_path = PurePath(
                    sd_webui_path,
                    userdata,
                    "models",
                    "Stable-diffusion",
                )
                lora_path = PurePath(
                    sd_webui_path,
                    userdata,
                    "models",
                    "Lora",
                )
                vae_path = PurePath(
                    sd_webui_path,
                    userdata,
                    "models",
                    "VAE",
                )
                embeddings_path = PurePath(
                    sd_webui_path,
                    userdata,
                    "embeddings",
                )
                ui_config_path = PurePath(
                    sd_webui_path,
                    userdata,
                    "ui-config.json",
                )
                ui_settings_path = PurePath(
                    sd_webui_path,
                    userdata,
                    "config.json",
                )
                styles_file_path = PurePath(
                    sd_webui_path,
                    userdata,
                    "styles.csv",
                )

                if not "--ckpt-dir" in override_args:
                    cmdline_args += [f'--ckpt-dir "{ckpt_path}"']
                if not "--lora-dir" in override_args:
                    cmdline_args += [f'--lora-dir "{lora_path}"']
                if not "--vae-dir" in override_args:
                    cmdline_args += [f'--vae-dir "{vae_path}"']
                if not "--embeddings-dir" in override_args:
                    cmdline_args += [f'--embeddings-dir "{embeddings_path}"']
                if not "--ui-config-file" in override_args:
                    cmdline_args += [f'--ui-config-file "{ui_config_path}"']
                if not "--ui-settings-file" in override_args:
                    cmdline_args += [f'--ui-settings-file "{ui_settings_path}"']
                if not "--styles-file" in override_args:
                    cmdline_args += [f'--styles-file "{styles_file_path}"']

            cmdline_args += [f"{extra_args}"]

            return cmdline_args

        def has_extension_settings(extensions, name):
            return (
                True
                if [url for url in extensions["주소"].values if name in url]
                else False
            )

        def commit_url_from(git_url, hash):
            from urllib.parse import urljoin

            git_url = git_url.rstrip("/")
            return f"{urljoin(git_url, reponame_from(git_url))}/commit/{hash}"

        def git_url_from(commit_url: str):
            from urllib.parse import urljoin

            return commit_url.rpartition("/commit/")[0]

        def reponame_from(git_url):
            from urllib.parse import urlparse, unquote
            from pathlib import PurePath

            git_url = git_url.rstrip("/")
            return PurePath(unquote(urlparse(git_url).path)).stem  # .git

        def filename_from(url, rstrip=True):
            from urllib.parse import urlparse, unquote
            from pathlib import PurePath

            if rstrip:
                url = url.rstrip("/")
            return PurePath(unquote(urlparse(url).path)).name

        def on_execute_webui(
            workspace_googledrive,
            workspace_name,
            extensions,
            controlnet_models,
            models,
            loras,
            embeddings,
            vaes,
            auth_method,
            auth_username,
            auth_password,
            auth_token,
            extra_cmdline_args,
            torch_command,
            xformers_package,
            use_virtualenv,
            git_url,
            git_commit,
            apply_ddetailer_patches,
            copy_extensions_config,
            progress=lambda x, desc: "",  # gr.Blocks.queue 사용시 응답이 느려서 gr.Progress 대신 콘솔창에 출력
        ):
            def update_progress(progress, steps, total, desc):
                desc = f"({steps}/{total}) {desc}"
                logger.info(f"Launcher: {desc} - {steps/total*100:.2f}%")
                progress(steps / total, desc=desc)

            start_time_execute = time.perf_counter()

            userdata = workspace_name

            """
            진행 스탭 계산
            """
            steps = 0
            total = 4

            total += "gradio" in auth_method

            total += self.is_support_googledrive() and workspace_googledrive

            total += use_virtualenv or self.force_virtualenv()

            extensions = extensions.drop(extensions.query(f'주소 == ""').index)
            total += extensions.count()["주소"]

            controlnet_models = controlnet_models.drop(
                controlnet_models.query(f'주소 == ""').index
            )

            include_controlnet = has_extension_settings(
                extensions, "sd-webui-controlnet"
            )

            if include_controlnet:
                total += controlnet_models.count()["주소"]

            include_ddetailer = has_extension_settings(extensions, "ddetailer")
            if include_ddetailer:
                total += apply_ddetailer_patches

            total += bool(userdata and copy_extensions_config)

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
                self.cmd(
                    f'git -C "{sd_webui_path.parent}" clone {git_url} {sd_webui_path.name}',
                    check=True,
                )

            if git_commit:
                self.cmd(f'git -C "{sd_webui_path}" fetch origin master')
                self.cmd(f'git -C "{sd_webui_path}" checkout {git_commit}')
            else:
                self.cmd(f'git -C "{sd_webui_path}" pull origin master')

            time.sleep(0.1)

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

            if self.is_support_googledrive() and workspace_googledrive and not userdata:
                logger.warning(f"Launcher: 작업 디렉터리 이름이 없어서 구글 드라이브에 연결하지 않고 진행합니다")

            if self.is_support_googledrive() and workspace_googledrive and userdata:
                googledrive_path = Path(self.working_dir(), "drive")
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
                    userdata_path.unlink(missing_ok=True)
                elif userdata_path.exists():
                    logger.warning(
                        f'Launcher: 기존 "{userdata_path}" 디렉터리를 삭제하고 구글 드라이브에 연결 합니다'
                    )
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

            time.sleep(0.1)

            """
            확장 다운로드
            """
            for index, (name, url) in enumerate(
                zip(extensions["이름"], extensions["주소"])
            ):
                assert url
                steps += 1
                update_progress(
                    progress,
                    steps,
                    total,
                    desc=f"확장 다운로드, 이름: {name}, 주소: {url}",
                )
                repository_path = Path(extensions_path, reponame_from(url))
                if not repository_path.exists():
                    self.cmd(
                        f'git -C "{extensions_path}" clone --recursive --depth=1 {url}'
                    )
                    self.cmd(
                        f'git -C "{repository_path}" fetch --depth=1'
                    )  # SD Web UI의 Check for updates 기능을 위해
                time.sleep(0.1)

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
                            --lowest-speed-limit=256K \
                        """
                    )
                )

                u = urlparse(url)
                if u.hostname == "civitai.com":
                    self.cmd(f"aria2c {aria2c_options} {url}", cwd)

                    # 접속 장애로 실제 이름이 아닌, id 이름으로 받아진 모든 파일 삭제
                    import glob

                    assert filename(url).isnumeric()
                    for file in glob.glob(
                        str(Path(cwd, f"{filename(url)}*")),
                        recursive=False,
                    ):
                        logger.warning(f"Launcher: 다운로드 실패, 주소 : {url}")
                        Path(file).unlink(missing_ok=True)

                elif u.hostname == "huggingface.co":
                    url = url.replace("/blob/", "/resolve/")
                    self.cmd(
                        f"aria2c {aria2c_options} {url} --out={filename(url)}", cwd
                    )
                elif u.hostname == "drive.google.com":
                    self.cmd(f"gdown --fuzzy {url}", cwd)
                else:
                    self.cmd(f"aria2c {aria2c_options} {url}", cwd)

            """
            확장 설정 파일 복사
             - 심볼릭 링크를 통한 동기화를 사용하지 않는 이유 : gradio 접근 권한 문제
            """
            if userdata and copy_extensions_config:
                steps += 1
                extensions_path_target = Path(userdata_path, "extensions")
                assert extensions_path_target != extensions_path

                import glob

                # 하위 경로의 모든 json 파일 복사
                for file in glob.glob(
                    str(Path(extensions_path_target, "**/*.json")),
                    recursive=True,
                ):
                    src = Path(file).absolute()
                    rel = src.relative_to(extensions_path_target)
                    dst = Path(extensions_path, rel).absolute()

                    repository_path = Path(extensions_path, rel.parts[0])
                    if repository_path.exists():
                        update_progress(
                            progress,
                            steps,
                            total,
                            desc=f"확장 설정 파일 복사, 경로: {src} -> {dst}",
                        )
                        if dst.parent.is_dir():
                            dst.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copyfile(src, dst)

                for index, (name, url) in enumerate(
                    zip(extensions["이름"], extensions["주소"])
                ):
                    assert url

                    reponame = reponame_from(url)
                    repository_path = Path(extensions_path, reponame)
                    repository_path_target = Path(userdata_path, "extensions", reponame)
                    if (
                        repository_path != repository_path_target
                        and repository_path.exists()
                        and repository_path_target.exists()
                    ):
                        # 레포 디렉터리 지정 복사
                        if reponame == "sd-dynamic-prompts":
                            src = Path(repository_path_target, "wildcards")
                            dst = Path(repository_path, "wildcards")

                            update_progress(
                                progress,
                                steps,
                                total,
                                desc=f"확장 설정 파일 복사, 이름: {reponame}, 경로: {src} -> {dst}",
                            )
                            shutil.copytree(src, dst, dirs_exist_ok=True)

                    time.sleep(0.1)

            """
            컨트롤넷 모델 다운로드
            TODO : --controlnet-dir 옵션으로 구글 드라이브에 저장 가능 하도록 선택 기능 제공
            """
            for index, (name, url) in enumerate(
                zip(controlnet_models["이름"], controlnet_models["주소"])
            ):
                assert url
                controlnet_models_path = Path(
                    extensions_path, "sd-webui-controlnet", "models"
                )

                if include_controlnet and Path(controlnet_models_path).exists():
                    steps += 1
                    update_progress(
                        progress,
                        steps,
                        total,
                        desc=f"컨트롤넷 모델 다운로드, 이름: {name}, 주소: {url}",
                    )
                    download(url, cwd=controlnet_models_path)
                time.sleep(0.1)

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
                time.sleep(0.1)

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
                time.sleep(0.1)

            """
            임베딩 다운로드
            """
            for index, (name, url) in enumerate(
                zip(embeddings["이름"], embeddings["주소"])
            ):
                assert url
                steps += 1
                update_progress(
                    progress,
                    steps,
                    total,
                    desc=f"임베딩 다운로드, 이름: {name}, 주소: {url}",
                )
                download(url, cwd=embeddings_path)
                time.sleep(0.1)

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
                time.sleep(0.1)

            if use_virtualenv or self.force_virtualenv():
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

                venv_path = Path(sd_webui_path, "venv")
                if not venv_path.exists():
                    self.cmd(
                        f'python -m venv "{venv_path}" --without-pip',
                        check=True,
                    )

                python_path = self.python_path(venv_path)
            else:
                python_path = self.python_path()

            webui_environ = self.environ.copy()
            webui_environ["PATH"] = (
                str(python_path.parent) + os.pathsep + webui_environ["PATH"]
            )

            # No module named pip
            # No module named ensurepip
            pip_path = python_path.with_stem("pip")
            if not pip_path.exists():
                # curl https://bootstrap.pypa.io/get-pip.py 방법은 SSL certificate 문제가 있음
                import urllib.request

                Path("temp").mkdir(parents=True, exist_ok=True)
                get_pip_py = Path("temp", "get-pip.py")
                urllib.request.urlretrieve(
                    "https://bootstrap.pypa.io/get-pip.py",
                    get_pip_py,
                )

                self.cmd(
                    f'"{python_path}" "{get_pip_py}"',
                    check=True,
                    env=webui_environ,
                )

                self.cmd(
                    f'"{python_path}" -m pip --help', check=True, env=webui_environ
                )

            # Repect SD Web UI default, need --reinstall-torch for already installed
            if torch_command:
                webui_environ["TORCH_COMMAND"] = torch_command

            # Repect SD Web UI default, need --reinstall-xformers for already installed
            if xformers_package:
                webui_environ["XFORMERS_PACKAGE"] = xformers_package

            def torch_cuda_version(torch_command):
                import re

                pattern = re.compile(
                    r"pip\s+install\s+torch==([0-9]+\.[0-9]+\.[0-9]+)\+cu(\d\d\d)\s+.*",
                    re.IGNORECASE,
                )
                return pattern.match(torch_command)

            if torch_command:
                torch_version, cuda_version = torch_cuda_version(torch_command).groups()
                versioning = ["major", "minor", "patch"]
                torch_version = dict(
                    zip(versioning, map(int, torch_version.split(".", maxsplit=2)))
                )

            # Patch extensions dependencies
            for index, (name, url) in enumerate(
                zip(extensions["이름"], extensions["주소"])
            ):
                assert url
                reponame = reponame_from(url)
                if reponame == "ddetailer":
                    if torch_command and torch_version["major"] > 1:
                        version_string = ".".join(
                            str(torch_version[x]) for x in sorted(torch_version)
                        )
                        logger.warning(
                            f"Launcher: {reponame} 확장은 Torch {version_string} 버전과 호환되지 않을 수 있습니다"
                        )
                    if apply_ddetailer_patches:
                        diff_path = Path(
                            extensions_path,
                            reponame,
                            "deprecate_lib2to3.diff",
                        )
                        steps += 1
                        update_progress(
                            progress,
                            steps,
                            total,
                            desc=f"{reponame} 확장 패치 적용, {diff_path}",
                        )

                        self.cmd(
                            f'curl -sS --location --output "{diff_path}" https://raw.githubusercontent.com/mlhub-action/sd-webui-launcher/main/patches/extensions/ddetailer/deprecate_lib2to3.diff'
                        )
                        self.cmd(
                            f'patch -N -d "{diff_path.parent}" -p1 < "{diff_path}" || true',
                            check=False,
                        )
                    break
                time.sleep(0.1)

            """
            SD Web UI 실행 시작
            """
            cmdline_args = " ".join(
                build_cmdline_args(
                    workspace_name,
                    auth_method,
                    auth_username,
                    auth_password,
                    auth_token,
                    extra_cmdline_args,
                )
            )  # shlex.join

            steps += 1

            update_progress(
                progress,
                steps,
                total,
                desc=f"SD Web UI 실행 시작, 인자: {cmdline_args}",
            )

            time.sleep(0.1)

            tunnel_url = None

            if "cloudflare" in auth_method:
                if not self.is_installed("pycloudflared"):
                    self.cmd('pip -q install "pycloudflared"', check=True, live=False)

                from pycloudflared import try_cloudflare

                tunnel_url = f"Running on public URL: {try_cloudflare(port=SD_WEBUI_PORT).tunnel}"

            import subprocess

            launch_path = Path(sd_webui_path, "launch.py")
            with subprocess.Popen(
                [
                    self.shell,
                    "-c",
                    f'"{python_path}" -u "{launch_path}" {cmdline_args}',
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                bufsize=1,
                text=True,
                encoding="utf8",
                errors="ignore",
                cwd=sd_webui_path,
                env=webui_environ,
            ) as proc:
                for handler in (
                    logging.getLogger("Launcher").handlers
                    + logging.getLogger().handlers
                ):
                    handler.terminator = ""
                for line in proc.stdout:
                    # Skip huggingface.co ad link
                    if not line.startswith("This share link expires in"):
                        logger.info("SDWebUI: " + line)

                    if line.startswith("ngrok connected to"):
                        tunnel_url = f"Running on public URL: {line.partition(':')[-1]}"
                    if line.startswith("Running on local URL:") or line.startswith(
                        "Running on public URL:"
                    ):
                        end_time_execute = time.perf_counter()
                        steps += 1
                        update_progress(
                            progress,
                            steps,
                            total,
                            desc=f"SD Web UI 실행 완료, {tunnel_url if tunnel_url else line}\n",
                        )
                        from datetime import datetime as dt
                        from datetime import timedelta

                        duration = dt.utcfromtimestamp(
                            timedelta(
                                seconds=end_time_execute - start_time_execute
                            ).total_seconds()
                        )
                        logger.info(
                            f'Launcher: 실행까지 걸린 시간: {duration.strftime("%H:%M:%S")}\n'
                        )

            return f"SD Web UI 실행 종료"

        """
        SD Web UI 런처 앱
        """
        with gr.Blocks(
            gr.themes.Soft(),
            css="#info-box {background-color: Gainsboro} #progress-box {background-color: DarkSeaGreen} #progress-tooltip {color:DeepPink !important; text-align: center;}",
        ) as demo:
            gr.Markdown(
                f"""
                # 코랩/런팟용 SD Web UI 런처 {VERSION}
                - [최신 버전](https://github.com/mlhub-action/sd-webui-launcher)
                - [이슈/버그 리포트](https://github.com/mlhub-action/sd-webui-launcher/issues)
                > 💡 팁1: 인증 정보가 담긴 설정 파일을 다른 사람과 공유하지 마세요
                {"> 💡 팁2: 웹 페이지가 로드될 때 마지막 실행한 설정을 불러 옵니다" if self.is_support_load() else ''}
                """
            )

            with gr.Row():
                default_settings = gr.Button("설정 초기화", variant="secondary")
                import_settings = gr.UploadButton(
                    "설정 가져오기",
                    file_types=["file"],
                    file_count="single",
                )
                export_settings = gr.Button("설정 내보내기")
                execute_webui = gr.Button("실행", variant="primary")

            with gr.Box():
                settings_file = gr.File(
                    label="설정 파일", file_types=["file"], visible=False, interactive=True
                )

            with gr.Box():
                progress_tooltip = gr.Markdown(
                    f'<p style="color:DeepPink !important; text-align: center;"><em>진행 과정은 {service_type} 출력창에서 확인해 주세요</em></p>',
                    elem_id="progress-tooltip",
                )
                progress = gr.Text(
                    elem_id="progress-box", show_label=False, interactive=False
                )

            with gr.Box():
                gr.Markdown(
                    """
                    # 1. 작업 디렉터리
                    모델, 로라, VAE, 설정 파일 등을 따로 저장할 작업 디렉터리 이름을 입력해주세요. 
                    """
                )

                with gr.Tabs():
                    with gr.Tab(self.service_name()) as tab:
                        workspace_googledrive = gr.Checkbox(
                            label="구글 드라이브 연결",
                            info="사용 가능한 저장 용량이 5GB 이상 남았는지 확인해주세요",
                            visible=self.is_support_googledrive(),
                        )
                        workspace_name = gr.Text(
                            label="이름",
                            info="  디렉터리 이름 규칙에 따라 입력해주세요",
                            placeholder="비워두면 기본 작업 디렉토리를 사용합니다. 예) SD 또는 userdata",
                            interactive=True,
                        )
                        workspace_tooltip = gr.Markdown(visible=False)
                        workspace_path = gr.Textbox(
                            elem_id="info-box",
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
                        workspace_name.submit(
                            fn=on_change_workspace,
                            inputs=[workspace_name, workspace_googledrive],
                            outputs=[workspace_path, workspace_tooltip],
                        )

            with gr.Box():
                gr.Markdown(
                    """
                    # 2. 다운로드 주소
                    [civitai](https://civitai.com/) 또는 [huggingface](https://huggingface.co/)에서 다운로드 할 주소 목록을 작성해주세요.
                    > 💡 이름은 표시 용도니 자유롭게 정하세요.
                    > 💡 테이블의 셀을 더블 클릭하면 편집/삭제 가능합니다.
                    > 💡 오른쪽 즐겨찾기를 클릭하면 자동으로 테이블에 추가됩니다.
                    > 💡 작업 디렉터리에 저장되는 것만(⭕) 구글 드라이브 연결시 동기화 됩니다. 
                    """
                )
                gr.Markdown("<br/>")

                def favorite_tuple(markdown: str):
                    from bs4 import BeautifulSoup

                    try:
                        soup = BeautifulSoup(markdown, features="lxml")
                        return soup.p.text.rstrip("⧉"), soup.a.get("href")
                    except Exception as error:
                        message = "즐겨찾기 형식이 올바르지 않습니다"
                        logger.info(f"Launcher: {message}, error: {error}")
                        return "", ""

                def on_click_favorites(table, evt: gr.SelectData):
                    import pandas

                    name, url = favorite_tuple(evt.value[0])
                    if url:
                        logger.info(f"Launcher: 즐겨찾기 추가 이름: {name} 주소: {url}")

                        exist = table.query(f'주소 == "{url}"')
                        if len(exist.index.tolist()) > 0:
                            return table
                        else:
                            empty = table.query(f'이름 == "" and 주소 == ""')
                            table = table.drop(empty.index)
                            favorite = pandas.DataFrame({"이름": [name], "주소": [url]})
                            editable = pandas.DataFrame({"이름": [""], "주소": [""]})
                            return pandas.concat(
                                [table, favorite, editable], ignore_index=True
                            )
                    else:
                        return gr.DataFrame.update()

                with gr.Accordion("모델", open=True):
                    gr.Markdown(
                        """
                        > 작업 디렉터리에 저장 ⭕
                        """
                    )
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
                    gr.Markdown(
                        """
                        > 작업 디렉터리에 저장 ❌, 설정 파일은 복사 ⭕
                        """
                    )
                    with gr.Row():
                        with gr.Column(scale=0.8):
                            with gr.Tab("저장소"):
                                extensions = gr.Dataframe(
                                    headers=["이름", "주소"],
                                    datatype=["str", "str"],
                                    row_count=3,
                                    col_count=(2, "fixed"),
                                    interactive=True,
                                )
                            with gr.Tab("(선택) 설정 파일 복사") as ddetailer_tab:
                                copy_extensions_config = gr.Checkbox(
                                    label="구글 드라이브에 연결시 확장별 설정 파일 복사",
                                    info="작업 디렉터리의 extensions 경로 아래 저장된 확장별 설정 파일을 복사해서 사용합니다. 기본값, 체크",
                                    value=True,
                                )
                                gr.Markdown(
                                    """
                                    > 📝 체크시: 확장별 설정 파일을 복사해서 사용 함 
                                    > 📝 해제시: 확장별 설정 파일을 복사해서 사용 안함
                                    > 💡 확장별 설정 파일: extensions/\*\*/\*.json | extensions/sd-dynamic-prompts/wildcards/\*.txt
                                    """
                                )
                            with gr.Tab("ControlNet 모델") as controlnet_tab:
                                controlnet_models = gr.Dataframe(
                                    headers=["이름", "주소"],
                                    datatype=["str", "str"],
                                    row_count=3,
                                    col_count=(2, "fixed"),
                                    interactive=True,
                                )
                                gr.Markdown(
                                    """
                                    > 📝 컨트롤넷 모델은 작업 디렉터리에 저장하지 않고 매번 다운로드
                                    > 📝 구글 드라이브 이용은 [ControlNet 모델 추가 경로 설정](https://github.com/mlhub-action/sd-webui-launcher/tree/main/docs/settings#controlnet-%EB%AA%A8%EB%8D%B8-%EC%B6%94%EA%B0%80-%EA%B2%BD%EB%A1%9C-%EC%84%A4%EC%A0%95) 참고
                                    """
                                )
                            with gr.Tab("Detection Detailer") as ddetailer_tab:
                                apply_ddetailer_patches = gr.Checkbox(
                                    label="설치 문제 패치 적용",
                                    info="기본값, 체크",
                                    value=True,
                                )
                                gr.Markdown(
                                    """
                                    > 📝 체크시: No module named 'lib2to3' 문제 해결 => ⚠️버전 호환성 나쁨
                                    > 📝 해제시: 패치 안함 => 👍버전 호환성 좋음
                                    """
                                )

                        with gr.Column(scale=0.2):
                            with gr.Tab("확장 저장소"):
                                gr.Markdown(
                                    "[찾아보기](https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui-extensions/master/index.json)"
                                )
                                extensions_favorites = gr.Dataset(
                                    components=[gr.Markdown(visible=False)],
                                    label="즐겨찾기",
                                    samples=FAVORITES_EXTENSIONS,
                                    samples_per_page=10,
                                )
                                extensions_favorites.select(
                                    fn=on_click_favorites,
                                    inputs=extensions,
                                    outputs=extensions,
                                )
                            with gr.Tab("ControlNet v10 모델"):
                                gr.Markdown(
                                    "[찾아보기](https://huggingface.co/webui/ControlNet-modules-safetensors/tree/main)"
                                )
                                controlnet_v10_favorites = gr.Dataset(
                                    components=[gr.Markdown(visible=False)],
                                    label="즐겨찾기",
                                    samples=FAVORITES_CONTROLNET_V10_MODELS,
                                    samples_per_page=10,
                                )
                                controlnet_v10_favorites.select(
                                    fn=on_click_favorites,
                                    inputs=controlnet_models,
                                    outputs=controlnet_models,
                                )
                            with gr.Tab("ControlNet v11 모델"):
                                gr.Markdown(
                                    "[찾아보기](https://huggingface.co/lllyasviel/ControlNet-v1-1/tree/main)"
                                )
                                controlnet_v11_favorites = gr.Dataset(
                                    components=[gr.Markdown(visible=False)],
                                    label="즐겨찾기",
                                    samples=FAVORITES_CONTROLNET_V11_MODELS,
                                    samples_per_page=10,
                                )
                                controlnet_v11_favorites.select(
                                    fn=on_click_favorites,
                                    inputs=controlnet_models,
                                    outputs=controlnet_models,
                                )
                    gr.Markdown("<br/>")

                with gr.Accordion("로라", open=self.is_support_load()):
                    gr.Markdown(
                        """
                        > 작업 디렉터리에 저장 ⭕
                        """
                    )
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

                with gr.Accordion("임베딩", open=self.is_support_load()):
                    gr.Markdown(
                        """
                        > 작업 디렉터리에 저장 ⭕
                        """
                    )
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
                                fn=on_click_favorites,
                                inputs=embeddings,
                                outputs=embeddings,
                            )
                    gr.Markdown("<br/>")

                with gr.Accordion("VAE", open=self.is_support_load()):
                    gr.Markdown(
                        """
                        > 작업 디렉터리에 저장 ⭕
                        """
                    )
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
                    SD Web UI에 접속할 방법을 선택해 주세요.
                    """
                )
                auth_method_mapping = {
                    "gradio(기본값)": "gradio",
                    "cloudflare": "cloudflare",
                    "ngrok": "ngrok",
                }
                auth_method = gr.Text(visible=False, value="gradio")
                auth_method_dropdown = gr.Dropdown(
                    label="Tunnel",
                    info="  웹 응답이 느릴 때 다른 Tunnel을 선택해 보세요.",
                    value="gradio(기본값)",
                    choices=[*auth_method_mapping.keys()],
                    interactive=True,
                )

                with gr.Box(visible=True) as tab_gradio:
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

                with gr.Box(visible=False) as tab_cloudflare:
                    gr.Markdown("[인증 정보 필요 없음](https://try.cloudflare.com/)")

                with gr.Box(visible=False) as tab_ngrok:
                    gr.Markdown(
                        "[인증 토큰?](https://dashboard.ngrok.com/get-started/your-authtoken)"
                    )
                    auth_token = gr.Text(
                        label="Authtoken",
                        placeholder="인증 토큰을 입력해 주세요",
                        interactive=True,
                    )

                def on_update_auth_method(value):
                    return [
                        gr.Box.update(visible=value in v)
                        for k, v in auth_method_mapping.items()
                    ]

                def resolve_auth_method(auth_method):
                    for (
                        key,
                        value,
                    ) in auth_method_mapping.items():
                        if auth_method == value:
                            break
                    return key, value

                def on_change_auth_method(auth_method):
                    key, value = resolve_auth_method(auth_method)
                    return [
                        gr.Dropdown.update(value=key),
                        *on_update_auth_method(value),
                    ]

                auth_method.change(
                    fn=on_change_auth_method,
                    inputs=auth_method,
                    outputs=[
                        auth_method_dropdown,
                        tab_gradio,
                        tab_cloudflare,
                        tab_ngrok,
                    ],
                )

                def on_select_auth_method(evt: gr.SelectData):
                    value = auth_method_mapping[evt.value]
                    return [
                        gr.Text.update(value=value),
                        *on_update_auth_method(value),
                    ]

                auth_method_dropdown.select(
                    fn=on_select_auth_method,
                    inputs=None,
                    outputs=[
                        auth_method,
                        tab_gradio,
                        tab_cloudflare,
                        tab_ngrok,
                    ],
                )

            with gr.Box():
                gr.Markdown(
                    """
                    # 4. 실행 방법
                    [SD Web UI 실행 인자](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Command-Line-Arguments-and-Settings#all-command-line-arguments)를 입력해 주세요.
                    > 🔥 RTX 40 시리즈 사용시, 속도 향상을 위해 Torch 버전 2.0.0+cu118, xFormers 버전 0.0.17, 가상 환경 사용을 추천합니다.
                    """
                )
                gr.Markdown("<br/>")
                with gr.Row():
                    with gr.Column(scale=0.8):
                        with gr.Tab("실행 인자"):
                            gr.Markdown(
                                """
                                > 💡 팁: 설치된 확장을 모두 업데이트 하려면, --update-all-extensions 실행 인자를 추가해 주세요
                                """
                            )

                            extra_cmdline_args = gr.Text(
                                label="추가 실행 인자",
                                info="  추가 실행 인자를 입력해 주세요",
                                placeholder="필요 없으면 비칸으로 두세요. 예) --xformers",
                                value="",
                                interactive=True,
                            )
                            cmdline_args = gr.Text(
                                elem_id="info-box",
                                label="전체 실행 인자",
                                info="  실행 인자를 입력하면 아래에 전체 실행 인자가 표시됩니다",
                                interactive=False,
                            )

                            extra_cmdline_args.change(
                                fn=lambda *args: "\n".join(build_cmdline_args(*args)),
                                inputs=[
                                    workspace_name,
                                    auth_method,
                                    auth_username,
                                    auth_password,
                                    auth_token,
                                    extra_cmdline_args,
                                ],
                                outputs=cmdline_args,
                            )
                            workspace_name.blur(
                                fn=lambda *args: "\n".join(build_cmdline_args(*args)),
                                inputs=[
                                    workspace_name,
                                    auth_method,
                                    auth_username,
                                    auth_password,
                                    auth_token,
                                    extra_cmdline_args,
                                ],
                                outputs=cmdline_args,
                            )
                            auth_method.change(
                                fn=lambda *args: "\n".join(build_cmdline_args(*args)),
                                inputs=[
                                    workspace_name,
                                    auth_method,
                                    auth_username,
                                    auth_password,
                                    auth_token,
                                    extra_cmdline_args,
                                ],
                                outputs=cmdline_args,
                            )
                            auth_username.blur(
                                fn=lambda *args: "\n".join(build_cmdline_args(*args)),
                                inputs=[
                                    workspace_name,
                                    auth_method,
                                    auth_username,
                                    auth_password,
                                    auth_token,
                                    extra_cmdline_args,
                                ],
                                outputs=cmdline_args,
                            )
                            auth_password.blur(
                                fn=lambda *args: "\n".join(build_cmdline_args(*args)),
                                inputs=[
                                    workspace_name,
                                    auth_method,
                                    auth_username,
                                    auth_password,
                                    auth_token,
                                    extra_cmdline_args,
                                ],
                                outputs=cmdline_args,
                            )
                            auth_token.blur(
                                fn=lambda *args: "\n".join(build_cmdline_args(*args)),
                                inputs=[
                                    workspace_name,
                                    auth_method,
                                    auth_username,
                                    auth_password,
                                    auth_token,
                                    extra_cmdline_args,
                                ],
                                outputs=cmdline_args,
                            )
                        with gr.Tab("(선택) Torch+xFormers"):
                            with gr.Box():
                                # https://pytorch.org/get-started/locally/
                                torch_command_mapping = {
                                    "빈칸(기본값)": "",
                                    "1.13.1+cu116": "pip install torch==1.13.1+cu116 torchvision==0.14.1+cu116 --extra-index-url https://download.pytorch.org/whl/cu116",
                                    "1.13.1+cu117": "pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 --extra-index-url https://download.pytorch.org/whl/cu117",
                                    "2.0.0+cu118": "pip install torch==2.0.0+cu118 torchvision==0.15.1+cu118 --extra-index-url https://download.pytorch.org/whl/cu118",
                                    "직접 입력": "",
                                }

                                torch_command_dropdown = gr.Dropdown(
                                    label="Torch 버전",
                                    info="  Torch 버전을 선택해 주세요. 해당 버전으로 재설치 하려면 --reinstall-torch 실행 인자를 추가해 주세요",
                                    value="빈칸(기본값)",
                                    choices=[*torch_command_mapping.keys()],
                                    interactive=True,
                                )

                                torch_command = gr.Text(
                                    elem_id="info-box",
                                    label="TORCH_COMMAND",
                                    info="  Torch 버전을 선택하면 아래에 TORCH_COMMAND 환경 변수가 표시됩니다",
                                    # value=torch_command_mapping[torch_command_dropdown.value],
                                    interactive=False,
                                )

                                gr.Markdown(
                                    """
                                    > ⚠️ Torch 2.0.0 버전은 아직 공식 지원 버전이 아닙니다 
                                    > ⚠️ 따라서 호환되지 않은 확장이 있을 수 있습니다
                                    """
                                )

                                def resolve_torch_command(torch_command):
                                    if not torch_command:
                                        for (
                                            key,
                                            value,
                                        ) in torch_command_mapping.items():
                                            if "기본값" in key:
                                                break
                                        return key, value
                                    else:
                                        for (
                                            key,
                                            value,
                                        ) in torch_command_mapping.items():
                                            if torch_command == value:
                                                break
                                        return key, value

                                def on_change_torch_command(torch_command):
                                    key, value = resolve_torch_command(torch_command)
                                    return gr.Dropdown.update(value=key)

                                torch_command.change(
                                    fn=on_change_torch_command,
                                    inputs=torch_command,
                                    outputs=torch_command_dropdown,
                                )

                                def on_select_torch_command(evt: gr.SelectData):
                                    value = torch_command_mapping[evt.value]
                                    return gr.Text.update(
                                        value=value, interactive=not value
                                    )

                                torch_command_dropdown.select(
                                    fn=on_select_torch_command,
                                    inputs=None,
                                    outputs=torch_command,
                                )
                            with gr.Box():
                                # https://pypi.org/project/xformers/#history
                                xformers_package_mapping = {
                                    "빈칸(기본값)": "",
                                    "0.0.16rc425(torch==1.13.1)": "xformers==0.0.16rc425",
                                    "0.0.17(torch==2.0.0)": "xformers==0.0.17",
                                    "직접 입력": "",
                                }

                                xformers_package_dropdown = gr.Dropdown(
                                    label="xFormers 버전",
                                    info="  xFormers 패키지 버전을 선택해 주세요. 해당 버전으로 재설치 하려면 --reinstall-xformers 실행 인자를 추가해 주세요",
                                    value="빈칸(기본값)",
                                    choices=[*xformers_package_mapping.keys()],
                                    interactive=True,
                                )

                                xformers_package = gr.Text(
                                    elem_id="info-box",
                                    label="XFORMERS_PACKAGE",
                                    info="  xFormers 패키지 버전을 선택하면 아래에 XFORMERS_PACKAGE 환경 변수가 표시됩니다",
                                    # value=xformers_package_mapping[xformers_package_dropdown.value],
                                    interactive=False,
                                )

                                gr.Markdown(
                                    """
                                    > ⚠️ Torch 버전과 일치하는 패키지를 선택해 주세요
                                    """
                                )

                                def resolve_xformers_package(xformers_package):
                                    if not xformers_package:
                                        for (
                                            key,
                                            value,
                                        ) in xformers_package_mapping.items():
                                            if "기본값" in key:
                                                break
                                        return key, value
                                    else:
                                        for (
                                            key,
                                            value,
                                        ) in xformers_package_mapping.items():
                                            if xformers_package == value:
                                                break
                                        return key, value

                                def on_change_xformers_command(xformers_package):
                                    key, value = resolve_xformers_package(
                                        xformers_package
                                    )
                                    return gr.Dropdown.update(value=key)

                                xformers_package.change(
                                    fn=on_change_xformers_command,
                                    inputs=xformers_package,
                                    outputs=xformers_package_dropdown,
                                )

                                def on_select_xformers_command(evt: gr.SelectData):
                                    value = xformers_package_mapping[evt.value]
                                    return gr.Text.update(
                                        value=value, interactive=not value
                                    )

                                xformers_package_dropdown.select(
                                    fn=on_select_xformers_command,
                                    inputs=None,
                                    outputs=xformers_package,
                                )

                        with gr.Tab("(선택) 가상 환경"):
                            use_virtualenv = gr.Checkbox(
                                label="Python 가상 환경 venv 사용",
                                info="기본값, 체크",
                                value=True,
                            )
                            gr.Markdown(
                                f"""
                                > 📝 체크시: 가상 환경 venv 생성 => 🐢설치 속도 느림, 👍버전 호환성 좋음
                                > 📝 해제시: 코랩/런팟 기본 환경 사용 => 🐇설치 속도 빠름, ⚠️버전 호환성 나쁨
                                {"> ⚠️ 단, 로컬/런팟은 가상 환경 사용이 강제" if self.force_virtualenv() else ''}
                                """
                            )
                    with gr.Column(scale=0.2):
                        args_favorites = gr.Dataset(
                            components=[gr.Textbox(visible=False)],
                            label="주요 성능 관련 인자",
                            samples=FAVORITES_ARGS,
                        )

                        def on_click_args_favorites(cmdargs: str, evt: gr.SelectData):
                            arg = evt.value[0]
                            logger.info(f"Launcher: 실행 인자 추가: {arg}")
                            if cmdargs.find(evt.value[0]) != -1:
                                return cmdargs
                            else:
                                return f"{cmdargs} {arg}"

                        args_favorites.select(
                            fn=on_click_args_favorites,
                            inputs=extra_cmdline_args,
                            outputs=extra_cmdline_args,
                        )

            with gr.Box():
                gr.Markdown(
                    """
                    # 5. 깃 저장소 설정
                    [SD Web UI 깃 저장소](https://github.com/AUTOMATIC1111/stable-diffusion-webui.git)를 입력해 주세요.
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
                            info="  (선택) 다른 버전을 사용하려면 입력해 주세요. 예) 22bcc7be428c94e9408f589966c2040187245d81",
                            placeholder="최신 버전을 사용하려면 빈칸으로 두세요.",
                            interactive=True,
                        )
                    with gr.Column(scale=0.2):
                        with gr.Tab("사전에 등록된"):
                            commit_favorites = gr.Dataset(
                                components=[gr.Markdown(visible=False)],
                                label="즐겨찾기",
                                samples=FAVORITES_COMMITS,
                            )

                            def on_click_commit_favorites(evt: gr.SelectData):
                                name, commit_url = favorite_tuple(evt.value[0])
                                commit = filename_from(commit_url)
                                logger.info(
                                    f"Launcher: 커밋 해시 변경, 이름: {name} , 해시:{commit}"
                                )
                                return {
                                    git_url: gr.Text.update(
                                        value=git_url_from(commit_url)
                                    ),
                                    git_commit: gr.Text.update(
                                        value=commit, label=f"Commit hash - {name}"
                                    ),
                                }

                            commit_favorites.select(
                                fn=on_click_commit_favorites,
                                inputs=None,
                                outputs=[git_url, git_commit],
                            )

                        with gr.Tab("최근 5일간 변경 내역") as commit_since5days_tab:
                            commit_since5days = gr.Dataset(
                                components=[gr.Markdown(visible=False)],
                                label="즐겨찾기",
                                samples=[[""]],
                            )

                            def on_click_commit_since5days(evt: gr.SelectData):
                                name, commit_url = favorite_tuple(evt.value[0])
                                if commit_url:
                                    commit = filename_from(commit_url)
                                    logger.info(
                                        f"Launcher: 커밋 해시 변경, 이름: {name} , 해시:{commit}"
                                    )
                                    return {
                                        git_url: gr.Text.update(
                                            value=git_url_from(commit_url)
                                        ),
                                        git_commit: gr.Text.update(
                                            value=commit, label=f"Commit hash - {name}"
                                        ),
                                    }
                                else:
                                    return {
                                        git_url: gr.Text.update(),
                                        git_commit: gr.Text.update(),
                                    }

                            commit_since5days.select(
                                fn=on_click_commit_since5days,
                                inputs=None,
                                outputs=[git_url, git_commit],
                            )

                            def on_select_commit_since5days_tab(git_url):
                                try:
                                    if not self.is_installed("git"):
                                        self.cmd(
                                            'pip -q install "GitPython"',
                                            check=False,
                                            live=True,
                                        )

                                    import git

                                    if not sd_webui_path.exists():
                                        samples = [[f"<p>다운로드 받은 저장소 없음</p>"]]
                                    else:
                                        repo = git.Repo(sd_webui_path)
                                        repo.remotes.origin.fetch()
                                        since5days = [
                                            entry.split(" ", 2)
                                            for entry in git.Git(sd_webui_path)
                                            .log(
                                                "--since=5.days",
                                                "--format=%cd %H %s",
                                                "--date=short",
                                            )
                                            .split("\n")
                                        ]
                                        if not since5days:
                                            samples = [[f"<p>변경 내역 없음</p>"]]
                                        else:
                                            samples = list()
                                            only_lastest_per_day = set()
                                            for log in since5days:
                                                (date, hash, msg) = log
                                                if not date in only_lastest_per_day:
                                                    only_lastest_per_day.add(date)
                                                    samples.append(
                                                        # Actual html markdown
                                                        [
                                                            f'<p>{date}<a href="{commit_url_from(repo.remotes.origin.url, hash)}" target="_blank">⧉</a></p>\n'
                                                        ]
                                                    )

                                except Exception as error:
                                    message = "변경 내역 가져오기 실패"
                                    logger.info(f"Launcher: 최근 5일간 {message}, {error}")
                                    samples = [[f"<p>{message}</p>"]]

                                return gr.Dataset.update(samples=samples)

                            commit_since5days_tab.select(
                                fn=on_select_commit_since5days_tab,
                                inputs=git_url,
                                outputs=commit_since5days,
                            )

            settings = [
                workspace_googledrive,
                workspace_name,
                extensions,
                controlnet_models,
                models,
                loras,
                embeddings,
                vaes,
                auth_method,
                auth_username,
                auth_password,
                auth_token,
                extra_cmdline_args,
                torch_command,
                xformers_package,
                use_virtualenv,
                git_url,
                git_commit,
                apply_ddetailer_patches,
                copy_extensions_config,
            ]

            default_settings.click(
                fn=on_default_settings,
                inputs=None,
                outputs=[*settings, settings_file],
            )

            import_settings.upload(
                fn=on_import_settings,
                inputs=import_settings,
                outputs=[*settings, settings_file],
            )

            settings_file.upload(
                fn=on_import_settings,
                inputs=settings_file,
                outputs=[*settings, settings_file],
            )

            export_settings.click(
                fn=on_export_settings,
                inputs=settings,
                outputs=settings_file,
            )

            def disable_reexecution():
                return {
                    # UploadButton이 interactive=False 업데이트가 안되서 visible=False로
                    default_settings: gr.Button.update(
                        visible=False,
                        interactive=False,
                    ),
                    import_settings: gr.UploadButton.update(
                        visible=False,
                        interactive=False,
                    ),
                    export_settings: gr.Button.update(
                        visible=False,
                        interactive=False,
                    ),
                    execute_webui: gr.Button.update(
                        value=f"중지는 {service_type}에서만 가능",
                        interactive=False,
                    ),
                    settings_file: gr.File.update(
                        visible=False,
                        interactive=False,
                    ),
                    progress_tooltip: gr.Markdown.update(
                        value=f'<p style="color:DeepPink !important; text-align: center;"><em>진행 과정은 {service_type} 출력창에서 확인해 주세요</em></p><p style="color:DeepPink !important; text-align: center;"><em>이제 웹 페이지를 닫으셔도 됩니다</em></p>'
                    ),
                }

            execute_webui.click(
                fn=disable_reexecution,
                inputs=None,
                outputs=[
                    default_settings,
                    import_settings,
                    export_settings,
                    execute_webui,
                    settings_file,
                    progress_tooltip,
                ],
            ).then(
                fn=on_execute_settings,
                inputs=settings,
                outputs=settings_file,
            ).then(
                fn=on_execute_webui,
                inputs=settings,
                outputs=progress,
            )

            # gr.Accordion이 모두 open 되어 있어야만 호출됨, LocalLauncher에서만 마지막 실행한 설정 값 로드
            if self.is_support_load():
                demo.load(
                    fn=on_load_last_settings,
                    inputs=None,
                    outputs=[*settings, settings_file],
                )

        demo.launch(
            share=USE_GRADIO_LIVE and self.is_support_share(),  # 공유 연결 사용할지 여부
            debug=True,  # 노트북 결과창에 출력 여부
            inline=not USE_GRADIO_LIVE,  # 노트북에 웹 표시 여부
            server_port=LAUNCHER_PORT,
            inbrowser=inbrowser,
        )

    def stop(self):
        try:
            from pycloudflared import try_cloudflare

            try_cloudflare.terminate(SD_WEBUI_PORT)
        except (ImportError, NameError, ValueError):
            pass

        try:
            import gradio as gr

            gr.close_all()
        except (ImportError, NameError):
            pass


class LinuxPlatform(Launcher):
    def __init__(self):
        super().__init__()

    def setup(self):
        super().setup()

        self.cmd("apt-get update -qq -y", check=True, live=True)

        if not self.has_executable("git"):
            self.cmd("apt-get install -qq -y git", check=True, live=True)

        if not self.has_executable("curl"):
            self.cmd("apt-get install -qq -y curl", check=True, live=True)

        if not self.has_executable("aria2c"):
            self.cmd("apt-get install -qq -y aria2", check=True, live=True)

    @staticmethod
    def system_info():
        def platform_info():
            import platform

            try:
                return {
                    "arch": platform.machine(),
                    "cpu": platform.processor(),
                    "system": platform.system(),
                    "release": platform.platform(),
                    "python": platform.python_version(),
                }
            except Exception as e:
                return {"error": e}

        def cpu_info():
            def vCPU():
                def cpu_count():
                    count = run(
                        LinuxPlatform.bash_path(),
                        f"cat /proc/cpuinfo | grep processor | wc -l",
                        check=False,
                        live=False,
                    ).rstrip("\n")
                    return len(
                        os.sched_getaffinity(0)
                    )  # vs os.cpu_count(), psutil.cpu_count()

                try:
                    with open("/sys/fs/cgroup/cpu/cpu.cfs_quota_us") as cfs:
                        cfs_quota_us = int(cfs.read())
                    with open("/sys/fs/cgroup/cpu/cpu.cfs_period_us") as cfs:
                        cfs_period_us = int(cfs.read())
                    return (
                        cfs_quota_us / cfs_period_us
                        if cfs_quota_us == -1
                        else cpu_count()
                    )
                except:
                    return cpu_count()

            try:
                query_cpu = run(
                    LinuxPlatform.bash_path(),
                    f'cat /proc/cpuinfo | grep "model name" | uniq',
                    check=False,
                    live=False,
                ).rstrip("\n")
                key, colon, name = tuple(
                    map(lambda x: x.strip(), query_cpu.partition(":"))
                )
                return {"name": name, "vCPU": vCPU()}
            except ValueError as e:
                return {"error": query_cpu}
            except Exception as e:
                return {"error": e}

        def gpu_info():
            if not LinuxPlatform.has_executable("nvidia-smi"):
                return {}
            else:
                try:
                    query_gpu = run(
                        LinuxPlatform.bash_path(),
                        f'nvidia-smi --query-gpu="name,memory.total,driver_version" --format=csv',
                        check=False,
                        live=False,
                    ).rstrip("\n")
                    name, memory, driver = query_gpu.split("\n")[-1].split(", ")
                    return {
                        "name": name,
                        "memory": memory,
                        "driver": driver,
                    }
                except ValueError as e:
                    return {"error": query_gpu}
                except Exception as e:
                    return {"error": e}

        return {"Platform": platform_info(), "CPU": cpu_info(), "GPU": gpu_info()}

    @staticmethod
    def bash_path():
        return "/usr/bin/bash"

    @staticmethod
    def python_path(venv_path=None):
        if venv_path:
            return Path(venv_path, "bin", "python")
        else:
            return Path(shutil.which("python"))


class WindowsPlatform(Launcher):
    def __init__(self):
        super().__init__()

        self.environ["PATH"] = (
            str(Path(self.working_dir(), "bin")) + os.pathsep + self.environ["PATH"]
        )

    def setup(self):
        import urllib.request
        import zipfile

        super().setup()

        if not self.has_executable("git"):
            raise RuntimeError("다음 링크를 통해 git를 설치해 주세요. https://gitforwindows.org/")

        bin_path = Path(self.working_dir(), "bin")
        bin_path.mkdir(parents=True, exist_ok=True)
        if not self.has_executable("curl", path=bin_path):
            Path("temp").mkdir(parents=True, exist_ok=True)
            curl_zip = Path("temp", "curl.zip")
            urllib.request.urlretrieve(
                "https://curl.se/windows/dl-8.0.1_4/curl-8.0.1_4-win64-mingw.zip",
                curl_zip,
            )
            curl_exe = bin_path / "curl.exe"

            with zipfile.ZipFile(curl_zip) as z:
                with z.open("curl-8.0.1_4-win64-mingw/bin/curl.exe") as src, open(
                    curl_exe, "wb"
                ) as dst:
                    shutil.copyfileobj(src, dst)

        if not self.has_executable("aria2c", path=bin_path):
            Path("temp").mkdir(parents=True, exist_ok=True)
            aria2c_zip = Path("temp", "aria2c.zip")
            urllib.request.urlretrieve(
                "https://github.com/aria2/aria2/releases/download/release-1.36.0/aria2-1.36.0-win-64bit-build1.zip",
                aria2c_zip,
            )
            aria2c_exe = bin_path / "aria2c.exe"

            with zipfile.ZipFile(aria2c_zip) as z:
                with z.open("aria2-1.36.0-win-64bit-build1/aria2c.exe") as src, open(
                    aria2c_exe, "wb"
                ) as dst:
                    shutil.copyfileobj(src, dst)

    @staticmethod
    def system_info():
        def platform_info():
            import platform

            try:
                return {
                    "arch": platform.machine(),
                    "cpu": platform.processor(),
                    "system": platform.system(),
                    "release": platform.platform(aliased=True, terse=False),
                    "python": platform.python_version(),
                }
            except Exception as e:
                return {"error": e}

        def cpu_info():
            def cpu_count():
                return os.cpu_count()

            return {"count": cpu_count()}

        def gpu_info():
            if not WindowsPlatform.has_executable("nvidia-smi"):
                return {}
            else:
                try:
                    query_gpu = run(
                        WindowsPlatform.bash_path(),
                        f'nvidia-smi --query-gpu="name,memory.total,driver_version" --format=csv',
                        check=False,
                        live=False,
                    ).rstrip("\n")
                    name, memory, driver = query_gpu.split("\n")[-1].split(", ")
                    return {
                        "name": name,
                        "memory": memory,
                        "driver": driver,
                    }
                except ValueError as e:
                    return {"error": query_gpu}
                except Exception as e:
                    return {"error": e}

        return {"Platform": platform_info(), "CPU": cpu_info(), "GPU": gpu_info()}

    @staticmethod
    def bash_path():
        path = ""
        path += "C:\\Program Files (x86)\\Git\\bin" + os.pathsep
        path += "C:\\Program Files\\Git\\bin" + os.pathsep
        path += os.environ.copy()["PATH"]

        return str(Path(shutil.which("bash", path=path)))

    @staticmethod
    def python_path(venv_path=None):
        if venv_path:
            return Path(venv_path, "Scripts", "python.exe")
        else:
            return Path(shutil.which("python"))


class ColabLauncher(LinuxPlatform):
    def setup(self):
        # 코랩 출력창 스크롤 높이 조정
        from google.colab.output import eval_js

        eval_js(f'google.colab.output.setIframeHeight("{DISPLAY_OUTPUT_LINES*10}")')

        super().setup()

        # 코랩 tcmalloc 관련 이슈 우회
        # https://github.com/googlecolab/colabtools/issues/3412
        try:
            # 패키지가 이미 다운그레이드 됐는지 확인하기
            self.cmd("dpkg -l libunwind8-dev", check=True, live=True)
        except RuntimeError:
            for url in (
                "http://launchpadlibrarian.net/367274644/libgoogle-perftools-dev_2.5-2.2ubuntu3_amd64.deb",
                "https://launchpad.net/ubuntu/+source/google-perftools/2.5-2.2ubuntu3/+build/14795286/+files/google-perftools_2.5-2.2ubuntu3_all.deb",
                "https://launchpad.net/ubuntu/+source/google-perftools/2.5-2.2ubuntu3/+build/14795286/+files/libtcmalloc-minimal4_2.5-2.2ubuntu3_amd64.deb",
                "https://launchpad.net/ubuntu/+source/google-perftools/2.5-2.2ubuntu3/+build/14795286/+files/libgoogle-perftools4_2.5-2.2ubuntu3_amd64.deb",
            ):
                self.cmd(
                    f"curl -sS --location --output {url.rsplit('/', 1)[-1]} {url}",
                    check=False,
                    live=True,
                )
            self.cmd("apt install -qq libunwind8-dev", check=False, live=True)
            self.cmd("dpkg -i *.deb", check=False, live=True)
            self.cmd("rm *.deb", check=False, live=True)

        # https://github.com/googlecolab/colabtools/issues/3412
        self.environ["LD_PRELOAD"] = "libtcmalloc.so"
        # Deactivate tensorflow print standard error
        self.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

    @staticmethod
    def working_dir():
        return Path("/content")

    @staticmethod
    def service_name():
        return "코랩(colab)"

    @staticmethod
    def service_type():
        return "노트북"

    @staticmethod
    def is_support_googledrive():
        return True

    @staticmethod
    def is_support_share():
        return True

    @staticmethod
    def is_support_load():
        return False

    @staticmethod
    def force_virtualenv():
        return False


class RunPodLauncher(LinuxPlatform):
    def setup(self):
        # 런팟 출력창 스크롤 높이 조정
        from IPython.display import display, HTML

        display(
            HTML(
                f"""
                <style>
                .jp-OutputArea-child {{
                    max-height: {DISPLAY_OUTPUT_LINES}em;
                }}

                .jp-OutputArea-child .jp-OutputArea-output {{
                    overflow: auto;
                }}
                </style>
                """
            )
        )

        super().setup()

        self.cmd(
            "apt-get install -qq -y libgl1",
            check=True,
            live=True,
        )

        # For ddetailer extension, mmcv, mmdet dependency
        self.cmd(
            "apt-get install -qq -y libpython3.10-dev build-essential python3-lib2to3 python3-distutils python3-toolz",
            check=True,
            live=True,
        )
        # And
        self.cmd(
            "pip install -q --upgrade pip setuptools wheel",
            check=True,
            live=True,
        )

    @staticmethod
    def working_dir():
        return Path("/workspace")

    @staticmethod
    def service_name():
        return "런팟(runpod)"

    @staticmethod
    def service_type():
        return "노트북"

    @staticmethod
    def is_support_googledrive():
        return False

    @staticmethod
    def is_support_share():
        return True

    @staticmethod
    def is_support_load():
        return False

    @staticmethod
    def force_virtualenv():
        return True


class LocalLauncher(WindowsPlatform):
    def setup(self):
        super().setup()
        from os import system

        system("title " + f"SD Web UI 런처 127.0.0.1:{LAUNCHER_PORT}")

    def start(self, inbrowser=False):
        import argparse

        parser = argparse.ArgumentParser(description="SD Web UI 런처")
        parser.add_argument(
            "--inbrowser", action="store_true", help="기본 웹브라우저로 런처 창 띄우기"
        )

        args = parser.parse_args()
        super().start(inbrowser=args.inbrowser)

    @staticmethod
    def working_dir():
        return Path.cwd()

    @staticmethod
    def service_name():
        return "로컬(windows)"

    @staticmethod
    def service_type():
        return "터미널"

    @staticmethod
    def is_support_googledrive():
        return False

    @staticmethod
    def is_support_share():
        return False

    @staticmethod
    def is_support_load():
        return True

    @staticmethod
    def force_virtualenv():
        return True


class JupyterLauncher(WindowsPlatform):
    def setup(self):
        # 주피터 출력창 스크롤 높이 조정
        from IPython.display import display, HTML

        display(
            HTML(
                f"""
                <style>
                .jp-OutputArea-child {{
                    max-height: {DISPLAY_OUTPUT_LINES}em;
                }}

                .jp-OutputArea-child .jp-OutputArea-output {{
                    overflow: auto;
                }}
                </style>
                """
            )
        )
        super().setup()

    def start(self, inbrowser=False):
        super().start()

    @staticmethod
    def working_dir():
        return Path.cwd()

    @staticmethod
    def service_name():
        return "주피터(windows)"

    @staticmethod
    def service_type():
        return "노트북"

    @staticmethod
    def is_support_googledrive():
        return False

    @staticmethod
    def is_support_share():
        return False

    @staticmethod
    def is_support_load():
        return True

    @staticmethod
    def force_virtualenv():
        return True


class LauncherFactory:
    import platform

    @staticmethod
    def create():
        if LauncherFactory.is_colab():
            return ColabLauncher()
        elif LauncherFactory.is_runpod():
            return RunPodLauncher()
        elif LauncherFactory.is_local():
            return LocalLauncher()
        elif LauncherFactory.is_jupyter():
            return JupyterLauncher()

    @staticmethod
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

    @staticmethod
    def is_runpod():
        return Launcher.platform.system() == "Linux" and Launcher.is_interactive()

    @staticmethod
    def is_local():
        return Launcher.platform.system() == "Windows" and not Launcher.is_interactive()

    @staticmethod
    def is_jupyter():
        return Launcher.platform.system() == "Windows" and Launcher.is_interactive()


if __name__ == "__main__":
    try:
        launcher = LauncherFactory.create()
        launcher.setup()
        launcher.start()
    finally:  # KeyboardInterrupt
        launcher.stop()
