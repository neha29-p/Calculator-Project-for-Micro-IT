from IPython.display import display, clear_output
import ipywidgets as widgets

# Input fields
num1 = widgets.FloatText(description="Number 1:", value=0)
num2 = widgets.FloatText(description="Number 2:", value=0)

# Dropdown to choose operation (Corrected: keys are labels, values are actual operation symbols)
operation = widgets.Dropdown(
    options={'Addition': '+', 'Subtraction': '-', 'Multiplication': '*', 'Division': '/'},
    value='+',
    description='Operation:'
)

# Output display
output = widgets.Output()

# Button to calculate
button = widgets.Button(description="Calculate", button_style='success')

# Function to perform calculation
def calculate(b):
    with output:
        clear_output()
        try:
            if operation.value == '+':
                result = num1.value + num2.value
            elif operation.value == '-':
                result = num1.value - num2.value
            elif operation.value == '*':
                result = num1.value * num2.value
            elif operation.value == '/':
                if num2.value == 0:
                    print("Error: Cannot divide by zero.")
                    return
                result = num1.value / num2.value

            print(f"Result: {result}")
        except Exception as e:
            print("Error:", e)

# Button click event
button.on_click(calculate)

# Layout
display(widgets.VBox([num1, num2, operation, button, output]))
