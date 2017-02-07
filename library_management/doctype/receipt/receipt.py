# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Receipt(Document):
	def validate(self):
		content = "Hi {0} {1}, your Frappe Library membership is confirmed!".format(self.member_first_name, member_last_name)

		frappe.sendmail(recipients=[self.member_email_id],
			subject="Frappe Library Membership Receipt",
			content=content)
