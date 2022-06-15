# importando o modulo 'matplotlib'
import matplotlib.pyplot as plt
# importando o modulo 'os' para enviar comandos para o terminal
import os

plt.rcParams.update({'font.size': 8})

#Compilando e os arquivos C com os cli args
limite = 5000  #valores muito grandes podem causar falta de memoria (5k 100 1-5)
incremento = 500
k = 1
#executa a conversao da mesma imagem k vezes, evita outliers, pois o
#tempo real é a mediana das k tentativas - multiplica o tempo total execucao por k
os.system("gcc programa_1.c -o ./executaveis/programa_1.exe")
os.system("gcc programa_2.c -o ./executaveis/programa_2.exe")
runArquivo1 = "./executaveis/programa_1.exe " + str(limite) + " " + str(
    incremento) + " " + str(k)
runArquivo2 = "./executaveis/programa_2.exe " + str(limite) + " " + str(
    incremento) + " " + str(k)

os.system("date")

print("\n" + runArquivo1)
print("=============PROGRAMA 1============")
os.system(runArquivo1)
print("\n" + runArquivo2)
print("=============PROGRAMA 2============")
os.system(runArquivo2)

print("Fim Execucao Programas C\n")
###############################################################################

#abrindo arquivos para leitura
f1 = open("saida1.txt", "r")
f2 = open("saida2.txt", "r")

#armazenam os tamanhos e tempos de execucao dos dois programas
x1 = []
y1 = []
x2 = []
y2 = []
i = 0

#lê os dados dos arquivos e armazena em vetores
vetorF1 = f1.read().split()
vetorF2 = f2.read().split()

#apaga os arquivos gerados temporariamente (C)
os.system("rm saida1.txt saida2.txt")

#percorre o vetor  e armazena os valores em x1 e y1
while i < len(vetorF1):
    x1.append(int(vetorF1[i]))
    i = i + 1
    y1.append(float(vetorF1[i]))
    i = i + 1

i = 0
#percorre o vetor e armazena os valores em x2 e y2
while i < len(vetorF2):
    x2.append(int(vetorF2[i]))
    i = i + 1
    y2.append(float(vetorF2[i]))
    i = i + 1

# gera os graficos
plt.plot(x1, y1, 'g.:', label="Programa 1", markersize=2, linewidth=1)
plt.plot(x2, y2, 'r.:', label="Programa 2", markersize=2, linewidth=1)

# configura aspectos visuais do grafico
plt.title('Tamanho da imagem x Tempo de processamento')
plt.legend()
plt.xlabel('Tamanho da imagem em pixels²')
plt.ylabel('Tempo em milisegundos')

#salva o grafico em um arquivo .png se nao ocorreu nenhum erro
if (len(x1) == len(y1) and len(x2) == len(y2) and x1 != [] and y1 != []
        and x2 != [] and y2 != []):
    plt.savefig('./imagens/Grafico Tamanho-Tempo.png', dpi=600)
else:
    print("Erro ao gerar grafico")

#gerando tabelas
data = []
i = 0
for i in range(len(x1)):
    data.append([x1[i], y1[i], y2[i]])

columns = ('TAMANHO', 'TEMPO PROGRAMA 1', 'TEMPO PROGRAMA 2')

plt.clf()
plt.axis('off')
plt.axis('tight')
plt.tight_layout()

plt.table(cellText=data,
          colLabels=columns,
          loc='center',
          rowLoc='center',
          colColours=['#9F9F9F', '#23E25C', '#df3535'])
# salva o grafico em uma imagem png
if (len(x1) == len(y1) and len(x2) == len(y2) and x1 != [] and y1 != []
        and x2 != [] and y2 != []):
    plt.savefig('./imagens/Tabela Tamanho-Tempo.png',
                dpi=150,
                bbox_inches="tight",
                pad_inches=.1)
else:
    print("Erro ao gerar tabela")

os.system("date")