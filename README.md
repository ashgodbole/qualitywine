<<<<<<< HEAD
=======
create env

```bash
conda create -n qualitywine python=3.7 -y
```

activate env
```bash
conda activate qualitywine
```

created a req file

install the req
```bash
pip install -r requirement.txt
```
download the data from

https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

```bash
git init
```
```bash
dvc init
```
```bash
dvc add data_given/winequality.csv
```
```bash
git add .
```
```bash
git commit -m "first commit"
```

oneliner updates  for readme

```bash
git add . && git commit -m "update Readme.md"
```
```bash
git remote add origin https://github.com/ashgodbole/qualitywine.git
git branch -M main
git push origin main
```

tox command -
```bash
tox
```
for rebuilding -
```bash
tox -r
```
pytest command
```bash
pytest -v
```

setup commands -
```bash
pip install -e .
```

build your own package commands-
```bash
python setup.py sdist bdist_wheel
```
>>>>>>> 9aaf4d37d52dde3bdcf7b6d6157acdfe31e3f5c9
