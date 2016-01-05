from setuptools import setup, find_packages

setup(
    name = "hotdoc_tag_extension",
    version = "0.6.6",
    keywords = "tags metadata custom filtering hotdoc",
    url='https://github.com/hotdoc/hotdoc_tag_extension',
    author_email = 'mathieu.duponchelle@opencreed.com',
    license = 'LGPL',
    description = ("An extension for hotdoc that allows defining new valid tags,"
                    " and filtering the output based on symbol's tags"),
    author = "Mathieu Duponchelle",
    packages = find_packages(),
    entry_points = {'hotdoc.extensions': 'get_extension_classes = hotdoc_tag_extension.tag_extension:get_extension_classes'},
)
