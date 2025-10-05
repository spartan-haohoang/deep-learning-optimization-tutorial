# Deep Learning Optimization Tutorial Makefile

.PHONY: help install install-dev test test-cov clean setup run-notebooks validate-data format lint docs

help: ## Show this help message
	@echo "Deep Learning Optimization Tutorial"
	@echo "=================================="
	@echo ""
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install core dependencies
	uv sync

install-dev: ## Install development dependencies
	uv sync --dev

setup: ## Complete setup (install dependencies, validate data)
	@echo "Setting up Deep Learning Optimization Tutorial..."
	./setup.sh
	@echo "Setup complete!"

uv-install: ## Install UV package manager
	curl -LsSf https://astral.sh/uv/install.sh | sh

test: ## Run tests
	uv run pytest

test-cov: ## Run tests with coverage
	uv run pytest --cov=. --cov-report=html --cov-report=term-missing

validate-data: ## Validate data files
	uv run python scripts/validate_data.py

run-notebooks: ## Execute all notebooks
	uv run python scripts/run_notebook.py

format: ## Format code with black and isort
	uv run black .
	uv run isort .

lint: ## Run linting checks
	uv run flake8 .
	uv run black --check .
	uv run isort --check-only .

clean: ## Clean up generated files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/
	rm -rf dist/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .pytest_cache/

docs: ## Generate documentation (if using Sphinx)
	@echo "Documentation generation not yet implemented"

jupyter: ## Start Jupyter Lab
	uv run jupyter lab

notebook: ## Start Jupyter Notebook
	uv run jupyter notebook

docker-build: ## Build Docker image
	docker build -t deep-learning-optimization .

docker-run: ## Run Docker container
	docker-compose up

docker-test: ## Run tests in Docker
	docker-compose run --rm jupyter uv run pytest
