<div align="center">

# super - inspire

English | [中文](./docs/README-zh.md)



### Get a clean, out of the box, temporary Linux in under 30s.

What's a super-inspire?It allows you to access the web to operate an out-of-the-box Linux system in less than 30 seconds using only a browser. Of course, the "system" here is implemented with docker, so it cannot be considered as a more isolated virtualization system like KVM.

![](./terminal.png)

</div>

[![Backers on Open Collective](https://opencollective.com/super-inspire-end/backers/badge.svg)](#backers)
 [![Sponsors on Open Collective](https://opencollective.com/super-inspire-end/sponsors/badge.svg)](#sponsors) 

## Current status and acceptance of sponsorship

Currently, the server resources are all provided by myself at my own expense.
In order to provide a better experience for everyone, we accept personal/corporate server resources (!!Urgent need!!!!!) and promotional sponsorship, but do not accept any financial support
If super-inspire can help you and provide sponsorship with conditions and interests, I really hope you can get in touch with me. Please send me an email to zhuyuefeng0@gmail.com. Thank you very much.

- start domestic temporary server has resumed, but still behind the wall of temporary server performance, request address is http://60.190.81.133:8888
- the newly started temporary test server outside the wall has good performance and requests the address
- http://34.80.61.20:8888
- http://35.220.241.175:8888

In the case of over the GFW(Great Firewall of China), it is preferred to try using a foreign temporary test server

## Introduction

** So what can a super-inspire do? **

1. When you need a clean Linux environment for your presentation, you can try to use it to give a presentation to the audience

2. When the school teaching /LUG activity needs everyone to use linux system, you can let students who can't install Linux temporarily experience the charm of Linux

3. When you have an inspiration and want to try it in a clean environment, why not use a super-inspire out of the box?

4. When I'm outside and I don't have a device , the super-inspire allows me to manage servers on any device.

5. See a project on GitHub that you're very interested in trying, but was put off by the fact that it's running on Linux?Super-inspire allows you to get a clean environment in 30s, and you can even open a port for testing programs that need ports (for instance,Develop port 80 for testing).

6. Super-inspire due to use docker as its support, so we use cgroups to manage performance. If you want to test whether one of your apps can run under a certain performance, it is a good choice to use super-inspire

More useful things of super-inspire are you thinking about

In addition, we are planning to develop persistence containers so that some user containers can be destroyed without closing the web page, and they can still be used for a short period of time (Containers that do not support external development).

---

## Screenshot of the web interface

![](./demo/demo.jpg)

## QuickStart/quickStart

To access the temporary server address, you can choose a favorite system here, and then the system will automatically create the system's container, and automatically open a new web page into the web shell interaction.

- currently support Ubuntu14.04, 16.04, 18.04;CentOS6.10;CentOS7;Alpine Latest.
- please note that pop-up windows are allowed.

## How to deploy super-inspire?

If you think the experience provided by the official server is too slow, welcome to deploy one yourself! It's very easy to deploy a super-inspire, and you need to have the following environment:

1. Linux system with docker, Ubuntu:16.04 is recommended

![](./demo/demo.png)

Now you can use the local super-inspire! 
By default, please visit localhost:8888 to test.

## The questions?

If you have any questions, please submit the issue, we will check and reply soon.
Thanks a lot to the **ttyd** project of tsl0922 . It was with it that super-inspire was able to complete the components of webshell.

I wish you greater access to Linux and open source through the super-inspire, which is our biggest dream.

## Contributors

This project exists thanks to all the people who contribute. 
<a href="https://github.com/super-inspire/super-inspire-end/graphs/contributors"><img src="https://opencollective.com/super-inspire-end/contributors.svg?width=890&button=false" /></a>


## Backers

Thank you to all our backers! 🙏 [[Become a backer](https://opencollective.com/super-inspire-end#backer)]

<a href="https://opencollective.com/super-inspire-end#backers" target="_blank"><img src="https://opencollective.com/super-inspire-end/backers.svg?width=890"></a>


## Sponsors

Support this project by becoming a sponsor. Your logo will show up here with a link to your website. [[Become a sponsor](https://opencollective.com/super-inspire-end#sponsor)]

<a href="https://opencollective.com/super-inspire-end/sponsor/0/website" target="_blank"><img src="https://opencollective.com/super-inspire-end/sponsor/0/avatar.svg"></a>
<a href="https://opencollective.com/super-inspire-end/sponsor/1/website" target="_blank"><img src="https://opencollective.com/super-inspire-end/sponsor/1/avatar.svg"></a>
<a href="https://opencollective.com/super-inspire-end/sponsor/2/website" target="_blank"><img src="https://opencollective.com/super-inspire-end/sponsor/2/avatar.svg"></a>
<a href="https://opencollective.com/super-inspire-end/sponsor/3/website" target="_blank"><img src="https://opencollective.com/super-inspire-end/sponsor/3/avatar.svg"></a>
<a href="https://opencollective.com/super-inspire-end/sponsor/4/website" target="_blank"><img src="https://opencollective.com/super-inspire-end/sponsor/4/avatar.svg"></a>
<a href="https://opencollective.com/super-inspire-end/sponsor/5/website" target="_blank"><img src="https://opencollective.com/super-inspire-end/sponsor/5/avatar.svg"></a>
<a href="https://opencollective.com/super-inspire-end/sponsor/6/website" target="_blank"><img src="https://opencollective.com/super-inspire-end/sponsor/6/avatar.svg"></a>
<a href="https://opencollective.com/super-inspire-end/sponsor/7/website" target="_blank"><img src="https://opencollective.com/super-inspire-end/sponsor/7/avatar.svg"></a>
<a href="https://opencollective.com/super-inspire-end/sponsor/8/website" target="_blank"><img src="https://opencollective.com/super-inspire-end/sponsor/8/avatar.svg"></a>
<a href="https://opencollective.com/super-inspire-end/sponsor/9/website" target="_blank"><img src="https://opencollective.com/super-inspire-end/sponsor/9/avatar.svg"></a>


