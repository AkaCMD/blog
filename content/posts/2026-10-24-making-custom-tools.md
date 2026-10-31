---
title: 做了一些小工具
date: 2026-10-24
slug: making-custom-tools
tags:
  - 随笔
  - 开发
description: 最近用 AI Agent 辅助，做了点工具给自己用。分享&说说想法。
---
最近用 AI Agent 辅助，做了点工具给自己用，觉得有点价值可以分享出来。顺便说说自己对使用 AI 的看法。

## 3D解谜游戏关卡编辑器
<!-- .card slug=https://github.com/AkaCMD/grid-game-groundwork-godot title="3D 解谜游戏关卡编辑器" text="一个 Godot 3D 网格解谜游戏插件——在编辑器里像画格子一样刷关卡、定义可复用实体、一键试玩，再用 GDScript 扩展独特的玩法机制，自带三个完整示例（推箱子、接水管、滑块）。" content_type="GitHub" -->

![Godot 关卡编辑器界面](media/making-custom-tools/grid-editor.png "Godot 关卡编辑器界面")

这件事儿起因大概主要有二。

一是确实我对类似工具的使用起源已久，在[小石头人](https://akacmd.itch.io/stoneman-adventure)开发的时候用的关卡编辑器就一直是用 Corey Martin 的一个 Unity 上的3D网格游戏框架 [Grid Game Groundwork](https://github.com/corey-martin/grid-game-groundwork) 改的。这次也是想移植到目前用的 Godot 上，让自己之后要是想开发点小解谜游戏也能用。另外有了不少各种编辑器工具（类似 Trenchbroom 这种就很好用）的使用经验后也想做不少功能上的完善让关卡编辑更加高效，减少摩擦。

二是自己想尝试全程用 AI Agent 开发做完整一个项目/工具，顺便一提这次用了不少[这个仓库](https://github.com/mattpocock/skills)的 Skill。

所以这次基本上完整复刻了原版 Grid Game Groundwork 的功能到 Godot 上，并且加了些实用的新功能。

比较有意思的是这次拿这个工具快速做了自己之前的 Jam 作品 [Quack!!! on ICE](https://akacmd.itch.io/quack-on-ice) 的3D版本（3D滑块是吧）。没有做新的建模，先用最简陋的方式拿方块贴图示意了在3D情况下的鸭子滑块机制：
![3D 鸭子滑块机制演示](media/making-custom-tools/quack-3d-slider-demo.gif)


## Steam 浅色主题
<!-- .card slug=https://github.com/AkaCMD/rose-pine-dawn-steam-store-theme title="Steam 浅色主题" text="一个给 Steam 桌面客户端用的浅色主题，Rosé Pine Dawn 配色。" content_type="GitHub" -->

![Steam 客户端浅色主题库界面](media/making-custom-tools/steam-theme-1.png "Steam 库界面应用主题后的效果")

![Steam 客户端浅色主题商店页](media/making-custom-tools/steam-theme-2.png "Steam 商店页应用主题后的效果")

一直觉得 Steam 客户端原生默认的黑色主题有点过于冰冷，过于商业，加之也没有能够随系统切换的亮暗变化。自己也比较喜欢 [Rosé Pine](https://rosepinetheme.com/) 这个主题配色，就把这个配色主题放到 Steam 客户端上。最后的效果感觉还是比较好看的，可读性也不错，虽然有些地方可能定制 css 没有覆盖到，之后可以持续修复一下。


工作上其实也用 AI 做了点比较搞耍的小工具也分享给周围的人，不过就不在这里多提了。

## 聊聊 AI
我对 AI 的看法是，它是一个用好了能很好用的工具，但确实很容易培养人的惰性并且客观上确实造成了各种 AI Slop 的现象。

目前也算是体验过 AI 的各种用法了，从早期一问一答的聊天，到后面用 AI 搜集整合信息、帮忙安排生活、分析个人状态、学习新领域知识，也用 agent 帮自己修了不少问题、安装各种环境、做各种自制工具和辅助游戏开发，在工作上天天也会用到。

某种意义上，我觉得 AI 是一种元工具，能够用其制造各种工具来大幅度提高生产力。可以让想法到落地的实现验证变得快速。个人也主动地学习如何更好地利用这种元工具。

但就“好的工具是 Invisible 的”这一点来说，AI 确实会对人本身的心态造成各种影响而导致快速而没有价值的产出。不管是使用 AI 后用户对自己的产物逐渐失去细节的掌控越来越依赖 AI 还是在追逐各种“热点 AI 新闻和技术”中花费时间学了很易朽的东西而忽视提升真正的技艺。

我始终认为 AI 无法取代人类的创造活动，不管是做游戏这件事还是其他各种艺术领域。在游戏开发和设计上，目前的 AI 无法判断是否好玩这件事。在艺术创作上，创造过程本身具备很大的价值而不只是结果，不论是对创作者个人来说还是对观众。我热爱的是具有独特个人趣味和光芒的作品以及带着过去一切经历成为自己做出这样作品的人。