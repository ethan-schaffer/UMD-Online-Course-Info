/*
	Data Structure Explained
	
	catalog is a dictionary with course codes as its keys. Course codes are assumed
	to be unique ('primary keys')
	
	let catalog = {
		'course code 1' : 'course 1 data structure',
		...
	}
	
	Data about each course is currently nested under other data structures.
	Unnesting course data will help with implementing search.
	
	
	The 'course data structure' referred to by 'course code' keys is expanded below
	
	let catalog = {
		'course code 1' : 	{
								'department' : 'four letter department code',
								'course-name' : 'name of the course'
								'sections' : 'sections data structure'
							},
		...
	}
	
	The 'sections data structure' refered to by the 'sections' key is shown next
	
	...
	'sections' : 	{
						'four digit section code 1' : 'section data structure' (expanded below)
						'four digit section code 2' : 	{
															'instructor' : 'instructor name',
															'lecture-time' : 'lecture time string',
															'lab-time' : 'lab time string',
															'learning-mode' : 'online' 'in-person' or 'blended',
															'capacity' : '# of total seats',
															'open-seats' : '# of open seats'
														}
					}
	...
	
	I made two new keys for storing infomation about a course's lecture time and
	dicussion/lab time. I hope no classes have a three meeting time.
	
	Our current data list the lecture class and the dicussion/lab class as
	seperate sections, which is what above is trying to rectify. In the case where
	a class only has lab, there needs to be extra webscraping to know that the
	time listed is for a lab dicussion. I'm ok with just having an array of the
	listed times for a section called 'class-times'
	
	Note ii : some classes have no time listed. That is an edge case that we will need
	to catch.
	
	I moved infomation about mode of learning to section data "level." Classes like ENGL101
	have sections with in-person learning and sections with blended learning.
*/

let last_updated = '01/01/1970 12:00am';

let catalog = 	[
					'CMSC131' : {
									'department' : 'CMSC',
									'course-name' : 'Object-Oriented Programming I',
									'sections' : 	{
														'0101' : 	{
																		'instructor' : 'Nelson Padua-Perez',
																		'lecture-time' : 'MWF 10:00am - 10:50am',
																		'lab-time' : 'MW 11:00am - 11:50am',
																		'learning-mode' : 'in-person',
																		'capacity' : '32',
																		'open-seats' : '0'
																	},
														'0102' :	{
																		'instructor' : 'Nelson Padua-Perez',
																		'lecture-time' : 'MWF 10:00am - 10:50am',
																		'lab-time' : 'MW 12:00pm - 12:50pm',
																		'learning-mode' : 'in-person',
																		'capacity' : '32',
																		'open-seats' : '0'
																	}
													}
								},
					'KNES137N' : {
									'department' : 'KNES',
									'course-name' : 'Physical Education Activities: Coed; Golf (Beginning)',
									'sections' :	{
														'0101' :	{
																		'instructor' : 'Jeff Maynor',
																		'lecture-time' : null,
																		'lab-time' : 'MW 10:00am - 12:00pm', // only meets for 'lab'
																		'learning-mode' : 'in-person',
																		'capacity' : '20',
																		'open-seats' : '0'
																	}
													}
								},
					'ISRL249N' : {
									'department' : 'ISRL',
									'course-name' : 'Zionism and Sexual Revolution',
									'sections' :	{
														'0101' :	{
																		'instructor' : 'Shirelle Doughty',
																		'lecture-time' : null, // no meeting time listed
																		'lab-time' : null,
																		'learning-mode' : 'online',
																		'capacity' : '40',
																		'open-seats' : '0'
																	}
													}
								}
				];