def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("pythonic 1 - 음수 인덱스")
    print(arr[-1])

    print("pythonic 2 - 슬라이싱")
    print(arr[2:5])

    print("pythonic 3 - 슬라이싱과 스탭")
    print(arr[:4])
    print(arr[4:])
    print(arr[::3])

    print("슬라이싱과 스탭은 사실 slice 객체를 전달한 것이다.")
    print(type(slice(1, 1, 1)))
    slice_object = slice(0, 4, 1)
    print(arr[slice_object])

    slice_object = slice(4, 9, 1)
    print(arr[slice_object])

    slice_object = slice(0, 9, 3)
    print(arr[slice_object])

if __name__ == '__main__':
    main()