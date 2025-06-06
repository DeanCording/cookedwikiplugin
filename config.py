#!/usr/bin/env python
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__ = 'GPL v3'
__copyright__ = '2011, Kovid Goyal <kovid@kovidgoyal.net>, 2025 Dean Cording <dean@cording.id.au>'
__docformat__ = 'restructuredtext en'

try:
    from PyQt5.Qt import QWidget, QHBoxLayout, QLabel, QLineEdit
except ImportError:
    from PyQt4.Qt import QWidget, QHBoxLayout, QLabel, QLineEdit

from calibre.utils.config import JSONConfig

# This is where all preferences for this plugin will be stored
# Remember that this name (i.e. plugins/interface_demo) is also
# in a global namespace, so make it as unique as possible.
# You should always prefix your config file name with plugins/,
# so as to ensure you dont accidentally clobber a calibre config file
prefs = JSONConfig('plugins/cookedwiki')

# Set defaults
prefs.defaults['hello_world_msg'] = 'Cooked Wiki recipe link'


class ConfigWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ly = QHBoxLayout(self)

        self.label = QLabel('Cooked Wiki recipe link:')
        self.ly.addWidget(self.label)

        self.msg = QLineEdit(self)
        self.msg.setText(prefs['hello_world_msg'])
        self.ly.addWidget(self.msg)
        self.label.setBuddy(self.msg)

    def save_settings(self):
        prefs['hello_world_msg'] = self.msg.text()
