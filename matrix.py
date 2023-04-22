class Matrix22:
    def __init__(self, tl, tr, bl, br):
        self.tl = tl
        self.tr = tr
        self.bl = bl
        self.br = br

    def __mul__(self, other):
        tl = self.tl * other.tl + self.tr * other.bl
        tr = self.tl * other.tr + self.tr * other.br
        bl = self.bl * other.tl + self.br * other.bl
        br = self.bl * other.tr + self.br * other.br
        return Matrix22(tl, tr, bl, br)

    def __str__(self):
        return f"""
            {self.tl} {self.tr}
            {self.bl} {self.br}
        """


if __name__ == "__main__":
    m_orig = Matrix22(0, 1, 1, 1)
    m = m_orig
    for i in range(10):
        print(m)
        m = m * m_orig