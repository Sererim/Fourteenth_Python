# 1. Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное и шестинадцеричное строковое представление.

class Base:
    """
    summary: Simple class with static methods for conversion to different bases.
    Binary, Octagonal and Hexagonal.
    Methods return false if number can not be processed by the class.
    """
    @staticmethod
    def dec_to_bin(num: int) -> str:
        if not Base.valid(num):
            raise ValueError("Error!\nIncorrect number was entered.")
        num_str = ""

        # Base cases
        if num == 0:
            for i in range(8):
                num_str += f"{0}"
        elif num == 1:
            for i in range(7):
                num_str += f"{0}"
            num_str += f"{1}"
        # Main case
        else:
            while num != 1:
                if num % 2 == 0:
                    num_str += f"{0}"
                    num /= 2
                else:
                    num_str += f"{1}"
                    num //= 2
            num_str += f"{1}"
            num_str = num_str[::-1]
        num_str = num_str[::-1] + "b0"
        return num_str[::-1]

    @staticmethod
    def dec_to_oct(num: int) -> str:
        if not Base.valid(num):
            raise ValueError("Error!\nIncorrect number was entered.")
        num_str: str = ""
        octagonal: list[int] = [i for i in range(8)]
        # Base case
        if num in octagonal:
            num_str += f"{num}"
        # Main case
        else:
            while num not in octagonal:
                num_str += f"{num % 8}"
                num //= 8
            num_str += f"{num}"
            num_str = num_str[::-1]
        num_str = num_str[::-1] + "o0"
        return num_str[::-1]

    @staticmethod
    def dec_to_hex(num: int) -> str:
        if not Base.valid(num):
            raise ValueError("Error!\nIncorrect number was entered.")
        h_dict: dict[int: str] = {10: "a", 11: "b", 12: "c",
                                  13: "d", 14: "e", 15: "f"}
        num_str: str = ""

        # Base case
        if num in range(0, 16):
            if h_dict.get(num) is not None:
                return "0x" + str(h_dict[num])
            else:
                return f"0x{num}"
        else:
            while num not in range(0, 16):
                if h_dict.get(num % 16) is not None:
                    num_str += f"{h_dict.get(num % 16)}"
                else:
                    num_str += f"{num % 16}"
                num //= 16
            if h_dict.get(num % 16) is not None:
                num_str += f"{h_dict.get(num)}"
            else:
                num_str += f"{num}"
            num_str = num_str[::-1]
        num_str = num_str[::-1] + "x0"
        return num_str[::-1]

    @staticmethod
    def valid(num: int) -> bool:
        if num < 0:
            return False
        elif not isinstance(num, int):
            return False
        else:
            return True


if __name__ == "__main__":
    print(Base.dec_to_bin(7) == bin(7))
    print(Base.dec_to_oct(7) == oct(7))
    print(Base.dec_to_hex(7) == hex(7))
    print(Base.dec_to_hex(7))
    # print(Base.dec_to_bin(-10))
