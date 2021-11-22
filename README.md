:warning: Archived!

# Autonity-init
This Docker image was used for initialisation Autonity in a Kubernetes cluster and is used alongside the below Helm charts:
* [autonity](https://github.com/clearmatics/charts-ose-helm3/tree/master/stable/autonity)

This process has now been replaced by extening the Helm chart to manage the keys within GitHub Secrets, or manually.

## Description
1. If the `keystore` does not exist:
   1. `autonity account import` (will get the priv_key and password from k8s secrets)
1. If the `blockchain` does not exist and the flag `--account-import-only` is NOT used:
   1. `autonity init` (will get the `genesis.json` from k8s configmaps)

## Usage
Docker build
```shell script
docker build -t autonity-init .
```

Docker run
```shell script
docker run -ti --rm -v $(pwd)/tmp:/autonity autonity-init --debug=true --account-import-only=true
```
