update-deps:
	pip install pip-tools --upgrade

	pip-compile streamlit_app/requirements/base.in
	pip-compile dash_app/requirements/base.in
	pip-compile panel_app/requirements/base.in

up:
	docker-compose up --build

down:
	docker-compose down

build:
	docker-compose build

streamlit:
	docker exec -it streamlit_app bash

streamlit-build:
	docker build . -f streamlit_app/Dockerfile -t streamlit_app:latest

dash:
	docker exec -it dash_app bash

dash-build:
	docker build . -f dash_app/Dockerfile -t dash_app:latest

panel:
	docker exec -it panel_app bash

panel-build:
	docker build . -f panel_app/Dockerfile -t panel_app:latest

panel-run:
	docker run --rm -it panel_app bash
