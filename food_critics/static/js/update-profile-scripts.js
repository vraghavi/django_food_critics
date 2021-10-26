$(document).ready(function () {
    updateProfile();
    showSuccessMessage();
});

function updateProfile() {
    var queryString = window.location.search;
    var urlParam = new URLSearchParams(queryString);
    var profileFormUpdated = document.forms.profileFormUpdated;
    if (urlParam.has('name')) {
        profileFormUpdated.children[0].children[0].children[0].setAttribute("value", urlParam.get('name'));
    }
    if (urlParam.has('email')) {
        profileFormUpdated.children[0].children[1].children[0].setAttribute("value", urlParam.get("email"));
    }
    if (urlParam.has('number')) {
        profileFormUpdated.children[0].children[2].children[0].setAttribute("value", urlParam.get("number"));
    }
    if (urlParam.has('username')) {
        profileFormUpdated.children[0].children[3].children[0].setAttribute("value", urlParam.get("username"));
    }
}

function showSuccessMessage() {
    var successMessage = document.createElement("div");
    successMessage.innerHTML = "<p><i class='fa fa-check' aria-hidden='true'></i> Profile Updated Successfully!</p>";
    document.getElementById("edit").style = "float:none; text-align: center;margin-left:40%";
    successMessage.children[0].style = "border: 1px solid green; color: green;width:fit-content;padding:5px;"
    document.getElementById("edit").append(successMessage);

}