import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.info("Application started")

def add(a, b):
    logging.info(f"Addition called: {a} + {b}")
    result = a + b
    logging.info(f"Addition result: {result}")
    return result

def multiply(a, b):
    logging.info(f"Multiplication called: {a} * {b}")

    if b == 0:
        logging.warning(f"Multiplying by zero: {a} * 0")

    result = a * b
    logging.info(f"Multiplication result: {result}")
    return result
