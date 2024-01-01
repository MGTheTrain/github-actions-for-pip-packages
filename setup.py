from setuptools import setup
import sys

# Default version
version = "0.1.0"

if "--version" in sys.argv:
    version_index = sys.argv.index("--version") + 1
    if version_index < len(sys.argv):
        version = sys.argv[version_index]
        del sys.argv[version_index]
        del sys.argv[version_index - 1]

setup(
    name="common-lib",
    version=version,
    description="Common logic utilized in several services and applications",
    author="MGTheTrain",
    author_email="mgthetrain@email.com",
    packages=["web.dtos", "domain.models"],
    install_requires=[
        "pydantic",
    ],
)
