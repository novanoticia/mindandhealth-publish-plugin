# mindandhealth-publish-plugin

[English](README.md) · [Français](README.fr.md) · [简体中文](README.zh-CN.md)

这是一个 Claude Code 插件，为 [mindandhealth.org](https://mindandhealth.org) 的 Obsidian Publish 文章提供**对话式编辑协助**。

插件兼容 [Agent Plugins 1.0.0](https://agent-plugins.org/specification) 和 [Agent Skills](https://agentskills.io/specification) 格式，也提供适用于聊天客户端的版本。

助手先参与讨论，待想法成形后再整理草稿，并可按要求生成 LinkedIn 通讯、动态帖子和图片提示词。**所有编辑内容都留在对话中，不会修改 Obsidian 知识库。**

## 输出语言

**默认输出语言仍为西班牙语**。阅读中文说明或提供中文资料，不会自动改变这一设置。你可以明确要求使用英语、法语、简体中文或双语；助手会保持所选语言，直到你再次更改。

示例：

- “请用简体中文继续，帮我润色这篇草稿。”
- “请用简体中文为这篇文章准备 LinkedIn 通讯。”
- “请制作法语和简体中文双语版本，先法语，后中文。”
- “Volvamos al español.”

内部指令使用英语。引文、网址、文件名和 YAML 字段名保持不变。标题等自由文本字段使用所选语言，受控字段值继续遵循现有约定。详情见[语言指南](plugins/mindandhealth-publish/skills/mindandhealth-publish/references/languages.md)。

## i18n 语言资源

Skill 会从 [i18n 目录](plugins/mindandhealth-publish/skills/mindandhealth-publish/i18n/README.md)加载固定文本：`es.json` 是西班牙语基准；`en.json`、`fr.json` 和 `zh-CN.json` 包含相同的键和命名占位符。提问、界面标题及提醒使用这些资源；文章正文和伦理声明仍会根据内容重新撰写。

[术语表](plugins/mindandhealth-publish/skills/mindandhealth-publish/i18n/GLOSSARY.md)和[翻译状态](plugins/mindandhealth-publish/skills/mindandhealth-publish/i18n/STATUS.md)记录了覆盖范围及限制。这些翻译是 AI 草稿，尚无人工语言审核记录。自动测试检查结构、源文件摘要和 ZIP 内容，不能证明模型在实际平台上的行为。

```bash
python3 scripts/build_distribution.py --sync-i18n --check
python3 scripts/validate_i18n.py
python3 -m unittest discover -s tests -v
```

## 工作方式

1. **探索性对话：** Pablo 提出主题、直觉、问题或阅读材料，助手提供不同视角、补充细节和反论点。
2. **想法成形：** Pablo 要求创建草稿，或由助手在材料充分时提出一次建议。
3. **对话草稿：** 用聊天中的 Markdown 代码块整理讨论成果，也称为 canvas。
4. **迭代修改：** 只有明确的修改请求或已获批准的建议才会改变草稿。
5. **完成：** Pablo 手动将文章复制到 Obsidian，再按需生成衍生内容。

草稿不是磁盘文件。探索性对话也可以一直保持为讨论，而不必产出文章。

## 功能与边界

插件可以协助思考，生成兼容 Obsidian 的 Markdown 草稿、最小 YAML 元数据和文末伦理声明。按要求，它还可生成 LinkedIn 通讯、动态帖子，以及比例为 1570:880 的图片提示词。

Claude Code 版本可读取知识库以核实已有文章并建议内部链接。聊天版本只能使用 Pablo 在对话中提供或确认的文章标题与内容。

插件不会写入文件、发布内容或直接生成图片。Pablo 负责用 Tagger GPT 添加共同创作的 YAML 区块，用 Obsidian 模板添加文末标签，并自行添加图片。

## 两个版本

| 版本 | 位置 | Skill 名称 | 使用环境 |
|---|---|---|---|
| 插件版 | `plugins/mindandhealth-publish/skills/mindandhealth-publish/` | `mindandhealth-publish` | Claude Code / Claude Desktop 的 Code 页；可读取知识库，提供 `/publish`。 |
| 聊天版 | `claude-ai/mindandhealth-publish/` | `mindandhealth-publish-chat` | 支持 Skill 的 Claude.ai、Perplexity、Mistral 和 ChatGPT 环境；不能访问本地知识库。 |

请勿在同一环境中同时安装两个版本，以免触发条件相互重叠。

## 安装

### Claude Code 和 Claude Desktop Code

```text
/plugin marketplace add novanoticia/mindandhealth-publish-plugin
/plugin install mindandhealth-publish@mindandhealth-publish-plugin
```

安装后可使用 `/publish` 命令，也可通过自然语言调用。

### Claude.ai

1. 从 [Releases 下载 mindandhealth-publish-claude-ai.zip](https://github.com/novanoticia/mindandhealth-publish-plugin/releases/latest/download/mindandhealth-publish-claude-ai.zip)。
2. 打开 **Settings → Capabilities → Skills → Upload skill**。
3. 上传 ZIP 并启用该 Skill。

自定义 Skill 是否可用，取决于账户套餐及已启用的功能。

### Perplexity

下载同一个 ZIP，在 **Skills** 管理界面选择上传或导入，然后启用。

### Mistral AI

解压 ZIP，在 **Work** 空间的 **Skills** 页面选择包含 `SKILL.md` 的 `mindandhealth-publish-chat/` 文件夹。

### ChatGPT

在提供 **Work** 和 **Plugins** 的环境中，通过插件名称或仓库网址添加。具体可用性取决于账户及已启用的功能。

聊天版描述字段遵循已记录的兼容性限制：Mistral 最多 500 个字符，Perplexity 最多 1,024 个 UTF-8 字节。

## 使用

```text
/publish [可选上下文]
```

- **无参数：** 开始探索性对话。
- **主题或开放问题：** 先讨论，再确定文章结构。
- **已有草稿：** 先给出简短诊断，再确认轻度、中度或深度修改。
- **网址、引文或资料：** 先整理来源，再转化为草稿。
- **明确请求：** 直接进入相应模式或生成所需衍生内容。

## 迭代规则

| 意图 | 示例 | 助手行为 |
|---|---|---|
| 提问 | “你觉得第二节怎么样？” | 在对话中回答，不重写草稿。 |
| 建议 | “要不要用这段引文开头？” | 先评估，获得同意后再修改。 |
| 修改请求 | “请重写开头。” | 返回完整更新稿，并简述改动。 |
| 探索方案 | “给我三个不同的开头。” | 提供候选方案，暂不修改草稿。 |
| 旁支讨论 | “顺便问一下……” | 保留草稿，展开相关讨论。 |
| 确认 | “就保留这一版。” | 确认当前状态，建议下一步。 |
| 暂停 | “让我想一想。” | 说明当前状态并停止推进。 |

更改输出语言不会自动翻译或替换已获批准的草稿。

## 编辑原则

- 联系技术与人文学科，提供跨学科视角。
- 保持认识上的诚实，允许疑问和暂定判断。
- 保留建设性异议、反论点和细微差别。
- 在适当情况下采用具体、可感知的引导性隐喻。
- 以开放问题或小幅行动收尾。
- 每篇文章重新撰写伦理声明，说明 AI 协助与人类编辑责任，并按主题添加必要说明。
- 所有编辑成果都保留在对话中。

简体中文输出使用自然的中文标点与表达。英语模板中的字数范围仅供估计；需要严格控制篇幅时，应确认适合中文的字符数。

## 仓库结构

```text
.claude-plugin/marketplace.json           插件市场目录
plugins/mindandhealth-publish/
  plugin.json                            共享元数据的来源
  .claude-plugin/plugin.json              Claude 兼容清单
  commands/publish.md                    随插件安装的命令
  skills/mindandhealth-publish/           指令、模式与参考资料
claude-ai/mindandhealth-publish/          聊天版本
scripts/build_distribution.py            校验和 ZIP 构建
.github/workflows/distribution.yml       自动校验与版本发布
README.fr.md                             法语文档
README.zh-CN.md                          简体中文文档
```

根目录中的 `.claude-plugin/` 描述插件市场，并不是第二份插件。插件内部的两个清单分别用于通用 Agent Plugins 客户端和 Claude。共享元数据只在 `plugins/mindandhealth-publish/plugin.json` 中维护，再由脚本同步到其他所需清单。

## 构建与发布

ZIP 从 [Releases](https://github.com/novanoticia/mindandhealth-publish-plugin/releases) 下载，不再作为文件提交到 `main`。也可以使用 Python 3.10 或更高版本本地构建：

```bash
python3 scripts/build_distribution.py
```

输出为 `dist/mindandhealth-publish-claude-ai.zip`。Git 会忽略 `dist/`；相同源码会生成完全相同的 ZIP。

修改共享元数据后，运行：

```bash
python3 scripts/build_distribution.py --sync-manifests --check
python3 -m unittest discover -s tests -v
```

请保持插件 Skill 与通用清单的版本号一致。在 `docs/releases/<version>.md` 中添加发布说明后，推送 `v<version>` 标签。GitHub Actions 会校验、构建并将 ZIP 添加到对应 Release。旧版本 ZIP 仍可从 Git 历史记录中恢复。

## 知识库访问

Claude Code 版本可以读取知识库中的 Markdown 文件。默认路径：

```text
~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Pablo's Vault/website/
```

请根据本地环境调整插件指令中的路径。插件不会向知识库写入内容。

## 作者与许可证

**Pablo Rodríguez López** — [mindandhealth.org](https://mindandhealth.org)。许可证：Apache-2.0。
