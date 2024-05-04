// New Version resolves the issue that `ID takes and activates the first button only`.
document.addEventListener("DOMContentLoaded", function() {
    var seeDetailsButtons = document.querySelectorAll('.seeDetails');
    var userDetailsPopups = document.querySelectorAll('.userDetails');

    seeDetailsButtons.forEach((btn, index) => {
        btn.addEventListener("click", function () {
            userDetailsPopups[index].classList.add("show");
        });
    });

    var hideDetailsButtons = document.querySelectorAll('.hideDetails');

    hideDetailsButtons.forEach((btn, index) => {
        btn.addEventListener("click", function () {
            userDetailsPopups[index].classList.remove("show");
        });
    });

    window.addEventListener("click", function (event) {
        userDetailsPopups.forEach((popup) => {
            if (event.target === popup) {
                popup.classList.remove("show");
            }
        });
    });
});