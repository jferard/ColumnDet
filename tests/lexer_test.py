#  ColumnDet - A column type detector
#      Copyright (C) 2020 J. Férard <https://github.com/jferard>
#
#   This file is part of ColumnDet.
#
#   ColumnDet is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   ColumnDet is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import unittest

from columndet import OpCode
from columndet.lexer import Lexer
from columndet.util import Token


class LexerTest(unittest.TestCase):
    def test(self):
        lexer = Lexer()
        self.assertEqual([Token(OpCode.TEXT, 'entrée')], lexer.lex("entrée"))


if __name__ == '__main__':
    unittest.main()
