#!/usr/bin/env python
# -*- coding: utf-8 -*-

import neovim

from {{cookiecutter.plugin_prefix}}.{{cookiecutter.plugin_prefix}} import {{cookiecutter.plugin_prefix|capitalize}}Handler


@neovim.plugin
class {{cookiecutter.plugin_prefix|capitalize}}Plugin():

    def __init__(self, nvim):
        self.nvim = nvim
        # Note: In initialization phase(=in __init__ method), Neovim APIs mayn't be used properly.
        self.handler = {{cookiecutter.plugin_prefix|capitalize}}Handler(self.nvim)

    @neovim.command('{{cookiecutter.plugin_prefix|capitalize}}TestCommand', nargs='1', range='%')
    def test_command(self, args, range):
        arg1 = args[0]
        start, end = range
        # range starts 1, but Neovim API to get lines accept 0 origin.
        text = '\n'.join(self.nvim.current.buffer[slice(start - 1, end)])
        self.handler.handle(arg1, text)

# https://wiki.python.org/moin/Vim
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
