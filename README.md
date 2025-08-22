# FAACTOPI Python Template Library :library
===========================================

This simple python project example to give a project structure template for library (Package, Module) for a Python development.

Without other specification, library must be develop with :
- Python 3.9
- pytest for unit tests

## Licence

This particular library template is under MIT licence.

## Coding style
Without otherwise specification, Coding style must comply with [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)

## Documentation
In the development part of the project, you can use [GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/ to write your content and to document the development. Your documentation files must be filed in the docs directory like this [example](./docs/README.md).

For the API documentation, the development teams must use code styling describe in the ad-hoc PEP section : [Documentations strings](https://peps.python.org/pep-0008/#documentation-strings).

Following readings could help :

- [PEP 256](https://peps.python.org/pep-0256/) – Docstring Processing System Framework

- [PEP 257](https://peps.python.org/pep-0257/) – Docstring Conventions

- [PEP 258](https://peps.python.org/pep-0258/) – Docutils Design Specification

## Tests
Without otherwise specification, development must use [Pytest](https://docs.pytest.org/en/stable/) library for the unit test framework.

## Structure

The following file project structure is with sample python files :
```bash
.
├── docs
│   └── README.md
├── library
│   ├── __init__.py
│   ├── core.py
│   └── helpers.py
├── LICENSE
├── Makefile
├── MANIFEST.in
├── README.md
├── requirements.txt
├── setup.py
└── tests
    ├── __init__.py
    ├── context.py
    ├── test_advanced.py
    └── test_basic.py
```
Any way, the package must be buildable and testable through the setup 



