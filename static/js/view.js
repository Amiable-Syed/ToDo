function openTab(tabName) {
	console.log(tabName);
	  var i, x;
	  x = document.getElementsByClassName("containerTab");
	  for (i = 0; i < x.length; i++) {
	     x[i].style.display = "none";
	  }
	  document.getElementById(tabName).style.display = "block";
}

$(document).ready(function(){

	$(".sidenav-right a").on('click',function(){
		console.log("clicked");
		openTab($(this).attr('name'));
	});

	



	$.ajax({
		  url: "http://127.0.0.1:5000/getTodolists"
		}).done(function(resp) {


			var arr = ["b1","b2","b3","b4","b5"];
			var a_s  = $(".sidenav-right a")
			$(resp).each(function(i,value){
				$("#"+arr[i]+" h2").text(value.title);
				$("#"+arr[i]+" p").text(value.description);
				$(a_s[i]).text(value.title);
			});

		});
});