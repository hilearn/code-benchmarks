PROJECT = bench-sql-gen
PYTHON=python3.7
venv_name = py${PYTHON_VERSION}-${PROJECT}
venv = .venv/${venv_name}

default: ${venv}
	${venv}/bin/python test.py
.PHONY: default

${venv}: requirements.txt
	${PYTHON} -m venv ${venv}
	${venv}/bin/pip install -r requirements.txt --cache .tmp/


