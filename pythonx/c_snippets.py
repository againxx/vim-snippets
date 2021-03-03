def get_left_curly_brace_style(snip):
    style = snip.opt("b:ultisnips_cpp_style")
    if style is None:
        style = snip.opt("g:ultisnips_cpp_style", "google")
    if style == "google":
        snip.rv += " {"
    else:
        snip += snip.mkline("{")

def get_right_curly_brace_style(snip, str_after_brace):
    style = snip.opt("b:ultisnips_cpp_style")
    if style is None:
        style = snip.opt("g:ultisnips_cpp_style", "google")
    if style == "google":
        snip.rv += "} " + str_after_brace
    else:
        snip.rv += "}"
        snip += snip.mkline(str_after_brace)
