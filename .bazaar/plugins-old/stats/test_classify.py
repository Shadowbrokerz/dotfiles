# Copyright (C) 2008 Jelmer Vernooij <jelmer@samba.org>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
from bzrlib.tests import TestCase
from bzrlib.plugins.stats.classify import classify_filename, classify_delta


class TestClassify(TestCase):
    def test_classify_code(self):
        self.assertEquals("code", classify_filename("foo/bar.c"))

    def test_classify_documentation(self):
        self.assertEquals("documentation", classify_filename("bla.html"))

    def test_classify_translation(self):
        self.assertEquals("translation", classify_filename("nl.po"))

    def test_classify_art(self):
        self.assertEquals("art", classify_filename("icon.png"))

    def test_classify_unknown(self):
        self.assertEquals(None, classify_filename("something.bar"))

    def test_classify_doc_hardcoded(self):
        self.assertEquals("documentation", classify_filename("README"))
