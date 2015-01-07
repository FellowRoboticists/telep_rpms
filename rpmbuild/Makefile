# The makefile to orchestrate the RPM building process
# for telep/ws_server

PROJECT_DIR=projects
BUILD_DIR=build

WS_SERVER_DIR=$(PROJECT_DIR)/ws_server
WS_SERVER_REPO="git@github.com:FellowRoboticists/ws_server.git"
WS_SERVER_BRANCH=master
WS_SERVER_BUILD_DIR=$(BUILD_DIR)/ws_server

TELEP_DIR=$(PROJECT_DIR)/telep
TELEP_REPO="git@github.com:FellowRoboticists/telep.git"
TELEP_BRANCH=master

default: ws_server

$(PROJECT_DIR):
	mkdir -p $(PROJECT_DIR)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

#############################################################################
# Targets for ws_server
#
$(WS_SERVER_DIR): $(PROJECT_DIR)
	if [ ! -d $(WS_SERVER_DIR) ]; then cd $(PROJECT_DIR); git clone $(WS_SERVER_REPO); fi

ws_server: $(WS_SERVER_DIR)
	cd $(WS_SERVER_DIR); git fetch origin $(WS_SERVER_BRANCH):$(WS_SERVER_BRANCH); git checkout $(WS_SERVER_BRANCH)

$(WS_SERVER_BUILD_DIR): $(BUILD_DIR)
	mkdir -p $(WS_SERVER_BUILD_DIR)

ws_server.tar.gz: ws_server $(WS_SERVER_BUILD_DIR)
	rm -fr $(WS_SERVER_BUILD_DIR)/*
	tar --exclude-vcs --directory $(PROJECT_DIR) -zcf $(WS_SERVER_BUILD_DIR)/ws_server.tar.gz ws_server

ws_server-$(WS_SERVER_BRANCH).tar.bz2: telep ws_server.tar.gz
	mkdir -p $(WS_SERVER_BUILD_DIR)/ws_server-$(WS_SERVER_BRANCH)/init
	mkdir -p $(WS_SERVER_BUILD_DIR)/ws_server-$(WS_SERVER_BRANCH)/conf
	cp $(TELEP_DIR)/scripts/ws_server $(WS_SERVER_BUILD_DIR)/ws_server-$(WS_SERVER_BRANCH)/init
	cp $(TELEP_DIR)/config/ws_server $(WS_SERVER_BUILD_DIR)/ws_server-$(WS_SERVER_BRANCH)/conf
	cp $(WS_SERVER_BUILD_DIR)/ws_server.tar.gz $(WS_SERVER_BUILD_DIR)/ws_server-$(WS_SERVER_BRANCH)
	tar --directory $(WS_SERVER_BUILD_DIR) -jcf $(WS_SERVER_BUILD_DIR)/ws_server-$(WS_SERVER_BRANCH).tar.bz2 ws_server-$(WS_SERVER_BRANCH)
	cp $(WS_SERVER_BUILD_DIR)/ws_server-$(WS_SERVER_BRANCH).tar.bz2 SOURCES

ws_server_rpm: ws_server-$(WS_SERVER_BRANCH).tar.bz2
	rpmbuild -ba SPECS/ws_server.spec

#############################################################################
# Targets for telep
#
$(TELEP_DIR): $(PROJECT_DIR)
	if [ ! -d $(TELEP_DIR) ]; then cd $(PROJECT_DIR); git clone $(TELEP_REPO); fi

telep: $(TELEP_DIR)
	cd $(TELEP_DIR); git fetch origin $(TELEP_BRANCH):$(TELEP_BRANCH); git checkout $(TELEP_BRANCH)
