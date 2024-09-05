BINDIR = /usr/local/bin
BINFILE = $(BINDIR)/pkg
VENVDIR = $(HOME)/.local/venv/unipkg
CONFIGDIR = $(HOME)/.config/unipkg
CONFIGFILE = config.toml

.PHONY: install no_sudo install_py create_venv install_bin install_cfg uninstall clean

install: no_sudo create_venv install_py install_bin install_cfg

dist:
	python setup.py sdist bdist_wheel

no_sudo:
	@if [ -n "$$SUDO_USER" ]; then \
		echo "Do not run with sudo."; \
		exit 1; \
	fi

create_venv:
	@if [ ! -d "$(VENVDIR)" ]; then \
		python -m venv $(VENVDIR) 1> /dev/null; \
		echo "A new virtualenv was created at $(VENVDIR)"; \
	fi

install_py:
	@$(VENVDIR)/bin/pip install -e . 1> /dev/null

install_bin:
	@sudo sh -c "\
		install -d $(BINDIR); \
		echo '#!$(VENVDIR)/bin/python' > $(BINFILE); \
		echo 'import unipkg' >> $(BINFILE); \
		echo 'unipkg.run()' >> $(BINFILE); \
		chmod +x $(BINFILE)"
	@echo "Executable created at $(BINFILE)"

install_cfg:
	@install -d $(CONFIGDIR)
	@install -m 644 $(CONFIGFILE) $(CONFIGDIR)/$(CONFIGFILE)
	@echo "Config file created at $(CONFIGDIR)/$(CONFIGFILE)"

uninstall:
	sudo rm -f $(BINFILE)
	rm -rf $(CONFIGDIR)
	rm -rf $(VENVDIR)

clean:
	@rm -rf ./dist/ ./build/ ./*.egg-info
	@find . -name '*.pyc' -delete
	@find . -name '__pycache__' -delete