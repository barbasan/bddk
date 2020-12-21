from setuptools import setup

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    name="bddk",
    version="0.1",
    description="Bddk Veri",
    py_modules=["bddk"],
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
	"License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "pandas",
        "openpyxl",
        "selenium",
        "urllib3",
        "requests"
    ],
    url="https://github.com/barbasan",
    author="Ilyas Burak Hizarci",
    author_email="i.burakhizarci@gmail.com"
)
