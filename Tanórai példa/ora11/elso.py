def upper_case(szoveg: str) -> None:
    for karakter in szoveg:
        if karakter >= 'a' and karakter <= 'z':
            print(chr(ord(karakter) - ord('a') + ord('A')), end="")
        else:
            print(karakter, end="")
