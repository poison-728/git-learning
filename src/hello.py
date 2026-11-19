"""练习用的最小脚本：能跑起来就说明 Python 环境正常。

改这个文件是练习「修改 → 暂存 → 提交」最安全的素材。
"""


def greet(name: str) -> str:
    """返回一句问候，用来验证脚本能正常执行。"""
    return f"你好，{name}！Git 已经接管这个项目了。"


if __name__ == "__main__":
    print(greet("同学"))
