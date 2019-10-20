# -*- coding: utf-8 -*-
from .regexanalyzer import RegexAnalyzer


class CreditCardAnalyzer(RegexAnalyzer):
    """Analyzer to match Credit Cards"""

    def __init__(self, action):
        """
        Analyzer to match Credit Cards
        :param action: Single action or list of actions to be executed when a paste matches
        """
        # Regex taken from https://www.regular-expressions.info/creditcard.html
        regex = r"^4(\d{12}(?:\d{3})?|\d{3}( \d{4}){2} (\d{4}|\d{1}))$|" \
                r"^(?:5[1-5]\d{2}|222[1-9]|22[3-9]\d|2[3-6]\d{2}|27[01]\d|2720)(\d{12}|( \d{4}){2} (\d{4}|\d{1}))$|" \
                r"^3[47](\d{13}|\d{2} \d{6} \d{5})$|" \
                r"^3(?:0[0-5]|[68]\d)(\d{11}|\d \d{6} \d{4})$|" \
                r"^6(?:011|5\d{2})(\d{12}|( \d{4}){3})|" \
                r"^(?:2131|1800|35\d{2,3})(\d{11}|( \d{4}){3})$"

        super().__init__(action, regex)
