frappe.ui.form.on("Item",{
    before_save: function(frm){
        frappe.call({
            method:'kt.api.create_book',
            args: {
                
            },
            callback: function(resp){
                //
            }
        })
    }
})

