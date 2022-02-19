def context_in_finally(filename):
    """
    Context Manager 를 사용하지 않고 리소스관리.
    finally 블럭에 리소스 해제를 하여 리소스 누수를 막음
    """
    global process_file
    fd = open(filename)
    try:
        process_file(fd)
    finally:
        fd.close()

def context_by_pythonic(filename):
    global process_file
    with open(filename) as fd:
        process_file(fd)

def main():
    """
    Contect Manager
        - 사전조건과 사후조건을 가지고 있음
        - 일반적으로 리소스를 다루는 코드에서 유용
    """


if __name__ == '__main__':
    main()