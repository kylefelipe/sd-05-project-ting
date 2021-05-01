from ting_file_management.file_process import process
from ting_file_management.queue import Queue


def exists_word(word, instance):
    """Aqui irá sua implementação"""
    mtw = []
    for i in range(len(instance)):
        file = instance.search(i)
        word_found = {"palavra": word,
                      "arquivo": file["nome_do_arquivo"],
                      "ocorrencias": []}
        lines = [row.lower() for row in file["linhas_do_arquivo"]]
        for index, line in enumerate(lines):
            if word.lower() in line:
                word_found["ocorrencias"].append({"linha": index + 1})
        if len(word_found['ocorrencias']):
            mtw.append(word_found)
    return mtw


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


if __name__ == '__main__':
    project = Queue()
    process("statics/nome_pedro.txt", project)
    word = exists_word("Pedro", project)
