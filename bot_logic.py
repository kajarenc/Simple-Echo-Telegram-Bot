result = 0


class Result():
    def __init__(self):
        self.res = 0

    def reset_result(self):
        self.res = 0

    def increment_result(self):
        self.res += 1

    def get_result(self):
        return self.res
