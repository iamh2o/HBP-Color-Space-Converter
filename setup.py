import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rgbw_colorspace_converter",
    version="0.1.4",
    author="John Major",
    author_email="iamh2o@gmail.com",
    description="Convert between RGB / HSV / HSL / HSI / HEX Color Spaces. And, emit the RGBW code for each.",
    long_description="see description",
    long_description_content_type="text/markdown",
    url="https://github.com/iamh2o/rgbw_colorspace_converter",
    project_urls={
        "Bug Tracker": "https://github.com/iamh2o/rgbw_colorspace_converter/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    scripts=[
        "bin/run_color_module_RGB_HSV_HEX_demo.py",
        "bin/run_spectrum_saturation_cycler.py",
        "bin/path_between_2_colors.py",
        "bin/print_colored_txt.py",
    ],
    python_requires=">=3.7",
    install_requires=["colr", "docopt", "html2image", "ansi2html"],
)
