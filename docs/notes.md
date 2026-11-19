# 学习笔记

> 每次学会一个新命令，就在下面补一条。改完记得提交，作为练习。

## 一、三层模型（最重要的一张图）

```
工作区（你正在改的文件）
   │  git add
   ▼
暂存区（这次的改动确认要提交的部分）
   │  git commit
   ▼
本地仓库（历史记录，.git 目录）
   │  git push
   ▼
远程仓库（GitHub 上的副本）
```

- `git status` 永远先看这三层各有什么。
- `git diff` 看「工作区 vs 暂存区」；`git diff --staged` 看「暂存区 vs 上次提交」。

## 二、命令笔记

### 2026-11-19 初始化

- `git init -b main`：建仓库并直接命名主分支为 main。
- `git status -sb`：一行看清分支和改动（别名 `git st`）。

（在下面继续记录……）

## 三、踩坑记录

| 现象 | 原因 | 解法 |
|---|---|---|
| 中文文件名显示成 `\346\226\207` | `core.quotepath=true` | `git config --global core.quotepath false` |
| 每次提交都提示 CRLF | 换行符转换 | 配 `core.autocrlf` + `.gitattributes` |

（在下面继续记录……）
