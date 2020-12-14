# -*- encoding: utf-8 -*-
# Copyright (c) 2020 Stephen Bunn <stephen@bunn.io>
# ISC License <https://choosealicense.com/licenses/isc>

"""
"""

from enum import Enum


class Style(Enum):

    RESET = "reset"
    BOLD = "bold"
    DIM = "dim"
    ITALIC = "italic"
    UNDERLINE = "underline"
    SLOW_BLINK = "slow_blink"
    RAPID_BLINK = "rapid_blink"
    REVERSED = "reversed"
    CONCEAL = "conceal"
    STRIKETHROUGH = "strikethrough"
    NORMAL = "normal"