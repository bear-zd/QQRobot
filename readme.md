# 一个我自己拿来玩的QQ机器人

由于QQ封杀了一些QQ机器人，导致只能自己硬搞了。

该机器人的后台主要靠两个项目实现：

| [GMC](https://github.com/protobufbot/go-Mirai-Client/releases)**【推荐】** | miraigo | 不需要 | 一个程序可以登陆一个号，多个号需要多 |
| ------------------------------------------------------------ | ------- | ------ | ------------------------------------ |

| Python | [PHIKN1GHT/pypbbot](https://github.com/PHIKN1GHT/pypbbot) | [example](https://phikn1ght.github.io/2021/02/01/beginners-guide-for-pypbbot/) | [PHIKN1GHT](https://github.com/PHIKN1GHT) | [文档](https://phikn1ght.github.io/2021/02/01/beginners-guide-for-pypbbot/) 有插件机制 |
| ------ | --------------------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------- | ------------------------------------------------------------ |

具体的内容详见此项目：[ProtobufBot](https://github.com/ProtobufBot/ProtobufBot)

我在此基础上根据给的框架进行插件的开发。但是由于看不懂源代码，导致仍然无法实现很多内容。

目前已经实现的：

- [ ] sayHello

- [ ] 发送新闻

将来想要实现的：

- [ ] 微博热搜
- [ ] 发送趣图
- [ ] 历史上的今天
- [ ] 小游戏