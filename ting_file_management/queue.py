class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._fila = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._fila)

    def enqueue(self, value=0):
        """Aqui irá sua implementação"""
        self._fila.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        item = self._fila[0]
        del self._fila[0]
        return item

    def search(self, index):
        """Aqui irá sua implementação"""
        if 0 <= index < len(self._fila):
            return self._fila[index]
        raise IndexError
