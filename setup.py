import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weishaupt-wcm-com",
    version="0.0.7",
    author="Philip Schmiegelt",
    author_email="philip@schmiegelt.it",
    description="Interfacing the Weishaupt WCM-COM module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/schmiegelt/Py-Weishaupt-WCM-COM",
    install_requires=["requests"],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
