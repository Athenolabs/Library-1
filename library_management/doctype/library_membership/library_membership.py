# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LibraryMembership(Document):
	def on_payment_authorized(self, *args, **kwargs):
		self.db_set("paid", 1)

	def validate(self):
		receipt = frappe.new_doc("Receipt")
		receipt.membership_id = self.name
		receipt.member_first_name = self.member_first_name
		receipt.member_last_name = self.member_last_name
		receipt.member_email_id = self.email_id
		receipt.membership_start_date = self.from_date
		receipt.membership_end_date = self.to_date
		receipt.save()
