from datetime import datetime
import time


class ConvertUnixToDatetime:
    def __init__(self, date):
        self.date = date

    # Convert unix to date object
    def convert_unix(self):
        unix = self.date

        # Check if unix is a string or int & proceeds with correct conversion
        if type(unix).__name__ == 'str':
            unix = int(unix[0:10])
        else:
            unix = int(str(unix)[0:10])

        date = datetime.fromtimestamp(unix)

        return date


if __name__ == '__main__':

    # Test Unix
    unix_test = ConvertUnixToDatetime(15391296000)
    print(unix_test.convert_unix())