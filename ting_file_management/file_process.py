import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    data = txt_importer(path_file)
    output = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data
    }
    sys.stdout.write(f"{output}\n")
    instance.enqueue(output)


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) == 0:
        sys.stdout.write(f"Não há elementos\n")
        return
    remove = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {remove} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        item = str(instance.search(position))
    except IndexError:
        sys.stderr.write("Posição inválida\n")
    else:
        sys.stdout.write(item)


if __name__ == "__main__":
    proj = Queue()
    process("statics/arquivo_teste.txt", proj)
    
    
