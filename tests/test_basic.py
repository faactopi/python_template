# -*- coding: utf-8 -*-

from .context import library

import pytest


class TestBasicCase:
    """Basic test cases."""

    def test_simple(self):
        library.hello()
        assert True
    def test_logger(self):
        assert library.long_function_name(1,2,3,4) == 1
