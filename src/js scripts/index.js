/*
	dynamically insert text/graphics for index.html
	By: Ethan Schaffer
*/

// create pie chart graphic and return link to image
function getChartUrl(in_person, online) {
	return "https://quickchart.io/chart?bkg=white&c=%7Btype%3A%27pie%27%2Cdata%3A%7Bdatasets%3A%5B%7Bdata%3A%5B"+ in_person + "%2C" + online + "%5D%2CbackgroundColor%3A%5B%27rgb(232%2C56%2C79)%27%2C%27rgb(32%2C142%2C163)%27%5D%2Clabel%3A%27Dataset%25201%27%2C%7D%2C%5D%2Clabels%3A%5B%27Online%27%2C%27In Person%27%5D%7D%7D";
}

// return summary text about course infomation
function get_course_count_info() {
    return "A section is a single time that a class meets during. We found that there were " + parseInt(total_online,10).toLocaleString() + " online sections and " + parseInt(total_in_person,10).toLocaleString() + " in person sections. In total, there are at least " + parseInt(total_classes,10).toLocaleString() + " sections.";
}

// return summary text about seat infomation
function get_seat_count_info() {
    return "A seat is a single spot in a class a student can fill, so a student will fill multiple seats. We found that there were " + parseInt(seats_online,10).toLocaleString() + " seats online and " + parseInt(seats_in_person,10).toLocaleString() + " seats in person. Of the ones we could scan, there are " + parseInt(seats_total,10).toLocaleString() + " total seats.";
}

// wait until html elements are ready
$(document).ready(function () {
	
	// create footer text
    $('#footer').text(`2020. Ethan Schaffer, Bill Shi. Last updated ${last_updated}`);
	
	// display pie chart graphics
    $('#chart1').attr("src",getChartUrl(percent_online, percent_in_person));
    $('#chart2').attr("src",getChartUrl(percent_seats_online, percent_seats_in_person));
	
	// display summary texts
    $('#course_count_info').text(get_course_count_info());
	$('#seat_count_info').text(get_seat_count_info());
})