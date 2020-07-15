
function getFooterContent() {
    //console.log("here!");
    let time = `2020. Ethan Schaffer, Bill Shi. Last updated ${last_updated}`;
    //console.log(time);
    return time;
}

function getChartUrl(in_person, online) {
    console.log(in_person, online);
    let url = "https://quickchart.io/chart?bkg=white&c=%7Btype%3A%27pie%27%2Cdata%3A%7Bdatasets%3A%5B%7Bdata%3A%5B"+ in_person + "%2C" + online + "%5D%2CbackgroundColor%3A%5B%27rgb(255%2C99%2C132)%27%2C%27rgb(54%2C162%2C235)%27%5D%2Clabel%3A%27Dataset%25201%27%2C%7D%2C%5D%2Clabels%3A%5B%27Online%27%2C%27In Person%27%5D%7D%7D";
    console.log(url);
    return url;
}

function get_course_count_info() {
    return "We define a course as a single section that a class meets during. In total, we found that there were " + total_online + " online sections and " + total_in_person + " in person sections, making " + total_classes + " classes in all.";
}

function get_seat_count_info() {
    return "A seat is a single spot in a class a student can fill, so a student will fill multiple seats. In total, we found that there were " + seats_online + " seats online and " + seats_in_person + " seats in person, making " + seats_total + " total seats.";
}

// wait until html elements are ready
$(document).ready(function () {
    $('#footer').text(getFooterContent());
    $('#chart1').attr("src",getChartUrl(percent_online, percent_in_person));
    $('#chart2').attr("src",getChartUrl(percent_seats_online, percent_seats_in_person));
    $('#course_count_info').text(get_course_count_info());
    $('#seat_count_info').text(get_seat_count_info());
	
	// fill department summary table
	for (dept_code in dept_summary) {
		let dept_info = dept_summary[dept_code];
		
		let summary_container = $(`<li>
									<table>
										<p>${dept_code} | ${dept_info['department-name']}</p>
										<tr>
											<td>In Person Sections:<br>${dept_info['inPersonSections']}</td>
											<td>Online Sections:<br>${dept_info['onlineSections']}</td>
											<td>In Person Seats:<br>${dept_info['inPersonSeats']}</td>
											<td>Online Sections<br>${dept_info['onlineSeats']}</td>
										</tr>
									</table>
								</li>`);
		
		$('$dept-summary-table').append(XXX);
	}
})