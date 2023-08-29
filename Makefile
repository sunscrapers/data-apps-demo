.PHONY: update-deps, up, down, build

update-deps:
	pip install pip-tools --upgrade

	pip-compile streamlit_app/requirements.in
	pip-compile dash_app/requirements.in
	pip-compile panel_app/requirements.in

up:
	docker-compose up --build

down:
	docker-compose down

build:
	docker-compose build
