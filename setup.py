from setuptools import setup, find_packages

setup(
    name = "hotdoc-tag-extension",
    version = "0.6",
    keywords = "tags metadata custom filtering hotdoc",
    url='https://github.com/MathieuDuponchelle/hotdoc-c-extension',
    author_email = 'mathieu.duponchelle@opencreed.com',
    license = 'LGPL',
    description = ("An extension for hotdoc that allows defining new valid tags,"
                    " and filtering the output based on symbol's tags"),
    author = "Mathieu Duponchelle",
    packages = find_packages(),
    entry_points = {'hotdoc.extensions': 'get_extension_classes = tag_extension:get_extension_classes'},
    install_requires = [
        'hotdoc>=0.6',
    ]
)
