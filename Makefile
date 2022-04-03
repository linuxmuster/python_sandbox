#!/usr/bin/make
# This is the sophomorix Makefile
# for Debian packaging (make DESTDIR=/root/sophomorix)
DESTDIR=

# Debian
#====================================

# Homes
#HOME=$(DESTDIR)/home

# Developement
#USERROOT=$(DESTDIR)/root

# Python Module
PYTHON_MODULE_DIR=$(DESTDIR)/usr/lib/python3/dist-packages/
PYTHON_BINARY_DIR=$(DESTDIR)/usr/sbin/


help:
	@echo ' '
	@echo 'Most common options of this Makefile:'
	@echo '-------------------------------------'
	@echo ' '
	@echo '   make help'
	@echo '      show this help'
	@echo ' '
	@echo '   sudo make install'
	@echo '      install module and script'
	@echo ' '
	@echo '   sudo make uninstall'
	@echo '      uninstall module and script'
	@echo ' '

install:
	@install -d -m755 -oroot -groot $(PYTHON_MODULE_DIR)
	@install -m644 -oroot -groot ./module/python_sandbox_module.py $(PYTHON_MODULE_DIR)
	@install -m755 -oroot -groot ./script/python_sandbox $(PYTHON_BINARY_DIR)

uninstall:
	@rm $(PYTHON_MODULE_DIR)python_sandbox_module.py
	@rm $(PYTHON_BINARY_DIR)python_sandbox
