import string

class Base():

    @staticmethod
    def snakeCaseToPascalCase(test_str):
        return string.capwords(test_str.replace("_", " ")).replace(" ", "")
