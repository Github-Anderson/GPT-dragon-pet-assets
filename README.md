# GPT 龙娘宠物素材包

本包整理了本次龙娘宠物制作的全部现存素材，包括原始参考、选定成品、动画预览、动作源图、透明帧、视线方向、检查报告、生成配置、处理脚本及历史生成版本。

## 快速使用

- 可直接使用的宠物图集：`02_final/spritesheet-extended.png`。
- 全动作动画：`03_previews/all-states.gif`；视频：`03_previews/all-states.mp4`。
- 鼠标视线循环：`03_previews/look-loop.gif`。
- 待机、跳跃和落地衔接：`03_previews/idle-jump-idle.gif`。
- 方向总览：`07_quality_checks/direction-qa.png`。
- 全帧总览：`07_quality_checks/contact-sheet-final.png`。

## 目录说明

| 目录 | 内容 |
| --- | --- |
| 01_references | 原始参考、标准形象、组合参考和布局引导 |
| 02_final | 最终透明图集、基础图集、清理前图集和最终验证报告 |
| 03_previews | GIF、MP4、静态动作总览及从最终图集提取的帧 |
| 04_animation_strips | 九组基础动作的选定源图 |
| 05_look_directions | 上下左右锚点及两组八方向源图 |
| 06_frames | 图集组装前的透明动作帧 |
| 07_quality_checks | 结构、动作、方向、边缘、盲评报告及检查图片 |
| 08_prompts_config | 生成提示词、配置、任务记录和宠物信息 |
| 09_scripts | 预览生成脚本和确定性处理工具 |
| 10_history | 修订前版本及其他原始生成输出 |

## 图集规格

最终图集为 PNG，1536 × 2288 像素，透明背景。网格为 8 列 × 11 行，每格 192 × 208 像素，共 73 个有效帧，其余 15 格透明。角色白发紫眸，保留一个头饰徽和两个腰间饰徽；在侧身动作中部分饰物会自然遮挡。

| 行（从 0 开始） | 动作 | 帧数 |
| --- | --- | --- |
| 0 | idle：待机 | 6 |
| 1 | running-right：向右跑动 | 8 |
| 2 | running-left：向左跑动 | 8 |
| 3 | waving：挥手 | 4 |
| 4 | jumping：跳跃 | 5 |
| 5 | failed：失落反应 | 8 |
| 6 | waiting：等待回应 | 6 |
| 7 | running：工作或思考 | 6 |
| 8 | review：检查成果 | 6 |
| 9 | 000° 至 157.5° 的视线方向 | 8 |
| 10 | 180° 至 337.5° 的视线方向 | 8 |

视线方向按屏幕坐标顺时针排列：0° 向上，90° 向右，180° 向下，270° 向左。中间角度步长为 22.5°。

## 整理规则

图片和视频保留原始字节、尺寸、画质和透明通道。JSON 统一为 UTF-8、双空格缩进，报告中的本次工作区绝对路径改为包内路径。历史版与选定版分别存放。

完全相同的素材只保留一份，`file-index.csv` 和 `file-index.json` 记录每个原始文件到包内文件的对应关系。原始生成文件名没有动作语义时使用 `generation-001.png` 等顺序名称，实际内容以对应图片为准。报告中的校验结果来自创建时的实际检查；历史版本不等同于最终成品。

## 工具使用

需要 Python 3 和 Pillow；输出 MP4 另需安装 FFmpeg。从解压后的包目录运行：

```bash
python3 -m pip install -r 09_scripts/requirements.txt
python3 09_scripts/render_previews.py
```

该命令从最终图集重新输出动画预览。其他处理工具位于 `09_scripts/pipeline`，可用 `python3 工具路径 --help` 查看参数。预览脚本不会修改最终图集。

`checksums.sha256` 记录包内文件校验值。
