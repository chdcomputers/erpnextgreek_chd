# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnextgreek_chd"
app_title = "ERPnext Greek support by ChD Computers"
app_publisher = "ChD Computers"
app_description = "Greek support for ERPnext"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "chdcomputers@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnextgreek_chd/css/erpnextgreek_chd.css"
# app_include_js = "/assets/erpnextgreek_chd/js/erpnextgreek_chd.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnextgreek_chd/css/erpnextgreek_chd.css"
# web_include_js = "/assets/erpnextgreek_chd/js/erpnextgreek_chd.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnextgreek_chd.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnextgreek_chd.install.before_install"
# after_install = "erpnextgreek_chd.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnextgreek_chd.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnextgreek_chd.tasks.all"
# 	],
# 	"daily": [
# 		"erpnextgreek_chd.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnextgreek_chd.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnextgreek_chd.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnextgreek_chd.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnextgreek_chd.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnextgreek_chd.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "erpnextgreek_chd.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]
fixtures = ["Custom Field"]
