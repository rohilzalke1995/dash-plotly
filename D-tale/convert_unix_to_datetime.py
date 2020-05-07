from datetime import datetime



class ConvertToDateTime:
    def __init__(self, date):
        self.date = date

    def convert_unix(self):
        date = self.date
        if type(date).__name__ == 'str':
            unix = int(date)
        elif type(date).__name__ == 'int':
            unix = date
        date = datetime.utcfromtimestamp(unix).strftime('%Y-%m-%d')
        return date


if __name__ == '__main__':
    unit_test = ConvertToDateTime(1587081600).convert_unix()
    print(unit_test)