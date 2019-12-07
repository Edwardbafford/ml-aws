window.onload = function(){
    $("#image-alert").hide()

    $(".custom-file-input").on("change", function() {
	    var fileName = $(this).val().split("\\").pop();
	    $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
	    if (fileName.split(".").slice(-1)[0] == 'jpg') {
		    $('#submit-button').prop('disabled', false);
		    $("#image-alert").hide()
	    }else{
		    $("#image-alert").show()
	    }
    })
};