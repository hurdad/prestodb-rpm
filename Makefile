# Master MakeFile

SUBDIRS = client server jdbc

all: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@

.PHONY: $(SUBDIRS)
