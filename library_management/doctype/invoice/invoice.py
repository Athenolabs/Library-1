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
		content = "Library membership initiated for {0}. Please visit localhost:8000/razorpay-payment to complete the transaction.".format(member_name)

		frappe.sendmail(recipients=[email],
			subject="Invoice details",
			content=content)
