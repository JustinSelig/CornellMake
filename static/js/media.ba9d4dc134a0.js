$(document).ready(function(){

	$('body').jKit({ 
		'plugins': {
			date: { 'path': "../js/plugins/datepicker/js/datepicker.js", 'fn': 'DatePicker' },
			hint: { 'path': "../js/plugins/jquery.ztinputhint-1.2.js", 'fn': 'ztInputHint' },
			maxlength: { 'path': "../js/plugins/maxlength/jquery.maxlength-min.js", 'fn': 'maxlength' },
			confirm: { 'path': "../js/plugins/jquery.confirm-1.3.js", 'fn': 'confirm' }
		},
		'replacements': {
			'encode': specialEncodeCommand
		}
	});

	if ($('#custombuilder').length > 0){
		calculateCustomSizes();
		$('#custombuilder').find('input').on( 'change click', function(){
			calculateCustomSizes();
		});
		$('#custombuilder').find('.customcmd').on( 'click', function(){
			$(this).find('input').prop("checked", !$(this).find('input').prop("checked"));
			calculateCustomSizes();
		});
	}

	prettyPrint(); // Google Code Prettify

});

function downloadCustom(){
	var commands = '';
	$('#custombuilder').find('.customcmd input:checked').each( function(){
		var name = $(this).attr('name');
		if (commands != '') commands += '-';
		commands += name;
	});
	window.location = 'http://jquery-jkit.com/jkit.custom/download.php?commands='+commands;
}

function calculateCustomSizes(){
	if ($('#custombuilder').length > 0){
		var sizefull = parseInt($('#size_src_auto').text().slice(0,-1))*1024;
		var sizemin = parseInt($('#size_min_auto').text().slice(0,-1))*1024;
		var sizegzip = parseInt($('#size_gzip_auto').text().slice(0,-1))*1024;
		$('#custombuilder').find('.customcmd').each( function(){
			if ($(this).find('input').is(':checked')){
				sizefull += parseInt($(this).attr('data-size-full'));
				sizemin += parseInt($(this).attr('data-size-min'));
				sizegzip += parseInt($(this).attr('data-size-gzip'));
			}
		});
		$('#size_src_custom').text(Math.round(sizefull/1024)+'k');
		$('#size_min_custom').text(Math.round(sizemin/1024)+'k');
		$('#size_gzip_custom').text(Math.round(sizegzip/1024)+'k');
	}
}

function specialEncodeCommand(that, type, options){

	var s = this.settings; // we don't need this one, but I'll leave it here so you know how to get the plugin settings in case you need them
	var $that = $(that);

	this.executeCommand(that, type, options); // execute the original command

	// now add some additional functionality:

	if (options.format == 'uppercase'){
		$that.html($that.html().toUpperCase());
	}

}