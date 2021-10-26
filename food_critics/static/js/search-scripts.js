$(document).ready(function () {
    //update values for edit form
    updateValues();
    // event delegation for edit icon click
    $("#edit").on("click", function (event) {
        event.preventDefault();
        document.getElementById("buttons").removeAttribute("hidden");
        document.getElementById("details").firstElementChild.firstElementChild.focus();
        // console.log(event);
        // make the inputs editable 
        Array.from(document.getElementById("details").children).forEach(function (element) {
            if (element.hasChildNodes()) {
                if (element.firstElementChild.hasAttribute("type") && element.firstElementChild.getAttribute("type") != "number")
                    element.firstElementChild.removeAttribute("readonly");
            }
        });
    });

    $("#validateButton").on("click", function (event) {
        event.preventDefault();
        validateForm();
    });
});

function validateForm() {
    var editProfileForm = document.forms.editProfileForm;
    var editFormData = new FormData(editProfileForm);
    var alphabetsRegex = new RegExp('^[A-Za-z ]+$', 'i');
    var emailidRegex = new RegExp('^[a-z0-9]+@vt\.edu$');
    var numberRegex = new RegExp('^[0-9]{10}');
    var usernameRegex = new RegExp('^[a-z0-9_@]+$');

    if (editFormData.has("name") && alphabetsRegex.test(editFormData.get("name")) &&
        editFormData.has("email") && emailidRegex.test(editFormData.get("email")) &&
        editFormData.has("number") && numberRegex.test(editFormData.get("number").replace(/[\(\)\- ]/g, "")) &&
        editFormData.has("username") && usernameRegex.test(editFormData.get("username"))) {
        document.getElementById("submit").removeAttribute("disabled");
        editProfileForm.children[0].children[0].children[0].setAttribute("value", editFormData.get("name"));
        editProfileForm.children[0].children[1].children[0].setAttribute("value", editFormData.get("email"));
        editProfileForm.children[0].children[2].children[0].setAttribute("value", editFormData.get("number"));
        editProfileForm.children[0].children[3].children[0].setAttribute("value", editFormData.get("username"));

    }
}

function updateValues() {
    var editProfileForm = document.forms.editProfileForm;
    editProfileForm.children[0].children[0].children[0].setAttribute("value", "Raghavi Vannala");
    editProfileForm.children[0].children[1].children[0].setAttribute("value", "vraghavi@vt.edu");
    editProfileForm.children[0].children[2].children[0].setAttribute("value", "(897) 766-4522");
    editProfileForm.children[0].children[3].children[0].setAttribute("value", "boringfoodie");
}