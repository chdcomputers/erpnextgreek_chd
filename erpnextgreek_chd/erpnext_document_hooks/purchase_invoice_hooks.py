from __future__ import unicode_literals

import frappe

def pi_on_submit(doc, method):
    needsUpdate = False
    
    for item in doc.get("items"):
        print(item.item_code)
        pr = item.purchase_receipt
        print(pr)

    if pr is not None:
        print("Purchase receipt found")
        pr_doc = frappe.get_doc("Purchase Receipt", pr)
        if pr_doc is not None:
            print("Purchase receipt document retrieved")
            for pr_item in pr_doc.get("items"):
                print(pr_item.item_code)
                if item.item_code == pr_item.item_code:
                    if pr_item.valuation_rate != item.rate:
                        needsUpdate = True
                        pr_item.valuation_rate = item.rate

            if needsUpdate:
                print("Updating")
                # save will update landed_cost_voucher_amount and voucher_amount in PR,
                # as those fields are allowed to edit after submit
                pr_doc.save()

                # update stock & gl entries for cancelled state of PR
                pr_doc.docstatus = 2
                pr_doc.update_stock_ledger(allow_negative_stock=True, via_landed_cost_voucher=False)
                pr_doc.make_gl_entries_on_cancel(repost_future_gle=False)

                # update stock & gl entries for submit state of PR
                pr_doc.docstatus = 1
                pr_doc.update_stock_ledger(via_landed_cost_voucher=True)
                pr_doc.make_gl_entries()