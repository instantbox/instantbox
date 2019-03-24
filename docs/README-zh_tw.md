<p align="right">繁體中文 | <a href="./README-zh_cn.md">简体中文</a> | <a href="../README.md">English</a></p>

<div align="center">

![logo](https://user-images.githubusercontent.com/5880908/53614582-6ebdfc80-3ba8-11e9-819e-d96a3f7c22f0.png)

# instantbox

在不到 30s 內得到一個乾淨、開箱即用的臨時 Linux 系統.

[![Travis CI](https://badgen.net/travis/instantbox/instantbox)](https://travis-ci.com/instantbox/instantbox)
[![Docker](https://badgen.net/badge//instantbox%2Finstantbox?icon=docker)](https://hub.docker.com/r/instantbox/instantbox)
![Python 3.6](https://badgen.net/badge/python/3.6/3776ab)
![Code Style Pep8](https://badgen.net/badge/code%20style/pep8/ffd343)
[![Chat on Telegram](https://badgen.net/badge/chat/on%20telegram/0088cc)](https://t.me/joinchat/HtYtxRSerOwrMLg_2_wZTQ)
[![MIT](https://badgen.net/badge/license/MIT/3da639)](LICENSE)

</div>


## 介紹

### instantbox 是什麼？

它能夠讓你僅透過瀏覽器的情況下，在不到30s 的時間內，就可以使用web 來操作一個開箱即用的Linux 系統，當然這裡的"系統" 是通過docker 實現的，所以也不能直接認為就是如同KVM 般隔離更嚴格的虛擬化系統。


### 所以 instantbox 可以用來幹什麼？

1. 當你在演講時，臨時需要一個乾凈的 Linux 環境，你就可以嘗試使用它為觀眾做呈現
2. 當學校教學/LUG 活動需要大家一起進行 Linux 實驗時，你可以讓暫時無法安裝 Linux 的同學體驗到 Linux 的魅力
3. 當你有了一個靈感，想要在乾凈的環境下嘗試，為什麽不使用開箱即用的 instantbox 呢？
4. 當你在外邊，卻沒有攜帶設備時，instantbox 甚至可以讓你在任何一臺設備上對服務器進行管理（跳板機）
5. 看到 GitHub 上某個非常感興趣的項目想要嘗試，卻因為該項目運行在 Linux 而望而卻步？ instantbox 可以讓你立刻獲得一個乾凈的環境，你甚至可以開放一個通訊埠(Port)用於測試需要使用通訊埠的程序（例如開放 80 通訊埠進行測試 nginx）
6. instantbox 由於使用 docker 作為支持，所以我們使用了 cgroups 來對性能進行管理，如果你想測試的你的某個應用在某個性能下是否能夠運行，使用 instantbox 是一個非常好的選擇

instantbox 更多的用處由你來創想.


## 快速開始

你可以在這裡選擇一個喜歡的系統，然後系統將自動創建該系統的容器，並自動打開新的網頁進入 webshell 互動.

![Demo screenshot](https://user-images.githubusercontent.com/5880908/53613565-6237a500-3ba4-11e9-9e39-8ea48cee73ee.png)


## 如何部署

如果你認為官方的服務器提供的體驗過慢的話，歡迎自行部署一個~，部署 instantbox 非常簡單，你需要擁有以下環境:

* 已裝有 docker 的 Linux 系統

```bash
mkdir instantbox && cd $_
bash <(curl -sSL https://raw.githubusercontent.com/instantbox/instantbox/master/init.sh)
```

預設請訪問 `http://<ip地址>:8888` 來進行測試.


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

