# this allows typehints to function
# FIXME pylint in particular still seems to complain, pylance works fine
def mutate(fpath: str, rows: list[int], columns: list[int], mutation_chance: float) -> None:
    """Mutates a circuit.asc in place. Rows and columns are 0 indexed."""