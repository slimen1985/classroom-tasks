class ExceptionPrintData(Exception):
    def __str__(self):
        return "Error of printing data"

# raise Exception("Printer is not available")
class PrintData:

    def print(self, data):
        if not self.send_to_print():
            raise ExceptionPrintData
        print(f"Печать {data}")

    def send_to_print(self):
         return True



p = PrintData()
try:
    p.print(123)
except ExceptionPrintData as err:
    print(f"Print error {err}")