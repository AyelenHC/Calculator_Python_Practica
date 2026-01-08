from app.interfaz.calculator_gui import CalculatorGUI
from app.logica.calculator import Calculator

if __name__ == "__main__":
    logic = Calculator()
    app = CalculatorGUI(logic)
    app.run()