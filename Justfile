roots:
    pants roots

deps-all:
    pants dependencies ::

deps-app target:
    pants dependencies apps/{{target}}::

deps-pkg target:
    pants dependencies packages/{{target}}::

run-app target:
    pants run apps/{{target}}:{{target}}

run-pkg target:
    pants run packages/{{target}}:{{target}}

test-app target:
    pants test apps/{{target}}:{{target}}_tests

test-pkg target:
    pants test packages/{{target}}:{{target}}_tests
