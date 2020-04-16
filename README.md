# Autonity-init
This container used for initialisation autonity in kubernetes cluster  
* [autonity-network](https://github.com/clearmatics/charts-ose/tree/master/stable/autonity-network)  
* [autohity](https://github.com/clearmatics/charts-ose/tree/master/stable/autonity)

# It will:

1. if `keystore` not exist:  
   1. `autonity account import ` (get priv_key and password from k8s secret)
1. if `blockchain` not exist and `NOT` `--account-import-only`:
   1. `autonity init` (get `genesis.json` from k8s configmap)

# Docker usage

Docker build
```shell script
docker build -t autonity-init .
```
Docker run
```shell script
docker run -ti --rm -v $(pwd)/tmp:/autonity autonity-init --debug=true --account-import-only=true
```
