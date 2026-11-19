# Analyses métier UC08

Les données sont synthétiques et les colonnes ne disposent pas d’un dictionnaire
métier complet. Les constats ci-dessous sont donc descriptifs et techniques.

## Analyse 1 – Répartition des promotions par catégorie

**Question :** quelles valeurs de `field_07` concentrent le plus d’observations ?

**Données utilisées :** Gold `gold/promotion_summary`, issu du Silver UC06.

**Méthode :** classement décroissant de `promotion_count` par valeur de `field_07`.

**Résultats :**

- `able` : 37 lignes ;
- `anti` et `ation` : 36 lignes chacune ;
- `pri` : 35 lignes ;
- `bar` et `cally` : 33 lignes chacune ;
- `ought` : 32 lignes ;
- `eing` : 31 lignes ;
- `ese` : 27 lignes.

**Interprétation :** la catégorie `able` est la plus fréquente dans cet extrait,
tandis que `ese` est la moins fréquente. Les écarts restent limités entre les
catégories.

**Limite :** `field_07` est un nom technique ; il n’est pas possible d’identifier
un produit, une campagne ou une famille commerciale réelle.

**Recommandation :** valider le dictionnaire métier de `field_07` avant de prendre
une décision commerciale à partir de cette répartition.

## Analyse 2 – Distribution de field_05

**Question :** comment les valeurs de `field_05` sont-elles distribuées dans le
Silver ?

**Données utilisées :** Silver `silver/promotion`, 300 lignes.

**Méthode :** calcul du minimum, du maximum, de la moyenne et de la médiane, puis
production d’un histogramme.

**Résultats :**

| Indicateur | Valeur |
|---|---:|
| Minimum | 12,63 |
| Maximum | 995,16 |
| Moyenne | 521,23 |
| Médiane | 559,51 |

**Interprétation :** les observations couvrent une plage large. La médiane est
supérieure à la moyenne, ce qui suggère une distribution influencée par des valeurs
plus faibles, sans permettre à elle seule d’identifier une cause.

**Limite :** l’unité et la signification métier de `field_05` ne sont pas connues.
Il ne faut pas le présenter comme un prix, un coût ou un montant de vente.

**Recommandation :** faire qualifier `field_05` par le métier avant toute
interprétation financière ou opérationnelle.

## Visualisations

- `analytics/visualizations/promotions_par_categorie.png` : comparaison des
  fréquences par catégorie technique ;
- `analytics/visualizations/distribution_field_05.png` : histogramme de la mesure
  technique `field_05`.

Les deux graphiques sont générés par `scripts/tp4_uc08.py` et sont reproductibles.
