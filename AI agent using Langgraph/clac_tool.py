def calculate(expression: str) -> str:
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception:
        return "Invalid expression."
