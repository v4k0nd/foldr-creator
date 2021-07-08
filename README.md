# foldr-creator
Quick python script to create custom folder structure predefined in a YAML file.

## How to use
The repo will contain a `.exe` file that parses a `dir_structure.yaml.backup` file. Create a copy of the `.yaml.backup` and rename it to just `.yaml`. 


### How to customize .yaml
Below is a valid `.yaml` setup, with `task1` enabled, one `task2` disabled (by being commented out). 

```yaml
where: 'HOMEPATH%\Desktop'
what: 
  - task1:
    - prog: 'Photoshop'
    - dirs: 
      - import
      - export
      - raw:
        - before
#   - task2:
#     - prog: 'Premier Pro'
#     - dirs:
#       - raw
#       - export
```

## How to develop
Tested on Python v3.8.10 (might work with version above 3.6).

Clone to your system:
```sh
git clone https://github.com/v4k0nd/foldr-creator
```

Recommended to use virtualenv's.
To install the required packages run:
```sh
pip install -r requirements.txt
```

I used `pipenv`, so for that, run this (should find that this repo has a `requirements.txt` file and will install dependencies from there):
```sh
pipenv install
```

I used `pyinstaller` to compile this to one executable file, as far as I know, you can not cross compile (from linux to windows, and vice versa), so you should compile it on your machine.

To compile it for yourself (to get an executable):
```sh
pyinstaller --onefile main.py
```
