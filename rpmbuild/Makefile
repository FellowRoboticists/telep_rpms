# The makefile to orchestrate the RPM building process
# for telep/ws_server

PROJECT_DIR = projects
BUILD_DIR = $(PWD)/build

# This is the command to prep a git repo for use.
PULL_REPO = $(PWD)/pull-repo.sh

WS_SERVER_DIR = $(PROJECT_DIR)/ws_server
WS_SERVER_REPO = "git@github.com:FellowRoboticists/ws_server.git"
WS_SERVER_BRANCH = master
WS_SERVER_BUILD_DIR = $(BUILD_DIR)/ws_server

TELEP_DIR = $(PROJECT_DIR)/telep
TELEP_REPO = "git@github.com:FellowRoboticists/telep.git"
TELEP_BRANCH = master
TELEP_BUILD_DIR=$(BUILD_DIR)/telep

TELEP_CREDENTIALS_VERSION=0.1.0

# Always force the project directories to have the recipe run. Remember
# these projects must have the correct version of their code checked out.
.PHONY : $(WS_SERVER_DIR) $(TELEP_DIR)

REBAR_DIR = $(PWD)/third-party/rebar
REBAR=$(REBAR_DIR)/rebar

default: ws_server

$(PROJECT_DIR):
	mkdir -p $(PROJECT_DIR)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

#############################################################################
# Targets for ws_server
#
$(WS_SERVER_DIR): $(PROJECT_DIR)
	$(PULL_REPO) -b $(WS_SERVER_BRANCH) -r $(WS_SERVER_REPO) $(WS_SERVER_DIR)

$(WS_SERVER_BUILD_DIR): $(BUILD_DIR)
	mkdir -p $(WS_SERVER_BUILD_DIR)

ws_server.tar.gz: $(WS_SERVER_DIR) $(WS_SERVER_BUILD_DIR)
	rm -fr $(WS_SERVER_BUILD_DIR)/*
	tar --exclude-vcs --directory $(PROJECT_DIR) -zcf $(WS_SERVER_BUILD_DIR)/ws_server.tar.gz ws_server

ws_server-$(WS_SERVER_BRANCH).tar.bz2: $(TELEP_DIR) ws_server.tar.gz
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
# Targets for rebar
#
$(REBAR):
	cd $(REBAR_DIR); ./bootstrap

#############################################################################
# Targets for telep
#
$(TELEP_DIR): $(PROJECT_DIR)
	$(PULL_REPO) -b $(TELEP_BRANCH) -r $(TELEP_REPO) -s $(TELEP_DIR)

$(TELEP_DIR)/third-party/ranch/ebin/ranch.beam:
	cd $(TELEP_DIR)/third-party/ranch; make

$(TELEP_DIR)/third-party/syslog/ebin/syslog.beam:
	cd $(TELEP_DIR)/third-party/syslog; ./rebar compile

$(TELEP_DIR)/third-party/beanstalk/ebin/beanstalk.beam:
	cd $(TELEP_DIR)/third-party/beanstalk; make

$(TELEP_DIR)/third-party/bson/ebin/bson.beam:
	cd $(TELEP_DIR)/third-party/bson; erlc -o ebin -I include src/*.erl

$(TELEP_DIR)/third-party/mongodb/ebin/mongodb.beam:
	cd $(TELEP_DIR)/third-party/mongodb; erlc -o ebin -I include -I .. src/*.erl

$(TELEP_DIR)/third-party/mustache/ebin/mustache.beam:
	cd $(TELEP_DIR)/third-party/mustache; make

telep: $(TELEP_DIR) \
	third-party/rebar \
	$(TELEP_DIR)/third-party/ranch/ebin/ranch.beam \
	$(TELEP_DIR)/third-party/syslog/ebin/syslog.beam \
	$(TELEP_DIR)/third-party/beanstalk/ebin/beanstalk.beam \
	$(TELEP_DIR)/third-party/bson/ebin/bson.beam \
	$(TELEP_DIR)/third-party/mongodb/ebin/mongodb.beam \
	$(TELEP_DIR)/third-party/mustache/ebin/mustache.beam

	cd $(TELEP_DIR); $(REBAR) compile; $(REBAR) generate

$(TELEP_BUILD_DIR): $(BUILD_DIR)
	mkdir -p $(TELEP_BUILD_DIR)

telep-$(TELEP_BRANCH).tar.bz2: telep
	mkdir -p $(TELEP_BUILD_DIR)/telep-$(TELEP_BRANCH)/conf
	cd $(TELEP_DIR); \
		cp -R rel/telep $(TELEP_BUILD_DIR)/telep-$(TELEP_BRANCH); \
		cp -R www $(TELEP_BUILD_DIR)/telep-$(TELEP_BRANCH); \
		cp 8080.conf $(TELEP_BUILD_DIR)/telep-$(TELEP_BRANCH)/conf/telep.conf
	tar --directory $(TELEP_BUILD_DIR) -jcf $(TELEP_BUILD_DIR)/telep-$(TELEP_BRANCH).tar.bz2 telep-$(TELEP_BRANCH)
	cp $(TELEP_BUILD_DIR)/telep-$(TELEP_BRANCH).tar.bz2 SOURCES

telep_rpm: telep-$(TELEP_BRANCH).tar.bz2
	rpmbuild -ba SPECS/telep.spec

telep_credentials_rpm:
	rpmbuild -ba SPECS/telep-credentials.spec
