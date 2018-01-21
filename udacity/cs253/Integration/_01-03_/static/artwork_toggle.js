function toggle_bg(e){
	//Checking if select field is enabled
	if (document.getElementById("btn").value=="Dark on Light"){
		//Change the select field state to disabled and changing the value of button to enable
		document.getElementById("btn").value="Light on Dark";
		document.getElementById("artwork_list").style.background = "#FFFFFF";
		document.getElementById("artwork_list").style.color = "#000000";
	}

	//Checking if select field is disabled
	else {
		//Change the select field state to enabled and changing the value of button to disable
		document.getElementById("btn").value="Dark on Light";
		document.getElementById("artwork_list").style.background = "#2A4767";
		document.getElementById("artwork_list").style.color = "#FFFFFF";
	}
}