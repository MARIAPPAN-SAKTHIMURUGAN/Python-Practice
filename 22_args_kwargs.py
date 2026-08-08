def argskwargs(*args, **kwargs):
    print("ARGS:", args)
    print("KWARGS:", kwargs)

    print("Items:", kwargs.items())
    print("Keys:", kwargs.keys())
    print("Values:", kwargs.values())
    print("Mari:", kwargs.get("mari"))

    for key, value in kwargs.items():
        print(key, "=", value)


argskwargs(
    "mari",
    "muppidathi",
    mari="jk",
    mup="hj"
)
