# data-apps-demo
Data apps comparison for: Streamlit, Panel and Dash.

## What is Streamlit?
`Streamlit` is a popular Python library used for creating interactive web applications for data visualization and machine learning. `Streamlit` is served via [Tornado](https://www.tornadoweb.org/en/stable/).

## What is Dash by Plotly?
`Dash` is a Python framework for creating interactive web applications for data visualization and analytics. `Dash` is built on top of [Flask](https://flask.palletsprojects.com/en) and [Plotly](https://plotly.com/python/).

## What is a Panel by HoloViz?
Panel is a Python library within the HoloViz ecosystem, used for creating interactive web applications for data visualization, analysis, and modeling. `Panel` is served via [Tornado](https://www.tornadoweb.org/en/stable/).

## Pre-Requirements
* `docker`
* `docker-compose`

## How to run applications
* Create `.env` file basing on `.env_example`
* Run command `make up`
+ `Streamlit` will be exposed under [localhost:8001](http://localhost:8001) url
+ `Dash` will be exposed under [localhost:8002](http://localhost:8002) url
+ `Panel` will be exposed under [localhost:8003](http://localhost:8003) url

## Available commands (using `make`)
* `make update-deps` - use if any libraries has been added / changed / removed
* `make up` - use to run all applications
* `make down` - use to stop all applications
* `make build` - use to manually build all applications
* `make streamlit` - use to enter into `streamlit_app` docker container. For debugging purposes.
* `make dash` - use to enter into `dash_app` docker container. For debugging purposes.
* `make panel` - use to enter into `panel_app` docker container. For debugging purposes.

### Maintenance recommendations
* Install `pre-commit` ([link](https://pre-commit.com/))
* Run command `make update-deps` after any packages modifications
