import setuptools

setuptools.setup(
    name="greenlight",
    version="0.1.10",
    author="Joseph Ryan-Palmer",
    author_email="joseph@ryan-palmer.com",
    description="A small application to poll for response code or text",
    url="https://github.com/JosephRPalmer/greenlight",
    project_urls={
        "Bug Tracker": "https://github.com/JosephRPalmer/greenlight/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"greenlight": "greenlight"},
    packages=["greenlight"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": ["greenlight=greenlight.greenlight:main"]
    },
)
