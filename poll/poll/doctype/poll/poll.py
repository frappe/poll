# Copyright (c) 2013, Web Notes Technologies
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class DuplicateVoteError(frappe.ValidationError): pass

class InactivePollStatusError(frappe.ValidationError): pass

class Poll(WebsiteGenerator):
	template = "templates/generators/poll.html"
	condition_field = "published"
	no_cache = 1
	no_sitemap = 1
	def get_context(self, context):
		context.maxvotes = max([(d.previous_votes or 0) + (d.votes or 0) for d in self.poll_options])
		context.sorted_options = sorted(self.poll_options,
			key=lambda d: ((d.previous_votes or 0) + (d.votes or 0), -d.idx), reverse=True)
		context.status = frappe.db.get_value("Poll", {"name": self.name}, fieldname = "poll_status")
		context.parents = [{'name': self.parent_website_route, 'title': 'Polls'}]
		return context

def insert_vote(option_name):
	vote = frappe.new_doc("Poll Vote")
	vote.option_name = option_name
	vote.poll = frappe.db.get_value("Poll Option", option_name, "parent")
	vote.insert(ignore_permissions=True)

@frappe.whitelist(allow_guest=True)
def add_vote(option_name):
	try:
		insert_vote(option_name)
		return "Thank you for voting. Your vote has been registered!"
	except DuplicateVoteError:
		return "You have already voted on this poll"
	except InactivePollStatusError:
		return "This Poll is Inactive. You cannot vote on this Poll!"
