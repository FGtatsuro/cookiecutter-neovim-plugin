#!/usr/bin/env python
# -*- coding: utf-8 -*-


class {{cookiecutter.plugin_prefix|capitalize}}Handler():

    def __init__(self, nvim):
        self.nvim = nvim

    def handle(self, arg, text):
        firstline = text.split('\n')[0]
        self.nvim.command(f'echo "arg:{arg}/text:{firstline}"')

# https://wiki.python.org/moin/Vim
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
