# Makefile for building RPMs from a local project directory

# Define the RPM build directories
BUILD_DIRS = SPECS SOURCES BUILD RPMS SRPMS BUILDROOT

# Define the location of the spec file
SPEC_FILE = SPECS/melonDS.spec

# Get the absolute path to the current directory
TOP_DIR = $(shell pwd)
TMP_DIR = $(TOP_DIR)/tmp

# Phony targets aren't actual files
.PHONY: all help scaffold sources build clean

# Default target: build the RPM
all: build

# The scaffold target creates the directory structure
scaffold:
	@echo "Creating RPM build directory structure..."
	@mkdir -p $(BUILD_DIRS)
	@echo "Done."

# The 'sources' target downloads sources locally
sources: scaffold
	@echo "Downloading sources to $(TOP_DIR)/SOURCES..."
	@spectool -g -R --define "_topdir $(TOP_DIR)" $(SPEC_FILE)

# The 'build' target builds the binary and source RPMs
build: sources
	@echo "Building RPMs in $(TOP_DIR)..."
	@mkdir -p $(TMP_DIR)
	@rpmbuild -ba --define "_topdir $(TOP_DIR)" --define "_tmppath $(TMP_DIR)" $(SPEC_FILE)
	@echo "Build complete. Find RPMs in $(TOP_DIR)/RPMS and $(TOP_DIR)/SRPMS."

# The 'clean' target removes build outputs
clean:
	@echo "Cleaning build directories..."
	@rm -rf BUILD BUILDROOT RPMS SRPMS
	@echo "Done."

# The help target explains available commands
help:
	@echo "Available commands:"
	@echo "  make help      - Shows this help message."
	@echo "  make scaffold  - Creates the standard RPM build directories."
	@echo "  make sources   - Downloads source tarballs into the local SOURCES directory."
	@echo "  make build     - Builds the binary and source RPMs (default)."
	@echo "  make clean     - Removes the BUILD, BUILDROOT, RPMS, and SRPMS directories."
