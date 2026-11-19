# Preuves de réalisation Azure

## 1. Groupe de ressources

Le groupe `rg-retail-intelligence` a été créé dans la région `francecentral`.
Son état de provisioning est `Succeeded`.

## 2. Compte ADLS Gen2

Le compte `retailtp4widad2026` est de type `StorageV2`, avec la réplication
`Standard_LRS`. Le Hierarchical Namespace est activé (`isHnsEnabled: true`).
Le trafic HTTPS est obligatoire et le niveau minimal TLS est `TLS1_2`.

## 3. Système de fichiers et arborescence

Le système de fichiers `retail-intelligence` contient les chemins suivants :

- `bronze/tpcxbb/`
- `silver/promotion/`
- `gold/promotion_summary/`
- `quality/`
- `documentation/`

## 4. Fichiers déposés

- Bronze : `bronze/tpcxbb/promotion.dat`, 46 396 octets ;
- Silver : fichier Parquet de promotion, 23 957 octets ;
- Gold : fichier Parquet `promotion_summary`, 1 214 octets.

## 5. Commandes de reproduction

Les commandes Azure CLI sont exécutées dans l’image Docker officielle :

```powershell
docker volume create azure-cli-config
docker run --rm -it -v azure-cli-config:/root/.azure mcr.microsoft.com/azure-cli az login --use-device-code
```

Les commandes d’architecture utilisent `az group`, `az storage account`,
`az storage fs`, `az storage fs file`, `az role assignment` et `az storage fs access`.

## 6. Distinction réalisé / étudié

Réalisé : groupe de ressources, compte ADLS Gen2, HNS, système de fichiers,
arborescence, dépôt des données, RBAC et ACL.

Étudié mais non déployé : Azure Data Factory, Synapse Analytics, Synapse Studio,
Spark Pools et Power BI.
