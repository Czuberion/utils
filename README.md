
# Utils

Small utils and scripts for personal use.

## nvrt

Script making nvim open one server instance per qtile group. Trying to open more
nvim instances results in opening a new tab on the instance associated with the
group.
extract_key.py needs to be in the same directory. If you want to change that
just change `$EX_KEY_SOURCE`

### dependencies
- [nvim](https://neovim.io/) [\[GitHub\]](https://github.com/neovim/neovim)
- [nvr](https://github.com/mhinz/neovim-remote)
- [extract_key.py](#extract_keypy)

## extract_key.py

Meant to be used with [nvrt](#nvrt). Extracts the value from the Python dict
printed by qtile cmd-obj.

## <span>diagnostics.py</span>

A silly script for running [scc](https://github.com/boyter/scc) and showing
project tree.

