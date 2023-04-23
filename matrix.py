class Matrix22:
    def __init__(self, top, bottom):
        self.tl, self.tr = top
        self.bl, self.br = bottom

    def __mul__(self, other):
        tl = self.tl * other.tl + self.tr * other.bl
        tr = self.tl * other.tr + self.tr * other.br
        bl = self.bl * other.tl + self.br * other.bl
        br = self.bl * other.tr + self.br * other.br
        return Matrix22((tl, tr), (bl, br))

    def __str__(self):
        return f"""
            |{self.tl:3} {self.tr:3} |
            |{self.bl:3} {self.br:3} |
        """


if __name__ == "__main__":
    """
    0 1  * a b  =    b   c
    1 1    b c     a+b b+c
    """
    q_matrix = Matrix22(
        (0, 1),
        (1, 1),
    )
    m = q_matrix
    for i in range(10):
        print(m)
        m = q_matrix * m
