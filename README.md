# git-learning

这是配套《Git 安装配置与入门管理》的**练习仓库**。目的不是写代码，而是把 Git 的每个动作亲手跑一遍，让肌肉记住命令。

## 目录说明

| 路径 | 用途 |
|---|---|
| `src/hello.py` | 最小的可运行示例，改它来练习「改代码 → 提交」 |
| `docs/notes.md` | 学习笔记，练习怎么把新文件加进仓库 |
| `学习计划.md` | 七天安排与自测题（也顺便练习中文文件名） |
| `.gitignore` | 规定哪些文件永远不进仓库 |
| `.gitattributes` | 统一换行符，避免 Windows/Linux 来回改 |

## 三条铁律

1. **一次提交只做一件事**，提交信息写清楚「为什么改」。
2. **提交前先看**：`git status` 看改了哪些文件，`git diff` 看改了什么。
3. **密钥、密码、`.env` 永不进仓库**——进了历史就很难彻底删掉。

## 常用命令速查

```powershell
git status                     # 我现在改了什么
git diff                       # 具体改动内容
git add -p                     # 一块一块挑着暂存（强烈推荐）
git commit -m "feat: ..."      # 提交
git log --oneline --graph      # 看历史
git switch -c feat/xxx         # 开新分支
git merge feat/xxx             # 合并分支
git remote -v                  # 远程仓库在哪
git push -u origin main        # 推送到 GitHub
```

## 每次开始前

```powershell
cd C:\Users\28492\Documents\deepseek-harness\default-workspace\git-learning
git status
```

更完整的讲解在上一层的 `git-bootstrap\docs\` 里，建议顺序：`01-install` → `02-config` → `03-daily-workflow` → `04-troubleshooting` → `05-cheatsheet` → `06-seven-days`。
