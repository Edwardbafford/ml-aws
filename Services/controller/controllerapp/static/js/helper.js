// retrieve nav-bar values
function getNav(href){
    $.ajax({
        url:href,
   		type:'GET',
   		success: function(data){
            $('#sidenav').html(data);
   		}
	});
}