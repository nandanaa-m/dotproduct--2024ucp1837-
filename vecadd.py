from concurrent.futures import ThreadPoolExecutor

def vecadd(a, b):
    with ThreadPoolExecutor() as executor:
        return list(executor.map(lambda x, y: x + y, a, b))
