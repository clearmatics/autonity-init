# Autonity-init
This container used for initialisation autonity in kubernetes cluster
[Autonity-helm](https://github.com/clearmatics/autonity-helm)

# It will:

1. if `keystore` not exist:  
   1. `autonity account import ` (get priv_key and password from k8s secret
   1. if `validator`:  generate `node.key`
1. if `blockchain` not exist:
   1. `autonity init` (get `genesis.json` from k8s configmap)
 