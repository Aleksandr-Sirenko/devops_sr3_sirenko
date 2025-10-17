# DevOps – Самостійна робота 3

### Студент:
Сіренко Олександр Сергійович

# CLI Tools Demonstration

This repository demonstrates three approaches to building CLI tools in Python: `sys.argv`, `click`, and `fire`.

## Prerequisites
- Python 3.8+
- Install dependencies:
  ```bash
  pip install click fire
  ```

## Project Structure
- `src/sys_tool.py`: Basic CLI tool using `sys.argv`.
- `src/click_tool.py`: CLI tool using the `click` library.
- `src/utils.py`: Utility functions for `fire_expose.py`.
- `src/fire_expose.py`: CLI tool exposing functions via `fire`.

## Usage

### 1. sys_tool.py
Prints "командна строка" when run directly. Does nothing when imported.

```bash
python src/sys_tool.py
# Output: командна строка

python src/sys_tool.py --help
# Output: Usage: python sys_tool.py
# Prints 'командна строка' when run directly.

python -c "import src.sys_tool"
# Output: (none)
```

### 2. click_tool.py
Prints the provided name unless it starts with 'p' or 'P'.

```bash
python src/click_tool.py say --name Alice
# Output: Alice

python src/click_tool.py say --name Peter
# Output: Ім’я не підходить

python src/click_tool.py --help
# Shows auto-generated help
```

### 3. fire_expose.py
Exposes `greet` and `goodbye` functions from `utils.py` via CLI.

```bash
python src/fire_expose.py greet Alice
# Output: Привіт, Alice!

python src/fire_expose.py goodbye Bob
# Output: До побачення, Bob!

python src/fire_expose.py --help
# Shows fire-generated help
```