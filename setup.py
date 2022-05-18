from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in kt/__init__.py
from kt import __version__ as version

setup(
	name="kt",
	version=version,
	description="custom app",
	author="grand hyper",
	author_email="info@test.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
