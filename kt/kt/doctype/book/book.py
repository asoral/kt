# Copyright (c) 2022, grand hyper and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Book(Document):
	def validate(self):
		self.validate_price()
		self.validate_no_of_pages()
		#self.validate_edition_year()
    
	def validate_price(self):
		if not self.price:
			frappe.throw("Please enter the price BOOK DT")
	def validate_no_of_pages(self):
		if self.total_no_of_pages < 1:
			frappe.throw("Invalid no. of pages this message from book DT")
	
	def validate_edition_year(self):
		for i in self.book_edition:
			print("current year is: ",self.current_edition)
			if self.current_edition == i.get("year"):
				frappe.throw("Duplicate entry for edition")
	
	def before_save(self):
		#pass
		self.calculate_value()
		# if not self.current_edition:
		# 	pass
		# no_of_ed = "{0}- edition".format(len(self.book_edition)+1)
		
		# self.append("book_edition", {
		# 	"edition" : no_of_ed,
		# 	"year": self.current_edition
		# })
		# self.current_edition = None
		# if self.clear_table:
		# 	self.book_edition = []

	def calculate_value(self):
		prepared_data = []
		for row in self.book_edition:
			val = float(row.get("edition")) * 10
			prepared_data.append({
				"edition" : row.get("edition"),
				"year" : val
			})

		self.book_edition = []
		for d in prepared_data:
			self.append("book_edition", {
				"edition" : d.get("edition"),
				"year" : d.get("year")
			})
			


		
	

