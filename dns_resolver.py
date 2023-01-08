from dns_record import DNSRecord

class DNSResolver:
    def __init__(self):
        #используем словать для симуляции базы данных
        self.records = {}

    def add_record(self, name, data):
        """
        записываем в базу данных
        """
        record = DNSRecord(name, data)

        if name not in self.records:
            self.records[name] = []

        self.records[name].append(record)

    def lookup(self, name):
        """
        поиск
        """
        results = []

        # проверяем есть ли запись в базе данных
        if name in self.records:
            results.extend(self.records[name])

        return results
