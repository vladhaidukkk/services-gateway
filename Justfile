roots:
    pants roots

run-app target:
    pants run apps/{{target}}:{{target}}

run-pkg target:
    pants run packages/{{target}}:{{target}}

test-app target:
    pants test apps/{{target}}:{{target}}_tests

test-pkg target:
    pants test packages/{{target}}:{{target}}_tests
