# GVUV - Graphviz Updating Viewer

## Aim

Create a graphviz viewer that updates as you save edits in a text editor.

## Status

* Graph generation and display: __working__.
* Auto-refresh __not implemented__. User must press `View>Refresh` (`Ctrl-R`).

### Milestones

1. SVG Viewer. [done]

2. Refresh SVG shortcut. [done]

3. Generate SVG from .dot file. [done]

4. Generate + Refresh button (same button). [done]

5. Watch .dot file for changes and auto-refresh.

## Requirements

Python with PyQt4 (only tested in WinPython 3.4.2)

Graphviz (either put its bin in path, or modify `dotpath` in `gvgen.py`)

The graph file should have `.dot` as its extension.


## License
3-clause BSD.
