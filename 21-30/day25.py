def match(string, exp):
    allowed = ""
    for i in range(len(string)):
        if i > len(exp)-1:
            if string[i] != allowed:
                return False
        else:
            if exp[i] == "*":
                allowed = string[i]
            if string[i] != allowed:
                allowed = ""
            if (exp[i] != string[i] and exp[i] != "." and string[i] != allowed):
                return False
    return True

print(match("chats", ".*at"))
