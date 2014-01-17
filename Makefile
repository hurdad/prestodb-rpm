# Master MakeFile

SUBDIRS = client server discovery jdbc

all: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@

.PHONY: $(SUBDIRS)
