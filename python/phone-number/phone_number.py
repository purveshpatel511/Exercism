class PhoneNumber:
    number = ""
    copy_number = ""
    area_code = ""

    def __init__(self, number):
        self.copy_number = number
        number = (
            number.replace("(", " ")
            .replace(")", " ")
            .replace("-", " ")
            .replace(".", " ")
            .replace("+", " ")
            .replace("@", " ")
            .replace(":", " ")
            .replace("!", " ")
            .strip()
        )

        invalid_area = ["0", "1"]
        number_split = number.split()[-3:]
        clean_number = "".join(number_split)
        if len(clean_number) < 10:
            raise ValueError("Invalid")
        if len(clean_number) == 11 and clean_number[0] == "1":
            print(clean_number)
            clean_number = clean_number[1:]
            print(clean_number)
        if len(clean_number) == 11 and clean_number[0] != "1":
            print(clean_number)
            raise ValueError("Invalid")
        if len(clean_number) > 11:
            raise ValueError("Invalid")
        if clean_number[0] in invalid_area or clean_number[3] in invalid_area:
            raise ValueError("Invalid Code.")
        else:
            self.number = clean_number
            self.area_code = clean_number[:3]

    def pretty(self):
        if len(self.copy_number) == 11:
            return f"({self.copy_number[1:4]})-{self.copy_number[4:7]}-{self.copy_number[7:]}"
        if len(self.copy_number) == 10:
            return f"({self.copy_number[0:3]})-{self.copy_number[3:6]}-{self.copy_number[6:]}"