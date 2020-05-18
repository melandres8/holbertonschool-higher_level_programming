#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for item in range(list_length):
        try:
            result = my_list_1[item] / my_list_2[item]
        except ZeroDivisionError:
            print("Division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except Exception:
            print("out of range")
            result = 0
        finally:
            new.append(result)
    return new
