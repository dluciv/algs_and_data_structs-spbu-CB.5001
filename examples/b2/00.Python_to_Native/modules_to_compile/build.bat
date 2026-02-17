uv run mypyc mypy_python.py
uv run setup.py build_ext --inplace
move *.pyd ..
