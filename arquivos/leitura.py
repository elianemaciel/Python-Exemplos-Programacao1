# Programa - Abrindo, lendo e fechando um arquivo

arquivo = open("numeros.txt", "w")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()