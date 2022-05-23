frappe.ui.form.on("Item",{
    // setup: function(frm){
    //     console.log("Setup is running.........")
    //     if(frm.doc.item_name){
    //         console.log("inside if operator")
    //         frappe.call({
    //             method:'kt.api.create_book',
    //             args: {
    //                 "book_name" : frm.doc.item_name,
    //                 "price" : frm.doc.price,
    //                 "pages" : frm.doc.to_no_of_pages
    //             },
    //             callback: function(resp){
    //                 //
    //                 if(resp.message){
    //                     console.log("resp is: ",resp.message)
    //                     frappe.msgprint(`Book ${resp.message} created!`)
    //                 }
    //             }
    //         })
    //     }
    // }
})

