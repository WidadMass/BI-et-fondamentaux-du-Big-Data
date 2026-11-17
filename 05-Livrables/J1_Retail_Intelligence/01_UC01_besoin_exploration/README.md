# UC-01 Besoin métier et exploration

Ce dossier traite le socle UC-01 du TP Retail Intelligence.

**Travail individuel — Widad MASGHAR**

## Livrables

- `UC01_cadrage_metier.pdf`
- `UC01_questions_decisionnelles.pdf`
- `UC01_dictionnaire_KPI.xlsx`
- `UC01_inventaire_sources.xlsx`
- `UC01_qualification_donnees.pdf`
- `UC01_limites_et_hypotheses.pdf`
- `UC01_preuves/`

## Résultats principaux

- 23 fichiers principaux et 11 fichiers de rafraîchissement ont été inspectés.
- Les fichiers principaux représentent 1 024 447 801 octets et 33 907 536 lignes.
- Aucun écart de nombre de champs n'a été détecté.
- Les 35 relations principales contrôlées ne présentent aucune référence orpheline lorsque les référentiels `data` et `data_refresh` sont pris en compte.
- Les couples ticket-produit et commande-produit ne sont pas uniques dans les tables de ventes et de retours. Un identifiant de ligne devra être créé à l'ingestion.
- Les fichiers réels `web_sales` et `web_clickstreams` ne contiennent pas respectivement `ws_sk` et `wcs_click_sk`.

## Traçabilité

Les noms de colonnes sont rapprochés de l'annexe de chargement de la spécification TPCx-BB version 1.7.0. La version exacte du kit de données reste à confirmer séparément.
