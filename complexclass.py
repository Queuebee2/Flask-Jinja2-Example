from random import randint, shuffle, choice, seed
from string import ascii_uppercase


class ComplexClass():
    """random data generator class"""

    def __init__(self):
        self.name = 'complex class'
        self.chars = list(ascii_uppercase)

    def complex_function(self, amt=10):
        """returns a nested dict with random stuff
        format like this:
        {
         'item 1':{
                'attr1: value1,
                'attr2: value2,
                'attr3: value3 },
         'item 2':{
                'attr1: value4,
                'attr2: value5,
                'attr3: value6 }
         }
         """

        def random_string(min=25, amt=100):
            def random_word(min=1, len=0):
                return "".join([choice(ascii_uppercase) for i in range(randint(min, min + abs(len)))])

            return f"{choice([' ', ', ', '. '])}".join(
                [random_word(randint(0, 12)) for _ in range(randint(min, min + abs(amt)))])

        def random_key():
            """ create a random key"""
            random_key = "xp_" + "".join([choice(ascii_uppercase) for i in range(randint(4, 6))])
            return random_key

        def random_number(max=1000000):
            return randint(0, abs(max))

        def random_attributes():
            """"create a dictionary with random attributes"""
            shuffle(self.chars)
            random_attribute = {
                'attr1': random_number(),
                'attr2': "".join(self.chars)[:10],
                'attr3': random_string()
            }
            return random_attribute

        complex_data_object = {random_key(): random_attributes() for _ in range(amt)}

        return complex_data_object
