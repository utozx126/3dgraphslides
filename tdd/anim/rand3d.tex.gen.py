from random import random, seed
from math import sqrt
seed(2)
count = 15
x = [random()*4-2 for _ in range(15)]
y = [random()*4-2 for _ in range(15)]
z = [random()*4-2 for _ in range(15)]

def d(a, b): 
    return sqrt((x[a]-x[b])**2 + (y[a]-y[b])**2 + (z[a]-z[b])**2) 


    

print("""\\documentclass[tikz]{standalone}
\\usepackage{tikz-3dplot}
\\begin{document}
\\tdplotsetmaincoords{40}{100}
\\foreach \\rot in {0, 1, ..., 359} {
    \\tdplotsetrotatedcoords{0}{0}{\\rot}
    \\begin{tikzpicture}[tdplot_rotated_coords,scale=1,line join=round]
    \\useasboundingbox (-3cm, -3cm) -- (3cm, 3cm);
    \\path
""")
for i in range(count):
    print(f"""  coordinate ({i}) at ({x[i]}, {y[i]}, {z[i]})
""")
print(""";""")
for a in range(count):
    for b in range(count):
        if (d(a, b) + random() < 4):
            print(f"""\\draw ({a}) -- ({b});""")

print("""\\end{tikzpicture}
}
\\end{document}""")
