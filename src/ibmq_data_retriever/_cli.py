import argparse
from pathlib import Path

from ibmq_data_retriever.save_all_backends import save_all_accessible_backends


def main():
    parser = argparse.ArgumentParser(description="Saving the raw IBMQ chip data")

    parser.add_argument(
        "-v", "--verbose", action="store_true", help="I will tell you what I am doing"
    )
    parser.add_argument(
        "--hub",
        type=str,
        help="IBMQ hub used to register to the quantum-experience API",
        default="ibm-q",
    )
    parser.add_argument(
        "--group",
        type=str,
        help="IBMQ group used to register to the quantum-experience API",
        default="open",
    )
    parser.add_argument(
        "--project",
        type=str,
        help="IBMQ project used to register to the quantum-experience API",
        default="main",
    )

    parser.add_argument(
        "-d",
        "--directory",
        type=Path,
        help="Directory where the data will be saved",
        default=None,
    )

    args = parser.parse_args()
    save_all_accessible_backends(
        args.hub, args.group, args.project, args.directory, args.verbose
    )
