#!/usr/bin/env python3

from ingredient_parser.en import inspect_parser_en, parse_ingredient_en

from . import SUPPORTED_LANGUAGES
from .dataclasses import ParsedIngredient, ParserDebugInfo


def parse_ingredient(
    sentence: str,
    lang: str = "en",
    discard_isolated_stop_words: bool = True,
    string_units: bool = False,
    imperial_units: bool = False,
) -> ParsedIngredient:
    """Parse an ingredient sentence to return structured data.

    Parameters
    ----------
    sentence : str
        Ingredient sentence to parse
    lang : str
        Language of sentence.
        Currently supported options are: en
    discard_isolated_stop_words : bool, optional
        If True, any isolated stop words in the name, preparation, or comment fields
        are discarded.
        Default is True.
    string_units : bool
        If True, return all IngredientAmount units as strings.
        If False, convert IngredientAmount units to pint.Unit objects where possible.
        Dfault is False.
    imperial_units : bool
        If True, use imperial units instead of US customary units for pint.Unit objects
        for the the following units: fluid ounce, cup, pint, quart, gallon.
        Default is False, which results in US customary units being used.
        This has no effect if string_units=True.

    Returns
    -------
    ParsedIngredient
        ParsedIngredient object of structured data parsed from input string
    """
    if lang not in SUPPORTED_LANGUAGES:
        raise ValueError(f'Unsupported language "{lang}"')

    match lang:
        case "en":
            return parse_ingredient_en(
                sentence,
                discard_isolated_stop_words=discard_isolated_stop_words,
                string_units=string_units,
                imperial_units=imperial_units,
            )
        case _:
            raise ValueError(f'Unrecognised value "{lang}"')


def parse_multiple_ingredients(
    sentences: list[str],
    lang: str = "en",
    discard_isolated_stop_words: bool = True,
    string_units: bool = False,
    imperial_units: bool = False,
) -> list[ParsedIngredient]:
    """Parse multiple ingredient sentences in one go.

    This function accepts a list of sentences, with element of the list representing
    one ingredient sentence.
    A list of dictionaries is returned, with optional confidence values.
    This function is a simple for-loop that iterates through each element of the
    input list.

    Parameters
    ----------
    sentences : list[str]
        List of sentences to parse
    lang : str
        Language of sentence.
        Currently supported options are: en
    discard_isolated_stop_words : bool, optional
        If True, any isolated stop words in the name, preparation, or comment fields
        are discarded.
        Default is True.
    string_units : bool
        If True, return all IngredientAmount units as strings.
        If False, convert IngredientAmount units to pint.Unit objects where possible.
        Dfault is False.
    imperial_units : bool
        If True, use imperial units instead of US customary units for pint.Unit objects
        for the the following units: fluid ounce, cup, pint, quart, gallon.
        Default is False, which results in US customary units being used.
        This has no effect if string_units=True.

    Returns
    -------
    list[ParsedIngredient]
        List of ParsedIngredient objects of structured data parsed
        from input sentences
    """
    return [
        parse_ingredient(
            sentence,
            lang=lang,
            discard_isolated_stop_words=discard_isolated_stop_words,
            string_units=string_units,
            imperial_units=imperial_units,
        )
        for sentence in sentences
    ]


def inspect_parser(
    sentence: str,
    lang: str = "en",
    discard_isolated_stop_words: bool = True,
    string_units: bool = False,
    imperial_units: bool = False,
) -> ParserDebugInfo:
    """Dataclass for holding intermediate objects generated during parsing.

    Parameters
    ----------
    sentence : str
        Ingredient sentence to parse
    lang : str
        Language of sentence.
        Currently supported options are: en
    discard_isolated_stop_words : bool, optional
        If True, any isolated stop words in the name, preparation, or comment fields
        are discarded.
        Default is True.
    string_units : bool
        If True, return all IngredientAmount units as strings.
        If False, convert IngredientAmount units to pint.Unit objects where possible.
        Dfault is False.
    imperial_units : bool
        If True, use imperial units instead of US customary units for pint.Unit objects
        for the the following units: fluid ounce, cup, pint, quart, gallon.
        Default is False, which results in US customary units being used.
        This has no effect if string_units=True.

    Returns
    -------
    ParserDebugInfo
        ParserDebugInfo object containing the PreProcessor object, PostProcessor
        object and Tagger.
    """
    if lang not in SUPPORTED_LANGUAGES:
        raise ValueError(f'Unsupported language "{lang}"')

    match lang:
        case "en":
            return inspect_parser_en(
                sentence,
                discard_isolated_stop_words=discard_isolated_stop_words,
                string_units=string_units,
                imperial_units=imperial_units,
            )
        case _:
            raise ValueError(f'Unrecognised value "{lang}"')
