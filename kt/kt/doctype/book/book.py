# Copyright (c) 2022, grand hyper and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Book(Document):
	pass

def for_test(item_code):
	print("########")
	return item_code
