# nikita-bier-skill

> A public-materials skill derived from Nikita Bier's writing, interviews, and product history.

Nikita Bier 的公开 consumer-social 产品增长框架。不是语录合集，也不是角色扮演皮肤，而是一个可复用的判断系统。

基于 best-effort 公开 X 语料、thread 镜像、公开访谈和产品报道，
提炼出关于 `dense networks`、`time-to-value`、`distribution advantage`、
`viral vs durable`、`interest-graph cold start` 的一套实战启发式。

## 先说边界

这个项目的目标不是模仿真人，也不是声称“还原 Nikita Bier 本人”。

它只做一件事：

- 把公开材料里反复出现、可操作、可复用的 consumer-social heuristics 整理成一个 skill

所以你应该把它理解成：

- a public-heuristics package

而不是：

- an identity simulator

这个 skill 与 Nikita Bier 本人没有官方关系，也不代表其本人立场。

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
- 对真人身份、人格或私有观点的重建

## 适合什么问题

- 这个社交 app 为什么“有用但不传播”？
- 这个 network product 为什么 dead on arrival？
- 这个 launch 应该怎么做，还是根本不该 launch？
- 这个点子该先切哪个 dense network？
- 这条增长观点怎么改得更尖锐、更像 operator？

## 使用方式

安装后直接在对话里这样提：

```text
用 nikita-bier-skill 帮我判断这个社交产品点子
用 Nikita Bier 的公开 heuristics 看这个增长策略
把这条观点改得更有 mechanism，不要 cosplay
这个产品为什么 retain 了但不 spread？
```

## 效果示例

### 问：这个匿名社交产品为什么总是拉不起来？

```text
匿名不是这个产品的优势。
它只是包装纸。

真正的问题是：
你没法稳定制造第一口 social dopamine。

用户打开之后，没有人等着他，没有内容让他紧张，
没有反馈让他想截图，也没有关系让他立刻回来。

这类产品最常见的误判是把“匿名”当成机制。
不是的。

机制是：
用户为什么要现在打开？
为什么要把别人拉进来？
为什么拉进来之后场子会立刻热起来？

如果这三件事回答不了，
那这个产品不是增长差。
是 dead on arrival。
```

### 问：这个产品很有用，为什么没人分享？

```text
因为 usefulness 不是 distribution.

用户会保留一个工具。
但他们只会邀请朋友进入一个 social situation。

所以问题不是“这东西有没有价值”。
问题是“这个价值有没有社交形态”。

如果输出物不能被截图、转发、比较、炫耀、
丢进群聊里引发一句“这是什么，发我”，
那它就只是 utility。

utility 可以留住一部分人。
但 spread 需要谈资、身份信号和分享动机。

很多产品死在这里：
他们把留存逻辑误以为是传播逻辑。
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

你以为你缺的是 distribution.
其实你缺的是一个能被稳定触发的 moment.

一个连价值都无法按需制造出来的产品，
根本还没资格谈增长。
```

### 问：我们该大范围 launch，还是先小范围测试？

```text
不要把 launch 当成庆典。
把它当成曝光管理。

consumer 产品不是 B2B 软件。
用户不会给你 7 次机会慢慢修。

如果产品需要 network density 才成立，
那过早曝光最危险的地方不是“转化低”。
而是你会得到一堆被污染的信号：
看起来像没人要，
其实只是场子没热起来。

正确的问题不是：
“我们该不该 launch？”

而是：
“我们有没有办法在一个足够小、足够密、足够可重复的环境里，
先把价值状态稳定编排出来？”

如果能，就先测试。
如果不能，再考虑一次性打满的大 launch。
但那不是更轻松，
那只是更贵的赌博。
```

### 问：为什么很多做 messaging 的团队最后都死了？

```text
因为他们低估了 messaging 不是功能竞争，
而是基础设施竞争。

用户对聊天产品的预期不是“还不错”。
而是：
100% 送达、
所有联系人都在、
功能没有短板、
切过去没有成本。

这几乎是创业公司最不该正面硬撞的赛道。

更糟的是，
如果你真的把聊天迁进自己产品，
还可能削弱原本的外部传播。
因为用户不再把链接和内容发到第三方 app 里。

所以多数团队不是输在产品做得不够好。
而是从一开始就选了一个需要奇迹才能赢的战场。
```

更多示例见 [examples/prompts.md](examples/prompts.md)。

## 为什么这个项目可能有用

很多“名人 skill”最后变成两种东西：

- 语气模仿器
- 断章取义的语录合集

这两个方向都很容易失真。

这个项目更关心的是另一层：

- 哪些判断在不同公开材料里反复出现
- 哪些结论是可执行的，而不只是好听
- 哪些启发式在真实产品讨论里能复用

所以它重点不是“像他讲话”，而是：

- 帮你更快定位 consumer/social 产品里的机制问题

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

## 可能被质疑的点

### 1. 为什么 repo 直接用了真人名字？

因为这个 skill 的研究对象就是 Nikita Bier 的公开材料。

但项目内容始终强调：

- public materials
- heuristics
- no identity simulation

如果你希望进一步降低误解风险，可以在自己的 fork 中改成更中性的名字，比如：

- `consumer-social-growth-skill`
- `public-consumer-growth-heuristics`

### 2. 为什么不是“完整推文全集”？

因为公开网页、镜像站、搜索接口和 API 配额都有限。

所以这里明确采用的是：

- best-effort public corpus

而不是：

- complete historical archive

### 3. 会不会把个人风格误当成普适真理？

会，所以仓库专门加入了：

- source coverage
- theme matrix
- anti-patterns

它们的目的就是提醒使用者：

- 这是提炼出来的 lens，不是不可挑战的 doctrine

## 使用边界

你可以说：

- 基于 Nikita Bier 的公开材料提炼
- 用 Nikita Bier 的公开 consumer-growth heuristics 分析

你不应该说：

- 这就是 Nikita 本人的真实观点
- 这完整覆盖了他全部历史推文
- 这是对真人身份的模仿

## 更好的使用方式

推荐这样用：

- 分析一个 consumer/social 产品为什么不传播
- 拆解 launch、cold start、network density、shareability
- 把一段平庸的增长表达改得更有机制感

不推荐这样用：

- “请完整扮演 Nikita Bier”
- “请像他本人一样骂人”
- “请给我生成他没说过的私人观点”

## 目录结构

```text
nikita-bier-skill/
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
