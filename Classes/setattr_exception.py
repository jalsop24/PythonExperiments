
ATTR_NAME = "an_attribute"

class ANewClass():
    pass

try:
    an_instance = ANewClass()
    setattr(an_instance, ATTR_NAME, "Another value, maybe 2. I hope no one else changed this.")
except Exception as err:
    print(err)
else:
    print(getattr(an_instance, ATTR_NAME))