import tinify
import sys
import os


try:
    tinify.key = os.environ['TINIFY_API_KEY']
except KeyError:
    print('TINIFY_API_KEY is not defined in your environment.')


def compress(fname):
    source = tinify.from_file(fname)
    source.to_file(fname)


def compress_all(files):
    for file in files:
        size = os.path.getsize(file)
        print('Compressing', file + '. Original size:', str(size), 'bytes.')
        compress(file)


if __name__ == '__main__':
    compress_all(sys.argv[1:])
