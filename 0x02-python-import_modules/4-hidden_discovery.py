#!/usr/bin/python3
"""prints all the names defined by the compiled module"""

if __name__ == "__main__":
    import hidden_4

    for i in range(len(dir(hidden_4))):
        if dir(hidden_4)[i][:2] != "__":
            print("{}".format(dir(hidden_4)[i]))
