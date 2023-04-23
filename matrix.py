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
        return f"\mm{{{self.tl}}}{{{self.tr}}}{{{self.bl}}}{{{self.br}}}"

if __name__ == "__main__":
    with open("overleaf.preamble") as f:
        print(f.read())

    print("\\begin{document}")

    q_matrix = Matrix22(
        (0, 1),
        (1, 1),
    )
    m = q_matrix
    for i in range(15):
        new_m = q_matrix * m
        print("\\begin{equation}")
        print(f"{q_matrix} \\times {m} = {new_m}")
        print("\\end{equation}")
        print()
        m = new_m

    print("\\end{document}")
