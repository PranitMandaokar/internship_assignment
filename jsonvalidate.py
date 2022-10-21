import json

def Check(file):
    try:
        json.loads(file)
    except ValueError as err:
        return False
    return True

# m1 is a correct JSON file and m2 is a incorrect JSON file

m1 = """{"name": "jane doe", "salary": 9000, "email": "jane.doe@pynative.com"}"""
m2 = """{"name": "jane doe", "salary": 9000, "email": "jane.doe@pynative.com",}"""
m = Check(m1)
print(m)


