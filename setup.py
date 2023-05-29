import setuptools

setuptools.setup(
    name="smeagol", 
    version="0.0.1",
    author="Justin Janquart",
    author_email="j.janquart@uu.nl",
    description="Companion package to Golum package for selection effects",
    long_description="Companion package to Golum package for selection effects",
    url="https://github.com/lemnis12/smeagol",
    packages=["smeagol"], 
    install_requires=["golum",
                      "hanabi"],
    extras_require = {"faster_model_selection" : "jax"},
    classifiers=["Development Status :: 3 - Alpha",
                 "Intended Audience :: GW lensing community",
                 "Topic :: Strongly lensed Gravitational-wave parameter estimation",
                 "Programming Language :: Python :: 3.8",
                 "Programming Language :: Python :: 3.9"],
    python_requires = ">=3.8"
    )