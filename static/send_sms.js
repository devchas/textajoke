function validateForm() {
	$(".alert").remove();
    var x = document.forms["numForm"]["number"].value;
    if (x == null || x == "") {
    	addAlert("Enter a phone number");
        return false;
    } else if (!valPhone(x)) {
    	addAlert("That's not a valid number- try again.");
    	return false;
    } else {
    	var newNum = getClnNum(x);
    	document.forms["numForm"]["number"].value = newNum;
    	return true;
    }
}

function valPhone(num) {
  var reg = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
  if (num.match(reg)) {
    return true;
  }
  else {
    return false;
  }
}

function getClnNum(num) {
	var numStr = "";
	var nums = /[0-9]/;
	for (var i = 0; i < num.length; i++) {
		if (num.charAt(i).match(nums)) {
			numStr += num.charAt(i);
		}
	}
	return numStr;
}

function addAlert(message) {
	$( "#numClass" ).after( "<span class='alert'>" + message + "</span>" );	
}