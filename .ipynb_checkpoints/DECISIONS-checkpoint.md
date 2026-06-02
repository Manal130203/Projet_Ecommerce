\# Journal de Nettoyage des Données





&#x20;**1. Suppression des doublons**



Les lignes dupliquées ont été supprimées afin d’éviter

la duplication artificielle des transactions.



Impact :



\* Nombre de doublons supprimés : **5268**



\---



&#x20;**2. Gestion des valeurs manquantes**



Les transactions sans CustomerID ont été supprimées

car elles ne permettent pas les analyses RFM et CLV.



Impact :



Nombre de lignes supprimées :**135080**

\---



**3. Conversion des dates**



La colonne InvoiceDate a été convertie en format datetime

pour permettre les analyses temporelles.



\---



**4. Gestion des prix invalides**



Les lignes avec UnitPrice <= 0 ont été supprimées

car elles représentent des anomalies ou ajustements comptables.



\---



**5. Gestion des retours**



Les transactions avec Quantity négative ont été séparées

des ventes normales car elles représentent des retours clients.



**---**

**6. Suppression des codes spéciaux**



Les codes POST, D, C2, M et BANK CHARGES ont été exclus

car ils ne représentent pas des produits réels.



\---



**7. Impact global du nettoyage**



\* Nombre initial de lignes : 541909

\* Nombre final de lignes :**399691**

\* Nombre total supprimé :142218

\* Pourcentage supprimé : 26.24 %



**Le dataset Shipping semble :**

**✅ déjà très propre**

**✅ sans nulls**

**✅ bien typé**



