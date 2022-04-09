class Integer:
    def __init__(self, value):
        self.value = value


    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))


    @classmethod
    def from_roman(cls, value):
        trans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        values = [trans[r] for r in value]
        return cls(sum(
            val if val >= next_val else -val
            for val, next_val in zip(values[:-1], values[1:])
        ) + values[-1])

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            return cls(int(value))
        return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
