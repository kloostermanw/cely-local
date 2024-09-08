import string

class Base():

    @staticmethod
    def snakeCaseToPascalCase(test_str):
        return string.capwords(test_str.replace("_", " ")).replace(" ", "")

    
    # removes suffix from the end of string s
    @staticmethod
    def rchop(s, suffix):
        if suffix and s.endswith(suffix):
            return s[:-len(suffix)]
        return s
    
    # removes prefix from the start of string str
    @staticmethod
    def lchop(str, prefix):
        return str.lstrip(prefix)