BINDIR = /usr/local/bin
BINFILE = $(BINDIR)/pkg
VENVDIR = $(HOME)/.local/venv/unipkg
CONFIGDIR = $(HOME)/.config/unipkg
CONFIGFILE = config.toml

.PHONY: install no_sudo install_py install_bin install_cfg uninstall clean

install: no_sudo install_py install_bin install_cfg

no_sudo:
	@if [ -n "$$SUDO_USER" ]; then \
		echo "Do not run with sudo."; \
		exit 1; \
	fi

create_venv:
	@if [ ! -d "$(VENVDIR)" ]; then \
		python -m venv $(VENVDIR); \
		@echo "source $(VENVDIR)/bin/activate" > .venv
	fi

install_py:
	@if [ ! -d "$(VENVDIR)" ]; then \
		python -m venv $(VENVDIR); \
	fi
	@$(VENVDIR)/bin/pip install -e .

install_bin:
	@sudo sh -c "\
		install -d $(BINDIR); \
		echo '#!$(VENVDIR)/bin/python' > $(BINFILE); \
		echo 'import unipkg' >> $(BINFILE); \
		echo 'unipkg.run()' >> $(BINFILE); \
		chmod +x $(BINFILE)"

install_cfg:
	@install -d $(CONFIGDIR)
	@install -m 644 $(CONFIGFILE) $(CONFIGDIR)/$(CONFIGFILE)

uninstall:
	@sudo rm -f $(BINFILE)
	@rm -rf $(CONFIGDIR)
	@rm -rf $(VENVDIR)

clean:
	@rm -rf ./dist/ ./build/ ./*.egg-info
	@find . -name '*.pyc' -delete
	@find . -name '__pycache__' -delete