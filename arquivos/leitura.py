# Programa - Abrindo, lendo e fechando um arquivo

arquivo = open("nomes.txt", "r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()
