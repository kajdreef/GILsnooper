from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from random import randint


def task(id):
    while True:
        sum = 0
        for i in range(0, randint(0, 50000)):
            sum += i
        print(f"Hello {id}: {sum}")


def main():
    parser = ArgumentParser()
    parser.add_argument('threads', type=int, help="Number of threads used by the program")
    args = parser.parse_args()

    with ThreadPoolExecutor(args.threads) as executor:
        executor.map(task,  list(range(args.threads)))

if __name__ == '__main__':
    main()