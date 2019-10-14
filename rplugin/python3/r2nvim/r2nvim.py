# ============================================================================
# FILE: r2nvim.py
# AUTHOR: Philip Karlsson Gisslow <philipkarlsson at me.com>
# License: MIT license
# ============================================================================

class R2Nvim(object):
    def __init__(self):
        self.logstr = []
        self.logstr.append('== R2Nvim debug log ==')
        self.log('Hello world')

    def log(self, s):
        self.logstr.append(str(s))

    def get_log(self):
        return self.logstr
