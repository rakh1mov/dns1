import unittest
from dns_resolver import DNSResolver

class TestDNSResolver(unittest.TestCase):
    def setUp(self):
        # создаем объект 
        self.resolver = DNSResolver()

        # добавляем записи в базу данных
        self.resolver.add_record("example.com", "192.0.2.1")
        self.resolver.add_record("www.example.com", "192.0.2.2")
        self.resolver.add_record("mail.example.com", "192.0.2.3")

    def test_lookup(self):
        # проверяем запрос
        records = self.resolver.lookup("example.com")
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].name, "example.com")
        self.assertEqual(records[0].data, "192.0.2.1")

        # проверяем поиск несуществующего домена
        records = self.resolver.lookup("nonexistent.com")
        self.assertEqual(len(records), 0)

    def test_add_record(self):
        # проверяем добавление записи
        self.resolver.add_record("test.com", "192.0.2.4")
        records = self.resolver.lookup("test.com")
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].name, "test.com")
        self.assertEqual(records[0].data, "192.0.2.4")

if __name__ == "__main__":
    unittest.main()