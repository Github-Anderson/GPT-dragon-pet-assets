# GPT 龙娘宠物素材包

白发紫眸、带有龙角、翅膀和卷尾的 Q 版龙娘动画素材。成品图集包含九组动作和十六个注视方向，适用于支持该图集格式的 ChatGPT / Codex 宠物功能。

![动作预览](previews/all-states.gif)

## 下载与使用

成品精灵图为 [`assets/spritesheet.png`](assets/spritesheet.png)。在 GitHub 中打开该文件后选择 **Download raw file**，保留原始尺寸与透明通道。

如果客户端宠物管理页面提供自定义精灵图导入功能，选择下载的 PNG，按客户端提示完成导入。不同客户端与版本的导入入口可能不同；仓库链接本身不是安装程序。

此包提供图片素材和格式说明，不含自动安装程序。`asset-info.json` 是素材描述文件，不是账户记录或客户端安装清单。

## 预览

- [全部动作](previews/all-states.gif) / [MP4](previews/all-states.mp4)
- [十六方向注视](previews/look-loop.gif)
- [待机与跳跃衔接](previews/idle-jump-idle.gif)
- [动作静态总览](previews/motion-stills.png)

各动作的独立 GIF 位于 `previews/`。

## 图集规格

PNG，RGBA 透明背景，1536 × 2288 像素。网格为 8 列 × 11 行，每格 192 × 208 像素，共 73 个有效帧、15 个透明空格。

| 行，从 0 开始 | 状态 | 帧数 |
| --- | --- | --- |
| 0 | idle，待机 | 6 |
| 1 | running-right，向右移动 | 8 |
| 2 | running-left，向左移动 | 8 |
| 3 | waving，挥手 | 4 |
| 4 | jumping，跳跃 | 5 |
| 5 | failed，失落反应 | 8 |
| 6 | waiting，等待回应 | 6 |
| 7 | running，工作或思考 | 6 |
| 8 | review，检查成果 | 6 |
| 9 | 000° 至 157.5° 注视方向 | 8 |
| 10 | 180° 至 337.5° 注视方向 | 8 |

注视方向按屏幕坐标顺时针排列：0° 向上，90° 向右，180° 向下，270° 向左；步长为 22.5°。

## 文件校验

`checksums.sha256` 列出包内文件的 SHA-256。使用 Python 3.9 或更高版本运行：

```bash
python3 scripts/verify_package.py
```

脚本使用 Python 标准库，检查文件校验值和图集尺寸，不修改文件。

## 许可

- 校验脚本与文字文档：见 [`LICENSE-CODE`](LICENSE-CODE)，MIT。
- 图片、GIF 与视频素材：CC BY-NC-SA 4.0，允许署名后的非商业分享和修改，衍生成品须沿用同一协议；见 [`LICENSE-ASSETS.md`](LICENSE-ASSETS.md)。MIT 不适用于素材。
- 制作来源与第三方范围：见 [`NOTICE.md`](NOTICE.md)。

本项目与 OpenAI 无隶属或官方背书关系。ChatGPT、Codex 等名称用于说明兼容用途。

制作所用图片由 gpt-image 生成，原始角色参考图来自 Bilibili 作者 ZipZipPipe。据发布者提供的作者声明，该形象采用 CC BY-NC-SA 4.0，本包衍生素材沿用该协议。原始作品与授权声明的具体链接尚未附入本包。
