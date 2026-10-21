# Skills

个人使用和持续打磨的 Agent Skills。每个 skill 独立维护，包含执行说明、必要示例和可选的 Agent 元信息。

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
└── productivity/
    └── plainspoken-tech-talk/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        └── references/
            └── writing-examples.md
```

- `SKILL.md`：技能入口，包含名称、适用场景与执行方法。
- `references/`：按需读取的改写示例。
- `agents/`：可选的 Agent 展示与调用元信息。
- 后续技能按实际用途增加分类，避免预建空目录。

## 使用边界

技能负责组织与表达，不替代技术事实核验。写作时区分已完成的实践、源码理解、建议方案和未验证设想；没有材料支持的经历、数字与结果不要补写。

目前以普通 skills 目录分发；不包含插件市场或自动更新配置。
