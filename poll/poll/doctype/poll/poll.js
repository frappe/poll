frappe.ui.form.on("Poll", "refresh", function (frm) {
	frm.set_intro("");
	if (!frm.doc.__islocal && frm.doc.published) {
		frm.set_intro(__("Published on website at: {0}",
			[repl('<a href="/%(website_route)s" target="_blank">/%(website_route)s</a>', 			frm.doc.__onload)]));
	}
});
