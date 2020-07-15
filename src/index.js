
function getFooterContent() {
    //console.log("here!");
    let time = `2020. Ethan Schaffer, Bill Shi. Last updated ${last_updated}`;
    //console.log(time);
    return time;
}

function getChartUrl(in_person, online) {
    console.log(in_person, online);
    let url = "https://quickchart.io/chart?bkg=white&c=%7Btype%3A%27pie%27%2Cdata%3A%7Bdatasets%3A%5B%7Bdata%3A%5B"+ in_person + "%2C" + online + "%5D%2CbackgroundColor%3A%5B%27rgb(232%2C56%2C79)%27%2C%27rgb(32%2C142%2C163)%27%5D%2Clabel%3A%27Dataset%25201%27%2C%7D%2C%5D%2Clabels%3A%5B%27Online%27%2C%27In Person%27%5D%7D%7D";
    console.log(url);
    return url;
}

function get_course_count_info() {
    return "A section is a single time that a class meets during. We couldn't scan every class, but we found that there were " + parseInt(total_online,10).toLocaleString() + " online sections and " + parseInt(total_in_person,10).toLocaleString() + " in person sections. In total, there are at least" + parseInt(total_classes,10).toLocaleString() + " sections.";
}

function get_seat_count_info() {
    return "A seat is a single spot in a class a student can fill, so a student will fill multiple seats. We couldn't scan every class, but we found that there were " + parseInt(seats_online,10).toLocaleString() + " seats online and " + parseInt(seats_in_person,10).toLocaleString() + " seats in person. Of the ones we could scan, there are " + parseInt(seats_total,10).toLocaleString() + " total seats.";
}

function get_dept_summary() {
	let output = 	$(`<div class='output'>
								<ul></ul>
							</div>`);
	let ul = output.find('ul');
	
	
	for (dept_code in dept_summary) {
		let dept_info = dept_summary[dept_code];
		
		let summary_container = $(`<li>
									<b><p>${dept_info['departmentName']}&nbsp;(${dept_code})</p></b>
									<table>
										<tr><td>Online Sections:</td><td>${dept_info['onlineSections']}</td><td>In Person Sections:</td><td>${dept_info['inPersonSections']}</td></tr>
										<tr><td>Online Seats:</td><td>${dept_info['onlineSeats']}</td><td>In Person Seats:</td><td>${dept_info['inPersonSeats']}</td></tr>
									</table>
									<br>
								</li>`);
		console.log(summary_container)
		console.log(dept_info);
		ul.append(summary_container);
		
	}
	console.log(output);
	return output;
}

// wait until html elements are ready
$(document).ready(function () {
    $('#footer').text(getFooterContent());
    $('#chart1').attr("src",getChartUrl(percent_online, percent_in_person));
    $('#chart2').attr("src",getChartUrl(percent_seats_online, percent_seats_in_person));
    $('#course_count_info').text(get_course_count_info());
	$('#seat_count_info').text(get_seat_count_info());
	$('#dept-summary-table').append(get_dept_summary());
	
	// fill department summary table

})