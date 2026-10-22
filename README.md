# Skills

用于前端验证、技术写作等工作的 Agent Skills。每个技能独立放在一个目录中，包含 `SKILL.md`、参考资料和必要脚本。

[English](README.en.md)

## Verify Feature

<p align="center">
  <a href="skills/development/verify-feature/README.zh-CN.md"><img src="skills/development/verify-feature/docs/hero-imagegen.png" alt="Verify Feature：AI 说做完了，拿什么证明？" width="100%"></a>
</p>

检查前端截图、组件行为和完整业务流程。用 Midscene 操作页面、Bifrost 模拟接口，把实际结果与截图、trace、日志写进 Markdown 报告。缺少工具时会给出安装提示。

```sh
npx skills@latest add baichen99/skills --skill verify-feature
```

调用 `$verify-feature`（Codex）或 `/verify-feature`（Claude Code / Cursor），然后描述预期：

> 验证个人资料表单：保存失败保留输入；点击一次重试只提交一次；保存成功后刷新仍能读到修改。使用 Mock 后端，交付实际结果与证据，不修改业务代码。

[中文文档](skills/development/verify-feature/README.zh-CN.md) · [English](skills/development/verify-feature/README.md) · [工具安装](skills/development/verify-feature/references/setup.md) · [报告示例](skills/development/verify-feature/docs/example-report.md)

## 安装

使用 [Skills CLI](https://github.com/vercel-labs/skills) 选择安装：

```sh
npx skills@latest add baichen99/skills
```

只安装某个技能：

```sh
npx skills@latest add baichen99/skills --skill plainspoken-tech-talk
```

也可以把所需技能的整个目录复制到编程助手的 skills 目录。请保留参考资料与脚本，具体位置见各技能文档。

## 技能目录

### Development

| Skill | 用途 |
| --- | --- |
| [verify-feature](skills/development/verify-feature/SKILL.md) | 按明确预期验证前端功能，支持截图、组件、接口 Mock 和需求验收，生成附有证据链接的报告。 |

### Productivity

| Skill | 用途 |
| --- | --- |
| [plainspoken-tech-talk](skills/productivity/plainspoken-tech-talk/SKILL.md) | 撰写或改写中文技术分享、观点文章、经验复盘和口播稿，用具体处境与决策细节讲清技术。 |

使用示例：

> 用 $plainspoken-tech-talk 把这份原理文章改成面向前端开发的 15 分钟分享。开头讲清技术特点与用途，案例服务于主线，不补造实践成果。

## 维护

目录按用途分类，组织方式参考 [mattpocock/skills](https://github.com/mattpocock/skills)：

```text
skills/
├── development/
│   └── verify-feature/
└── productivity/
    └── plainspoken-tech-talk/
```

每个目录以 `SKILL.md` 为入口，`references/` 存放按需读取的资料，`agents/` 存放可选的展示与调用信息。当前按普通技能目录分发，不包含插件市场或自动更新配置。

Verify Feature 的脚本和包结构有自动检查，尚未逐框架、逐助手完成浏览器验收。使用 Mock 后端的验证结果不代表真实后端通过。写作技能同样需要原始材料支持，不能补写没有发生的经历或成果。
