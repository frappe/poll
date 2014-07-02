# Copyright (c) 2013, Web Notes Technologies
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

from poll.poll.doctype.poll.poll import DuplicateVoteError
from poll.poll.doctype.poll.poll import InactivePollStatusError

import time
import datetime

class PollVote(Document):
	def validate(self):
		global duplicate, status
		self.ip = frappe.get_request_header('REMOTE_ADDR', '127.0.0.2')
		duplicate = frappe.db.get_value("Poll Vote", {"ip": self.ip, "poll": self.poll})
		status = frappe.db.get_value("Poll", {"name": self.name}, "poll_status")

		if duplicate:
			raise DuplicateVoteError
		
		if status == "Inactive"
			raise InactivePollStatusError

	def on_update(self):
		poll = frappe.get_doc("Poll", self.poll)
		option = filter(lambda d: d.name == self.option_name, poll.poll_options)[0]
		option.votes = len(frappe.db.get_values("Poll Vote", {"option_name": self.option_name}))
		poll.save(ignore_permissions=True)