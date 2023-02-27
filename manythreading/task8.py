from PIL import Image, ImageFilter
import time
import os
from multiprocessing import Process


filenames = [
    'images/1.jpeg',
    'images/2.jpeg',
    'images/3.jpeg'
]


def create_thumbnail(filename, size=(50, 50), thumb_dir = 'thumbs'):
    img = Image.open(filename)
    img = img.filter(ImageFilter.GaussianBlur())
    img.thumbnail(size)
    img.save(f'{thumb_dir}/{os.path.basename(filename)}')
    print(f'{filename} was done!')


if __name__ == "__main__":
    start = time.perf_counter()

    processes = [Process(target=create_thumbnail, args=(filename, )) for filename in filenames]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'Exec time {finish - start} sec')
