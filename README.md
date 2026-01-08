# 🔢 CALCULADORA SIMPLE
_Programa de una calculadora gráfica construida con Python y CustomTkinter._

La aplicación consiste en una interfaz gráfica interactiva diseñada para realizar cálculos matemáticos simples, permitiendo la entrada de datos tanto por clics como por teclado físico.

<p align = "center" >
  <img width="450" height="600" alt="image" src="https://github.com/user-attachments/assets/0f4d7042-f475-4430-bd2c-15a1a66f3cdc" />
</p>

## ✨ Entrada
El sistema se encuentra en un estado de escucha constante (Event Loop), esperando una acción del usuario:

* **Interfaz Gráfica**: Botones clicables para números y operadores.
* **Teclado Físico**: Mapeo de teclas numéricas y operadores básicos.
* **Control de Ejecución**: La tecla Enter está vinculada directamente al operador =, permitiendo procesar la operación sin usar el ratón.


## ꩜ Lógica de Operación

El flujo de trabajo sigue el modelo de operación binaria:
1. **Entrada**: El usuario ingresa el primer operando.
2. **Selección**: Se elige una operación básica: Suma (+), Resta (-), Multiplicación (*) o División (/).
3. **Procesamiento**: Tras ingresar el segundo operando y presionar = (o Enter), el sistema calcula:
<p align = "center">
  <b> Resultado </b> = <b> A </b> op <b> B </b>
</p>
5. **Salida**: El resultado se despliega inmediatamente en la pantalla principal.

> [!NOTE]
> ### **Instalación**
> 1. Clona el repositorio.
> 
> 2. Instala las dependencias: pip install customtkinter
>
> 3. Ejecuta: python main.py
