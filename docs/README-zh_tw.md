<p align="right"><a href="../README.md">English</a> | <a href="./README-zh_cn.md">简体中文</a> | 繁體中文</p>

<div align="center">

![logo](https://user-images.githubusercontent.com/5880908/53614582-6ebdfc80-3ba8-11e9-819e-d96a3f7c22f0.png)

# instantbox

在不到 30s 内得到一个干净、开箱即用的临时 Linux 系统.

[![Travis CI](https://badgen.net/travis/instantbox/instantbox)](https://travis-ci.com/instantbox/instantbox)
[![Docker](https://badgen.net/badge//instantbox%2Finstantbox?icon=docker)](https://hub.docker.com/r/instantbox/instantbox)
![Python 3.6](https://badgen.net/badge/python/3.6/3776ab)
![Code Style Pep8](https://badgen.net/badge/code%20style/pep8/ffd343)
[![Chat on Telegram](https://badgen.net/badge/chat/on%20telegram/0088cc)](https://t.me/joinchat/HtYtxRSerOwrMLg_2_wZTQ)
[![MIT](https://badgen.net/badge/license/MIT/3da639)](LICENSE)

</div>


## 介绍

### instantbox 是什么？

它能够让你仅通过浏览器的情况下，在不到 30s 的时间内，就可以使用 web 来操作一个开箱即用的 Linux 系统，当然这里的 "系统" 是通过 docker 实现的，所以也不能直接认为就是如同 KVM 般隔离更严格的虚拟化系统。


### 所以 instantbox 可以用来干什么？

1. 当你在演讲时，临时需要一个干净的 Linux 环境，你就可以尝试使用它为观众做演示
2. 当学校教学/LUG 活动需要大家一起进行 Linux 实验时，你可以让暂时无法安装 Linux 的同学体验到 Linux 的魅力
3. 当你有了一个灵感，想要在干净的环境下尝试，为什么不使用开箱即用的 instantbox 呢？
4. 当你在外边，却没有携带设备时，instantbox 甚至可以让你在任何一台设备上对服务器进行管理（跳板机）
5. 看到 GitHub 上某个非常感兴趣的项目想要尝试，却因为该项目运行在 Linux 而望而却步？ instantbox 可以让你立刻获得一个干净的环境，你甚至可以开放一个端口用于测试需要使用端口的程序（例如开放 80 端口进行测试 nginx）
6. instantbox 由于使用 docker 作为支持，所以我们使用了 cgroups 来对性能进行管理，如果你想测试的你的某个应用在某个性能下是否能够运行，使用 instantbox 是一个非常好的选择

instantbox 更多的用处由你来创想.


## 快速开始

你可以在这里选择一个喜欢的系统，然后系统将自动创建该系统的容器，并自动打开新的网页进入 webshell 交互.

![Demo screenshot](https://user-images.githubusercontent.com/5880908/53613565-6237a500-3ba4-11e9-9e39-8ea48cee73ee.png)


## 如何部署

如果你认为官方的服务器提供的体验过慢的话，欢迎自行部署一个~，部署 instantbox 非常简单，你需要拥有以下环境:

* 已装有 docker 的 Linux 系统

```bash
mkdir instantbox && cd $_
bash <(curl -sSL https://raw.githubusercontent.com/instantbox/instantbox/master/init.sh)
```

默认请访问 `http://<ip地址>:8888` 来进行测试.


## 捐助

目前服务器资源都是我自费提供的，学生党压力非常大...

为了给大家提供更好的体验，我们接受个人/公司对于服务器资源 **(!! 急需 !!)** 和宣传帮助上的赞助，但是暂不接受任何资金上的赞助～

如果 instantbox 有帮助到你，并且能够有条件和兴趣提供赞助。非常希望您能与我们取得联系，请发送邮件到 team@instantbox.org 感激不尽！


## 有疑问？

请提交 issue 或前往 [telegram](https://t.me/joinchat/HtYtxRSerOwrMLg_2_wZTQ) 与我们交流。


## 感谢

* [tsl0922/ttyd](https://github.com/tsl0922/ttyd) - webshell


## 
愿你通过 instantbox 更加方便的接触 Linux 和开源，这是我们最大的梦想.

