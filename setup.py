from setuptools import find_packages, setup

import churning_mists


setup(
    name=churning_mists.__name__,
    version=churning_mists.__version__,
    description=churning_mists.__description__,
    author=churning_mists.__author__,
    author_email=churning_mists.__author_email__,
    url=churning_mists.__url__,
    packages=find_packages(),
    python_requires='>=3.8',
)
