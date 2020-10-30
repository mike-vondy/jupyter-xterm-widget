jupyter-xterm-widget
===============================

Jupyter Widget for an interactive xterm moerm.js

Installation
------------

To install use pip:

    $ pip install jupyter_xterm_widget
    $ jupyter nbextension enable --py --sys-prefix jupyter_xterm_widget

To install for jupyterlab

    $ jupyter labextension install jupyter_xterm_widget

For a development installation (requires npm),

    $ git clone https://github.com//jupyter-xterm-widget.git
    $ cd jupyter-xterm-widget
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --sys-prefix jupyter_xterm_widget
    $ jupyter nbextension enable --py --sys-prefix jupyter_xterm_widget
    $ jupyter labextension install js

When actively developing your extension, build Jupyter Lab with the command:

    $ jupyter lab --watch

This takes a minute or so to get started, but then automatically rebuilds JupyterLab when your javascript changes.

Note on first `jupyter lab --watch`, you may need to touch a file to get Jupyter Lab to open.

