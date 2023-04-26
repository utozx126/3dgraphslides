print("""\\documentclass[tikz]{standalone}
\\usepackage{tikz-3dplot}
\\begin{document}
\\tdplotsetmaincoords{40}{100}
\\foreach \\rot in {0, 1, ..., 359} {
    \\tdplotsetrotatedcoords{0}{0}{\\rot}
    \\begin{tikzpicture}[scale=0.7, tdplot_rotated_coords,line join=round]
    \\useasboundingbox (-6cm, -4cm) -- (6cm, 5cm);
    \\coordinate (tr) at (-2, -2, -2);
    \\begin{scope}[shift=(tr)]
    \\draw[->] (0,0,0) -- (4, 0, 0);
    \\draw[->] (0,0,0) -- (0, 4, 0);
    \\draw[->] (0,0,0) -- (0, 0, 4);
    \\node at (5,0,0) {x};
    \\node at (0,5,0) {y};
    \\node at (0,0,5) {z};
""")

print("""\draw (0,0,0)""")
for i in range(50*4):
    t = i/50
    a = (t, (t**2)%5, (t**3)%5)
    b = (t+.02, ((t+.02)**2)%5, ((t+.02)**3)%5)
    if (b[1] < a[1] or b[2] < a[2]): 
        print(f"""({b[0]}, {b[1]}, {b[2]})""")
    else:
        print(f"""-- ({b[0]}, {b[1]}, {b[2]})""")
print(""";""")

print("""   \\foreach \\t[evaluate=\\t as \\y using {Mod(\\t*\\t,5)}, evaluate=\\t as \\z using {Mod(\\t*\\t*\\t,5)}] in {0, 1, 2, 3, 4} {
	\\fill (\\t, \\y, \\z) circle [radius = 0.1];
    }
    \\end{scope}
\\end{tikzpicture}
}
\\end{document}""")
