import multiprocessing as mp

fruits = ['apple', 'orange', 'pineapple', 'banana', 'lemon']
count = 1


if __name__ == "__main__":
    queue = mp.Queue()
    print("Inserting objects into queue...")
    for fruit in fruits:
        print('Item # ', ' ', count, ' - ', fruit)
        queue.put(fruit)
        count += 1

    count = 1
    print('\n Getting objects from queue...')
    while not queue.empty():
        print('Item # ', ' ', count, ' - ', queue.get())
        count += 1

