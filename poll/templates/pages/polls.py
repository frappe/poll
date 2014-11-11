from __future__ import unicode_literals
import frappe

no_cache = 1

def get_context(context):
	context.listed_polls = frappe.get_all("Poll",
		fields = ["title", "page_name", "description", "poll_status", "parent_website_route"],
		filters={"published":1})
	context.std_footer = frappe.db.get_value("Poll Settings", fieldname = "standard_footer")
	context.std_header = frappe.db.get_value("Poll Settings", fieldname = "standard_header")
	return context
