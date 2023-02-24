# Sets the scope so that multiple users can use the same org
ifndef EDGE_OWNER
$(error EDGE_OWNER is not set. Set to com or your two-letter initials e.g: export EDGE_OWNER=sg.edge )
endif

# Lets you manage and deploy different group of code across dev, demo, test, prod
ifndef EDGE_DEPLOY
$(error EDGE_DEPLOY is not set. Set to either dev, demo, test, prod etc. e.g: export EDGE_DEPLOY=example.visual )
endif

ifndef HZN_ORG_ID
$(error HZN_ORG_ID is not set. export HZN_ORG_ID=<org-id>))
endif

ifndef HZN_EXCHANGE_USER_AUTH
$(error HZN_EXCHANGE_USER_AUTH is not set. export HZN_EXCHANGE_USER_AUTH=iamapikey:<your-iamapikey> )
endif

ifndef CR_IBM_HOST
$(error CR_IBM_HOST is not set. export CR_IBM_HOST=<us.icr.io> )
endif

ifndef CR_IBM_HOST_NAMESPACE
$(error CR_IBM_HOST_NAMESPACE is not set. export CR_IBM_HOST_NAMESPACE=<ieam-dev> )
endif

ifndef CR_IBM_USERNAME
$(error CR_IBM_USERNAME is not set. export CR_IBM_USERNAME=<iamapikey> )
endif

ifndef CR_APP_API_KEY_RO_PULL
$(error CR_APP_API_KEY_RO_PULL is not set. export CR_APP_API_KEY_RO_PULL=<cr-app-api-key-ro-pull> )
endif

ifndef CR_APP_API_KEY_RW_PUSH
$(error CR_APP_API_KEY_RW_PUSH is not set. export CR_APP_API_KEY_RW_PUSH=<cr-app-api-key-rw-push> )
endif

ifndef APP_BIND_HORIZON_DIR
$(error APP_BIND_HORIZON_DIR is not set. export APP_BIND_HORIZON_DIR=/var/local/horizon )
endif
