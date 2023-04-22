class Matrix22:
    def __init__(self, top, bottom):
        assert len(top) == 2
        assert len(bottom) == 2
        self.tl = top[0]
        self.tr = top[1]
        self.bl = bottom[0]
        self.br = bottom[1]

    def __mul__(self, other):
        tl = self.tl * other.tl + self.tr * other.bl
        tr = self.tl * other.tr + self.tr * other.br
        bl = self.bl * other.tl + self.br * other.bl
        br = self.bl * other.tr + self.br * other.br
        return Matrix22((tl, tr), (bl, br))

    def __str__(self):
        return f"""
            {self.tl} {self.tr}
            {self.bl} {self.br}
        """


if __name__ == "__main__":
    q_matrix = Matrix22(
        (0, 1),
        (1, 1),
    )
    m = q_matrix
    for i in range(10):
        print(m)
        m = m * q_matrix
