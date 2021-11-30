import setuptools


def get_version(fname='source/flake8_class_constants.py'):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


requires = [
    "flake8 > 4.0.0",
]

flake8_entry_point = 'flake8.extension'

setuptools.setup(
    name="flake8_class_constants",
    license="MIT",
    version=get_version(),
    description="Check PEP-8 class constants naming conventions, plugin for flake8",
    author="Roman Korneev",
    author_email="rm@ipadla.org",
    url="https://github.com/ipadla/flake8-class-constants",
    py_modules=[
        "flake8_class_constants",
    ],
    install_requires=requires,
    entry_points={
        flake8_entry_point: [
            'CCN = flake8_class_constants:ConstantChecker',
        ],
    },
    package_dir={'': 'source'},
    zip_safe=False,
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
