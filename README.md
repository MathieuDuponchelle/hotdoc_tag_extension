This is a tagging extension for [hotdoc](https://github.com/hotdoc/hotdoc)

It provides the user with the possibility of adding custom tags in their
comments, and to filter the produced documentation based on these tags.

> By default, hotdoc supports all the legacy gtk-doc tags.

### Install instructions:

This extension has no system-wide dependencies.

You can it either through pip:

```
pip install hotdoc_tag_extension
```

Or with setup.py if you checked out the code from git:

```
python setup.py install
```

This will of course work in a virtualenv as well.

### Usage:

Just run hotdoc's wizard for more information once the extension is installed with:

```
hotdoc conf --quickstart
```

### Hacking

Checkout the code from github, then run:

```
python setup.py develop
```

### Licensing

hotdoc's tag extension is licensed under the LGPL version 2.1 (or, at your option, any
later version). See COPYING for more details.
