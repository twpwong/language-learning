# -*- coding: utf-8 -*-
"""Minimal Japanese verb classification and conjugation utilities."""

# Godan "ru" verb exceptions. These verbs end with "る" but conjugate
# as godan verbs rather than ichidan verbs.
GODAN_RU_EXCEPTIONS = {
    "切る",  # to cut
    "走る",  # to run
    "入る",  # to enter
    "要る",  # to need
    "知る",  # to know
    "帰る",  # to return
    "減る",  # to decrease
    "滑る",  # to slip
    "握る",  # to grip
}


def classify_verb(verb):
    """Classify a verb as 'godan', 'ichidan', 'suru', or 'kuru'."""
    # Check exception list first
    if verb in GODAN_RU_EXCEPTIONS:
        return "godan"

    if verb.endswith("する"):
        return "suru"
    if verb.endswith("くる"):
        return "kuru"

    if verb.endswith("る"):
        # Assume verbs ending with る are ichidan unless in exception list
        return "ichidan"

    # Default to godan for other endings
    return "godan"


def conjugate_masu(verb):
    """Return the polite present affirmative (ます) form of *verb*."""
    classification = classify_verb(verb)

    if classification == "ichidan":
        # Drop the final る and add ます
        return verb[:-1] + "ます"

    if classification == "godan":
        base = verb[:-1]
        ending = verb[-1]
        mapping = {
            "う": "い",
            "く": "き",
            "ぐ": "ぎ",
            "す": "し",
            "つ": "ち",
            "ぬ": "に",
            "ぶ": "び",
            "む": "み",
            "る": "り",
        }
        return base + mapping.get(ending, ending) + "ます"

    if classification == "suru":
        return verb[:-2] + "します"

    if classification == "kuru":
        return "きます"

    raise ValueError(f"Unknown classification for verb: {verb}")


def conjugate(verb, form):
    """Conjugate *verb* into the specified *form*."""
    if form == "masu":
        return conjugate_masu(verb)
    raise NotImplementedError(f"Form {form} not implemented")
