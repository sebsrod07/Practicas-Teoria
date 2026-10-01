using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        // Diccionario o lista para almacenar los tres lenguajes cargados
        // Cada lenguaje será un HashSet<string> para garantizar que no haya palabras repetidas.
        List<HashSet<string>> lenguajes = new List<HashSet<string>>();

        Console.WriteLine("=== PRÁCTICA 2: OPERACIONES ENTRE LENGUAJES ===");

        // 1. CARGA DE ARCHIVOS
        for (int i = 1; i <= 3; i++)
        {
            HashSet<string> lenguajeActual = null;
            while (lenguajeActual == null)
            {
                Console.Write($"\nIntroduce la ruta del Archivo {i} (o presiona Enter para usar ruta por defecto): ");
                string ruta = Console.ReadLine();

                if (string.IsNullOrWhiteSpace(ruta))
                {
                    // Rutas por defecto de prueba (puedes cambiarlas si gustas)
                    ruta = $"archivo{i}.txt"; 
                }

                lenguajeActual = CargarLenguajeDesdeArchivo(ruta, i);
            }
            lenguajes.Add(lenguajeActual);
        }

        // 2. MENÚ INTERACTIVO (Ciclo hasta que el usuario decida salir)
        bool salir = false;
        while (!salir)
        {
            Console.WriteLine("\n--- MENÚ PRINCIPAL ---");
            Console.WriteLine("Lenguajes cargados actualmente:");
            for (int i = 0; i < lenguajes.Count; i++)
            {
                Console.WriteLine($"  L{i + 1} = {{ {string.Join(", ", lenguajes[i])} }}");
            }

            Console.WriteLine("\nElige una opción:");
            Console.WriteLine("1. Unión (Li ∪ Lj)");
            Console.WriteLine("2. Concatenación (Li • Lj)");
            Console.WriteLine("3. Potencia (L^n, rango -5 a 8)");
            Console.WriteLine("4. Cerradura Positiva (L^+)");
            Console.WriteLine("5. Cerradura de Kleene (L*)");
            Console.WriteLine("6. Reflexión / Inversión (L^-1)");
            Console.WriteLine("7. Salir");
            Console.Write("Opción: ");

            string opcion = Console.ReadLine();

            switch (opcion)
            {
                case "1":
                    EjecutarUnion(lenguajes);
                    break;
                case "2":
                    EjecutarConcatenacion(lenguajes);
                    break;
                case "3":
                    EjecutarPotencia(lenguajes);
                    break;
                case "4":
                    EjecutarCerraduraPositiva(lenguajes);
                    break;
                case "5":
                    EjecutarCerraduraKleene(lenguajes);
                    break;
                case "6":
                    EjecutarReflexion(lenguajes);
                    break;
                case "7":
                    salir = true;
                    Console.WriteLine("¡Saliendo del programa!");
                    break;
                default:
                    Console.WriteLine("Opción no válida. Inténtalo de nuevo.");
                    break;
            }
        }
    }

    /// <summary>
    /// Lee un archivo de texto, ignora espacios múltiples y saltos de línea, 
    /// y extrae todas las palabras separadas en un HashSet.
    /// </summary>
    static HashSet<string> CargarLenguajeDesdeArchivo(string ruta, int numeroArchivo)
    {
        try
        {
            if (!File.Exists(ruta))
            {
                // Si el archivo no existe físicamente, te sugerimos crearlo o avisamos
                Console.WriteLine($"[Aviso] El archivo '{ruta}' no se encontró en disco.");
                Console.WriteLine($"Creando un archivo de prueba predeterminado para el Archivo {numeroArchivo}...");
                
                string contenidoEjemplo = numeroArchivo == 1 ? "azul amarillo rojo verde rosa naranja morado blanco" :
                                          numeroArchivo == 2 ? "perro gato conejo tortuga mariposa ratón león" :
                                                               "cuadrado círculo triángulo rectángulo hexágono";
                File.WriteAllText(ruta, contenidoEjemplo);
            }

            // Lee todo el texto del archivo
            string textoTotal = File.ReadAllText(ruta);

            // Divide por cualquier carácter de espacio en blanco (espacios, tabulaciones, saltos de línea)
            string[] palabras = textoTotal.Split(new char[] { ' ', '\r', '\n', '\t' }, StringSplitOptions.RemoveEmptyEntries);

            HashSet<string> lenguaje = new HashSet<string>(palabras);
            Console.WriteLine($"[Éxito] Archivo {numeroArchivo} cargado correctamente con {lenguaje.Count} palabras.");
            return lenguaje;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"[Error] No se pudo leer el archivo: {ex.Message}");
            return null;
        }
    }

    // Métodos vacíos listos para que implementes la lógica matemática que prefieras:
    static void EjecutarUnion(List<HashSet<string>> lenguajes)
    {
        Console.WriteLine("\n[Operación: Unión]");
        // TODO: Pedir índices i y j, aplicar UnionWith o LINQ Union, y mostrar resultado.
    }

    static void EjecutarConcatenacion(List<HashSet<string>> lenguajes)
    {
        Console.WriteLine("\n[Operación: Concatenación]");
        // TODO: Multiplicar cada palabra de Li con cada palabra de Lj (aquí puedes integrar tu lógica en C para concatenar cadenas).
    }

    static void EjecutarPotencia(List<HashSet<string>> lenguajes)
    {
        Console.WriteLine("\n[Operación: Potencia (-5 a 8)]");
        // TODO: Manejar potencias negativas (reflexión inversa) y positivas (concatenaciones sucesivas).
    }

    static void EjecutarCerraduraPositiva(List<HashSet<string>> lenguajes)
    {
        Console.WriteLine("\n[Operación: Cerradura Positiva (L^1 ∪ L^2 ∪ L^3 ∪ L^4)]");
        // TODO: Unir las potencias de 1 a 4.
    }

    static void EjecutarCerraduraKleene(List<HashSet<string>> lenguajes)
    {
        Console.WriteLine("\n[Operación: Cerradura de Kleene (λ ∪ L^1 ∪ L^2 ∪ L^3 ∪ L^4)]");
        // TODO: Añadir cadena vacía (lambda/epsilon) y unir potencias de 1 a 4.
    }

    static void EjecutarReflexion(List<HashSet<string>> lenguajes)
    {
        Console.WriteLine("\n[Operación: Reflexión (L^-1)]");
        // TODO: Invertir los caracteres de cada cadena del lenguaje seleccionado.
    }
}