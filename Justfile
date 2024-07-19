defaukt: fmt lint

# Code Formatting & Linting
fmt:
    ruff format apps libs

lint:
    ruff check apps libs

fix:
    ruff check --fix apps libs

# Work with Apps & Libs
run-app target:
    python -m apps.{{target}}.app.main

test-app target:
    python -m unittest discover -s apps/{{target}}/tests -p "test_*.py"

test-lib target:
    python -m unittest discover -s libs/{{target}}/tests -p "test_*.py"
