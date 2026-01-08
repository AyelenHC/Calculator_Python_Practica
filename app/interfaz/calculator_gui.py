import tkinter as tk
import customtkinter as ctk
import re

ctk.set_appearance_mode("light")

# Create class CalculatorGUI
class CalculatorGUI:
    """
        Class to create the GUI of the calculator
    """
    def __init__(self, calculator):
        """
            Create the window for the calculator
        """
        self.calc = calculator
        self.root = ctk.CTk()
        self.root.title("Calculadora Simple")
        self.root.geometry("500x700+50+50")
        self.root.resizable(False, False)
        self.root.iconbitmap('iconAyelen.ico')
        self.root.configure(fg_color = "white")
        self.root.bind("<Key>", self.capture_keyboard)
        
        # Screen Frame 
        frame_screen = ctk.CTkFrame(self.root, height = 100, fg_color = "#f6c9a8", corner_radius = 15, border_width = 2, border_color = "#FDBD8B")
        frame_screen.pack(fill="x", padx = 15, pady = 15) # Se estira en el eje x
        frame_screen.pack_propagate(False)

        self.secondary_display = tk.StringVar()
        self.secondary_display.set("")
        self.screen = ctk.CTkLabel(
                            frame_screen,
                            textvariable = self.secondary_display,
                            font = ("Helvetica", 12, "bold"),
                            text_color = "#C4530E",
                            anchor = "e"
                        )
        self.screen.pack(expand=True, padx=10, pady=5)

        self.screen_text = tk.StringVar()
        self.screen_text.set("0")
        self.number_text = ""
        self.screen = ctk.CTkLabel(
                            frame_screen,
                            textvariable = self.screen_text,
                            font = ("Helvetica", 30, "bold"),
                            text_color = "#C4530E",
                            anchor = "e"
                        )
        self.screen.pack(expand=True, fill="both", padx=10, pady=10)

        # Button Frame
        frame_buttons = ctk.CTkFrame(self.root, fg_color="#fefaf6")
        frame_buttons.pack(expand = True, fill = "both", padx = 15, pady = 10)
        
        for i in range(5):
            frame_buttons.rowconfigure(i, weight = 1)
        for j in range(4):
            frame_buttons.columnconfigure(j, weight = 1)

        # Operations
        self.operator_control = ""

        button_clearAll = ctk.CTkButton(
            frame_buttons,
            text = "AC",
            font = ("Helvetica", 20),
            fg_color = "#f0a269",
            text_color = "#ffffff",
            hover_color = "#e76f51",
            border_width = 1,
            border_color = "#FC8126",
            command = lambda symbol = "AC": self.clear_calculator(symbol)
        )
        button_clearAll.grid(row = 0, column = 2, sticky = "nsew", padx = 7, pady = 7)
        
        button_clear = ctk.CTkButton(
            frame_buttons,
            text = "←",
            font = ("Helvetica", 20),
            fg_color = "#f0a269",
            text_color = "#ffffff",
            hover_color = "#e76f51",
            border_width = 1,
            border_color = "#FC8126",
            command = lambda symbol = "DEL": self.clear_calculator(symbol)
        )
        button_clear.grid(row = 0, column = 1, sticky="nsew", padx=7, pady=7)
        
        self.operators = ["+", "-", "*", "/", "="]
        for row, operator in enumerate(self.operators):
            ctk.CTkButton(
                frame_buttons,
                text = operator,
                font = ("Helvetica", 18, "bold"),
                fg_color = "#f0a269",
                text_color = "#ffffff",
                hover_color = "#e76f51",
                border_width = 1,
                border_color = "#FC8126",
                command = lambda op = operator : self.operation_calculator(op)
            ).grid(row = row, column = 3, sticky = "nsew", padx = 7, pady = 7)

        # numbers
        number = 9
        aux = 2
        for row in range(1, 5):
            for col in range(3):
                if number == 0:
                    aux = 0

                if number >= 0:
                    ctk.CTkButton(
                        frame_buttons,
                        text = str(number),
                        font = ("Helvetica", 18),
                        fg_color = "#f5f5f5",
                        text_color = "#333333",
                        hover_color = "#e0e0e0",
                        border_width = 1,
                        border_color = "#8A8A87",
                        corner_radius = 10,
                        command = lambda n = number: self.number_calculator(n)
                    ).grid(row = row, column = aux - col, sticky = "nsew", padx = 7, pady = 7)
                    number -= 1
        
        button_comma = ctk.CTkButton(
                            frame_buttons,
                            text = " . ",
                            font = ("Helvetica", 24),
                            fg_color = "#f5f5f5",
                            hover_color = "#FFE1CF",
                            text_color = "#333333",
                            border_width = 1,
                            border_color = "#8A8A87",
                            corner_radius = 10,
                            command = lambda: self.comma_calculator()
                        ).grid(row = 4 , column = 1, sticky = "nsew", padx = 7, pady = 7)


    def comma_calculator(self):
        actual_text = self.screen_text.get()
        # No more than one comma is allowed
        parts = re.split(r'[\+\-\*\/]', actual_text) # expresion regular para dividir el texto solo por los operadores matemáticos
        
        if "." in parts[-1]:
            return
        self.screen_text.set(actual_text + ".")


    def operation_method(self, operation):
        num1 = self.calc.getNum1()
        num2 = self.calc.getNum2()

        if operation == "+":
            return self.calc.add(num1, num2)
        elif operation == "-":
            return self.calc.subtract(num1, num2)
        elif operation == "*":
            return self.calc.multiply(num1, num2)
        elif operation == "/":
            if num2 == 0:
                return None
            return self.calc.divide(num1, num2)

    
    def find_operator_index(self, text, operator):
        """
        Searches for the operator position from right to left.
        Distinguishes between a '-' that is a subtraction operator and a '-' that is a negative sign.
        
        Args:
            text: The screen text (e.g.: "-1--1")
            operator: The operator to search for (e.g.: "-")
        
        Returns:
            The index of the operator, or -1 if not found
        """
        # Search from right to left
        for i in range(len(text) - 1, -1, -1): # termina antes del -1 y incrementa en 1
            if text[i] == operator:
                if i == 0:
                    continue
                if text[i - 1].isdigit() or text[i - 1] == '.':
                    return i
                    
        return -1

    def operation_calculator(self, operator):
        """
            Process mathematical operations and operator input.
            Handles operator insertion, calculation execution, and result display.
            Special handling for negative numbers and operator replacement.
            Args:
                operator: The operator to process ("+", "-", "*", "/", or "=")
        """
        actual_text = self.screen_text.get()
        op_aux = self.operator_control

        if operator == "-":
            if actual_text.endswith("--"):
                return

            if actual_text[-1] in self.operators:
                self.screen_text.set(actual_text + "-")
                return

        if actual_text[-1] in self.operators:
            new_text = actual_text[:-1] + operator
            self.screen_text.set(new_text)
            self.operator_control = operator
            return
                
        if op_aux:
            indice = self.find_operator_index(actual_text, op_aux)
            
            if indice == -1:  # No se encontró el operador
                return
            
            num2_str = actual_text[indice + 1:]

            if num2_str:
                self.calc.setNum2(float(num2_str))
                result = self.operation_method(self.operator_control)

                # Control para la division por 0
                if result == None:
                    result = "Error"
                    self.screen_text.set(result)
                    self.root.after(1500, lambda: self.screen_text.set("0"))
                    return

                # clean format --> only 10 decimal

                clean_format = "{:.10f}".format(result).rstrip('0').rstrip('.') # Esto se realiza de forma secuencial 1ero: format, 2do rstrip('0') y por ultimo,rstrip('.') 
                # "{:.10f}".format(result): formatea result con 10 decimales como máximo. --> result = 3.01212 pasa a 3.0121200000
                # .rstrip('0'): elimina ceros finales a la derecha. --> result = 3.0121200000 pasa a 3.01212
                # .rstrip('.'): elimina el punto decimal si queda solo. --> result = 5. pasa a ser 5

                self.screen_text.set(clean_format)
        
        if operator == "=":
            self.operator_control = ""
        else:
            self.operator_control = operator
            actual_text = self.screen_text.get()
            if actual_text[-1] in self.operators or actual_text.endswith("."):
                return
            self.calc.setNum1(float(actual_text))
            self.calc.setNum2(0)
            self.screen_text.set(actual_text + operator)
                

    def clear_calculator(self, symbol):
        """
            Clear or delete characters form the calculator screen
            Args:
                symbol: The clear action to perform
                    - DEL : Delete the last character from the screen
                    - AC : Clears all content and resets the calculator
        """
        if symbol == "DEL":
            actual_text = self.screen_text.get()
            self.screen_text.set(actual_text[:-1])

            if self.screen_text.get() == "":
                self.screen_text.set("0")
            
        if symbol == "AC":
            self.screen_text.set("0")
            self.calc.clear()

    
    def number_calculator(self, number):
        """
            Display the number on the calculator screen
            Args:
                number: the number to display
        """
        actual_text = ""
        if self.screen_text.get() != "0": # Control for 0 initial in screen_text
            actual_text = self.screen_text.get()

        new_value = actual_text + str(number)
        self.screen_text.set(new_value)

    def capture_keyboard(self, event):
        """
            Capture keyboard input and allow using the keyboard to interact with the calculator.
            Processes numbers (0-9), operators (+, -, *, /) and the Enter key to perform operations.
            Args:
                event: keyboard event captured by Tkinter
        """
        key = event.char  
        if key.isdigit():
            self.number_calculator(int(key))
        elif key in ["+", "-", "*", "/"]:
            self.operation_calculator(key)
        elif key == "\r": # Key Enter
            self.operation_calculator("=")

    def run(self):
        """
            Run the calculator
        """
        self.root.mainloop()