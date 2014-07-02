from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

no_cache = 1

def get_context(context):
	context.listed_polls = frappe.get_list("Poll", fields = ["title", "page_name", "description", "poll_status", "parent_website_route"], filters={"published":1})
	#context.parents = 
	context.std_footer = frappe.db.get_value("Poll Settings", fieldname = "standard_footer")
	context.std_header = frappe.db.get_value("Poll Settings", fieldname = "standard_header")
	print context.listed_polls
	return context