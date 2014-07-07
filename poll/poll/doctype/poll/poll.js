frappe.ui.form.on("Poll", "refresh", function (frm) {
	frm.set_intro("");
	if (!frm.doc.__islocal && frm.doc.published) {
		frm.set_intro(__("Published on website at: {0}",
			[repl('<a href="/%(website_route)s" target="_blank">/%(website_route)s</a>', 			frm.doc.__onload)]));
	}

	frm.add_custom_button(__('Make Copy'), function() {
		var new_doc = frappe.model.copy_doc(cur_frm.doc);
		$.each(new_doc.poll_options, function(i, newopt) {
			$.each(cur_frm.doc.poll_options, function(i, oldopt) {
				if(newopt.option == oldopt.option) {
					newopt.previous_votes = cint(cint(oldopt.previous_votes) + cint(oldopt.votes) / 2);
					return false;
				}
			});
		});
		frappe.set_route("Form", "Poll", new_doc.name);
	}, "icon-copy");
});