# A1_report
## 目录

[TOC]
## 问题与解决
### 1. **网络代理**  
网络环境是我之前配置的，这次主要在TUN模式下，访问github,在linux终端也能顺利访问网络。其实还没切实体会到**系统代理和TUN模式**有什么区别，感觉好像没有遇到网络问题，从一开始到最后，网络都很顺畅。但是通过查资料能够了解到系统代理覆盖范围有限，无法接管所有流量，有些命令工具、后台会无视它，直连网络，适合上浏览器查资料，检索信息；TUN模式覆盖范围广，几乎接管所有流量，适合终端命令行工具。
### 2. **linux和git**
目前选用 WSL2 Ubuntu24.04


-  Windows 与 Linux 文件系统的“隔离墙”
    - AI (OpenCode) 在 Windows 下创建了 fibonacci.py，但在 Ubuntu 终端里运行提示“文件不存在”     
    
    -  AI是在windows的c:\user\...目录下建的文件，而linux是终端是在独立的WSL文件系统里，两者路径不通
    - OpenCode 切换到 WSL 的真实网络路径（\\wsl.localhost\...）去操作文件
- 虚拟环境“串味”报错
   - 当前项目敲 uv run 时，报错 VIRTUAL_ENV=/home/lune/git-test/.venv does not match...
  - 之前激活的旧环境没退出，就进入新项目，导致环境冲突
  - deactivate退出旧环境，source.venv/bin/activate激活新环境


### 3.**git**
- src refspec main does not match any
  - git config --global init.defaultBranch main
以后建的仓库默认是main
  - git init初始化这个仓库时，建了master这个分支，github默认main
本地叫 master，云端的是main ，Git 找不到，所以报错


- 远程仓库地址写错

  - does not appear to be a git repository
  - SSH 地址中把 github.com 后面的冒号 : 错写成了斜杠 /
  - 正确格式是 git@github.com:用户名/仓库名.git

## 普通网页对话式 AI vs 本地 Harness 工具

- 普通网页对话式AI像一个顾问，比如我在写代码，它帮我提供参考意见，需要我手动复制、建文件、运行、报错了还得复制回来告诉AI
- 本地harness可以接入本地工程，能自己建文件，跑命令，错了能自己修改代码，实现了自动闭环
- 普通网页对话式AI只说，只提供参考，本地 Harness 工具可以自己动手 

## 交付物 
## 三、 交付物清单

1. **个人 GitHub 仓库链接**：[https://github.com/lunedjj/zhize-training-2026](https://github.com/lunedjj/zhize-training-2026)
   - 包含测试脚本源码 (`A1_Base_and_AI_Tool/src/file_stats.py`)、规范配置的 `.gitignore` 与 `README.md`。
2. **AI 开发工具运行界面截图**：
   - 截图已保存在仓库 `A1_Base_and_AI_Tool/images/` 目录下，展示了 AI Harness 工具直接在工程中操作的界面。

