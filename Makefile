.PHONY: tests

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

streamlit-run:
	docker run --name streamlit_app -p 8001:8501 --rm -it streamlit_app:latest streamlit run app.py

dash:
	docker exec -it dash_app bash

dash-build:
	docker build . -f dash_app/Dockerfile -t dash_app:latest

dash-run:
	docker run --name dash_app -p 8002:8050 --rm -it dash_app:latest python app.py

panel:
	docker exec -it panel_app bash

panel-build:
	docker build . -f panel_app/Dockerfile -t panel_app:latest

panel-run:
	docker run --name panel_app -p 8003:5006 --rm -it panel_app:latest panel serve app.py --autoreload --show --allow-websocket-origin=localhost:8003

tests-build:
	docker build . -f tests/Dockerfile -t tests_e2e:latest

tests:
	make tests-build
	docker run --name tests_e2e --network="host" --rm -it tests_e2e:latest bash

tests-run:
	make tests-build
	docker run --name tests_e2e --network="host" --rm -it tests_e2e:latest pytest -s --base-url http://localhost:8002
