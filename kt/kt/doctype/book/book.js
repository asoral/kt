// Copyright (c) 2022, grand hyper and contributors
// For license information, please see license.txt

frappe.ui.form.on('Book', {
	after_save: function(frm){
		var book_name = frm.doc.book_name
		if(book_name.length < 10){
			frappe.msgprint("Book name must be atleast of 10 char");
			//frappe.throw("Book name must be atleast of 10 char")
		}
	},
	before_save: function(frm){
		console.log("before save is running.........................")
		if(!frm.doc.total_no_of_pages) {
			frm.doc.total_no_of_pages = 100
		}
	}
});
