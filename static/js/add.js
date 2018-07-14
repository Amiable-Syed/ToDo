$(document).ready(function(){

console.log("ready");



	$("#save").click(function(){
		console.log("d ready");
		$.ajax({
		  url: "http://127.0.0.1:5000/addtask/"+$("#title").val()+"/"+$("#description").val()
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