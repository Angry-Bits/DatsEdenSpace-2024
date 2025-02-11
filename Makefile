venv-setup:
	python -m venv venv

venv-activate-unix:
	source venv/bin/activate

venv-activate-windows:
	venv\Scripts\activate.bat

venv-deactivate-unix:
	deactivate

venv-deactivate-windows:
	deactivate.bat

install:
	pip install -r requirements.txt

start:
	python -m src.scripts.main

lint:
	flake8 src

freeze:
	pip freeze > requirements.txt

clear-logs:
	echo "" > journal.log
