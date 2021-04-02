from tqdm import tqdm
from time import sleep


def main():
    print("Method 1")
    for i in tqdm(range(100), bar_format='{l_bar}{bar:100}{r_bar}'):
        i += 1
        sleep(0.02)

    print("Method 2")
    for i in range(100):
        print(f"\r\033[{i % 6 + 31}m{i + 1}%|{'=' * i + '>':<100}|{i + 1}/{100}", end='', flush=True)
        i += 1
        sleep(0.02)


if __name__ == '__main__':
    main()
