# Virtual Environment
POETRY_RUN		:= poetry run

.PHONY: lint
lint:
	$(POETRY_RUN) black .
	$(POETRY_RUN) isort .
