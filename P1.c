#include <stdio.h>
#include <string.h>
char cadenas [100][100] = {
    "AAAAAA","BBBB"
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
void invertirCadena()
{
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
            int p;
            printf("Inserte Cadena\n");
            scanf("%d", &C1);
            printf("Inserte potencia\n");
            scanf("%d", &p);
            if(p<0)
            {
                char aux[100];
                strcpy(aux,cadenas[C1]);

            }
            strcpy(cadenas[HI],cadenas[C1]);
            for(int i=0;i<p-1;i++)
            {
                strcat(cadenas[HI],cadenas[C1]);
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
            int p;
            printf("Inserte Cadena\n");
            scanf("%d", &C1);
            printf("Inserte potencia\n");
            scanf("%d", &p);
            if(p<0)
            {
                char aux[100];
                strcpy(aux,cadenas[C1]);

            }
            strcpy(cadenas[HI],cadenas[C1]);
            for(int i=0;i<p-1;i++)
            {
                strcat(cadenas[HI],cadenas[C1]);
            }
            printf("Potencia: %s\n", cadenas[HI]);
            break;

        }
        

    }
    
}
int main()
{
    menuOpciones();
    menuCadenas();

}


