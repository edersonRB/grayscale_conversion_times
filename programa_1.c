#include <stdio.h>
#include <sys/time.h>
#include <stdlib.h>

struct pix
{
    unsigned int r, g, b;
};

// função parte do selectionSort
void swap(double *xp, double *yp)
{
    double temp = *xp;
    *xp = *yp;
    *yp = temp;
}

// função que faz o selectionSort de um vetor
void selectionSort(double arr[], int n)
{
    int i, j, min_idx;

    for (i = 0; i < n - 1; i++)
    {

        min_idx = i;
        for (j = i + 1; j < n; j++)
            if (arr[j] < arr[min_idx])
                min_idx = j;
        swap(&arr[min_idx], &arr[i]);
    }
}

int main(int argc, char *argv[])
{
    FILE *f = fopen("./saida1.txt", "w");
    int TAM = 0, limite = 5000, incremento = 500, k = 11, i, j;
    double ti = 0, tf = 0, tempo = 0;
    struct timeval tempo_inicio, tempo_fim; //coletar tempo de execução
    // ti = tempo inicial, tf = tempo final (mediana de tempos)
    if (argc == 4)
    {
        limite = atoi(argv[1]);
        incremento = atoi(argv[2]);
        k = atoi(argv[3]);
    }
    //tempos - vetor com k amostras de tempo
    double *tempos = (double *)malloc(sizeof(double) * k); 

    for (TAM; TAM <= limite; TAM += incremento)
    {
        struct pix(*color)[TAM] = malloc(sizeof(struct pix[TAM][TAM]));

        ////////////////////////Conversão para escalas de cinza/////////////////////////
        printf("TAM:%d convertendo imagem...\n", TAM);
        for (int h = 0; h < k; h++)
        {
            gettimeofday(&tempo_inicio, NULL);
            for (i = 0; i < TAM; i++)
            {
                for (j = 0; j < TAM; j++)
                {
                    color[i][j].r = (color[i][j].r +
                                     color[i][j].g +
                                     color[i][j].b) /
                                    3;
                }
            }
            gettimeofday(&tempo_fim, NULL);
            tf = (double)tempo_fim.tv_usec + ((double)tempo_fim.tv_sec * (1000000.0));
            ti = (double)tempo_inicio.tv_usec + ((double)tempo_inicio.tv_sec * (1000000.0));
            tempos[h] = (tf - ti) / 1000;
        }
        selectionSort(tempos, k);

        tempo = k % 2 == 0 && k != 0 ? tempos[(k - 1) / 2] : (tempos[k / 2] + tempos[k / 2 + 1]) / 2;

        printf("tempo->%f\n", tempo);
        fprintf(f, "%d %f\n", TAM, tempo);

        free(color);
    }

    fclose(f);
    return 0;
}