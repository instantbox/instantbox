<p align="right">繁 | <a href="./README-zh_cn.md">简</a> | <a href="../README.md">English</a></p>

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

它能夠讓你僅透過瀏覽器的情況下，在不到30s 的時間內，就可以使用 web 來操作一個開箱即用的 Linux 系統，當然這裡的 "系統" 是透過 docker 實現的，所以不能直接認為就是如 KVM 般隔離更嚴格的虛擬化系統。


### 所以 instantbox 可以用來做什麼？

1. 當你在演講時，臨時需要一個乾凈的 Linux 環境，你就可以嘗試使用它為觀眾做呈現
2. 當學校教學/LUG 活動需要大家一起進行 Linux 實驗時，你可以讓暫時無法安裝 Linux 的同學體驗到 Linux 的魅力
3. 當你有了一個靈感，想要在乾凈的環境下嘗試，為什麽不使用開箱即用的 instantbox 呢？
4. 當你人在外面，卻沒有攜帶設備時，instantbox 甚至可以讓你在任何一臺設備上對服務器進行管理（跳板機）
5. 看到 GitHub 上某個非常感興趣的項目想要嘗試，卻因為該項目運行在 Linux 而望而卻步？ instantbox 可以讓你立刻獲得一個乾凈的環境，你甚至可以開放一個 Port 用於測試需要使用 Port 的程序（例如開放 80 Port進行測試 nginx）
6. instantbox 由於使用 docker 作為支持，所以我們使用了 cgroups 來管理性能，如果你想測試的你的某個應用在某個性能下是否能夠運行，使用 instantbox 是一個非常好的選擇

instantbox 更多的好處由你來創想.


## 快速開始

你可以在這裡選擇一個喜歡的系統，系統將自動創建該系統的容器，並自動打開新的網頁進入 webshell 使用.

![Demo screenshot](https://user-images.githubusercontent.com/5880908/53613565-6237a500-3ba4-11e9-9e39-8ea48cee73ee.png)


## 如何安裝

如果你認為官方的服務器提供的效能過慢的話，歡迎自行安裝一個~，安裝 instantbox 非常簡單，你需要擁有以下環境:

* 已裝有 docker 的 Linux 系統

```bash
mkdir instantbox && cd $_
bash <(curl -sSL https://raw.githubusercontent.com/instantbox/instantbox/master/init.sh)
```

預設請透過 `http://<ip地址>:8888` 進行測試.


## 捐助

目前服務器資源都是我自費提供的，學生的壓力非常大...

為了給大家提供更好的體驗，我們接受個人/公司對於服務器資源 **(!! 急需 !!)** 和宣傳幫助上的贊助，但是暫不接受任何資金上的贊助～

如果 instantbox 有幫助到你，並且能夠有條件和興趣提供贊助。非常希望您能與我們取得聯繫，請發送郵件到 team@instantbox.org 感激不盡！


## 有疑問？

請提交 issue 或前往 [telegram](https://t.me/joinchat/HtYtxRSerOwrMLg_2_wZTQ) 與我們交流。


## 感谢

* [tsl0922/ttyd](https://github.com/tsl0922/ttyd) - webshell


## 
願你透過 instantbox 更加方便的接觸 Linux 和開源，這是我們最大的夢想.
