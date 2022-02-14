

class Session():

    def __enter__(self):
        print("entered")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exited")
        print(f"{exc_type=}, {exc_val=}, {exc_tb=}")


def get_a_number():

    with Session() as session:
        for i in range(100):
            yield i

def main():
    '''::
    >>> entered
    >>> 0
    >>> exited
    >>> exc_type=<class 'GeneratorExit'>, exc_val=GeneratorExit(), exc_tb=<traceback object at 0x00000280BA7B3CC0>   
    '''

    gen = get_a_number()
    print(next(gen))

if __name__ == "__main__":
    main()
