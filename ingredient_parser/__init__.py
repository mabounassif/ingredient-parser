from ._common import download_nltk_resources, show_model_card
from .parsers import inspect_parser, parse_ingredient, parse_multiple_ingredients

download_nltk_resources()

__all__ = [
    "inspect_parser",
    "parse_ingredient",
    "parse_multiple_ingredients",
    "show_model_card",
]

__version__ = "0.1.0-beta10"
