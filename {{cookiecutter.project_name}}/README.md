{{ cookiecutter.project_name }}
==================================================

[![Build Status](https://travis-ci.org/{{ cookiecutter.author }}/{{ cookiecutter.project_name }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.author }}/{{ cookiecutter.project_name }})

Neovim plugin for {{ cookiecutter.project_description }}.

Requirements
------------

The dependencies on other softwares/libraries for this project. 
This software may work even if these requirements aren't met, but the behavior on that case can't be supported officially.

- Neovim (>= 0.3.x)
- Python (>= 3.7.x)

Installation
------------

1. Create a directory to put this plugin.

```bash
$ mkdir -p ~/.config/nvim/bundle
```

2. Clone this project under step1's directory.

```bash
$ git clone git@github.com:{{ cookiecutter.author }}/{{ cookiecutter.project_name }}.git ~/.config/nvim/bundle/{{ cookiecutter.project_name }}
```

3. Add a directory of cloned this project to `$runtimepath`.

```vim
" Your vimrc
let &runtimepath.=','.$HOME.'/.config/nvim/bundle/{{ cookiecutter.project_name }}'
```

4. Update plugin info.

```vim
# In Neovim
:UpdateRemotePlugins
:qa!
```

How to
------

Development
-----------

1. Start Neovim with `NVIM_PYTHON_LOG_FILE` and `NVIM_PYTHON_LOG_FILE`, you can check logs of Neovim.

```bash
# FYI: https://github.com/neovim/python-client/blob/master/docs/usage/remote-plugins.rst
$ NVIM_PYTHON_LOG_LEVEL=DEBUG NVIM_PYTHON_LOG_FILE=./{{cookiecutter.plugin_prefix}}.log nvim -u tests/vimrc
```

2. Update the remote plugin manifest and restart Neovim. After that, please check futures of your plugin.

```
# In Neovim
:UpdateRemotePlugins
:qa!

...

$ (Same command to step1)
:(Run plugin's command/function/mapping and so on)
```
