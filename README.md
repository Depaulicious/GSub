# GSub

GSub is an Ampache/Subsonic client for GNOME, forked from GSub.
Beware that no work has been done yet except for rebranding. It is a work in progress.

Below you can find the GSub original README in case you want to try building it.
It will be updated as soon as some work is done.

# GSub

## Where can I find more?

We have a wiki page at
[https://wiki.gnome.org/Apps/Music](https://wiki.gnome.org/Apps/Music)

You can join us on the IRC:
\#gsub on GIMPNet


## Building from jhbuild

Follow the BuildGnome tutorial for newcomers at https://wiki.gnome.org/Newcomers/BuildGnome

After installing jhbuild, you have to build gsub and all its dependencies. The task can be done by simply running:

```shell
$ jhbuild sysdeps --install gsub
$ jhbuild build gsub
```

Finally, start gnome music with:

```shell
$ jhbuild run gsub
```

## Troubleshooting

Jhbuild fires import errors for python packages like:

```
ImportError: /opt/gnome/lib64/python2.7/site-packages/
```

Do:

```shell
 $ jhbuild shell
 $ export PYTHONPATH=/opt/gnome/lib/python3.3/site-packages:/opt/gnome/lib64/python3.3/site-packages
 $ gsub
```


# Coding style

GSub is written in Python and aspires to adhere to the coding style described in [PEP-8](https://www.python.org/dev/peps/pep-0008/).

Use of docstrings is recommended following [PEP-257](https://www.python.org/dev/peps/pep-0257/)


The content of docstrings uses the [Sphinx](http://www.sphinx-doc.org/) markup style.

Use PyGI shorthands for manipulating `GtkTreeModel`:

```python
 model[iter][0] = "artist"
 artist, title = model[iter][1, 4]
```