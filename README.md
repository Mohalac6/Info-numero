# Info-numero

Cet outil Python permet d'extraire des informations détaillées sur un numéro de téléphone, telles que l'opérateur mobile, le pays, la région et les fuseaux horaires associés. Il utilise la bibliothèque phonenumbers pour analyser les numéros et extraire les données.

## Fonctionnalités

**Détection de l'opérateur** : Identifiez l'opérateur téléphonique d'un numéro.
**Géolocalisation** : Déterminez le pays et la région associés à un numéro.
**Fuseaux horaires** : Obtenez les fuseaux horaires liés au numéro de téléphone.

## Prérequis

- Python 3.x
- Les bibliothèques Python suivantes sont requises :
    - phonenumbers
    - dataclasses (incluse par défaut dans Python 3.7+)
 
Vous pouvez installer la bibliothèque phonenumbers en exécutant :
```
pip install phonenumbers
```

## Utilisation

Le script contient deux fonctions principales :

1. about_phone(number: str, name: bool = False, country: bool = False, region: bool = False, tz: bool = False) -> PhoneNumberInfo :
   - Récupère des informations détaillées sur un numéro de téléphone en fonction des paramètres sélectionnés.

2. format_phone_info(info: PhoneNumberInfo) -> str :
   - Formatte les informations du numéro de téléphone en une chaîne lisible.
  
### Exemple
Pour obtenir des informations sur un numéro de téléphone, vous pouvez utiliser le code suivant :
```
from votre_module import about_phone, format_phone_info

number = "+33 6 19 19 28 50"
info = about_phone(number, name=True, country=True, region=True, tz=True)
formatted_info = format_phone_info(info)
print(formatted_info)
```
Cela affichera quelque chose comme :
```
Operator: SFR                       Country: France                     Region: France
Timezones: Europe/Paris
```

### Paramètres de **about_phone**
- **number (str)** : Le numéro de téléphone au format international (par ex., +213549405183).
- **name (bool)** : Mettez à True pour inclure les informations sur l'opérateur téléphonique.
- **country (bool)** : Mettez à True pour inclure les informations sur le pays.
- **region (bool)** : Mettez à True pour inclure les informations sur la région spécifique.
- **tz (bool)** : Mettez à True pour inclure les fuseaux horaires associés.

### Valeur de retour
La fonction about_phone retourne un objet PhoneNumberInfo contenant les attributs suivants :

- **operator (Optional[str])** : Le nom de l'opérateur mobile.
- **country (Optional[str])** : Le pays associé au numéro.
- **region (Optional[str])** : La région ou localité spécifique du numéro.
- **timezones (Optional[List[str]])** : Les fuseaux horaires associés au numéro.


### Gestion des erreurs
La fonction lève une exception ValueError dans les cas suivants :

- Aucun numéro de téléphone n'est fourni.
- Aucune information (opérateur, pays, région ou fuseau horaire) n'est demandée.

## Exécution du script

Pour exécuter directement le script, utilisez :
```
Python votre_script.py
```
Cela analysera le numéro de téléphone défini dans le script et affichera les informations formatées.

## Licence

Ce projet est open-source et disponible sous la Licence MIT.

## Remarques

- Cet outil nécessite que le numéro de téléphone soit fourni au format international.
- Assurez-vous que la bibliothèque phonenumbers est à jour pour une meilleure couverture et précision
