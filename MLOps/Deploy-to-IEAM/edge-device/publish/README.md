### Development of containers, services, policies and defintion files

Using a shared IEAM environment to Build and Publish services

#### Automated Steps

Start with reviewing Makefile for targets.

MUST Setup ENVIRONMENT variables.
```
export EDGE_OWNER=<arbitrary-values-to-organize-resources> e.g: sg.edge 
export EDGE_DEPLOY=<arbitrary-values-to-organize-resources> e.g: watson.nlp
export HZN_ORG_ID=<hzn-org-id>
export HZN_EXCHANGE_USER_AUTH=iamapikey:<auth-key>
export APP_BIND_HORIZON_DIR=/var/local/horizon

export CR_IBM_HOST=<container-registry-host> 
export CR_IBM_USERNAME=<container-registry-username>
export CR_IBM_HOST_NAMESPACE=<container-registry-namespace>
export CR_APP_API_KEY_RO_PULL=<container-registry-read-only-secret-to-pull>
export CR_APP_API_KEY_RW_PUSH=<container-registry-read-write-secret-to-push>
```

#### Build, push and publish all resources 
```
make
```

#### Register node and test


