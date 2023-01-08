import unittest
from dns_record import DNSRecord

class TestDNSRecord(unittest.TestCase):
    def test_init(self):
        # создаем объект
        record = DNSRecord("example.com", "192.0.2.1")

        # проверяем имя и адрес объекта
        self.assertEqual(record.name, "example.com")
        self.assertEqual(record.data, "192.0.2.1")

if __name__ == "__main__":
    unittest.main()