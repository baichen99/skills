<p align="center">
  <img src="docs/hero-imagegen.png" alt="Verify Feature：AI 说做完了，拿什么证明？" width="100%">
</p>

# Verify Feature

供编程助手使用的前端验证 skill。用 Midscene 操作页面，Bifrost 模拟接口，再用精确断言检查请求参数、提交次数等结果。验证结束后生成 Markdown 报告，附上截图、trace 和日志链接。

每条需求都能追到对应的用例、检查、结果和证据。构建成功、接口返回 200 或出现成功提示，都不能单独证明完整功能可用。

B 站视频：[横屏版](https://www.bilibili.com/video/BV1kLn16HEum/) · [竖屏版](https://www.bilibili.com/video/BV1rJn16UE8c/)。两版均为流程动画示意，并非完整工具链的实测录像。

[English](README.md) · [工具安装](references/setup.md) · [报告示例](docs/example-report.md)

[![包检查](https://github.com/baichen99/skills/actions/workflows/verify-feature.yml/badge.svg)](https://github.com/baichen99/skills/actions/workflows/verify-feature.yml)
[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 安装

在项目根目录执行：

```sh
npx skills@latest add baichen99/skills --skill verify-feature
```

按提示选择编程助手。[Skills CLI](https://github.com/vercel-labs/skills) 要求 Node.js 22.20+，默认安装到当前项目。

这条命令安装的是 skill 文档、模板与辅助脚本。页面交互和接口 Mock 所需的 Midscene、模型访问与 Bifrost 需按下方[工具准备](#工具准备)配置。

手动安装时，把本仓库的 `skills/development/verify-feature/` 整个目录复制到对应位置，保留其中的参考文档、脚本和模板。

| 编程助手 | 项目内目录 | 调用方式 |
| --- | --- | --- |
| [Codex](https://learn.chatgpt.com/docs/build-skills) | `.agents/skills/verify-feature/` | `$verify-feature` |
| [Claude Code](https://code.claude.com/docs/en/skills) | `.claude/skills/verify-feature/` | `/verify-feature` |
| [Cursor](https://cursor.com/docs/skills) | `.cursor/skills/verify-feature/` | `/verify-feature` |

目标目录须为空。安装后没出现时，重启编程助手。其他支持 [Agent Skills 格式](https://agentskills.io/specification) 的工具也可以读取这份目录。

## 工具准备

| 工具 | 用途 |
| --- | --- |
| [Midscene](https://midscenejs.com/) | 页面交互与视觉检查，需要配置模型访问。 |
| [Bifrost](https://github.com/bifrost-proxy/bifrost) | 接口 Mock 与流量检查，需要 CLI 和官方 agent skill。 |
| Python 3.9+（可选） | 检查报告中的本地链接，无需安装 Python 第三方包。 |

缺少工具时，skill 会给出安装提示。依赖该工具的用例暂记为阻塞，其他独立检查可以继续。具体命令与模型配置见[安装说明](references/setup.md)。模型调用可能产生费用。

## 使用

启动目标页面后，在项目中打开 Codex，替换地址并发送下面这段。Claude Code / Cursor 把第一行改为 `/verify-feature`：

```text
$verify-feature
验证 http://localhost:3000/settings 的个人资料表单。

- 保存失败后保留已填写的内容，并显示错误。
- 点击一次重试，只发送一次请求。
- 保存成功后刷新页面，仍能读到修改后的值。

用 Midscene 操作页面，Bifrost 准备接口场景。
保留真实组件和请求代码，交付实际结果与证据。
不要修改业务代码。
```

也可以只检查一张截图、一个组件，或只配置接口 Mock。验收依据可以是 Spec、issue、设计稿，也可以是你在消息中给出的明确预期。

验证沿用目标项目的框架和测试环境。已有 Playwright、Cypress、组件测试和 Mock 可以继续使用；新增的过程验证使用 Midscene，新增的代理 Mock 任务使用 Bifrost。

## 验证流程

![前端验证流程：Midscene、Bifrost、精确断言与报告](docs/workflow.zh-CN.svg)

[下载交互版流程图](docs/workflow.zh-CN.html)，在本地打开后可以切换主题、缩放和导出。仓库也保留了 [JSON 源文件](docs/workflow.zh-CN.json)。

## 报告

完整验收会逐项记录需求、用例 ID、实际检查、预期与实际结果，并链接本轮生成的证据。结果分为四种状态：

| 状态 | 含义 |
| --- | --- |
| PASS / 通过 | 已执行，结果符合明确预期。 |
| FAIL / 失败 | 预期不符，或工具错误使本次检查无效。 |
| BLOCKED / 阻塞 | 缺少执行所需的环境、工具或数据。 |
| NOT RUN / 未执行 | 尚未执行，或已采集材料但尚未判断。 |

报告同时记录应用版本、页面入口、环境与后端模式。首次失败和重跑分别保留。使用 Mock 后端的前端检查不能证明真实后端已通过。

参见[报告模板](assets/report.md)、[用例模板](assets/case.md)和[带说明的示例](docs/example-report.md)。示例为虚构的格式演示，已在文件中标明。

## 开发与反馈

在当前 skill 目录运行：

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_package.py
```

测试覆盖报告链接检查脚本和包内引用。已用 Codex 安装目标做过试装，尚未逐框架、逐助手完成浏览器验收。[评估场景](docs/evaluation.md)列出了待做的行为验证。

反馈问题时，请附预期行为、助手实际操作、框架与 runner 版本，以及脱敏后的最小复现。截图和 trace 公开前需检查其中的私人信息。

采用 [MIT](LICENSE) 许可证。交互图包含 [Archify 许可声明](docs/ARCHIFY-LICENSE.txt)。[素材来源与检查记录](docs/visuals.md)。
