import flet as ft
import math
from datetime import datetime, timedelta

def main(page: ft.Page):
    page.title = "Multi-Mode Calculator"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.window_width = 900
    page.window_height = 700
    page.bgcolor = "#1a1a2e"
    
    # Global state
    current_mode = "standard"
    
    # ==================== STANDARD CALCULATOR STATE ====================
    std_display_value = ft.Text("0", size=32, text_align=ft.TextAlign.END, color="#ffffff")
    std_expression_display = ft.Text("", size=16, text_align=ft.TextAlign.END, color="#888888")
    std_current_input = ""
    std_current_expression = ""
    std_is_result_shown = False
    
    # ==================== SCIENTIFIC CALCULATOR STATE ====================
    sci_display_value = ft.Text("0", size=32, text_align=ft.TextAlign.END, color="#ffffff")
    sci_expression_display = ft.Text("", size=16, text_align=ft.TextAlign.END, color="#888888")
    sci_current_input = ""
    sci_current_expression = ""
    sci_is_result_shown = False
    sci_is_degree = True
    
    # ==================== CURRENCY CONVERSION STATE ====================
    currency_rates = {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.79,
        "JPY": 149.50,
        "CAD": 1.36,
        "AUD": 1.52,
        "CHF": 0.88,
        "CNY": 7.23,
        "INR": 83.12,
        "MXN": 17.15,
        "BRL": 4.97,
        "ZAR": 18.95,
        "KRW": 1305.50,
        "SGD": 1.34,
        "HKD": 7.82,
        "NOK": 10.68,
        "SEK": 10.42,
        "DKK": 6.87,
        "NZD": 1.63,
        "RUB": 92.50,
        "TRY": 32.15,
    }
    
    currency_amount = ft.TextField(value="1", width=150, hint_text="Amount", text_size=16)
    currency_from = ft.Dropdown(
        options=[ft.dropdown.Option(k, k) for k in currency_rates.keys()],
        value="USD",
        width=120,
        text_size=14,
        label="From"
    )
    currency_to = ft.Dropdown(
        options=[ft.dropdown.Option(k, k) for k in currency_rates.keys()],
        value="EUR",
        width=120,
        text_size=14,
        label="To"
    )
    currency_result = ft.Text("0.00", size=24, color="#4a90d9")
    
    # ==================== TIME CALCULATOR STATE ====================
    time_operation = ft.Dropdown(
        options=[
            ft.dropdown.Option("add", "Add Time"),
            ft.dropdown.Option("subtract", "Subtract Time"),
            ft.dropdown.Option("difference", "Time Difference"),
            ft.dropdown.Option("convert", "Convert Units"),
        ],
        value="add",
        width=180,
        text_size=14,
        label="Operation"
    )
    time_date1 = ft.TextField(label="Date 1", value=datetime.now().strftime("%Y-%m-%d"), width=180, text_size=14)
    time_date2 = ft.TextField(label="Date 2", value="", width=180, text_size=14)
    time_years = ft.TextField(label="Years", value="0", width=80, text_size=14)
    time_months = ft.TextField(label="Months", value="0", width=80, text_size=14)
    time_days = ft.TextField(label="Days", value="0", width=80, text_size=14)
    time_hours = ft.TextField(label="Hours", value="0", width=80, text_size=14)
    time_minutes = ft.TextField(label="Minutes", value="0", width=80, text_size=14)
    time_seconds = ft.TextField(label="Seconds", value="0", width=80, text_size=14)
    time_unit_from = ft.Dropdown(
        options=[
            ft.dropdown.Option("seconds", "Seconds"),
            ft.dropdown.Option("minutes", "Minutes"),
            ft.dropdown.Option("hours", "Hours"),
            ft.dropdown.Option("days", "Days"),
            ft.dropdown.Option("weeks", "Weeks"),
            ft.dropdown.Option("months", "Months"),
            ft.dropdown.Option("years", "Years"),
            ft.dropdown.Option("decades", "Decades"),
        ],
        value="days",
        width=120,
        text_size=14,
    )
    time_unit_to = ft.Dropdown(
        options=[
            ft.dropdown.Option("seconds", "Seconds"),
            ft.dropdown.Option("minutes", "Minutes"),
            ft.dropdown.Option("hours", "Hours"),
            ft.dropdown.Option("days", "Days"),
            ft.dropdown.Option("weeks", "Weeks"),
            ft.dropdown.Option("months", "Months"),
            ft.dropdown.Option("years", "Years"),
            ft.dropdown.Option("decades", "Decades"),
        ],
        value="years",
        width=120,
        text_size=14,
    )
    time_result = ft.Text("", size=20, color="#4a90d9")
    
    # ==================== VECTOR CALCULATOR STATE ====================
    vector_a_x = ft.TextField(label="A X", value="0", width=100, text_size=14)
    vector_a_y = ft.TextField(label="A Y", value="0", width=100, text_size=14)
    vector_a_z = ft.TextField(label="A Z", value="0", width=100, text_size=14)
    vector_b_x = ft.TextField(label="B X", value="0", width=100, text_size=14)
    vector_b_y = ft.TextField(label="B Y", value="0", width=100, text_size=14)
    vector_b_z = ft.TextField(label="B Z", value="0", width=100, text_size=14)
    vector_operation = ft.Dropdown(
        options=[
            ft.dropdown.Option("add", "Addition (A + B)"),
            ft.dropdown.Option("subtract", "Subtraction (A - B)"),
            ft.dropdown.Option("dot", "Dot Product (A · B)"),
            ft.dropdown.Option("cross", "Cross Product (A × B)"),
            ft.dropdown.Option("magnitude_a", "Magnitude |A|"),
            ft.dropdown.Option("magnitude_b", "Magnitude |B|"),
            ft.dropdown.Option("angle", "Angle Between"),
        ],
        value="add",
        width=200,
        text_size=14,
        label="Operation"
    )
    vector_result = ft.Text("", size=20, color="#4a90d9")
    
    # ==================== UNIT CONVERTER STATE ====================
    unit_category = ft.Dropdown(
        options=[
            ft.dropdown.Option("length", "Length"),
            ft.dropdown.Option("weight", "Weight"),
            ft.dropdown.Option("temperature", "Temperature"),
            ft.dropdown.Option("area", "Area"),
            ft.dropdown.Option("volume", "Volume"),
            ft.dropdown.Option("speed", "Speed"),
            ft.dropdown.Option("pressure", "Pressure"),
            ft.dropdown.Option("energy", "Energy"),
        ],
        value="length",
        width=180,
        text_size=14,
        label="Category"
    )
    unit_value = ft.TextField(value="1", width=120, hint_text="Value", text_size=14)
    unit_from = ft.Dropdown(width=140, text_size=14, label="From")
    unit_to = ft.Dropdown(width=140, text_size=14, label="To")
    unit_result = ft.Text("0.00", size=24, color="#4a90d9")
    
    unit_options = {
        "length": ["mm", "cm", "m", "km", "in", "ft", "yd", "mi"],
        "weight": ["mg", "g", "kg", "oz", "lb", "ton"],
        "temperature": ["C", "F", "K"],
        "area": ["mm²", "cm²", "m²", "km²", "in²", "ft²", "yd²", "acre", "hectare"],
        "volume": ["ml", "l", "m³", "in³", "ft³", "gal", "qt", "pt", "cup"],
        "speed": ["m/s", "km/h", "mph", "knot", "ft/s"],
        "pressure": ["Pa", "kPa", "bar", "psi", "atm", "mmHg"],
        "energy": ["J", "kJ", "cal", "kcal", "Wh", "kWh", "BTU"],
    }
    
    # ==================== HELPER FUNCTIONS ====================
    
    def update_unit_options(e=None):
        category = unit_category.value
        options = unit_options.get(category, [])
        unit_from.options = [ft.dropdown.Option(opt, opt) for opt in options]
        unit_to.options = [ft.dropdown.Option(opt, opt) for opt in options]
        if options:
            unit_from.value = options[0]
            unit_to.value = options[1] if len(options) > 1 else options[0]
        page.update()
    
    update_unit_options()
    
    # --- Standard Calculator Functions ---
    def std_btn_click(e):
        nonlocal std_current_input, std_current_expression, std_is_result_shown
        data = e.control.data
        
        if data == "C":
            std_current_input = ""
            std_current_expression = ""
            std_is_result_shown = False
        elif data == "CE":
            std_current_input = ""
            std_is_result_shown = False
        elif data == "⌫":
            if std_current_input:
                std_current_input = std_current_input[:-1]
        elif data == "=":
            try:
                expr = std_current_expression + std_current_input
                expr = expr.replace("×", "*").replace("÷", "/")
                result = eval(expr)
                if isinstance(result, float):
                    if result == int(result):
                        result = int(result)
                    else:
                        result = round(result, 10)
                std_current_expression = ""
                std_current_input = str(result)
                std_is_result_shown = True
            except:
                std_current_input = "Error"
                std_is_result_shown = True
        elif data in ["+", "-", "×", "÷"]:
            std_current_expression += std_current_input + " " + data + " "
            std_current_input = ""
            std_is_result_shown = False
        elif data == ".":
            if "." not in std_current_input:
                std_current_input += "."
        elif data == "±":
            if std_current_input:
                if std_current_input.startswith("-"):
                    std_current_input = std_current_input[1:]
                else:
                    std_current_input = "-" + std_current_input
        elif data == "%":
            if std_current_input:
                try:
                    val = float(std_current_input) / 100
                    std_current_input = str(val)
                except:
                    pass
        else:
            if std_is_result_shown and data.isdigit():
                std_current_input = data
                std_current_expression = ""
                std_is_result_shown = False
            else:
                std_current_input += data
            std_is_result_shown = False
        
        if std_current_input:
            std_display_value.value = std_current_input
        elif std_current_expression:
            std_display_value.value = std_current_expression
        else:
            std_display_value.value = "0"
        page.update()
    
    # --- Scientific Calculator Functions ---
    def sci_btn_click(e):
        nonlocal sci_current_input, sci_current_expression, sci_is_result_shown, sci_is_degree
        data = e.control.data
        
        if data == "C":
            sci_current_input = ""
            sci_current_expression = ""
            sci_is_result_shown = False
        elif data == "CE":
            sci_current_input = ""
            sci_is_result_shown = False
        elif data == "⌫":
            if sci_current_input:
                sci_current_input = sci_current_input[:-1]
        elif data == "=":
            try:
                expr = sci_current_expression + sci_current_input
                expr = expr.replace("×", "*").replace("÷", "/").replace("π", "math.pi").replace("e", "math.e")
                expr = expr.replace("sin(", "math.sin(").replace("cos(", "math.cos(").replace("tan(", "math.tan(")
                expr = expr.replace("asin(", "math.asin(").replace("acos(", "math.acos(").replace("atan(", "math.atan(")
                expr = expr.replace("log(", "math.log10(").replace("ln(", "math.log(")
                expr = expr.replace("sqrt(", "math.sqrt(").replace("abs(", "abs(")
                expr = expr.replace("^", "**").replace("!", "factorial(")
                
                if sci_is_degree:
                    expr = expr.replace("math.sin(", "math.sin(math.radians(")
                    expr = expr.replace("math.cos(", "math.cos(math.radians(")
                    expr = expr.replace("math.tan(", "math.tan(math.radians(")
                
                result = eval(expr)
                if isinstance(result, float):
                    if result == int(result):
                        result = int(result)
                    else:
                        result = round(result, 10)
                sci_current_expression = ""
                sci_current_input = str(result)
                sci_is_result_shown = True
            except Exception as ex:
                sci_current_input = "Error"
                sci_is_result_shown = True
        elif data in ["+", "-", "×", "÷", "^"]:
            sci_current_expression += sci_current_input + " " + data + " "
            sci_current_input = ""
            sci_is_result_shown = False
        elif data == ".":
            if "." not in sci_current_input:
                sci_current_input += "."
        elif data == "±":
            if sci_current_input:
                if sci_current_input.startswith("-"):
                    sci_current_input = sci_current_input[1:]
                else:
                    sci_current_input = "-" + sci_current_input
        elif data == "%":
            if sci_current_input:
                try:
                    val = float(sci_current_input) / 100
                    sci_current_input = str(val)
                except:
                    pass
        elif data == "1/x":
            if sci_current_input:
                try:
                    val = 1 / float(sci_current_input)
                    sci_current_input = str(val)
                except:
                    sci_current_input = "Error"
        elif data == "x²":
            if sci_current_input:
                try:
                    val = float(sci_current_input) ** 2
                    sci_current_input = str(val)
                except:
                    sci_current_input = "Error"
        elif data == "√":
            if sci_current_input:
                sci_current_expression += f"sqrt({sci_current_input})"
                sci_current_input = ""
            else:
                sci_current_expression += "sqrt("
        elif data == "x!":
            if sci_current_input:
                try:
                    val = math.factorial(int(float(sci_current_input)))
                    sci_current_input = str(val)
                except:
                    sci_current_input = "Error"
        elif data == "sin":
            sci_current_expression += "sin("
            sci_current_input = ""
        elif data == "cos":
            sci_current_expression += "cos("
            sci_current_input = ""
        elif data == "tan":
            sci_current_expression += "tan("
            sci_current_input = ""
        elif data == "asin":
            sci_current_expression += "asin("
            sci_current_input = ""
        elif data == "acos":
            sci_current_expression += "acos("
            sci_current_input = ""
        elif data == "atan":
            sci_current_expression += "atan("
            sci_current_input = ""
        elif data == "log":
            sci_current_expression += "log("
            sci_current_input = ""
        elif data == "ln":
            sci_current_expression += "ln("
            sci_current_input = ""
        elif data == "π":
            sci_current_input += "π"
        elif data == "e":
            sci_current_input += "e"
        elif data == "(":
            sci_current_expression += "("
            sci_current_input = ""
        elif data == ")":
            sci_current_expression += sci_current_input + ")"
            sci_current_input = ""
        elif data == "DEG":
            sci_is_degree = not sci_is_degree
            if sci_is_degree:
                deg_rad_btn.content = ft.Text("DEG", size=16)
            else:
                deg_rad_btn.content = ft.Text("RAD", size=16)
            deg_rad_btn.bgcolor = "#4a90d9"
            page.update()
            return
        else:
            if sci_is_result_shown and data.isdigit():
                sci_current_input = data
                sci_current_expression = ""
                sci_is_result_shown = False
            else:
                sci_current_input += data
            sci_is_result_shown = False
        
        if sci_current_input:
            sci_display_value.value = sci_current_input
        elif sci_current_expression:
            sci_display_value.value = sci_current_expression
        else:
            sci_display_value.value = "0"
        page.update()
    
    # --- Currency Conversion Function ---
    def convert_currency(e):
        try:
            amount = float(currency_amount.value)
            from_curr = currency_from.value
            to_curr = currency_to.value
            
            amount_in_usd = amount / currency_rates[from_curr]
            result = amount_in_usd * currency_rates[to_curr]
            currency_result.value = f"{result:.2f} {to_curr}"
        except:
            currency_result.value = "Error"
        page.update()
    
    # --- Time Calculator Function ---
    def calculate_time(e):
        try:
            op = time_operation.value
            
            if op == "add":
                base_date = datetime.strptime(time_date1.value, "%Y-%m-%d")
                years = int(time_years.value or 0)
                months = int(time_months.value or 0)
                days = int(time_days.value or 0)
                hours = int(time_hours.value or 0)
                minutes = int(time_minutes.value or 0)
                seconds = int(time_seconds.value or 0)
                
                new_date = base_date + timedelta(days=years*365 + months*30 + days, 
                                                  hours=hours, minutes=minutes, seconds=seconds)
                time_result.value = f"Result: {new_date.strftime('%Y-%m-%d %H:%M:%S')}"
            
            elif op == "subtract":
                base_date = datetime.strptime(time_date1.value, "%Y-%m-%d")
                years = int(time_years.value or 0)
                months = int(time_months.value or 0)
                days = int(time_days.value or 0)
                hours = int(time_hours.value or 0)
                minutes = int(time_minutes.value or 0)
                seconds = int(time_seconds.value or 0)
                
                new_date = base_date - timedelta(days=years*365 + months*30 + days,
                                                  hours=hours, minutes=minutes, seconds=seconds)
                time_result.value = f"Result: {new_date.strftime('%Y-%m-%d %H:%M:%S')}"
            
            elif op == "difference":
                date1 = datetime.strptime(time_date1.value, "%Y-%m-%d")
                date2_str = time_date2.value if time_date2.value else datetime.now().strftime("%Y-%m-%d")
                date2 = datetime.strptime(date2_str, "%Y-%m-%d")
                
                diff = abs((date2 - date1).days)
                years_d = diff // 365
                months_d = (diff % 365) // 30
                days_d = (diff % 365) % 30
                
                time_result.value = f"Difference: {years_d}y {months_d}m {days_d}d ({diff} days total)"
            
            elif op == "convert":
                value = float(time_date1.value if time_date1.value else "0")
                from_unit = time_unit_from.value
                to_unit = time_unit_to.value
                
                # Convert to seconds first
                to_seconds = {
                    "seconds": 1,
                    "minutes": 60,
                    "hours": 3600,
                    "days": 86400,
                    "weeks": 604800,
                    "months": 2592000,
                    "years": 31536000,
                    "decades": 315360000,
                }
                
                seconds = value * to_seconds[from_unit]
                result = seconds / to_seconds[to_unit]
                time_result.value = f"{value} {from_unit} = {result:.4f} {to_unit}"
        
        except Exception as ex:
            time_result.value = f"Error: {str(ex)}"
        page.update()
    
    # --- Vector Calculator Function ---
    def calculate_vector(e):
        try:
            ax = float(vector_a_x.value or 0)
            ay = float(vector_a_y.value or 0)
            az = float(vector_a_z.value or 0)
            bx = float(vector_b_x.value or 0)
            by = float(vector_b_y.value or 0)
            bz = float(vector_b_z.value or 0)
            
            op = vector_operation.value
            
            if op == "add":
                result = f"({ax+bx}, {ay+by}, {az+bz})"
            elif op == "subtract":
                result = f"({ax-bx}, {ay-by}, {az-bz})"
            elif op == "dot":
                result = f"{ax*bx + ay*by + az*bz}"
            elif op == "cross":
                cx = ay*bz - az*by
                cy = az*bx - ax*bz
                cz = ax*by - ay*bx
                result = f"({cx}, {cy}, {cz})"
            elif op == "magnitude_a":
                result = f"{math.sqrt(ax**2 + ay**2 + az**2):.4f}"
            elif op == "magnitude_b":
                result = f"{math.sqrt(bx**2 + by**2 + bz**2):.4f}"
            elif op == "angle":
                dot = ax*bx + ay*by + az*bz
                mag_a = math.sqrt(ax**2 + ay**2 + az**2)
                mag_b = math.sqrt(bx**2 + by**2 + bz**2)
                if mag_a * mag_b != 0:
                    cos_angle = dot / (mag_a * mag_b)
                    cos_angle = max(-1, min(1, cos_angle))  # Clamp value
                    angle_rad = math.acos(cos_angle)
                    angle_deg = math.degrees(angle_rad)
                    result = f"{angle_deg:.2f}° ({angle_rad:.4f} rad)"
                else:
                    result = "Undefined (zero magnitude vector)"
            
            vector_result.value = f"Result: {result}"
        except Exception as ex:
            vector_result.value = f"Error: {str(ex)}"
        page.update()
    
    # --- Unit Converter Function ---
    def convert_units(e):
        try:
            value = float(unit_value.value)
            category = unit_category.value
            from_unit = unit_from.value
            to_unit = unit_to.value
            
            # Conversion factors to base unit
            conversions = {
                "length": {
                    "mm": 0.001, "cm": 0.01, "m": 1, "km": 1000,
                    "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.34
                },
                "weight": {
                    "mg": 0.001, "g": 1, "kg": 1000,
                    "oz": 28.3495, "lb": 453.592, "ton": 907185
                },
                "area": {
                    "mm²": 0.000001, "cm²": 0.0001, "m²": 1, "km²": 1000000,
                    "in²": 0.00064516, "ft²": 0.092903, "yd²": 0.836127,
                    "acre": 4046.86, "hectare": 10000
                },
                "volume": {
                    "ml": 0.001, "l": 1, "m³": 1000,
                    "in³": 0.016387, "ft³": 28.3168, "gal": 3.78541,
                    "qt": 0.946353, "pt": 0.473176, "cup": 0.236588
                },
                "speed": {
                    "m/s": 1, "km/h": 0.277778, "mph": 0.44704,
                    "knot": 0.514444, "ft/s": 0.3048
                },
                "pressure": {
                    "Pa": 1, "kPa": 1000, "bar": 100000,
                    "psi": 6894.76, "atm": 101325, "mmHg": 133.322
                },
                "energy": {
                    "J": 1, "kJ": 1000, "cal": 4.184, "kcal": 4184,
                    "Wh": 3600, "kWh": 3600000, "BTU": 1055.06
                }
            }
            
            if category == "temperature":
                # Special handling for temperature
                if from_unit == to_unit:
                    result = value
                elif from_unit == "C":
                    if to_unit == "F":
                        result = value * 9/5 + 32
                    elif to_unit == "K":
                        result = value + 273.15
                elif from_unit == "F":
                    if to_unit == "C":
                        result = (value - 32) * 5/9
                    elif to_unit == "K":
                        result = (value - 32) * 5/9 + 273.15
                elif from_unit == "K":
                    if to_unit == "C":
                        result = value - 273.15
                    elif to_unit == "F":
                        result = (value - 273.15) * 9/5 + 32
            else:
                factors = conversions.get(category, {})
                base_value = value * factors.get(from_unit, 1)
                result = base_value / factors.get(to_unit, 1)
            
            unit_result.value = f"{result:.6g} {to_unit}"
        except Exception as ex:
            unit_result.value = f"Error: {str(ex)}"
        page.update()
    
    # ==================== BUILD UI COMPONENTS ====================
    
    # Button styles
    btn_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=15),
        padding=ft.Padding.all(15),
    )
    
    num_btn_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=15),
        padding=ft.Padding.all(15),
        bgcolor="#2d2d44",
        color="#ffffff",
    )
    
    op_btn_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=15),
        padding=ft.Padding.all(15),
        bgcolor="#4a90d9",
        color="#ffffff",
    )
    
    sci_btn_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=15),
        padding=ft.Padding.all(15),
        bgcolor="#3d3d5c",
        color="#ffffff",
    )
    
    func_btn_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=15),
        padding=ft.Padding.all(15),
        bgcolor="#5c5c7a",
        color="#ffffff",
    )
    
    def create_btn(text_label, data, style=None, click_handler=None):
        return ft.Button(
            ft.Text(text_label, size=18),
            data=data,
            on_click=click_handler or std_btn_click,
            style=style or num_btn_style,
        )
    
    # --- Standard Calculator UI ---
    def create_standard_calculator():
        std_display_container = ft.Container(
            content=ft.Column(
                controls=[std_expression_display, std_display_value],
                horizontal_alignment=ft.CrossAxisAlignment.END,
            ),
            padding=ft.Padding.all(20),
            bgcolor="#16213e",
            border_radius=15,
            margin=ft.Margin.only(bottom=10),
        )
        
        clear_row = ft.Row(
            controls=[
                create_btn("C", "C", func_btn_style, std_btn_click),
                create_btn("CE", "CE", func_btn_style, std_btn_click),
                create_btn("⌫", "⌫", func_btn_style, std_btn_click),
                create_btn("÷", "÷", op_btn_style, std_btn_click),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
        
        num_row1 = ft.Row(
            controls=[
                create_btn("7", "7", None, std_btn_click),
                create_btn("8", "8", None, std_btn_click),
                create_btn("9", "9", None, std_btn_click),
                create_btn("×", "×", op_btn_style, std_btn_click),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
        
        num_row2 = ft.Row(
            controls=[
                create_btn("4", "4", None, std_btn_click),
                create_btn("5", "5", None, std_btn_click),
                create_btn("6", "6", None, std_btn_click),
                create_btn("-", "-", op_btn_style, std_btn_click),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
        
        num_row3 = ft.Row(
            controls=[
                create_btn("1", "1", None, std_btn_click),
                create_btn("2", "2", None, std_btn_click),
                create_btn("3", "3", None, std_btn_click),
                create_btn("+", "+", op_btn_style, std_btn_click),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
        
        num_row4 = ft.Row(
            controls=[
                create_btn("±", "±", None, std_btn_click),
                create_btn("0", "0", None, std_btn_click),
                create_btn(".", ".", num_btn_style, std_btn_click),
                create_btn("=", "=", op_btn_style, std_btn_click),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
        
        return ft.Column(
            controls=[
                std_display_container,
                clear_row,
                num_row1,
                num_row2,
                num_row3,
                num_row4,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    
    # --- Scientific Calculator UI ---
    deg_rad_btn = None  # Will be initialized in create_scientific_calculator
    
    def create_scientific_calculator():
        global deg_rad_btn
        
        sci_display_container = ft.Container(
            content=ft.Column(
                controls=[sci_expression_display, sci_display_value],
                horizontal_alignment=ft.CrossAxisAlignment.END,
            ),
            padding=ft.Padding.all(20),
            bgcolor="#16213e",
            border_radius=15,
            margin=ft.Margin.only(bottom=10),
        )
        
        deg_rad_btn = ft.Button(
            ft.Text("DEG", size=16),
            data="DEG",
            on_click=sci_btn_click,
            style=func_btn_style,
        )
        
        sci_row1 = ft.Row(
            controls=[
                deg_rad_btn,
                create_btn("sin", "sin", sci_btn_style, sci_btn_click),
                create_btn("cos", "cos", sci_btn_style, sci_btn_click),
                create_btn("tan", "tan", sci_btn_style, sci_btn_click),
                create_btn("log", "log", sci_btn_style, sci_btn_click),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
        
        sci_row2 = ft.Row(
            controls=[
                create_btn("asin", "asin", sci_btn_style, sci_btn_click),
                create_btn("acos", "acos", sci_btn_style, sci_btn_click),
                create_btn("atan", "atan", sci_btn_style, sci_btn_click),
                create_btn("ln", "ln", sci_btn_style, sci_btn_click),
                create_btn("e", "e", sci_btn_style, sci_btn_click),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
        
        sci_row3 = ft.Row(
            controls=[
                create_btn("π", "π", sci_btn_style, sci_btn_click),
                create_btn("x²", "x²", sci_btn_style, sci_btn_click),
                create_btn("x!", "x!", sci_btn_style, sci_btn_click),
                create_btn("√", "√", sci_btn_style, sci_btn_click),
                create_btn("^", "^", sci_btn_style, sci_btn_click),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
        
        sci_row4 = ft.Row(
            controls=[
                create_btn("(", "(", sci_btn_style, sci_btn_click),
                create_btn(")", ")", sci_btn_style, sci_btn_click),
                create_btn("1/x", "1/x", sci_btn_style, sci_btn_click),
                create_btn("abs", "abs", sci_btn_style, sci_btn_click),
                create_btn("%", "%", sci_btn_style, sci_btn_click),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
        
        clear_row = ft.Row(
            controls=[
                create_btn("C", "C", func_btn_style, sci_btn_click),
                create_btn("CE", "CE", func_btn_style, sci_btn_click),
                create_btn("⌫", "⌫", func_btn_style, sci_btn_click),
                create_btn("÷", "÷", op_btn_style, sci_btn_click),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
        
        num_row1 = ft.Row(
            controls=[
                create_btn("7", "7", None, sci_btn_click),
                create_btn("8", "8", None, sci_btn_click),
                create_btn("9", "9", None, sci_btn_click),
                create_btn("×", "×", op_btn_style, sci_btn_click),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
        
        num_row2 = ft.Row(
            controls=[
                create_btn("4", "4", None, sci_btn_click),
                create_btn("5", "5", None, sci_btn_click),
                create_btn("6", "6", None, sci_btn_click),
                create_btn("-", "-", op_btn_style, sci_btn_click),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
        
        num_row3 = ft.Row(
            controls=[
                create_btn("1", "1", None, sci_btn_click),
                create_btn("2", "2", None, sci_btn_click),
                create_btn("3", "3", None, sci_btn_click),
                create_btn("+", "+", op_btn_style, sci_btn_click),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
        
        num_row4 = ft.Row(
            controls=[
                create_btn("±", "±", None, sci_btn_click),
                create_btn("0", "0", None, sci_btn_click),
                create_btn(".", ".", num_btn_style, sci_btn_click),
                create_btn("=", "=", op_btn_style, sci_btn_click),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
        
        return ft.Column(
            controls=[
                sci_display_container,
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
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    
    # --- Currency Converter UI ---
    def create_currency_converter():
        return ft.Column(
            controls=[
                ft.Text("Currency Converter", size=28, weight=ft.FontWeight.BOLD, color="#ffffff"),
                ft.Divider(height=20, color="transparent"),
                ft.Row(
                    controls=[
                        ft.Text("Amount:", size=16, color="#ffffff"),
                        currency_amount,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[currency_from, ft.Icon("arrow_downward", color="#4a90d9"), currency_to],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Button("Convert", on_click=convert_currency, style=op_btn_style),
                ft.Divider(height=20, color="transparent"),
                currency_result,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    
    # --- Time Calculator UI ---
    def create_time_calculator():
        return ft.Column(
            controls=[
                ft.Text("Time Calculator", size=28, weight=ft.FontWeight.BOLD, color="#ffffff"),
                ft.Divider(height=20, color="transparent"),
                time_operation,
                ft.Divider(height=10, color="transparent"),
                ft.Text("Date Operations:", size=18, color="#888888"),
                time_date1,
                time_date2,
                ft.Divider(height=15, color="transparent"),
                ft.Text("Add/Subtract Time:", size=18, color="#888888"),
                ft.Row(
                    controls=[time_years, time_months, time_days],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[time_hours, time_minutes, time_seconds],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Divider(height=15, color="transparent"),
                ft.Text("Unit Conversion:", size=18, color="#888888"),
                ft.Row(
                    controls=[ft.Text("From:", color="#ffffff"), time_unit_from, ft.Text("To:", color="#ffffff"), time_unit_to],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Button("Calculate", on_click=calculate_time, style=op_btn_style),
                ft.Divider(height=20, color="transparent"),
                time_result,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        )
    
    # --- Vector Calculator UI ---
    def create_vector_calculator():
        return ft.Column(
            controls=[
                ft.Text("Vector Calculator", size=28, weight=ft.FontWeight.BOLD, color="#ffffff"),
                ft.Divider(height=20, color="transparent"),
                ft.Text("Vector A:", size=18, color="#888888"),
                ft.Row(controls=[vector_a_x, vector_a_y, vector_a_z], alignment=ft.MainAxisAlignment.CENTER),
                ft.Divider(height=15, color="transparent"),
                ft.Text("Vector B:", size=18, color="#888888"),
                ft.Row(controls=[vector_b_x, vector_b_y, vector_b_z], alignment=ft.MainAxisAlignment.CENTER),
                ft.Divider(height=15, color="transparent"),
                vector_operation,
                ft.Button("Calculate", on_click=calculate_vector, style=op_btn_style),
                ft.Divider(height=20, color="transparent"),
                vector_result,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        )
    
    # --- Unit Converter UI ---
    def create_unit_converter():
        return ft.Column(
            controls=[
                ft.Text("Unit Converter", size=28, weight=ft.FontWeight.BOLD, color="#ffffff"),
                ft.Divider(height=20, color="transparent"),
                unit_category,
                ft.Divider(height=15, color="transparent"),
                ft.Row(
                    controls=[ft.Text("Value:", color="#ffffff"), unit_value],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(controls=[unit_from, ft.Icon("arrow_downward", color="#4a90d9"), unit_to], alignment=ft.MainAxisAlignment.CENTER),
                ft.Button("Convert", on_click=convert_units, style=op_btn_style),
                ft.Divider(height=20, color="transparent"),
                unit_result,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    
    # ==================== MAIN LAYOUT WITH SIDEBAR ====================
    
    # Content area that changes based on mode
    content_area = ft.Container(
        content=create_standard_calculator(),
        expand=True,
        padding=20,
    )
    
    def change_mode(e):
        nonlocal current_mode
        current_mode = e.control.data
        
        # Update sidebar selection
        for item in sidebar_items:
            if item.data == current_mode:
                item.bgcolor = "#4a90d9"
            else:
                item.bgcolor = "transparent"
        
        # Update content based on mode
        if current_mode == "standard":
            content_area.content = create_standard_calculator()
        elif current_mode == "scientific":
            content_area.content = create_scientific_calculator()
        elif current_mode == "currency":
            content_area.content = create_currency_converter()
        elif current_mode == "time":
            content_area.content = create_time_calculator()
        elif current_mode == "vector":
            content_area.content = create_vector_calculator()
        elif current_mode == "units":
            content_area.content = create_unit_converter()
        
        page.update()
    
    # Sidebar items
    sidebar_items = [
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon("calculate", color="#ffffff"),
                    ft.Text("Standard", size=16, color="#ffffff"),
                ],
                spacing=10,
            ),
            data="standard",
            on_click=change_mode,
            padding=15,
            border_radius=10,
            bgcolor="#4a90d9",
            ink=True,
        ),
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon("science", color="#ffffff"),
                    ft.Text("Scientific", size=16, color="#ffffff"),
                ],
                spacing=10,
            ),
            data="scientific",
            on_click=change_mode,
            padding=15,
            border_radius=10,
            bgcolor="transparent",
            ink=True,
        ),
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon("currency_exchange", color="#ffffff"),
                    ft.Text("Currency", size=16, color="#ffffff"),
                ],
                spacing=10,
            ),
            data="currency",
            on_click=change_mode,
            padding=15,
            border_radius=10,
            bgcolor="transparent",
            ink=True,
        ),
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon("schedule", color="#ffffff"),
                    ft.Text("Time", size=16, color="#ffffff"),
                ],
                spacing=10,
            ),
            data="time",
            on_click=change_mode,
            padding=15,
            border_radius=10,
            bgcolor="transparent",
            ink=True,
        ),
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon("alt_route", color="#ffffff"),
                    ft.Text("Vector", size=16, color="#ffffff"),
                ],
                spacing=10,
            ),
            data="vector",
            on_click=change_mode,
            padding=15,
            border_radius=10,
            bgcolor="transparent",
            ink=True,
        ),
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon("swap_horiz", color="#ffffff"),
                    ft.Text("Units", size=16, color="#ffffff"),
                ],
                spacing=10,
            ),
            data="units",
            on_click=change_mode,
            padding=15,
            border_radius=10,
            bgcolor="transparent",
            ink=True,
        ),
    ]
    
    # Sidebar
    sidebar = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text("Calculator\nModes", size=20, weight=ft.FontWeight.BOLD, color="#ffffff", text_align=ft.TextAlign.CENTER),
                    padding=20,
                    bgcolor="#16213e",
                ),
                ft.Column(controls=sidebar_items, spacing=5),
            ],
            spacing=10,
        ),
        width=200,
        bgcolor="#1a1a2e",
        border=ft.border.only(right=ft.BorderSide(1, "#333355")),
    )
    
    # Main layout
    main_layout = ft.Row(
        controls=[sidebar, content_area],
        expand=True,
        spacing=0,
    )
    
    page.add(main_layout)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)
