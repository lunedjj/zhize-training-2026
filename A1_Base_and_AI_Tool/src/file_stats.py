"""统计当前目录下 README.md 的文件行数。

用法（在项目根目录 zhize-training-2026 下运行）：

    uv run A1_Base_and_AI_Tool/src/file_stats.py
"""

from pathlib import Path


def count_lines(path: Path) -> int:
    """返回文件的行数。

    splitlines() 会忽略文件末尾的换行符，因此 "a\\nb\\n" 与 "a\\nb" 都算 2 行，
    空文件算 0 行。
    """
    return len(path.read_text(encoding="utf-8").splitlines())


def main() -> None:
    readme = Path.cwd() / "README.md"
    if not readme.is_file():
        raise SystemExit(
            f"未找到 README.md：{readme}\n"
            "请在包含 README.md 的目录（项目根目录）下运行本脚本。"
        )

    print(f"{readme} 共 {count_lines(readme)} 行")


if __name__ == "__main__":
    main()
