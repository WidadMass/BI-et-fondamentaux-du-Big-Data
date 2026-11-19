# Dictionnaire des KPI calculables

Les champs de la source sont techniques (`field_00` à `field_18`) et ne sont pas
reliés à un dictionnaire métier de ventes. Les indicateurs ci-dessous sont donc des
KPI analytiques calculables, avec leurs limites explicitement documentées.

| KPI | Définition | Formule | Champs | Grain | Unité | Limite |
|---|---|---|---|---|---|---|
| Volume Silver | Nombre d’observations conservées après nettoyage | `COUNT(*)` | Silver | Jeu de données | lignes | Ne représente ni ventes ni transactions |
| Nombre de catégories | Nombre de catégories distinctes présentes dans le Gold | `COUNT(DISTINCT field_07)` | Gold `field_07` | Jeu de données | catégories | `field_07` n’a pas de signification métier validée |
| Promotions par catégorie | Nombre d’observations regroupées pour chaque catégorie | `COUNT(*) GROUP BY field_07` | Gold `field_07`, `promotion_count` | catégorie | lignes | Mesure une fréquence, pas une performance commerciale |
| Moyenne de field_05 | Moyenne de la mesure technique `field_05` | `AVG(field_05)` | Silver `field_05` | Jeu de données | unité inconnue | L’unité et le sens métier ne sont pas fournis |

## Valeurs obtenues

- Volume Silver : 300 lignes ;
- Nombre de catégories Gold : 9 ;
- Total des observations regroupées dans le Gold : 300 lignes ;
- Moyenne de `field_05` : 521,23.

Les KPI commerciaux du dictionnaire UC01, comme le montant des ventes, la marge ou
le panier moyen, ne sont pas calculés car les champs nécessaires ne sont pas
identifiables dans cet extrait.
