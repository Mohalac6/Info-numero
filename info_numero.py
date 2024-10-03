import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class PhoneNumberInfo:
    operator: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    timezones: Optional[List[str]] = None

def about_phone(number: str, name: bool = False, country: bool = False, region: bool = False, tz: bool = False) -> PhoneNumberInfo:
    """
    Retourne les informations détaillées sur un numéro de téléphone.

    Args:
        number (str): Numéro de téléphone au format international (ex: "+213549385183").
        name (bool): Si True, retourne l'opérateur téléphonique.
        country (bool): Si True, retourne le pays d'origine.
        region (bool): Si True, retourne la région spécifique du numéro.
        tz (bool): Si True, retourne la zone horaire associée au numéro.

    Returns:
        PhoneNumberInfo: Un objet contenant les informations du numéro de téléphone.
    
    Raises:
        ValueError: Si aucun numéro n'est fourni ou si aucun détail n'est demandé.
    """
    if not number:
        raise ValueError("Le numéro doit être fourni.")

    try:
        # Analyser le numéro
        parsed_number = phonenumbers.parse(number)

        # Extraire les informations en fonction des options
        operator = carrier.name_for_number(parsed_number, "fr") if name else None
        country_ = geocoder.country_name_for_number(parsed_number, "fr") if country else None
        region_ = geocoder.description_for_number(parsed_number, "fr") if region else None
        timezones_ = timezone.time_zones_for_number(parsed_number) if tz else None

        # Vérifier qu'au moins une information est demandée
        if not (operator or country_ or region_ or timezones_):
            raise ValueError("Au moins une option doit être activée (name, country, region ou tz).")

        # Retourner les informations sous forme d'un objet structuré
        return PhoneNumberInfo(operator=operator, country=country_, region=region_, timezones=timezones_)

    except phonenumbers.NumberParseException as e:
        raise ValueError(f"Erreur lors de l'analyse du numéro: {e}")

def format_phone_info(info: PhoneNumberInfo) -> str:
    """
    Formatte les informations du numéro de téléphone sous forme de texte lisible.

    Args:
        info (PhoneNumberInfo): Objet contenant les détails du numéro.

    Returns:
        str: Chaîne de texte formatée.
    """
    details = []
    if info.operator:
        details.append(f"Operator: {info.operator}")
    if info.country:
        details.append(f"Country: {info.country}")
    if info.region:
        details.append(f"Region: {info.region}")
    if info.timezones:
        details.append(f"Timezones: {', '.join(info.timezones)}")

    return "\n".join(details)

if __name__ == '__main__':
    number = ""
    try:
        info = about_phone(number, name=True, country=True, region=True, tz=True)
        print(format_phone_info(info))
    except ValueError as e:
        print(f"Erreur: {e}")
