import frappe
@frappe.whitelist()
def get_stock_availability(drug_id):
    actual_qty = frappe.db.get_value(
        "Stock Ledger Entry",
        filters={
            "item_code": drug_id,
            #"warehouse": "All Warehouses - T4GC",
            "is_cancelled": 0,
        },
        fieldname="qty_after_transaction",
        order_by="posting_date desc, posting_time desc, creation desc",
    ) or 0.0

    return actual_qty