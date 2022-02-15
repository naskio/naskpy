# Docs generation

```shell
cd ./docs
sphinx-apidoc -o ./source/_modules ../naskpy -f 
make html
```

## From GitHub Actions

- `pwd` in the BASE_DIR
- `cd ./docs && make html && cd ..`

## Readthedocs

```
naskpy.readthedocs.io
naskpy.rtfd.io
```