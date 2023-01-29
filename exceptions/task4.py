class CustomException(Exception):

    def __str__(self):
        return "This is custom exception"


try:
    f = open('test.txt')
    s = f.readline()
    i = s.split()
except Exception as exc:
    raise CustomException from exc