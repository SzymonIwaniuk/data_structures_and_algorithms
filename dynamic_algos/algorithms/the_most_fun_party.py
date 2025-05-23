from typing import TypeVar

EmpType = TypeVar("EmpType", bound="Emp")

#O(n)

class Emp:
    def __init__(self, fun: int) -> None:
        self.emp = []
        self.fun = fun
        self.f_val = -1
        self.g_val = -1

    def f(self: EmpType) -> int:
        if self.f_val != -1 and self.g_val != -1:
            return max(self.f_val, self.g_val)

        self.f_val = self.fun
        self.g_val = 0

        for employee in self.emp:
            employee.f()
            self.f_val += employee.g_val
            self.g_val += max(employee.f_val, employee.g_val)

        return max(self.f_val, self.g_val)


if __name__ == '__main__':
    senior = Emp(5)
    mid1 = Emp(3)
    mid2 = Emp(6)
    junior1 = Emp(1)
    junior2 = Emp(1)

    senior.emp = [mid1, mid2]
    mid1.emp = [junior1]
    mid2.emp = [junior2]

    print(senior.f())