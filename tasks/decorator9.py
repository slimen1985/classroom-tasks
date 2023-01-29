ACCOUNTS = {
    "user123": "user",
    "luke": "user",
    "alex123": "user",
    "vad": "admin"
}


def check_admin(func):
    def wrapper(name):
        if ACCOUNTS.get(name) == "admin":
            func(name)
            print("Access granted")
        else:
            func(name)
            print("Access denied")
    return wrapper


@check_admin
def log_in(name):
    if name in ACCOUNTS:
        print(f"User with name {name} exist")
    else:
        print(f"User with name {name} dose not exist")


log_in("vad")

