frappe.ui.form.on("Poll", "refresh", function (frm) {
	frm.add_custom_button(__('Make Copy'), function() {
		var new_doc = frappe.model.copy_doc(cur_frm.doc);
		$.each(new_doc.poll_options, function(i, newopt) {
			$.each(cur_frm.doc.poll_options, function(i, oldopt) {
				if(newopt.option == oldopt.option) {
					newopt.previous_votes = cint(cint(oldopt.previous_votes) + cint(oldopt.votes) / 2);
					return false;
				}
			});
		}, null, "btn-default");
		frappe.set_route("Form", "Poll", new_doc.name);
	}, "icon-copy");
});
