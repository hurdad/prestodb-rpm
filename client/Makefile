# Presto CLI
SHELL := /bin/bash 
version = 0.159
name = presto-cli
full_name = $(name)-$(version)
download_url = "http://search.maven.org/remotecontent?filepath=com/facebook/presto/$(name)-cli/$(version)/$(name)-cli-$(version)-executable.jar"

all: rpm

clean:
	rm -rf rpmbuild
	rm -rf tmp

mkdir: clean
	mkdir -p rpmbuild
	mkdir -p rpmbuild/BUILD
	mkdir -p rpmbuild/BUILDROOT
	mkdir -p rpmbuild/RPMS
	mkdir -p rpmbuild/SOURCES
	mkdir -p rpmbuild/SRPMS
	mkdir -p tmp

download: mkdir
	cd tmp; \
	curl -L -o presto $(download_url); \
	chmod a+x presto

rpm: download
	rpmbuild $(RPM_OPTS) \
	  --define "_topdir %(pwd)" \
	  --define "_builddir %{_topdir}/rpmbuild/BUILD" \
	  --define "_buildrootdir %{_topdir}/rpmbuild/BUILDROOT" \
	  --define "_rpmdir %{_topdir}/rpmbuild/RPMS" \
	  --define "_srcrpmdir %{_topdir}/rpmbuild/SRPMS" \
	  --define "_specdir %{_topdir}" \
	  --define "_sourcedir  %{_topdir}/rpmbuild/SOURCES" \
	  --define "PRESTO_VERSION $(version)" \
	  -ba $(name).spec
