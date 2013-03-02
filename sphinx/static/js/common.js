/* Includes the common functionalities required on almost every page */

$(document).ready(function() {
	$("#id_tags").tagit({
		allowSpaces : true,
		tagSource: function(search, showChoices) {
			var choices = ["a", "b", "c"]; 
			showChoices(this._subtractArray(choices, this.assignedTags()));
		}
	});
});
