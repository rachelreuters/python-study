import time


def medir_tempo(funcao):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f"A função '{funcao.__name__}' levou {fim - inicio:.4f} sec.")
        return resultado
    return wrapper


@medir_tempo
def tarefa_pesada():
    print("Executando tarefa pesada...")
    time.sleep(2)
    print("Tarefa concluída!")


tarefa_pesada()
