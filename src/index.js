// simple front end
// by Bill Shi


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
						<p>Meeting Time: ${class_time[0]} ${class_time[1]} -
						${class_time[2]}</p>
						<p>Seats (Total): ${course_obj[section]}</p>
					</li>`);
		ul.append(li);
	}
	
	return course_container;
}

// wait until html elements are ready
$(document).ready(function () {
	
	let department = 'AASP';
	let course = 'AASP100';
	let course_obj = in_person[department][course];
	
	$('#search-return').append(createCourseContainer(course, course_obj));
	
		
	
	$('#class-lookup').on('input', function () {
		let usr_input = $(this).val();
		
		if (usr_input.length == 0) {
			$('#search-return').empty();
		}
		
		if (usr_input.length == 4) {
			
			if (dept_codes.includes(usr_input)) {
				$('#search-return').empty();
				
				let department = usr_input;
				
				for (course in in_person[department]) {
					let course_obj = in_person[department][course];
					$('#search-return').append(createCourseContainer(course, course_obj));
				}
				
			}
			
		}
	})

})