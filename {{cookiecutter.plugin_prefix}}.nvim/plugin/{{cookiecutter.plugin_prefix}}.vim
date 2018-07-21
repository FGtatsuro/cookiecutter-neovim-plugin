if exists("g:loaded_{{ cookiecutter.plugin_prefix }}")
  finish
endif
let g:loaded_{{ cookiecutter.plugin_prefix }} = 1

" FYI: https://neovim.io/doc/user/options.html#'tabstop'
" vim: tabstop=8 shiftwidth=2 softtabstop=2
