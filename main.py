# import os
from sys import path
import sys
from typing import Dict
import yaml
import pathlib
import logging
from pprint import pprint

YAML_FILE = "dir_structure.yaml"

def load_yaml(file_name: str) -> dict:
    try: 
        with open(file_name, "r") as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
        return data
    except IOError:
            print("Unable to load from {file_name}, maybe it doesn't exist?\nExiting")
            sys.exit(1)

def execute_tasks(tasks, cwd):
    for task in tasks:
        print("\nTask to parse:")
        pprint(task)
        for key, value in task.items():
            task_name, task_todo = key, value
            if isinstance(task_name, str):
                program_name = value[0]["prog"]
                if isinstance(task_todo, list):
                    directory_list = value[1]["dirs"]
                    output = []
                    print(f"Directories to create for program: {program_name} \n")
                    create_directories(output, directory_list, cwd)
        # print(output)
        make_directories(output)

def setup_logging(wd: pathlib.Path):
    logging.basicConfig(
        filename=wd.joinpath("logging.log"),
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s : %(message)s",
    )

def create_directories(output: list, directories: list, parent):
    if isinstance(directories, dict):
        for key, value in directories.items():
            path = pathlib.Path.joinpath(parent, key)
            # output.append(path)
            if isinstance(value, list) or isinstance(value, dict):
                create_directories(output, value, path)  
            else:
                return
    elif isinstance(directories, list):
        for item in directories:
            if isinstance(item, list) or isinstance(item, dict):
                create_directories(output, item, parent)
            else:
                path = pathlib.Path.joinpath(parent, item)
                output.append(path)


def make_directories(list_directories: list):
    for name in list_directories:
        if not pathlib.Path.exists(name):
            pathlib.Path.mkdir(name, parents=True)
            print("Created:", name)
            logging.info(f"created folder: {name}")
        else:
            print("Exists:", name)
            logging.info(f"folder already exists: {name}")


def main():
    testing = False

    data = load_yaml(YAML_FILE)

    yaml_specified_location = data["where"]

    # setup where to create folders and logging
    if yaml_specified_location:
        cwd = pathlib.Path(yaml_specified_location)
    else:
        cwd = pathlib.Path.cwd()
    if testing:
        cwd = cwd.joinpath("test")
    
    # print(cwd)

    # setup logging
    setup_logging(cwd)
   
    tasks = data["what"]

    # run the tasks (create directories for a specific program)
    execute_tasks(tasks, cwd)


if __name__ == "__main__":
    main()
