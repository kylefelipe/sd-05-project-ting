import sys
from os.path import isfile


def txt_importer(path_file):
    """Aqui irá sua implementação
    Tá """
    try:
        assert path_file.endswith('.txt')
        with open(path_file, 'r') as file:
            data = file.read().splitlines()
    except AssertionError:
        sys.stderr.write("Formato inválido\n")
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    else:
        return data
