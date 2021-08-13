from setuptools import setup, find_packages
# The setup.py will make the project instalable
# this will be needed when you run tests -- pytest

setup(
    name="geofusion_api",
    version="0.1.0",  # major, minor, patch
    description="Project for a api, for learning purposes",
    packages=find_packages(exclude="../venv"),
    include_package_data=True,
    install_requires=["flask", "flask-sqlalchemy", "sqlalchemy", "flask-restful"]
)