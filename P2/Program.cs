using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Program
{
    static async Task Main(string[] args)
    {
    
        List<List<string>> lenguajes = new List<List<string>>();

   
        List<string> lenguajeActual = null;
        int Arch=1;
        while (true)
        {
            Console.Write($"\nIntroduce la ruta del Archivo {Arch} (o presiona Enter para usar ruta por defecto con \"\\archivo.txt\"): ");
            Console.WriteLine("Presione 0 para salir");
            string ruta = Console.ReadLine();
            Console.WriteLine($"RUTA: {ruta}, LENGUAJES.COUNT(): {lenguajes.Count()}");
            if(ruta=="0" && lenguajes.Count()!=0)
            {
                Console.WriteLine($"RUTA: {ruta}, LENGUAJES.COUNT(): {lenguajes.Count()}");
                break;
            }
            if (string.IsNullOrWhiteSpace(ruta))
            {
                ruta = $"archivo{Arch}.txt"; 
            }

            lenguajeActual = CargarLenguajeDesdeArchivo(ruta,Arch);
            Arch++;
            if(lenguajeActual is null)
                Arch--;
            if(lenguajeActual is not null)
                lenguajes.Add(lenguajeActual);
        }
        

        bool x = false;
        while (!x)
        {
            Thread.Sleep(7000);
            // Console.Clear();
            Console.WriteLine("Lenguajes cargados actualmente:");
            for (int i = 0; i < lenguajes.Count; i++)
            {
                Console.WriteLine($"  L{i + 1} = {{ {string.Join(", ", lenguajes[i])} }}");
            }

            Console.WriteLine("1. Unión");
            Console.WriteLine("2. Concatenación");
            Console.WriteLine("3. Potencia");
            Console.WriteLine("4. Cerradura Positiva");
            Console.WriteLine("5. Cerradura Estrella");
            Console.WriteLine("6. Reflexión");
            Console.WriteLine("7. Salir");

            string opcion = Console.ReadLine();
            switch (opcion)
            {
                case "1":
                    Union(lenguajes);
                    break;
                case "2":
                    Concatenar(lenguajes);
                    break;
                case "3":
                    Potencias(lenguajes);
                    break;
                case "4":
                    Cerradura(lenguajes);
                    break;
                case "5":
                    Estrella(lenguajes);
                    break;
                case "6":
                    Reflexion(lenguajes);
                    break;
                case "7":
                    x = true;
                    Console.WriteLine("Saliendo del programa");
                    break;
                default:
                    Console.WriteLine("Opción no válida");
                    break;
            }
        }
    }

    /// <summary>
    /// Lee un archivo CSV, separa por comas y retorna una List<string> limpia.
    // </summary>
    static List<string> CargarLenguajeDesdeArchivo(string ruta, int numeroArchivo)
    {
        try
        {
            if (!File.Exists(ruta))
            {
                Console.WriteLine($"[Aviso] El archivo '{ruta}' no se encontró.");
                return null;
            }

            string texto = File.ReadAllText(ruta);

            List<string> lenguaje = texto.Split(new char[] { ',' }, StringSplitOptions.RemoveEmptyEntries)
                                              .Select(palabra => palabra.Trim())
                                              .Where(palabra => !string.IsNullOrEmpty(palabra))
                                              .ToList();

            Console.WriteLine($"Archivo {numeroArchivo} cargado correctamente");
            return lenguaje;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"[Error] No se pudo leer el archivo: {ex.Message}");
            return null;
        }
    }

    static void Union(List<List<string>> lenguajes)
    {
        Console.Write("Seleccione lenguaje: ");
        if (int.TryParse(Console.ReadLine(), out int i) && i <= lenguajes.Count()&& i>0)
        {
            Console.Write("Seleccione lenguaje: ");
            if (int.TryParse(Console.ReadLine(), out int j) && i <= lenguajes.Count()&& i>0 && j!=i)
            {
                List<string> resultado = lenguajes[i - 1];
                foreach(string p1 in lenguajes[j-1])
                {
                    if(!resultado.Contains(p1))
                    {
                        resultado.Add(p1);
                    }
                }
                Console.WriteLine($"Lenguaje Resultante: {{ {string.Join(", ", resultado)} }}");
            }
            else { Console.WriteLine("Índice inválido."); }
        }
        else { Console.WriteLine("Índice inválido."); }
    }

    static void Concatenar(List<List<string>> lenguajes)
    {
        Console.Write("Seleccione el primer lenguaje: ");
        if (int.TryParse(Console.ReadLine(), out int i) && i <= lenguajes.Count()&& i>0)
        {
            Console.Write("Seleccione el segundo lenguaje: ");
            if (int.TryParse(Console.ReadLine(), out int j) && j <= lenguajes.Count())
            {
                List<string> L1 = lenguajes[i - 1];
                List<string> L2 = lenguajes[j - 1];
                List<string> concatenacion = new List<string>();

                foreach (string p1 in L1)
                    foreach (string p2 in L2)
                        concatenacion.Add(p1+p2);

                Console.WriteLine($"Lenguaje Resultante: {{ {string.Join(", ", concatenacion)} }}");
            }
            else { Console.WriteLine("Error, Intente de nuevo."); }
        }
        else { Console.WriteLine("Error, Intente de nuevo."); }
    }

    static void Potencias(List<List<string>> lenguajes)
    {
        Console.Write("Seleccione el lenguaje: ");
        if (int.TryParse(Console.ReadLine(), out int i) && i <= lenguajes.Count()&& i>0)
        {
            Console.Write("Introduce la potencia n (-5 a 8): ");
            if (int.TryParse(Console.ReadLine(), out int n) && n >= -5 && n <= 8)
            {
                List<string> L = lenguajes[i - 1];

                if (n == 0)
                {
                    Console.WriteLine("El lenguaje a la potencia 0 es la cadena vacía: { λ }");
                    return;
                } 
                else if (n < 0)
                {
                    List<string> invertida = new List<string>();
                    foreach (string c1 in L)
                    {
                        char[] pI = c1.ToCharArray();
                        Array.Reverse(pI);
                        invertida.Add(new string(pI));
                    }
                    L = invertida; 
                    n = n*-1;
                }
                List<string> resultado = L;
                for (int k = 2; k <= n; k++)
                {
                    List<string> aux = new List<string>();
                    foreach (string p1 in resultado)
                    {
                        foreach (string p2 in L)
                        {
                            aux.Add(p1 + p2);
                        }
                    }
                    resultado = aux;
                }

                Console.WriteLine($"Resultado (L^{n}): {{ {string.Join(", ", resultado)} }}");
            }
            else { Console.WriteLine("No es posible hacer la operacion con esa potencia"); }
        }
        else { Console.WriteLine("Error, Intente de nuevo."); }
    }

    static void Cerradura(List<List<string>> lenguajes)
    {
        Console.Write("Seleccione el lenguaje: ");
        if (int.TryParse(Console.ReadLine(), out int i) && i <= lenguajes.Count() && i>0)
        {
            List<string> L = lenguajes[i - 1];
            List<string> resultado = L;
            List<string> aux1 =L;

            for (int p = 2; p <= 4; p++)
            {
                List<string> aux2 = new List<string>();
                foreach (string p1 in aux1)
                {
                    foreach (string p2 in L)
                    {
                        aux2.Add(p1 + p2);
                    }
                }
                aux1 = aux2;
                foreach (string cadena in aux1)
                {
                    resultado.Add(cadena);
                }
            }

            Console.WriteLine($"Resultado (L^+): {{ {string.Join(", ", resultado)} }}");
        }
        else { Console.WriteLine("Error, Intente de nuevo."); }
    }

    static void Estrella(List<List<string>> lenguajes)
    {
        Console.WriteLine("\nCerradura de estrella");
        Console.Write("Elige el lenguaje a operar (1, 2 o 3): ");
        if (int.TryParse(Console.ReadLine(), out int i) && i<lenguajes.Count()&& i>0)
        {
            List<string> L = lenguajes[i - 1];
            List<string> resultado = new List<string> { "λ" };
            foreach (string p in L)
                resultado.Add(p);
            List<string> aux1 =L;

            for (int p = 2; p <= 4; p++)
            {
                List<string> aux2 = new List<string>();
                foreach (string p1 in aux1)
                {
                    foreach (string p2 in L)
                    {
                        aux2.Add(p1 + p2);
                    }
                }
                aux1 = aux2;
                foreach (string cadena in aux1)
                {
                    resultado.Add(cadena);
                }
            }

            Console.WriteLine($"Resultado: {{ {string.Join(", ", resultado)} }}");
        }
        else { Console.WriteLine("Error, Intente de nuevo."); }
    }

    static void Reflexion(List<List<string>> lenguajes)
    {
        Console.WriteLine("\nReflexion del lengiaje");
        Console.Write("Seleccione el lenguaje: ");
        if (int.TryParse(Console.ReadLine(), out int i) && i<lenguajes.Count())
        {
            List<string> L = lenguajes[i - 1];
            List<string> resultado = new List<string>();

            foreach (string p1 in L)
            {
                char[] charArray = p1.ToCharArray();
                Array.Reverse(charArray);
                string invertida = new string(charArray);
                resultado.Add(invertida);
            }

            Console.WriteLine($"Resultado{{ {string.Join(", ", resultado)} }}");
        }
        else { Console.WriteLine("Error, Intente de nuevo."); }
    }
}