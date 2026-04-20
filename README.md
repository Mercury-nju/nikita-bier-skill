# nikita-bier-public-heuristics

Nikita Bier 的公开 consumer-social 产品增长框架。不是语录合集，也不是角色扮演皮肤，而是一个可复用的判断系统。

基于 best-effort 公开 X 语料、thread 镜像、公开访谈和产品报道，
提炼出关于 `dense networks`、`time-to-value`、`distribution advantage`、
`viral vs durable`、`interest-graph cold start` 的一套实战启发式。

## 这是什么

这个 skill 用来做两类事：

1. 看产品
用于评估 consumer app、社交产品、分发机制、冷启动、传播路径和增长风险。

2. 写观点
用于把一段普通的产品/增长表达，改写成更短、更尖锐、更有机制感的短帖或判断。

它不是：

- Nikita Bier 本人语气模拟器
- 完整历史推文档案
- 万能增长答案生成器

## 适合什么问题

- 这个社交 app 为什么“有用但不传播”？
- 这个 network product 为什么 dead on arrival？
- 这个 launch 应该怎么做，还是根本不该 launch？
- 这个点子该先切哪个 dense network？
- 这条增长观点怎么改得更尖锐、更像 operator？

## 使用方式

安装后直接在对话里这样提：

```text
用 nikita-bier-public-heuristics 帮我判断这个社交产品点子
Nikita Bier 会怎么看这个增长策略？
用更 Nikita Bier 的方式锐化这条推文
这个产品为什么 retain 了但不 spread？
```

## 效果示例

### 问：这个匿名社交产品为什么总是拉不起来？

```text
这不是匿名的问题。
这是编排的问题。

你没有办法稳定地让用户在打开产品的前 30 秒里进入一个有情绪、有关系、
有反馈的社交场景。

匿名只是包装。
真正的变量是：第一口 dopamine 能不能被稳定制造出来。
如果做不到，这个产品就是 dead on arrival。
```

### 问：这个产品很有用，为什么没人分享？

```text
因为 usefulness 不是 distribution.

用户会反复使用工具。
但他们只会把朋友拉进一个 social situation。

如果输出物不能截图、转发、比较、炫耀、群聊讨论，
那你拥有的是 utility，不是 spread.
```

### 问：帮我把这条增长观点改得更像 Nikita Bier

原句：

```text
很多产品失败是因为没有做好增长。
```

改写：

```text
大多数产品不是死于增长太弱。
而是死于第一口价值太难被编排出来。

一个连价值都无法稳定触发的产品，
谈不上增长。
```

更多示例见 [examples/prompts.md](examples/prompts.md)。

## 蒸馏了什么

这份 skill 当前重点覆盖：

- primitive human demand
- dead-on-arrival orchestration
- replace launch with test
- do things that don't scale
- dense networks over broad abstraction
- teens vs adults in social spread
- latent demand over polite research
- screenshots / group chats as high-intent signals
- viral vs durable
- messaging as a brutal category
- interest-graph cold start
- distribution advantages decay

## 资料基础

当前主要依据包括：

- best-effort 公开 X corpus：`2024-01` 到 `2026-04`，去重后 `662` 条帖子
- Thread Reader 等公开 thread 镜像
- Lenny's Podcast / transcript
- TechCrunch、Lightspeed、Berkeley、Wikipedia 等公开报道与背景资料

详见：

- [SKILL.md](SKILL.md)
- [references/source-coverage.md](references/source-coverage.md)
- [references/sources.md](references/sources.md)

## 使用边界

你可以说：

- 基于 Nikita Bier 的公开材料提炼
- 用 Nikita Bier 的公开 consumer-growth heuristics 分析

你不应该说：

- 这就是 Nikita 本人的真实观点
- 这完整覆盖了他全部历史推文
- 这是对真人身份的模仿

## 目录结构

```text
nikita-bier-public-heuristics/
├── README.md
├── SKILL.md
├── examples/
│   └── prompts.md
└── references/
    ├── anti-patterns.md
    ├── distilled-principles.md
    ├── heuristics.md
    ├── posting-playbook.md
    ├── source-coverage.md
    ├── sources.md
    └── theme-matrix.md
```
