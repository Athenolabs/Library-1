# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Invoice(Document):
	def on_submit(self):
		date = frappe.get_value("Library Transaction", self.transaction_date, "transaction_date")
		content = "Invoice generated for {0} issued to {1} on {2}".format(self.article_name, self.member_first_name, date)

		frappe.sendmail(recipients=[self.email_id],
			sender="test@library.com",
			subject="Invoice details",
			content=content)
