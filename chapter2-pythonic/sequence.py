class Items:
    """
    slicing 은 __getitem__ 이라는 매직 메서드 덕분에 가능한 기능
    """
    def __init__(self, *values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values.__getitem__(item)
