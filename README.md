# Skills · 让 AI 的“做完了”，有据可查

给编程助手可复用的工作方法：前端功能拿证据验，技术分享把话说清楚。

兼容 Agent Skills 格式；提供 Codex、Claude Code、Cursor 等工具的安装方式。每个 skill 独立维护，不依赖个人项目的内部平台。

<p align="center">
  <a href="skills/development/verify-feature/README.zh-CN.md"><img src="skills/development/verify-feature/docs/hero.svg" alt="Verify Feature — AI 说做完了，拿什么证明？" width="100%"></a>
</p>

## 新增：Verify Feature

**AI 说做完了，拿什么证明？**

表单能打开、请求返回 200、弹出成功提示，仍可能漏掉输入丢失、重复提交和刷新失效。Verify Feature 把 **需求 → 用例 → 实际执行 → 证据** 连起来，交付能复查的 Markdown 验证报告。

- **Midscene 跑交互**：检查页面操作与状态变化，精确字段配合确定性断言。
- **Bifrost 做 Mock**：配置接口场景并检查实际流量命中，标明真实与模拟边界。
- **缺工具给安装提示**：不静默安装，不把没执行的用例写成通过。
- **沿用你的前端栈**：组件、集成、截图和完整需求按需验证，保留现有测试。

```bash
npx skills@latest add baichen99/skills --skill verify-feature
```

调用 `$verify-feature`（Codex）或 `/verify-feature`（Claude Code / Cursor），然后给出明确预期：

> 验证个人资料表单：保存失败保留输入，重试只提交一次，刷新后仍能读到修改。用 Mock 后端，交付实际结果与证据，未执行的也要写清楚。

[中文介绍与安装](skills/development/verify-feature/README.zh-CN.md) · [English](skills/development/verify-feature/README.md) · [工具安装](skills/development/verify-feature/references/setup.md) · [报告示例（格式示意）](skills/development/verify-feature/docs/example-report.md)

## 安装

使用 [Skills CLI](https://github.com/vercel-labs/skills) 选择安装：

```bash
npx skills@latest add baichen99/skills
```

只安装直白技术分享：

```bash
npx skills@latest add baichen99/skills --skill plainspoken-tech-talk
```

也可以手动复制 `skills/productivity/plainspoken-tech-talk/` 整个文件夹到所用 Agent 的 skills 目录。请保留 `references/`，正文会按需引用这些资料。

## 技能目录

### Development

| Skill | 用途 |
| --- | --- |
| [verify-feature](skills/development/verify-feature/SKILL.md) · 前端验证与证据报告 | 用 Midscene、Bifrost 与精确断言验证截图、组件、前端集成或完整需求；交付绑定需求、用例和实际证据的结果。缺少工具时提示安装。 |

### Productivity

| Skill | 用途 |
| --- | --- |
| [plainspoken-tech-talk](skills/productivity/plainspoken-tech-talk/SKILL.md) · 直白技术分享 | 撰写或改写中文技术分享、观点文章、经验复盘和口播稿，用具体处境、决策细节和适用条件讲清判断。 |

使用示例：

> 用 $plainspoken-tech-talk 把这份原理文章改成面向前端开发的 15 分钟分享。开头尽快讲清技术特点与用途，案例服务于主线，不补造实践成果。

## 目录组织

参考 [mattpocock/skills](https://github.com/mattpocock/skills) 的分类方式：

```text
skills/
├── development/
│   └── verify-feature/
│       ├── SKILL.md
│       ├── README.md / README.zh-CN.md
│       ├── references/     # 浏览器、组件、Mock、报告与安装
│       ├── assets/         # 用例与报告模板
│       ├── scripts/        # 本地链接及包结构检查
│       ├── tests/
│       └── agents/
└── productivity/
    └── plainspoken-tech-talk/
        ├── SKILL.md
        ├── agents/
        └── references/
```

- `SKILL.md`：技能入口，包含名称、适用场景与执行方法。
- `references/`：按需读取的执行指导、安装说明与示例。
- `agents/`：可选的 Agent 展示与调用元信息。
- 后续技能按实际用途增加分类，避免预建空目录。

## 使用边界

技能负责组织执行与表达，不能保证模型每次遵守或发现所有问题。验证结果绑定本次环境、版本与实际证据；Mock 通过不代表真实后端通过。写作时区分已完成的实践、源码理解、建议方案和未验证设想；没有材料支持的经历、数字与结果不要补写。

Verify Feature 尚未逐框架、逐助手完成兼容性实测；示例报告为格式示意。公开证据前检查隐私和凭证，验证本身不包含生产写入或部署授权。

目前以普通 skills 目录分发；不包含插件市场或自动更新配置。
