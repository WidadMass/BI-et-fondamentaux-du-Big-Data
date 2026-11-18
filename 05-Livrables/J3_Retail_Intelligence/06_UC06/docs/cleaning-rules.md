# Regles de nettoyage

1. Lire le fichier avec le separateur `|` et sans en-tete.
2. Ecarter les lignes dont `field_00` est nul.
3. Supprimer les doublons exacts.
4. Convertir `field_00`, `field_02`, `field_03` et `field_04` en entiers.
5. Convertir `field_05` en decimal `decimal(12,2)`.
6. Produire un rapport avec les lignes source, Silver, Gold, identifiants nuls et doublons.

Ces regles sont volontairement conservatrices car l extrait fourni ne contient pas de ligne d en-tete ni de dictionnaire de colonnes associe.

## Jointure

Aucune jointure n est effectuee dans cette demonstration. Le fichier ne contient pas d en-tete metier permettant de confirmer une cle de jointure avec une autre table. Realiser une jointure sur une cle seulement supposee risquerait de multiplier ou de perdre des lignes. Une jointure sera ajoutee uniquement apres validation du dictionnaire de donnees et verification de l unicite des cles des deux cotes.

## Valeurs atypiques

Les valeurs atypiques ne sont pas supprimees automatiquement. Sans regle metier validee, une valeur extreme peut etre une observation reelle. Elles doivent etre signalees, analysees et seulement corrigees ou exclues avec une justification documentee.
