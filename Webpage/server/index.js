window.onload = function () {
    let pestBox = document.getElementById("pest");
    let dateRangeBox = document.getElementById("date");
    const dateRe = /(\d{4})-(\d{2})-(\d{2})/
    pestBox.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            alert("Pest entered is: " + pestBox.value) // Need to grab this value and use it in the Twitter scraper.
        }
    })

    dateRangeBox.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            if (!dateRe.test(dateRangeBox.value)) {
                alert("Not a valid string!")
            } else {
                alert("Date entered is: " + dateRangeBox.value) // Need to grab this value and use it in the Twitter scraper.
            }
        }
    })
}