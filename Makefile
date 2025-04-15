ifeq ($(OS),Windows_NT)
    DETECTED_OS := windows
else
    UNAME_S := $(shell uname -s)
    ifeq ($(UNAME_S),Darwin)
        DETECTED_OS := mac
    else ifeq ($(UNAME_S),Linux)
        DETECTED_OS := ubuntu
    else
        DETECTED_OS := $(UNAME_S)
    endif
endif

.PHONY: installtkinter
installtkinter:
ifeq ($(DETECTED_OS),mac)
	@echo "REMEMBER TO RUN source .venv/bin/activate beforehand."
	brew install python-tk
else ifeq ($(DETECTED_OS),windows)
	@echo "REMEMBER TO RUN .venv\\Scripts\\activate beforehand."
	@echo "Tkinter is usually bundled with Python on Windows."
	@echo "To verify it's working, run: python -m tkinter"
	@echo "If it fails, reinstall Python from https://python.org and make sure to include Tcl/Tk support."
else
	@echo "REMEMBER TO RUN source .venv/bin/activate beforehand."
	sudo apt-get install python3-tk
endif

.PHONY: setpermissions
setpermissions:
	@echo "Setting permissions."
	chmod -R u=rwx,g=,o= .


.PHONY: runmain
runmain:
	@echo "Running main..."
	./main.sh


.PHONY: runtests
runtests:
	@echo "Running tests..."
	./test.sh
