# ============================================================================
# FILE: __init__.py
# AUTHOR: Philip Karlsson Gisslow <philipkarlsson at me.com>
# License: MIT license
# ============================================================================

import neovim

from r2nvim.r2nvim import R2Nvim

@neovim.plugin
class R2NvimWrapper(object):
    def __init__(self, nvim):
        self.nvim = nvim
        self.r2n = R2Nvim()

    @neovim.command("R2NvimRax", range='', nargs='*', sync=True)
    def R2NvimRax(self, args, range):
        if len(args) == 0:
            word = self.nvim.eval('expand(\'<cword>\')').strip('\n')
        else:
            word = args[0]
        ret = self.r2n.rax(word)
        retstr = ''+str(ret.split('\n'))
        self.nvim.command(":call TestMe(%s)" % retstr)

    @neovim.command("R2NvimShowLog", range='', nargs='*', sync=True)
    def R2NvimShowLog(self, args, range):
        """ Show the R2Nvim log

        Parameters:
            n/a

        Returns:
            n/a
        """
        self.nvim.command('e R2Nvim_log')
        self.nvim.command('setlocal buftype=nofile')
        self.nvim.command('setlocal filetype=R2Nvim_log')
        logStr = self.r2n.get_log()
        self.nvim.current.buffer.append(logStr)
