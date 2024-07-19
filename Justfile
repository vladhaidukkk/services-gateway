run-app target:
    python -m apps.{{target}}.app.main

test-app target:
    python -m unittest discover -s apps/{{target}}/tests -p "test_*.py"

test-lib target:
    python -m unittest discover -s libs/{{target}}/tests -p "test_*.py"
