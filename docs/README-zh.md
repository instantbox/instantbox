<div align="center">

# super-inspire-end

[Englist](../README.md) | 中文

### 在不到 30s 内得到一个干净的开箱即用的临时 linux 系统.

super-inspire 是什么? 它能够让你仅通过浏览器的情况下, 在不到 30s 的时间内, 就可以使用 web 来操作一个开箱即用的 linux 系统, 当然这里的"系统"是通过 docker 实现的, 所以也不能直接认为就是如同 KVM 般隔离更严格的虚拟化系统.

![](../terminal.png)

</div>

## 当前状况和接受赞助态度

目前服务器资源都是我自费提供的, 学生党压力非常大...
为了给大家提供更好的体验, 我们接受个人/公司对于服务器资源(!!急需!!)和宣传帮助上的赞助, 但是不接受任何资金上的赞助~
如果 super-inspire 有帮助到你, 并且能够有条件和兴趣提供赞助, 非常希望您能与我取得联系, 请发送邮件到 zhuyuefeng0@gmail.com, 感激不尽.

- 国内启动的临时服务器重新恢复, 但是性能仍然赶不上墙外的临时服务器, 请求地址 http://60.190.81.133:8888
- 墙外新启动的临时测试服务器性能较好, 请求地址
  - http://34.80.61.20:8888
  - http://35.220.241.175:8888

在可以翻墙的情况下优先推荐使用国外临时测试服务器进行尝试

## 介绍

**所以 super-inspire 可以用来干什么?**

1. 当你在演讲时, 临时需要一个干净的 linux 环境, 你就可以尝试使用它为观众做演示

2. 当学校教学/LUG 活动需要大家一起进行 linux 实验室, 你可以让暂时无法安装 linux 的同学体验到 linux 的魅力

3. 当你有了一个灵感, 想要在干净的环境下尝试, 为什么不使用开箱即用的 super-inspire 呢?

4. 当我在外边, 却没有携带设备时, super-inspire 甚至可以让我在任何一台设备上对服务器进行管理(跳板机)

5. 看到 GitHub 上某个非常感兴趣的项目想要尝试, 却因为该项目运行在 linux 而望而却步? super-inspire 可以让你在 30s 中获得一个干净的环境, 你甚至可以开放一个端口用于测试需要使用端口的程序(例如开放 80 端口进行测试 nginx)

6. super-inspire 由于使用 docker 作为支持, 所以我们使用了 cgroups 来对性能进行管理, 如果你想测试的你的某个应用在某个性能下是否能够运行, 使用 super-inspire 是一个非常好的选择

super-inspire 更多的用处由你来创想.

此外我们正计划开发持久性容器, 让部分用户容器不再关掉网页就被销毁, 在一小段时间内仍然可以持续使用(不支持对外开放端口的容器)

---

## web 界面截图

![](../demo/demo.jpg)

## quickStart/快速开始

访问临时服务器地址, 你可以在这里选择一个喜欢的系统, 然后系统将自动创建该系统的容器, 并自动打开新的网页进入 web shell 交互.

- 目前支持 Ubuntu14.04, 16.04, 18.04; CentOS6.10; CentOS7; Alpine Latest.

- 请注意允许弹出窗口.

## how to deploy super-inspire?/如何部署?

如果你认为官方的服务器提供的体验过慢的话, 欢迎自行部署一个~, 部署 super-inspire 非常简单, 你需要拥有以下环境:

1. 带有 docker 的 linux 系统, 推荐使用 Ubuntu:16.04

```
# git clone https://github.com/super-inspire/super-inspire-end.git
# cd super-inspire-end/
# sudo ./init.sh
# docker-compose up

```

接着就可以使用 super-inspire 的本地版啦!

默认请访问 localhost:8888 来进行测试.

# questions?/有疑问?

如果你有任何疑问, 请提交 issue, 我们会很快检查并回复.

非常感谢 tsl0922 大佬的**ttyd**项目, super-inspire 借助它才得以完成 webshell 部分的组件.

祝你通过 super-inspire 更加方便的接触 linux 和开源, 这是我们最大的梦想.
