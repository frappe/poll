app_name = "poll"
app_title = "Poll"
app_publisher = "Web Notes Technologies"
app_description = "Website Poll"
app_icon = "icon-ok-sign"
app_color = "#8e44ad"
app_email = "info@frappe.io"
app_url = "https://frappe.io"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/poll/css/poll.css"
# app_include_js = "/assets/poll/js/poll.js"

# include js, css files in header of web template
# web_include_css = "/assets/poll/css/poll.css"
# web_include_js = "/assets/poll/js/poll.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
website_generators = ["Poll"]

# Installation
# ------------

# before_install = "poll.install.before_install"
# after_install = "poll.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "poll.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.core.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.core.doctype.event.event.has_permission",
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
# 		"poll.tasks.all"
# 	],
# 	"daily": [
# 		"poll.tasks.daily"
# 	],
# 	"hourly": [
# 		"poll.tasks.hourly"
# 	],
# 	"weekly": [
# 		"poll.tasks.weekly"
# 	]
# 	"monthly": [
# 		"poll.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "poll.install.before_tests"

