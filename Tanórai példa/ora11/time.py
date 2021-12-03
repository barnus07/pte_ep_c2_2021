class Time:

    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print(self):
        print(number_with_leadzero(self.hour),
              number_with_leadzero(self.minute),
              number_with_leadzero(self.second), sep=":")


def number_with_leadzero(number: int) -> str:
    result = str(number)
    if number < 10:
        result = "0" + result
    return result