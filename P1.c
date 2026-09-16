#include <stdio.h>
#include <string.h>
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
void menuOperaciones()
{
    int opc;
    printf("Operaciones\n");
    printf("1. Concatenar\n");
    printf("2. Potencia Positiva o Negativa\n");
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
        

    }
    
}
void menuOpciones()
{
    int opc;
    printf("Operaciones\n");
    printf("1. Calcular longitud\n");
    printf("2. Generar prefijos\n");
    scanf("%d", &opc);
    menuCadenas();
    switch(opc)
    {
        case 1:
        {
            int cont=0;
            printf("Inserte cadena 1:\n");
            scanf("%d", &C1);
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
        case 2:
        {
            printf("Inserte Cadena\n");
            scanf("%d", &C1);
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
        case 3:
        {
            printf("Inserte Cadena:\n");
            scanf("%d", &C1);
            
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
        case 4:
        {
            printf("Inserte Cadena:\n");
            scanf("%d", &C1);
            
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
        

    }
    
}
int main()
{
    menuOpciones();
    menuCadenas();

}


