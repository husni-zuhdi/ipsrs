# Create a function seconds() that converts the keyword-only arguments hours , minutes and seconds
# to seconds. Each of these arguments is optional.
def seconds(**kwargs):
    return kwargs["seconds"] + kwargs["minutes"] * 60 + kwargs["hours"] * 60 * 60


if __name__ == "__main__":
    print(seconds(seconds=50, minutes=15, hours=12))
    print(seconds(seconds=10, minutes=5, hours=1))
