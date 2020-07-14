// simple front end
// by Bill Shi

// catalog

let courses = catalog[0]
let in_person = class_info['in person'];
let online = class_info['online'];

// list of department codes
// should be hardcoded
let dept_codes = [];
for (department in in_person) {
	dept_codes.push(department);
}


function createCourseContainer (course, course_obj) {
	let course_container = 	$(`<div class='course-container'>
								<h3>${course}</h3>
								<ul></ul>
							</div>`);
	let ul = $(course_container, 'ul');
	
	for (section in course_obj) {
		let section_string = section.substring(1,section.length-1)
							.replace(/'/g,'');
		let class_time = section_string.split(',');
		
		let li = 	$(`<li>
						<table id="section_table">
							<tr>
								<td style="text-align:left" width: 50%;>  Meeting Time: ${class_time[0]} ${class_time[1]} - ${class_time[2]}</td>
								<td style="text-align:left" width: 50%;>  Total Seats: ${course_obj[section]}</td>
							</tr>
						</table>
					</li>`);
		ul.append(li);
	}
	
	return course_container;
}

function createComplexCourseContainer (course, course_info) {
	let course_container = 	$(`<div class='course-container'>
								<h3>${course + " " + course_info["course-name"]}</h3>
								<ul></ul>
							</div>`);
	let ul = $(course_container, 'ul');
	
	for (section in course_info["sections"]) {
		let text = "";
		if(course_info["sections"][section]["lab-time"] !== null) { 
			text = "Additional Section:<br>" + course_info["sections"][section]["lab-time"]
		}
		let li = 	$(`<li>
						<table id="section_table">
							<tr>
								<td style="text-align:left">Section:<br>${section}</td>
								<td style="text-align:left">Total Seats:<br>${course_info["sections"][section]["capacity"]}</td>
								<td style="text-align:left">Taught by:<br>${course_info["sections"][section]["instructor"]}</td>
								<td style="text-align:left">Lecture Time:<br>${course_info["sections"][section]["lecture-time"]}</td>
								<td style="text-align:left">${text}</td>
								<td style="text-align:left">Learning Type:<br>${course_info["sections"][section]["learning-mode"]}</td>
								<td style="text-align:left">Seats Open:<br>${course_info["sections"][section]["open-seats"]}</td>
							</tr>
						</table>
					</li>`);
		ul.append(li);
	}
	
	return course_container;
}

// wait until html elements are ready
$(document).ready(function () {
	
	let department = '';
	let course = '';
		
	$('#search-return').empty();
		
	
	$('#class-lookup').on('input', function () {
		let usr_input = $(this).val().toUpperCase();
		
		if (usr_input.length == 0) {
			$('#search-return').empty();
		}
		
		else {
				$('#search-return').empty();
				
				let department = usr_input;
				
				/*for (course in in_person[department]) {
					let course_obj = in_person[department][course];
					$('#search-return').append(createCourseContainer(course, course_obj));
				}*/
				
				for (course in courses ) {
					if(department === courses[course]["department"]){
						$('#search-return').append(createComplexCourseContainer(course, courses[course]));
					}
				}

				
			
		}
	})

})