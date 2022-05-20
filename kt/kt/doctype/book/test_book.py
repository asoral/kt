# Copyright (c) 2022, grand hyper and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase
from kt.kt.doctype.book.book import for_test


def craete_doc(item_code):
		print("code completed")
		frappe.flags.test_events_created = True
		return for_test(item_code)
		
class TestBook(FrappeTestCase):
	def __init__(self):
		self.before_tests()
	def before_tests(self):
		print("####################################################### working")
		item_code = "Test"
		doc = craete_doc(item_code)
		self.assertEqual(item_code,doc)
