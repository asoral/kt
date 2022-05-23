import frappe
from erpnext.stock.doctype.item.item import Item

@frappe.whitelist()
def create_book(book_name,price,pages):
    doc = frappe.new_doc("Book")
    doc.book_name = book_name
    doc.price = price
    doc.total_no_of_pages = pages
    doc.insert()
    print("######"*20)
    return doc.get("name")

class CustomItem(Item):
    def before_insert(self):
        # create a new book on creation of new item
        print("####"*10)
        print(self.item_name,self.price,self.to_no_of_pages)
        create_book(self.item_name,self.price,self.to_no_of_pages)
    



