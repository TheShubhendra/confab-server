from setuptools import setup, find_packages


def readme():
    with open(r"README.md") as f:
        README = f.read()
    return README


def requirements():
    with open("requirements.txt", "r") as f:
        req = f.read()
        return req


setup(
    name="confab-server",
    packages=find_packages(),
    version="0.1.0",
    license="MIT",
    description="""A package for handling
API server of Confab.""",
    author="Shubhendra Kushwaha",
    author_email="shubhendrakushwaha94@gmail.com",
    url="https://github.com/TheShubhendra/confab-server",
    keywords=[
        "Server",
        "API server",
        "Messaging",
        "Chatting",
        "Confab",
    ],
    install_requires=requirements(),
    include_package_data=True,
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
