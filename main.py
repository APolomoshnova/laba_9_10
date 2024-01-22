import threading
import time
from lorem_text import lorem

locker = threading.Lock()


def analysis_text(text):
    frequency = {}
    count_symbols = len(text)
    for symbol in text:
        if symbol in frequency:
            frequency[symbol] += 1
        else:
            frequency[symbol] = 1
    time.sleep(1)
    result = [(symbol, frequency / count_symbols) for symbol, frequency in frequency.items()]
    return result


def auto_text():
    text = lorem.paragraph()
    time.sleep(1)
    with locker:
        print(text)

        return text


def menu():
    text = auto_text()
    result = analysis_text(text)
    for symbol, frequency in result:
        print(f"{symbol} - {frequency:.4f}")


for _ in range(5):
    thr = threading.Thread(target=menu)
    thr.start()
