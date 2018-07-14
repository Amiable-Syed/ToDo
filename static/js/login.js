$(document).ready(function(){

	console.log("ready");
	$("#auth").click(function(){
		sessionStorage.setItem("user",$("#email").val());
		console.log("clicked")
		$.ajax({
		  url: "http://127.0.0.1:5000/authenticate/"+$("#email").val()+"/"+$("#password").val()
		}).done(function(resp) {
			console.log(resp);
		  if(resp=="true"){
		  	window.location.href="/main"
		  }else{
		  	$("#msg").show();
		  }
		});
	});

});