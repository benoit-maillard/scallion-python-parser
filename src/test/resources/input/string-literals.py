""\
"test"\
"line1\nline2\nline3"\
"\\"\
"\'"\
"\""\
"\a"\
"\b"\
"\f"\
"\n"\
"\r"\
"\t"\
"\v"\
"\123"\
"\129"\
"\x5f"\
"\x5f\x3dtest\129abc"\
"\N{TAB}"\
"\N{TAB}abc"\
"\uafafabc"\
"\uafaf"\
r"\x5\b3\nabc"\
r"\""\
r"abc"\
rf"""abcdefg"| """\
r""" "" """\
r"""" """\
RF"test"\
Rf"test"\
rF"test"\
rf"test"\
FR"test"\
fR"test"\
Fr"test"\
fr"test"\
F"test"\
f"test"\
U"test"\
R"test"\
u"test"\
r"test"
RB"bbbbb"\
Rb"bbbbb"\
rB"bbbbb"\
rb"bbbbb"\
BR"bbbbb"\
bR"bbbbb"\
Br"bbbbb"\
br"bbbbb"\
B"bbbbb"\
b"bbbbb"
"""
"""
"\
"
r"\
"



# should fail
# "\x5",
# "\x"
# "\x5g",
# "\"
# r"\"
# "\uafag"
# "\ua"
