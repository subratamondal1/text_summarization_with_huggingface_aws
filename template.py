import os
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s : %(message)s :",
    datefmt="%m/%d/%Y %H:%M:%S",
    handlers=[logging.StreamHandler()],
)

project_name = "text_summarizer"

# List of files that I need
list_of_files = [
    ".github/workflows/.gitkeep", # responsible for auto CI/CD github deployment
    # Local package enables importing like: from ... import ...
    f"src/{project_name}/__init__.py", # init constructor converts {project_name} folder to a local package
    f"src/{project_name}/components/__init__.py", # init constructor converts components folder to a local package
    f"src/{project_name}/utils/__init__.py", # init constructor converts utils folder to a local package
    f"src/{project_name}/utils/common.py", # contains utilities related code
    f"src/{project_name}/logging/__init__.py", # init constructor converts logging folder to a local package
    f"src/{project_name}/config/__init__.py", # init constructor converts config folder to a local package
    f"src/{project_name}/config/configurations.py", # contains all the configuration related code
    f"src/{project_name}/pipelines/__init__.py", # init constructor converts pipeline folder to a local package
    f"src/{project_name}/entity/__init__.py", # init constructor converts entity folder to a local package
    f"src/{project_name}/constants/__init__.py", # init constructor converts constants folder to a local package
    "config/config.yaml", # another config related but yaml file
    "params.yaml", # contains all model related parameters
    "app.py", # python file
    "main.py", # python file
    "Dockerfile", # Docker Image file for AWS deployment
    "requirements.txt", # required libraries for the project
    "setup.py", # for the project setup script
    "research/trials.ipynb", # contains all the notebooks for the project research
] 


# NOTE: that this file template.py just automates the manual creation of files and directories one by one

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")