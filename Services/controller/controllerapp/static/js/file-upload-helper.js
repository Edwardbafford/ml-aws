//JS specific to the file-upload template

window.onload = function(){
    $("#image-alert").hide()

    // triggered when file is selected
    $(".custom-file-input").on("change", function() {
	    var fileName = $(this).val().split("\\").pop();
	    $(this).siblings(".custom-file-label").addClass("selected").html(fileName);

	    // check validate file extension
	    if (fileName.split(".").slice(-1)[0] == 'jpg') {
		    $('#submit-button').prop('disabled', false);
		    $("#image-alert").hide()
	    }else{
		    $("#image-alert").show()
	    }
    })
};