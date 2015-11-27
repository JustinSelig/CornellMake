$(document).ready(function() {
window.alert("in else!");
//AJAX SEARCH ON KEYSTROKE
	$(function() {
		$('#search-input').keyup(function(e) {
			if (e.keyCode == 27) { 	//escape key
				$("body").removeClass("stop-scrolling");
				$(".search").animate({top: "-332px"}, 500);
				$(".closeSearch").addClass("hidden");
			} else {
				$.ajax({
					type: "POST",
					url: "/ajax_result/",
					data: { 
						'search_text' : $('#search-input').val(),
						'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
					},
					success: searchSuccess,
					dataType: 'html'
				});
			}
		});
	});
	
	function searchSuccess(data, textStatus, jqXHR) {
		$('#search-results').html(data);
	}

}