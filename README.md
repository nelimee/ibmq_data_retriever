# `ibmq_data_retriever`

A small tool to automatically retrieve and save the data of IBMQ quantum chips available at [https://quantum-computing.ibm.com/](https://quantum-computing.ibm.com/).

## Installation

The package is not on [PyPi](https://pypi.org/) yet, so you need to clone this repository and install it locally with

``` shell
git clone git@github.com:nelimee/ibmq_data_retriever.git
python -m pip install ibmq_data_retriever/
```

## How to use it?

``` text
❯ ibmq_save_data --help
usage: ibmq_save_data [-h] [-v] [--hub HUB] [--group GROUP] [--project PROJECT] [-d DIRECTORY]

Saving the raw IBMQ chip data

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         I will tell you what I am doing
  --hub HUB             IBMQ hub used to register to the quantum-experience API
  --group GROUP         IBMQ group used to register to the quantum-experience API
  --project PROJECT     IBMQ project used to register to the quantum-experience API
  -d DIRECTORY, --directory DIRECTORY
                        Directory where the data will be saved
```

