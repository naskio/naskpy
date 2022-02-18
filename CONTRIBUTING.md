# Contributing

## Environment Setup

This project use [Poetry](https://python-poetry.org/) to manage dependencies.

### Requirements

- [macOS Monterey 12.2](https://www.apple.com/osx/download/)
    - [Homebrew](https://brew.sh/)
    - [Python](https://www.python.org/) v3.7 or higher
    - [PyCharm](https://www.jetbrains.com/pycharm/)

- [Poetry](https://python-poetry.org/) v1.1.12 or higher
    ```shell
    brew install poetry
    # or
    curl -sSL https://install.python-poetry.org | python3 -
    ```

- Pillow os dependencies (optional)
    ```shell
    brew install libtiff libjpeg webp little-cms2
    brew install freetype harfbuzz fribidi libraqm
    ```

Make sure to add `/usr/local/lib` to `$DYLD_FALLBACK_LIBRARY_PATH` in your `.bashrc` file (or `.bash_profile`).

### Install dependencies

```shell
poetry install
```

### Run tests

```shell
poetry run python -m unittest discover
# or
poetry run pytest
```

--------------------------------------------------------------------------------

## Documentation

Generated using `sphinx` and hosted by `ReadTheDocs`.

### Docstring guide

Example of a docstring:

```python
"""[Summary]
:param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
:type [ParamName]: [ParamType](, optional)
...
:raises [ErrorType]: [ErrorDescription]
...
:return: [ReturnDescription]
:rtype: [ReturnType]
"""
```

[Read more about docstrings](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html)

### Build the docs locally

```shell
cd ./docs 
rm -r build/ _autosummary/
make html
cd ../

# one-liner
cd docs/ && rm -r build/ _autosummary/ && make html && cd ../
```

To use apidoc run the following command before building the docs:

```shell
sphinx-apidoc -o ./_modules ../naskpy -f
```

### ReadTheDocs

Once enabled in readthedocs dashboard the docs will be built and deployed automatically on push to the main branch.

- [naskpy.readthedocs.io](https://naskpy.readthedocs.io)
- [naskpy.rtfd.io](https://naskpy.rtfd.io)

> A custom domain can be added throw the dashboard.

### GitHub Actions

Alternatively, the docs can be built and deployed using GitHub Actions and GitHub Pages.

- `pwd` in the BASE_DIR
- `cd ./docs && make html && cd ..`

--------------------------------------------------------------------------------

## Release

To release a new version of the project you need to:

- Update the version in `pyproject.toml` (version format: `X.Y.Z`)
- Commit the changes and push to run `test_workflow`
- Create a new tag locally
- Push the tag to the remote (**don't push tag until the end of `test_workflow`**)

### Create release

Once the `test_workflow` is done, you can create run:

```shell
VERSION="0.1.1"; MESSAGE=""; git tag $VERSION -a -m $MESSAGE; git push origin $VERSION
```

### Cancel release

- Remove the tag from local and remote
    ```shell
    VERSION="0.1.1"; git tag --delete $VERSION; git push --delete origin $VERSION
    ```

- Delete release from [GitHub](https://github.com/naskio/naskpy/releases/)

- Delete release from [PyPI](https://pypi.org/manage/project/naskpy/releases/)

- Delete release from [ReadTheDocs](https://readthedocs.org/projects/naskpy/)
