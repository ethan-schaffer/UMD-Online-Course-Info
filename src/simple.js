// simple front end
// by Bill Shi


// placeholder data structure to store course infomation, not final
let catalog = 	[
					{
						'course-name': 'CMSC389k',
						'sections': [
										{
											'section-code': '0101',
											'meeting-time': 'MWF 9:30 AM - 10:45 AM',
											'capacity': 32,
											'online': true
											
										},
										{
											'section-code': '0102',
											'meeting-time': 'MWF 11:00 AM - 12:15 PM',
											'capacity': 32,
											'online': true
											
										}
									]
					},
					{
						'course-name': 'CMSC216',
						'sections': [
										{
											'section-code': '0101',
											'meeting-time': 'TuTh 3:30 PM - 4:15 PM',
											'capacity': 200,
											'online': true
										}
									]
					}
				];
				

// adds course infomation to html list element
for (course of catalog) {
	
	console.log(course['course-name'])
	
	// dumb way of doing this
	let sections_html = '';
	for (section of course.sections) {
		sections_html += 	'<li> \
								<h3>Section#: ${section['section-code']}</h3> \
								<p>Meeting time: ${section['meeting-time']}</p> \
								<p>Seating: ${section.capacity}</p> \
								<p>Online?: ${section.online}</p> \
							</li>\n';
	};
	
	
	$('#catalog').append("<li> \
							<h2>${course['course-name']}</h2> \
							${sections_html} \
						</li>")
}
			
