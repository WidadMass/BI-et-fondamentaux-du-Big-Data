# Stratégie incrémentale et évolution du schéma

## Scénario démontré

1. Les 300 lignes Silver sont écrites dans une table Delta : version 0.
2. Un nouveau lot `incremental-001` apporte une ligne identifiée `DELTA-DEMO-001`.
3. Ce lot contient une nouvelle colonne `source_system`.
4. L’écriture utilise `mergeSchema=true`, ce qui produit une nouvelle version de la table.
5. La version courante contient 301 lignes, tandis que la lecture `versionAsOf=0` restitue toujours les 300 lignes initiales.

## Stratégie recommandée en production

- attribuer à chaque lot un `batch_id` et une date d’ingestion ;
- stocker un point de reprise fiable ;
- utiliser `MERGE` sur une clé métier stable pour rendre les reprises idempotentes ;
- valider le schéma avant toute évolution automatique ;
- surveiller l’historique et conserver les versions selon une politique de rétention ;
- compacter périodiquement les petits fichiers.

## Garanties et limites

Delta apporte des transactions ACID, un instantané cohérent, l’historique et le time travel. Ces garanties ne corrigent pas les problèmes de qualité métier : une mauvaise clé, un doublon logique ou une donnée erronée restent possibles. La performance dépend aussi du partitionnement, de la taille des fichiers, du moteur utilisé et de la maintenance de la table.

