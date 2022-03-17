


class ANewClass():
    pass

try:
    an_instance = ANewClass()
    setattr(an_instance, "an_attribute", "A value")
except Exception as err:
    print(err)
else:
    print(an_instance.an_attribute)