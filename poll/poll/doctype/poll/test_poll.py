# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Poll')

from .poll import insert_vote, add_vote, DuplicateVoteError

class TestPoll(unittest.TestCase):
	def setUp(self):
		frappe.db.sql("""delete from `tabPoll Vote`""")
		frappe.db.sql("""update `tabPoll Option` set votes = 0""")

	def test_valid_vote(self):
		frappe.local.request = frappe._dict({"headers":{"REMOTE_ADDR":"127.0.0.1"}})
		test_poll = frappe.get_doc("Poll", "_test-poll")
		add_vote(test_poll.poll_options[0].name)
		test_poll = frappe.get_doc("Poll", "_test-poll")
		self.assertEquals(test_poll.poll_options[0].votes, 1)

		frappe.request.headers["REMOTE_ADDR"] = "127.0.0.2"
		add_vote(test_poll.poll_options[0].name)
		test_poll = frappe.get_doc("Poll", "_test-poll")
		self.assertEquals(test_poll.poll_options[0].votes, 2)

	def test_invalid_vote(self):
		frappe.request = frappe._dict({"headers":{"REMOTE_ADDR":"127.0.0.1"}})
		test_poll = frappe.get_doc("Poll", "_test-poll")
		add_vote(test_poll.poll_options[0].name)
		self.assertRaises(DuplicateVoteError, insert_vote, test_poll.poll_options[0].name)

		test_poll = frappe.get_doc("Poll", "_test-poll-1")
		insert_vote(test_poll.poll_options[0].name)

