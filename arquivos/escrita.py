# Programa - Abrindo, escrevendo e fechando um arquivo

arquivo = open("numeros.txt", "w")
for linha in range(100):
    arquivo.write(f"{linha}\n")
arquivo.close()