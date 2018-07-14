$(document).ready(function(){

	console.log("ready");
	$("#auth").click(function(){
		console.log("clicked")
		$.ajax({
		  url: "http://127.0.0.1:5000/register/"+$("#email").val()+"/"+$("#password").val()
		}).done(function(resp) {
			console.log(resp);
			if(resp=="true"){
				window.location.href="/login"
			}
		});
	});

});