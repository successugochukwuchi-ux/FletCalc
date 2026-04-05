import flet as ft
import math

def main(page: ft.Page):
    page.title = "Scientific Calculator"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 10
    page.window_width = 400
    page.window_height = 750
    page.bgcolor = "#1a1a2e"
    
    # Display value
    display_value = ft.Text("0", size=32, text_align=ft.TextAlign.END, color="#ffffff")
    expression_display = ft.Text("", size=16, text_align=ft.TextAlign.END, color="#888888")
    
    # Current input buffer
    current_input = ""
    current_expression = ""
    is_result_shown = False
    is_degree = True  # Default to degrees for trig functions
    
    def update_display():
        if current_input:
            display_value.value = current_input
        elif current_expression:
            display_value.value = current_expression
        else:
            display_value.value = "0"
        page.update()
    
    def btn_click(e):
        nonlocal current_input, current_expression, is_result_shown, is_degree
        
        data = e.control.data
        
        if data == "C":
            current_input = ""
            current_expression = ""
            is_result_shown = False
        elif data == "CE":
            current_input = ""
            is_result_shown = False
        elif data == "⌫":
            if current_input:
                current_input = current_input[:-1]
        elif data == "=":
            try:
                # Replace display symbols with Python operators
                expr = current_expression + current_input
                expr = expr.replace("×", "*").replace("÷", "/").replace("π", "math.pi").replace("e", "math.e")
                
                # Handle scientific functions
                expr = expr.replace("sin(", "math.sin(").replace("cos(", "math.cos(").replace("tan(", "math.tan(")
                expr = expr.replace("asin(", "math.asin(").replace("acos(", "math.acos(").replace("atan(", "math.atan(")
                expr = expr.replace("log(", "math.log10(").replace("ln(", "math.log(")
                expr = expr.replace("sqrt(", "math.sqrt(").replace("abs(", "abs(")
                expr = expr.replace("^", "**").replace("!", "factorial(")
                
                # Convert degrees to radians for trig functions if in degree mode
                if is_degree:
                    # For trig functions in degree mode
                    expr = expr.replace("math.sin(", "math.sin(math.radians(")
                    expr = expr.replace("math.cos(", "math.cos(math.radians(")
                    expr = expr.replace("math.tan(", "math.tan(math.radians(")
                    # This is a simplified approach - may need adjustment for complex expressions
                
                result = eval(expr)
                
                # Format result
                if isinstance(result, float):
                    if result == int(result):
                        result = int(result)
                    else:
                        result = round(result, 10)
                
                current_expression = ""
                current_input = str(result)
                is_result_shown = True
            except Exception as ex:
                current_input = "Error"
                is_result_shown = True
        elif data in ["+", "-", "×", "÷", "^"]:
            current_expression += current_input + " " + data + " "
            current_input = ""
            is_result_shown = False
        elif data == ".":
            if "." not in current_input:
                current_input += "."
        elif data == "±":
            if current_input:
                if current_input.startswith("-"):
                    current_input = current_input[1:]
                else:
                    current_input = "-" + current_input
        elif data == "%":
            if current_input:
                try:
                    val = float(current_input) / 100
                    current_input = str(val)
                except:
                    pass
        elif data == "1/x":
            if current_input:
                try:
                    val = 1 / float(current_input)
                    current_input = str(val)
                except:
                    current_input = "Error"
        elif data == "x²":
            if current_input:
                try:
                    val = float(current_input) ** 2
                    current_input = str(val)
                except:
                    current_input = "Error"
        elif data == "√":
            if current_input:
                current_expression += f"sqrt({current_input})"
                current_input = ""
            else:
                current_expression += "sqrt("
        elif data == "x!":
            if current_input:
                try:
                    val = math.factorial(int(float(current_input)))
                    current_input = str(val)
                except:
                    current_input = "Error"
        elif data == "sin":
            current_expression += "sin("
            current_input = ""
        elif data == "cos":
            current_expression += "cos("
            current_input = ""
        elif data == "tan":
            current_expression += "tan("
            current_input = ""
        elif data == "asin":
            current_expression += "asin("
            current_input = ""
        elif data == "acos":
            current_expression += "acos("
            current_input = ""
        elif data == "atan":
            current_expression += "atan("
            current_input = ""
        elif data == "log":
            current_expression += "log("
            current_input = ""
        elif data == "ln":
            current_expression += "ln("
            current_input = ""
        elif data == "π":
            current_input += "π"
        elif data == "e":
            current_input += "e"
        elif data == "(":
            current_expression += "("
            current_input = ""
        elif data == ")":
            current_expression += current_input + ")"
            current_input = ""
        elif data == "DEG":
            is_degree = not is_degree
            if is_degree:
                deg_rad_btn.text = "DEG"
            else:
                deg_rad_btn.text = "RAD"
            deg_rad_btn.bgcolor = "#4a90d9"
            page.update()
        else:
            # Number input
            if is_result_shown and data.isdigit():
                current_input = data
                current_expression = ""
                is_result_shown = False
            else:
                current_input += data
            is_result_shown = False
        
        update_display()
    
    # Button style
    btn_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=15),
        padding=ft.padding.all(15),
    )
    
    num_btn_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=15),
        padding=ft.padding.all(15),
        bgcolor="#2d2d44",
        color="#ffffff",
    )
    
    op_btn_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=15),
        padding=ft.padding.all(15),
        bgcolor="#4a90d9",
        color="#ffffff",
    )
    
    sci_btn_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=15),
        padding=ft.padding.all(15),
        bgcolor="#3d3d5c",
        color="#ffffff",
    )
    
    func_btn_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=15),
        padding=ft.padding.all(15),
        bgcolor="#5c5c7a",
        color="#ffffff",
    )
    
    def create_btn(text, data, style=None):
        return ft.ElevatedButton(
            text=text,
            data=data,
            on_click=btn_click,
            style=style or num_btn_style,
            min_width=70,
            min_height=55,
        )
    
    # Degree/Radian toggle button
    deg_rad_btn = ft.ElevatedButton(
        text="DEG",
        data="DEG",
        on_click=btn_click,
        style=func_btn_style,
        min_width=60,
        min_height=45,
    )
    
    # Scientific functions row 1
    sci_row1 = ft.Row(
        controls=[
            deg_rad_btn,
            create_btn("sin", "sin", sci_btn_style),
            create_btn("cos", "cos", sci_btn_style),
            create_btn("tan", "tan", sci_btn_style),
            create_btn("log", "log", sci_btn_style),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    )
    
    # Scientific functions row 2
    sci_row2 = ft.Row(
        controls=[
            create_btn("asin", "asin", sci_btn_style),
            create_btn("acos", "acos", sci_btn_style),
            create_btn("atan", "atan", sci_btn_style),
            create_btn("ln", "ln", sci_btn_style),
            create_btn("e", "e", sci_btn_style),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    )
    
    # Scientific functions row 3
    sci_row3 = ft.Row(
        controls=[
            create_btn("π", "π", sci_btn_style),
            create_btn("x²", "x²", sci_btn_style),
            create_btn("x!", "x!", sci_btn_style),
            create_btn("√", "√", sci_btn_style),
            create_btn("^", "^", sci_btn_style),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    )
    
    # Scientific functions row 4
    sci_row4 = ft.Row(
        controls=[
            create_btn("(", "(", sci_btn_style),
            create_btn(")", ")", sci_btn_style),
            create_btn("1/x", "1/x", sci_btn_style),
            create_btn("abs", "abs", sci_btn_style),
            create_btn("%", "%", sci_btn_style),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    )
    
    # Main calculator buttons
    clear_row = ft.Row(
        controls=[
            create_btn("C", "C", func_btn_style),
            create_btn("CE", "CE", func_btn_style),
            create_btn("⌫", "⌫", func_btn_style),
            create_btn("÷", "÷", op_btn_style),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    )
    
    num_row1 = ft.Row(
        controls=[
            create_btn("7", "7"),
            create_btn("8", "8"),
            create_btn("9", "9"),
            create_btn("×", "×", op_btn_style),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    )
    
    num_row2 = ft.Row(
        controls=[
            create_btn("4", "4"),
            create_btn("5", "5"),
            create_btn("6", "6"),
            create_btn("-", "-", op_btn_style),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    )
    
    num_row3 = ft.Row(
        controls=[
            create_btn("1", "1"),
            create_btn("2", "2"),
            create_btn("3", "3"),
            create_btn("+", "+", op_btn_style),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    )
    
    num_row4 = ft.Row(
        controls=[
            create_btn("±", "±"),
            create_btn("0", "0"),
            create_btn(".", ".", num_btn_style),
            create_btn("=", "=", op_btn_style),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    )
    
    # Display container
    display_container = ft.Container(
        content=ft.Column(
            controls=[
                expression_display,
                display_value,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.END,
        ),
        padding=ft.padding.all(20),
        bgcolor="#16213e",
        border_radius=15,
        margin=ft.margin.only(bottom=10),
    )
    
    # Build the page
    page.add(
        display_container,
        sci_row1,
        sci_row2,
        sci_row3,
        sci_row4,
        ft.Divider(height=10, color="transparent"),
        clear_row,
        num_row1,
        num_row2,
        num_row3,
        num_row4,
    )

if __name__ == "__main__":
    ft.run(target=main, view=ft.AppView.WEB_BROWSER)
