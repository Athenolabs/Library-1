# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LibraryMember(Document):
	def validate(self):
		content = "Hello {0} {1}, welcome to the Frappe Library!".format(self.first_name, self.last_name)

		frappe.sendmail(recipients=[self.email_id],
			subject="Welcome!",
			content=content)
