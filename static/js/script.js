// Cal buttons

var pathname = window.location.pathname;
var urlArray = pathname.split("/");
var month = parseInt(urlArray[3])
var year = parseInt(urlArray[2])

$('#back-btn').click(function () {
    month -= 1
    if (month < 1) {
        month = 12
        year -=1
    }
    window.location.href = "/calendar/" + year + '/' + month;
})

$('#fwd-btn').click(function () {
    month += 1
    if (month > 12) {
        month = 1
        year += 1
    }
    window.location.href = "/calendar/" + year + '/' + month;
})


// Cal link

let date = new Date()
let thisyear = date.getFullYear()
let thismonth = date.getMonth() + 1
let calurl = '/calendar/' + thisyear + '/' + thismonth + '/'
$('#cal-link').attr('href', calurl)
