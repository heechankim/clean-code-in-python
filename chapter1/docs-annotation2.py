def data_from_response(response: dict) -> dict:
    if response["status"] != 200:
        raise ValueError
    return {"data": response["payload"]}


def main():
    """
    annotation 이 간편하고 강력한 지원을 하는데, 여전히 docstring?

    annotation 을 사용한 data_from_response 과 docstring 을 비교해보자.

    ################################################
    response에 문제가 없다면 response의 payload 를 반환
    chan: 문장으로 요약해서 전달받아 명확하게 이해가 가능하다.

    - response dict 예시::
    {
        "status": 200,
        "timestamp": "..."
        "payload": { ... } # dict data
    }

    - payload dict 예시::
    { "data": {...} }

    - 발생 가능한 예외:
    - HTTP status 가 200 이 아닌 경우 ValueError
    chan: annotation 으로는 작성할 수 없던 dict 의 내부구조, 데이터 포멧 예시 등을 작성할 수 있어 이해를 돕는다.
    ################################################
    """

if __name__ == '__main__':
    main()