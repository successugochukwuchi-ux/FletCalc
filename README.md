# Scientific Calculator App

A modern mobile scientific calculator built with Python and Flet.

## Features

- **Basic Operations**: Addition, subtraction, multiplication, division
- **Scientific Functions**: 
  - Trigonometric: sin, cos, tan, asin, acos, atan
  - Logarithmic: log (base 10), ln (natural log)
  - Other: square root, factorial, power, reciprocal, absolute value
- **Constants**: π (pi), e (Euler's number)
- **Mode Toggle**: Switch between Degrees (DEG) and Radians (RAD) for trigonometric functions
- **Modern Dark Theme**: Easy on the eyes with a sleek dark UI
- **Mobile-Friendly**: Optimized for mobile devices with responsive layout

## Requirements

- Python 3.8+
- Flet 0.84.0
- flet-web 0.84.0

## Installation

```bash
pip install flet==0.84.0
pip install flet-web==0.84.0
```

## Usage

Run the calculator app:

```bash
python calculator.py
```

The app will open in your default web browser.

## Button Functions

| Button | Function |
|--------|----------|
| C | Clear all |
| CE | Clear entry |
| ⌫ | Backspace |
| ÷, ×, -, + | Basic arithmetic operations |
| = | Calculate result |
| ± | Toggle sign |
| % | Percentage |
| 1/x | Reciprocal |
| x² | Square |
| √ | Square root |
| x! | Factorial |
| ^ | Power |
| ( ) | Parentheses |
| sin, cos, tan | Trigonometric functions |
| asin, acos, atan | Inverse trigonometric functions |
| log | Logarithm base 10 |
| ln | Natural logarithm |
| π | Pi constant |
| e | Euler's number |
| DEG/RAD | Toggle degree/radian mode |

## Version Compatibility

- Flet: 0.84.0
- Flutter: 3.41.4
- Pyodide: 0.27.7