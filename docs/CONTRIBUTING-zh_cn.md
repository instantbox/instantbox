<p align="right">简 | <a href="./CONTRIBUTING-zh_tw.md">繁</a> | <a href="../CONTRIBUTING.md">En</a></p>

### 一起来贡献 instantbox 吧！

> 首先感谢您关注 instantbox 的发展, 这里会告诉您如何参与共同构建更好的 instantbox !


# 贡献指南

> 按照共同的贡献指南才能更好的参与贡献和持续推进整个项目发展


### Commit message 指南

* 尽量 "一次修改" 就提交 "一次 message"

  例如当前有如下工作：

  * 一个 bug 需要修复
  * 一个新 feature 开发

  建议选择一个更为重要的工作先行处理，并在通过测试后进行 commit

  而不是在一次 commit 中完成多项工作（既完成 bug 修复, 同时也完成新 feature 开发）

* Commit message 格式

  项目使用 AngularJS 的 [commit message convention](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines) [[中文]](http://www.ruanyifeng.com/blog/2016/01/commit_message_change_log.html)

  `<type>(<scope>): <subject>`

  其中 `type` 有以下可选项：
    * feat：新功能（feature）
    * fix：修补bug
    * docs：文档（documentation）
    * style： 格式（不影响代码运行的变动）
    * refactor：重构（即不是新增功能，也不是修改bug的代码变动）
    * perf：提升性能
    * test：增加测试
    * chore：构建过程或辅助工具的变动

  例如:

    * docs(README): add sponsor link

    * style(file.py): fix syntax error

    * fix(api): fix create docker container bug


### Issue 指南

* 尽可能提供足够的运行环境信息

* 尽可能提供运行时问题

* 尽可能提供完整打印的错误堆栈信息


### Pull request 指南

* 尽量保持 commit history 干净完整

* 确认代码风格通过 pycodestyle 验证

* 编写并确认代码通过单元测试

* 尽量能够描述修改内容和原因

* 每一个 PR 需要经过至少一次他人的 review


### 加入 instantbox

想加入 instantbox 团队? 非常欢迎!

请将您的请求发送到 team@instantbox.org 并注明请求和需求即可~

欢迎你参与 instantbox , 同时希望 instantbox 能帮助你成长, 不过作为一个穷穷的小开源组织(哭), 我们暂时不能提供任何经济上的回馈, 还请理解 > . < 


### 其他疑问？

欢迎前往 [telegram](https://t.me/joinchat/HtYtxRSerOwrMLg_2_wZTQ) 参与交流或者直接提起 issue 来砸向我们呀～
