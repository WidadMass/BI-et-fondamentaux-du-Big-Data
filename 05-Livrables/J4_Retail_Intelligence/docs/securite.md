# Sécurité et droits d’accès

## RBAC Azure

Le compte `w.masghar@ecole-ipssi.net` possède le rôle **Storage Blob Data
Contributor**, limité au compte de stockage `retailtp4widad2026`.

Cette portée permet de manipuler les données du compte sans attribuer le rôle au
niveau de tout l’abonnement.

## ACL ADLS Gen2

Les zones Bronze, Silver et Gold utilisent l’ACL suivante :

```text
user::rwx,group::r-x,other::---
```

| Zone | Propriétaire | Groupe | Autres |
|---|---|---|---|
| Bronze | rwx | r-x | aucun accès |
| Silver | rwx | r-x | aucun accès |
| Gold | rwx | r-x | aucun accès |

## Matrice fonctionnelle cible

| Profil | Bronze | Silver | Gold |
|---|---|---|---|
| Équipe ingestion | Écriture contrôlée | Lecture limitée | Aucun accès par défaut |
| Data engineering | Lecture/écriture | Lecture/écriture | Écriture contrôlée |
| Analyste métier | Aucun accès par défaut | Lecture selon besoin | Lecture |
| Administrateur | Gestion selon habilitation | Gestion selon habilitation | Gestion selon habilitation |

RBAC porte sur les rôles Azure et la portée des ressources. Les ACL affinent les
droits sur les chemins ADLS. Les secrets et clés ne doivent pas être déposés dans
Git.
