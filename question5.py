def string_appender(name, append_str):
    return "%s_%s" % (name, append_str)


if __name__ == "__main__":
    name_list = ["kenny", "hippo", "peter", "kelly", "john", "bob"]

    funcs = []

    for n in name_list:
        # Bind the current value of n when the lambda is created.
        # Without n=n, every lambda would use the final loop value ("bob").
        funcs.append(lambda n=n: string_appender(n, "char"))

    # Don't modify the code below:
    for f in funcs:
        print(f())
