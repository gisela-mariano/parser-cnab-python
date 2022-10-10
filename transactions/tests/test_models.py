from django.test import TestCase
from django.db.utils import IntegrityError

from transactions.models import Transaction


class TransactionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.transaction_data = {
            "type": 3,
            "date": "20190301",
            "hour": "153453",
            "value": "0000014200",
            "cpf": "09620676017",
            "card": "4753****3153",
            "store_owner": "JOÃO MACEDO   ",
            "store_name": "BAR DO JOÃO        ",
        }

        cls.transaction_created = Transaction.objects.create(**cls.transaction_data)

        cls.transaction = Transaction.objects.get(cpf=f"{cls.transaction_data['cpf']}")


    def test_type_field_validators(self):
      print('test type field validatos')

      max_value_type_field = self.transaction._meta.get_field('type').validators[0].limit_value

      min_length_type_field = self.transaction._meta.get_field('type').validators[1].limit_value

      self.assertEquals(max_value_type_field, 9)
      self.assertEquals(min_length_type_field, 1)
      

    def test_date_field_validators(self):
      print('test date field validatos')

      max_length_date_field = self.transaction._meta.get_field('date').max_length

      min_length_date_field = self.transaction._meta.get_field('date').validators[0].limit_value

      self.assertEquals(max_length_date_field, 8)
      self.assertEquals(min_length_date_field, 8)


    def test_hour_field_validators(self):
      print('test hour field validatos')

      max_length_hour_field = self.transaction._meta.get_field('hour').max_length

      min_length_hour_field = self.transaction._meta.get_field('hour').validators[0].limit_value

      self.assertEquals(max_length_hour_field, 6)
      self.assertEquals(min_length_hour_field, 6)


    def test_value_field_validators(self):
      print('test value field validatos')

      max_length_value_field = self.transaction._meta.get_field('value').max_length

      min_length_value_field = self.transaction._meta.get_field('value').validators[0].limit_value

      self.assertEquals(max_length_value_field, 10)
      self.assertEquals(min_length_value_field, 10)


    def test_cpf_field_validators(self):
      print('test cpf field validatos')

      max_length_cpf_field = self.transaction._meta.get_field('cpf').max_length

      min_length_cpf_field = self.transaction._meta.get_field('cpf').validators[0].limit_value

      self.assertEquals(max_length_cpf_field, 11)
      self.assertEquals(min_length_cpf_field, 11)


    def test_card_field_validators(self):
      print('test card field validatos')

      max_length_card_field = self.transaction._meta.get_field('card').max_length

      min_length_card_field = self.transaction._meta.get_field('card').validators[0].limit_value

      self.assertEquals(max_length_card_field, 12)
      self.assertEquals(min_length_card_field, 12)


    def test_store_owner_field_validators(self):
      print('test store_owner field validatos')

      max_length_store_owner_field = self.transaction._meta.get_field('store_owner').max_length

      min_length_store_owner_field = self.transaction._meta.get_field('store_owner').validators[0].limit_value

      self.assertEquals(max_length_store_owner_field, 14)
      self.assertEquals(min_length_store_owner_field, 14)


    def test_store_name_field_validators(self):
      print('test store_name field validatos')

      max_length_store_name_field = self.transaction._meta.get_field('store_name').max_length

      min_length_store_name_field = self.transaction._meta.get_field('store_name').validators[0].limit_value

      self.assertEquals(max_length_store_name_field, 19)
      self.assertEquals(min_length_store_name_field, 19)