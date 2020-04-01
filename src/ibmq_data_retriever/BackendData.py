import os
import pickle
import typing as ty
from copy import deepcopy
from datetime import date, datetime
from pathlib import Path

from qiskit import IBMQ
from qiskit.providers.ibmq.ibmqbackend import IBMQBackend


class BackendData:
    @staticmethod
    def _get_backend(
        backend_name: str,
        hub: ty.Optional[str] = None,
        group: ty.Optional[str] = None,
        project: ty.Optional[str] = None,
        verbose: bool = False,
    ):
        if hub is None:
            hub = "ibm-q"
        if group is None:
            group = "open"
        if project is None:
            project = "main"
        provider = IBMQ.get_provider(hub=hub, group=group, project=project)
        matching_backends = provider.backends(backend_name)
        if not matching_backends:
            raise RuntimeError("No backend matching.")
        backend = matching_backends[0]
        return backend

    def __init__(
        self,
        backend: ty.Union[str, IBMQBackend],
        hub: ty.Optional[str] = None,
        group: ty.Optional[str] = None,
        project: ty.Optional[str] = None,
    ):
        if isinstance(backend, str):
            backend = self._get_backend(backend, hub, group, project)
        self.configuration = deepcopy(backend.configuration().to_dict())
        self.group = deepcopy(backend.group)
        self.hub = deepcopy(backend.hub)
        self.name = deepcopy(backend.name())
        self.project = deepcopy(backend.project)
        self.properties = deepcopy(backend.properties().to_dict())
        self.version = deepcopy(backend.version())

    def save(
        self,
        data_directory: ty.Optional[ty.Union[Path, str]] = None,
        verbose: bool = False,
    ):
        if data_directory is None:
            main_directory = Path(__file__).parent.parent.parent
            data_directory = main_directory / "data"
        backend_directory = data_directory / self.name
        UTC = datetime.utcnow()
        day_directory = backend_directory / str(UTC.date())
        if not os.path.isdir(day_directory):
            os.makedirs(day_directory)
        filename = f"{UTC.hour}-{UTC.minute}-{UTC.second}.pkl"
        if verbose:
            print(f"Saving backend '{self.name}' to '{day_directory / filename}'")
        with open(day_directory / filename, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(
        data_directory: Path, backend_name: str, date: date
    ) -> ty.Optional["BackendData"]:
        directory = data_directory / backend_name / str(date)
        # Take the first data of the day
        filenames = os.listdir(directory)
        if len(filenames) == 0:
            return None
        filename = filenames[0]
        with open(directory / filename, "rb") as f:
            return pickle.load(f)
