# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Invoice(Document):
	def on_submit(self):
		email = frappe.db.get_value("Library Member", self.member, "email_id")
		member_name = frappe.db.get_value("Library Member", self.member, "first_name")
		date = frappe.db.get_value("Library Transaction", self.transaction_id, "transaction_date")
		content = "Invoice generated for {0}, issued to {1} on {2}".format(self.article_name, member_name, date)

		frappe.sendmail(recipients=[email],
			subject="Invoice details",
			content=content)
