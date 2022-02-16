def docs_func():
    """
    This is docs_function's Docstring.
    """

def annotation_func(a: int, b: int) -> int:
    """
    annotation 지정시 docstring 에서 아래의 형식을 자동으로 생성해줌
    :param a:
    :param b:
    :return:

    annotation
        - type hinting 기능을 활성화
        - type 이상으로 많은 것에 대한 힌트를 줄 수 있음 ex) 변수 사용의도가 담긴 문자열, 콜백이나 유효성 검사 함수의 callable
        - 코드의 시맨틱이 보다 의미 있는 개념을 갖게 되면 코드를 이해하기 쉽고 예측 가능함

    """
    print(a, b)


def main():
    """
    Docstring
        - 소스코드에 포함된 문서
        - 리터럴 문자열
        - 로직의 일부분을 문서화

    1. 코드의 특정 컴포넌트(모듈, 클래스, 메서드, 함수)에 대한 문서화.
    2. 동적 타이핑을 사용하는 파이썬에서 타입에 대한 힌트
    3. __doc__ 속성을 통해 접근할 수 있다.
    4. Sphinx 등 툴을 통해 프로젝트 문서화를 위한 기본 골격을 만듬

    """

    print(docs_func.__doc__)
    annotation_func("Hello, ", "World!")

if __name__ == "__main__":
    main()