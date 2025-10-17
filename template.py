import os
from pathlib import Path
import logging

#creating logging report 
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] -[%(levelname)s]- %(message)s'
)

#creating folder structure with files
list_of_files=[
    "docs",
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "app.py"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'Creating directory {filedir} for filename {filename}')
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file: {filename}")
        
    else:
        logging.info(f"{filename} already exists.")