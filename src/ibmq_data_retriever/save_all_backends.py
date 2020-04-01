import typing as ty
from pathlib import Path

from ibmq_data_retriever.BackendData import BackendData
from qiskit import IBMQ
from qiskit.validation.exceptions import ModelValidationError

def save_all_accessible_backends(
    hub: ty.Optional[str] = None,
    group: ty.Optional[str] = None,
    project: ty.Optional[str] = None,
    output_directory: ty.Optional[ty.Union[str, Path]] = None,
    verbose: bool = False,
):
    if verbose:
        print("Connecting to IBMQ network...")
    IBMQ.load_account()
    provider = IBMQ.get_provider(hub=hub, group=group, project=project)
    backends = provider.backends(simulator=False)
    for backend in backends:
        try:
            BackendData(backend, hub, group, project).save(output_directory, verbose)
        except ModelValidationError:
            if verbose:
                print(f"Could not save {backend}.")
