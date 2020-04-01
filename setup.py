from setuptools import find_packages, setup

setup(
    name="ibmq_data_retriever",
    version="0.0.1a",
    packages=find_packages("src"),
    package_dir={"": "src"},
    # url="https://github.com/nelimee/ibmq_data_retriever",
    license="CeCILL-B",
    author="Adrien Suau",
    author_email="adrien.suau@protonmail.com",
    description="A small library to recover the data from IBMQ quantum chips.",
    install_requires=["qiskit-terra>=0.12", "qiskit-ibmq-provider>=0.5"],
    entry_points={"console_scripts": ["ibmq_save_data=ibmq_data_retriever._cli:main"]},
)

