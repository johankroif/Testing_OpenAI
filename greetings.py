from typing import Dict


def build_greeting(name: str = "φίλε", language: str = "el") -> str:
    """Build a friendly greeting.

    Args:
        name: The person to greet.
        language: Language code for the greeting. Supported codes: "el" (Greek),
            "en" (English), "es" (Spanish).

    Raises:
        ValueError: If the provided language code is not supported.
    """
    greetings: Dict[str, str] = {
        "el": "Γεια σου",
        "en": "Hello",
        "es": "Hola",
    }

    if language not in greetings:
        supported = ", ".join(sorted(greetings))
        raise ValueError(f"Unsupported language '{language}'. Supported languages: {supported}.")

    return f"{greetings[language]}, {name}!"
