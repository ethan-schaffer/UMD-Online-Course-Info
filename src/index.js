// simple front end
// by Bill Shi

let placeholder = ['CMSC216','CMSC250']

//$('#courses').length
// 0 when element is not loaded

// problem: can't modify html elements until they are loaded
// quick fix: use document.ready to wait
$(document).ready(function () {
	
	/*
	for (course of placeholder) {
		$('#courses').append(`<li>${course}</li>`)
	}
	*/
	

	let in_person = class_info['in person'];
	
	// only display courses from the AASP department
	let department = 'AASP';
	
	for (course in in_person[department]) {
		
		//console.log(course);
		
		let course_container = $(`<li><h3>${course}</h3></li>`);
		
		let section_list = $('<ul></ul>');
		for (section in in_person[department][course]) {
			section_list.append(`<li>${section} Seating: \
			${in_person[department][course][section]}</li>`)
		}
		
		course_container.append(section_list);
		$('#courses').append(course_container);
	}


})