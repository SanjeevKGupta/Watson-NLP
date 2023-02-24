#
# Makefile: WNLP
#

# Checks required environment variables
-include ../env.check.mk

all: publish-runtime publish-client deploy-policy

publish-runtime:
	make -C src/runtime build-image
	make -C src/runtime push-image
	make -C src/runtime publish-service

publish-client:
	make -C src/client build-image
	make -C src/client push-image
	make -C src/client publish-service

deploy-policy:
	make -C src/client deploy-policy
