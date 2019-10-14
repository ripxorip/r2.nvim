# ============================================================================
# FILE: r2nvim.py
# AUTHOR: Philip Karlsson Gisslow <philipkarlsson at me.com>
# License: MIT license
# ============================================================================

import os
import subprocess

class R2Nvim(object):
    def __init__(self):
        self.logstr = []
        self.logstr.append('== R2Nvim debug log ==')

    def log(self, s):
        if '\n' in s:
            ns = s.split('\n')
            for i in ns:
                self.logstr.append(i)
        else:
            self.logstr.append(str(s))

    def get_log(self):
        return self.logstr

    def rax(self, symbol):
        raxout = subprocess.check_output(['rax2', '-r', symbol]).decode()
        self.log(raxout)
        return raxout
