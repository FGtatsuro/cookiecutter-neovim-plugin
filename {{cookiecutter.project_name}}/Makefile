REMOTE_PLUGIN_DIR = rplugin/python3/{{cookiecutter.plugin_prefix}}/

.PHONY: lint format

# This target always return 0 as exit code.
# If you want to fail this target(ex. CI), you must create a wrapper script like:
# 	make lint 2>&1 | grep Error; if [ $? -eq 0 ]; then exit 1; fi
lint:
	-flake8 $(REMOTE_PLUGIN_DIR)
	-pydocstyle $(REMOTE_PLUGIN_DIR)
	-mypy $(REMOTE_PLUGIN_DIR)

format:
	autopep8 --in-place --aggressive --recursive $(REMOTE_PLUGIN_DIR)
