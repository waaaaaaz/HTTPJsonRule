function postWithAjax(myajax) {
  myajax = myajax || {};
  myajax.type = "POST";
  myajax.url = "/api/v2/request";
  myajax.accepts = 'application/json';
  myajax.contentType = 'application/json; charset=utf-8';
  myajax.data = JSON.stringify(requestData());
  myajax.complete = function(jqXHR) {
  	    retjson = $.parseJSON(jqXHR.responseText)
  	    if(!retjson.response_status){
  	    	$("#statuspre").text("Error Message : " + JSON.stringify(retjson));
  	    }
  	    else{
  	    $("#statuspre").text("Response Status : " + retjson.response_status);
		$("#outputpre").text(JSON.stringify(retjson.response_content, null, 2));
		$("#headerpre").text(JSON.stringify(retjson.response_header, null, 2));
  	    }
	}
	$("#outputframe").hide();
	$("#outputframe").attr("src", "")
	$("#ajaxoutput").show();
	$("#statuspre").text("waiting");
    $('#ajaxspinner').show();
	var req = $.ajax(myajax).always(function(){
    $('#ajaxspinner').hide();
	});
}

$("#submitajaxrequest").click(function(e) {
  e.preventDefault();
{
    postWithAjax({});
    $("#statuspre").text(" "); 
    $("#outputpre").text(" ");  
    $("#headerpre").text(" "); 
  }
});

$("#submitajaxsave").click(function(e){
	e.preventDefault();
	{
		postWithAjaxToSave({})
	}
});

function postWithAjaxToSave(myajax){
	myajax = myajax || {};
	myajax.type = "POST";
    myajax.url = "/api/v1/save";
    myajax.accepts = 'application/json';
    myajax.contentType = 'application/json; charset=utf-8';
    myajax.data = JSON.stringify(requestSaveData());
    myajax.complete = function(jqXHR){
    	retjson = $.parseJSON(jqXHR.responseText)
    	$("#statuspre").text(JSON.stringify(retjson));
    }
    $('#ajaxspinner22').show();
	var req = $.ajax(myajax).always(function(){
    $('#ajaxspinner22').hide();
    });
}

function checkForUrl(){
	return $("#paramform").find("urlvalue").length > 0;
}

function requestData(){
	var rdata = {}
	rdata.method = $("#httpmethod").val();
	rdata.url = $("#urlvalue").val();
	if (checkForJson){
		rdata.json = $("#jsonvalue").val();
	}
	return (rdata);
	
}

function requestSaveData(){
	var rsdata = {}
	rsdata.method = $("#httpmethod").val();
	rsdata.url = $("#urlvalue").val();
	rsdata.json = $("#jsonvalue").val();
	rsdata.resp_status = $("#statuspre").html();
	rsdata.resp_header = $("#headerpre").html();
	rsdata.resp_content = $("#outputpre").html();
	return (rsdata)
}

function checkForJson(){
	return $("#paramform").find("jsonvalue").length > 0;
}

function createHeaderData(){
  var mydata = {};
	var parameters = $("#allheaders").find(".realinputvalue");
	for (i = 0; i < parameters.length; i++) {
		name = $(parameters).eq(i).attr("name");
		if (name == undefined || name == "undefined") {
			continue;
		}
		value = $(parameters).eq(i).val();
		mydata[name] = value
	}
  return(mydata);
}

function httpZeroError() {
	$("#errordiv").append('<div class="alert alert-error"> <a class="close" data-dismiss="alert">&times;</a>Javascript returned an HTTP 0 error.</div>');
}
