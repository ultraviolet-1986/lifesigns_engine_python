#!/usr/bin/env python3

"""Display Lifesigns Engine metadata and main header."""

##########
# Notice #
##########

# Lifesigns Engine: A Python-based text adventure game engine.
# Copyright (C) 2020 William Willis Whinn

# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.

# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

###########
# Imports #
###########

from .colours import GREEN
from .colours import COLOUR_RESET

#############
# Variables #
#############

LIFESIGNS_VERSION = '0.0.1'
LIFESIGNS_URL = 'https://github.com/ultraviolet-1986/lifesigns_engine_python'

#############
# Functions #
#############

def display_prompt():
    """Display the main Lifesigns Engine header."""
    print("{0}Lifesigns Engine v{1} Copyright (C) 2020 William Whinn\n{2}{3}\n"
          .format(GREEN, LIFESIGNS_VERSION, LIFESIGNS_URL, COLOUR_RESET))

# End of File.
