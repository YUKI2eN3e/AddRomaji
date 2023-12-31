set windows-shell := ["C:\\Program Files\\Git\\bin\\sh.exe", "-c"]

_setup_poetry:
	poetry install

# SetUp project
setup: _setup_poetry
	poetry run pre-commit install

# Organize imports
sort:
	poetry run isort --profile black --line-length 88 .

# Format code
format:
	poetry run black .

# Run pre-commit to lint and reformat all files
lint:
	poetry check
	@just sort
	@just format

# List tasks
tasks:
	@just --list

# Build project
build: _setup_poetry
	poetry build

# Install program using pipx
install: build
	pipx install ./dist/`ls -t dist | head -n2 | grep whl`

# Uninstall program using pipx
uninstall:
	pipx uninstall addromaji

# Reinstall program using pipx
reinstall: uninstall
	@just install