#include <stdio.h>
#include <string.h>
#include <stdlib.h>
char cadenas [100][100] = {
    "AAAAAA","Hola"
};
int C1,C2,HI;
void menuCadenas()
{
    printf("Cadenas para usar\n");
    for(int i=0;i<100;i++)
    {
        HI=i;
        if(cadenas[i][0]!='\0')
            printf("%d. %s\n", i+1, cadenas[i]);
        else
            break;
        
    }

}
void ImprimeSubsecuencias(char *s, int n, int k, int inicio, int *indices, int profundidad) {
    if (profundidad == k) {
        for (int i = 0; i < k; i++) {
            printf("%c", s[indices[i]]);
        }
        printf("\n");
        return;
    }

    // Recorremos desde 'inicio' hasta 'n' para elegir los caracteres sin repetir orden
    for (int i = inicio; i < n; i++) {
        indices[
            profundidad] = i;
        ImprimeSubsecuencias(s, n, k, i + 1, indices, profundidad + 1);
    }
}

// Función principal que controla las longitudes (desde omitir pocos hasta omitir muchos)
void Subsecuencias(char *s) {
    int n = strlen(s);
    int indices[100]; 

    for (int k = 1; k <= n; k++) {
        ImprimeSubsecuencias(s, n, k, 0, indices, 0);
    }
}
void invertirCadena(char *cadena)
{
    if (cadena == NULL) return;

    int inicio = 0;
    int fin = strlen(cadena) - 1;
    char temp;
    while (inicio < fin)
    {
        temp = cadena[inicio];
        cadena[inicio] = cadena[fin];
        cadena[fin] = temp;
        
        inicio++;
        fin--;
    }

}

void menuOpciones()
{
    system("cls");
    int opc;
    printf("Operaciones\n");
    printf("1. Concatenar\n");
    printf("2. Potencia Positiva o Negativa\n");
    printf("3. Calcular longitud\n");
    printf("4. Generar prefijos\n");
    printf("5. Generar Sufijos\n");
    printf("6. Generar Subcadenas\n");
    printf("7. Generar Subsecuencias\n");
    printf("8. Mostrar Cadenas\n");
    printf("9. Salir\n");
    printf("Seleccione una opcion: ");
    scanf("%d", &opc);
    menuCadenas();
    switch(opc)
    {
        case 1:
        {
            printf("Inserte cadena 1:\n");
            scanf("%d", &C1);
            printf("Inserte cadena 2:\n");
            scanf("%d",&C2);
            C1--;
            C2--;
            strcpy(cadenas[HI],cadenas[C1]);
            strcat(cadenas[HI],cadenas[C2]);
            printf("Concatenacion: %s\n", cadenas[HI]);
            break;
        }
        case 2:
        {
            char aux[100];
            int p;
            printf("Inserte Cadena\n");
            scanf("%d", &C1);
            C1--;
            printf("Inserte potencia\n");
            scanf("%d", &p);
            strcpy(aux,cadenas[C1]);
            printf("AUX: %s", aux);
            if(p<0)
            {
                invertirCadena(aux);
                p=p*-1;
            }
                
            strcpy(cadenas[HI],aux);
            
            for(int i=0;i<p-1;i++)
            {
                strcat(cadenas[HI],aux);
            }
            printf("Potencia: %s\n", cadenas[HI]);
            break;

        }

        case 3:
        {
            int cont=0;
            printf("Inserte cadena 1:\n");
            scanf("%d", &C1);
            C1--;
            char c=cadenas[C1][0];
            do
            {
                c=cadenas[C1][cont];
                cont++;
            }while(c!='\0');
            cont=cont -1;
            printf("Longitud: %d\n", cont);
            break;
        }
        case 4:
        {
            printf("Inserte Cadena\n");
            scanf("%d", &C1);
            C1--; 
            char c=cadenas[C1][0];
            int i=0;
            for(int i=0;i<=strlen(cadenas[C1]);i++)
            {
                for(int j=0;j<i;j++)
                {
                    printf("%c",cadenas[C1][j]);
                }
                printf("\n");
            }
            break;

        }
        case 5:
        {
            printf("Inserte Cadena:\n");
            scanf("%d", &C1);
            C1--;
            int len = strlen(cadenas[C1]);
            for(int i = 0; i <= len; i++)
            {
                for(int j = i; j < len; j++)
                {
                    printf("%c", cadenas[C1][j]);
                }
                printf("\n");
            }
            break;
        }
        case 6:
        {
            printf("Inserte Cadena:\n");
            scanf("%d", &C1);
            C1--;
            int len = strlen(cadenas[C1]);
            for(int i = 0; i < len; i++)
            {
                for(int j = i; j < len; j++)
                {
                    for(int k = i; k <= j; k++)
                    {
                        printf("%c", cadenas[C1][k]);
                    }
                    printf("\n");
                }
            }
            break;
        }
        case 7:
        {
            printf("Inserte Cadena:\n");
            scanf("%d", &C1);
            C1--;
            if(strlen(cadenas[C1])>12)
            {
                printf("No se puede realizar esta operacion para cadenas de longitud mayor a 12\n");
                break;
            }
            Subsecuencias(cadenas[C1]);
            break;
            
        }
        case 8:
        {
            break;
        }
        case 9:
        {
            printf("Saliendo del programa...\n");
            exit(0);
        }
        default:
            printf("Opcion invalida. Intente de nuevo.\n");
            break;
    
    }
    system("pause");
    
}
int main()
{
    while(1)
    {
        menuOpciones();
    }
    return 1;
}


