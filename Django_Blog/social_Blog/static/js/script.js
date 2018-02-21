$(document).ready(function(){

	$(".subscribe").on("click",function () {
		// body...
		//console.log($(this).html());
		var userID=$(this).attr("userID");
		var catID=$(this).attr("catID");
    var catName=$(this).attr("catName");
		
// case of Subscribe user to certain catagory

	if($(this).html()=="Subscribe"){
		//change button to unsubscribe
		$(this).html("unsubscribe");
		console.log($(this).html());
		$.ajax({
        url: '/social_Blog/ajax/subscribe/',
        type: 'POST',
        data: {
          'userID': userID,
          'catID': catID,
          'catName':catName
        },
       
        dataType: 'json',
        success: function (data) {
          if (data.success) {
          	console.log("user subscribe in catagory");
          
          }
        }
      });

	}
// case of UnSubscribe user to certain catagory	
	else{
		$(this).html("Subscribe");
		$.ajax({
        url: '/social_Blog/ajax/unsubscribe/',
        type: 'POST',
        data: {
          'userID': userID,
          'catID': catID,
          'catName':catName
        },
       
        dataType: 'json',
        success: function (data) {
          if (data.success) {
          	console.log("user unsubscribe in catagory");
          
          }
        }
      });
	}	



	});
});