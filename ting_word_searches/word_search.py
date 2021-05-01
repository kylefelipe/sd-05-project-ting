def exists_word(word, instance):
    """Aqui irá sua implementação"""
    mtw = []
    for i in range(len(instance)):
        file = instance.search(i)
        word_found = {"palavra": word,
                      "arquivo": file["nome_do_arquivo"],
                      "ocorrencias": []}
        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                word_found["ocorrencias"].append({"linha": index + 1})
        if len(word_found['ocorrencias']):
            mtw.append(word_found)
    return mtw


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    mtw = exists_word(word, instance)
    if len(mtw):
        for idx_file in range(len(instance)):
            file = instance.search(idx_file)
            file_lines = file['linhas_do_arquivo']
            listed_lines = mtw[idx_file]["ocorrencias"]
            for idx_line, line in enumerate(listed_lines):
                str_idx = line.get("linha") - 1
                listed_lines[idx_line]["conteudo"] = file_lines[str_idx]
            mtw[idx_file]["ocorrencias"] = listed_lines
    return mtw
