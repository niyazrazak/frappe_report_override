from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_report_override/__init__.py
from frappe_report_override import __version__ as version

setup(
	name="frappe_report_override",
	version=version,
	description="Override Any Standard Report",
	author="Niyaz Razak",
	author_email="niyasibnurazak@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
