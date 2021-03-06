# used only for debugging -- read state and enter interactive mode
# use with files generated by endo with --dump-state option
import sys
import gzip
import cPickle as pickle

def main():
    f = gzip.GzipFile(filename=sys.argv[1], mode='r')
    backend = pickle.load(f)
    f.close()
    del f


if __name__ == "__main__":
    main()

