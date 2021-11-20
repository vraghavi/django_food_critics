$(document).ready(function () {
    // submitButtonClicked();
    // showSuccessMes   sage();
});

// function updateProfile() {
//     var queryString = window.location.search;
//     var urlParam = new URLSearchParams(queryString);
//     var profileFormUpdated = document.forms.profileFormUpdated;
//     if (urlParam.has('name')) {
//         profileFormUpdated.children[0].children[0].children[0].setAttribute("value", urlParam.get('name'));
//     }
//     if (urlParam.has('email')) {
//         profileFormUpdated.children[0].children[1].children[0].setAttribute("value", urlParam.get("email"));
//     }
//     if (urlParam.has('number')) {
//         profileFormUpdated.children[0].children[2].children[0].setAttribute("value", urlParam.get("number"));
//     }
//     if (urlParam.has('username')) {
//         profileFormUpdated.children[0].children[3].children[0].setAttribute("value", urlParam.get("username"));
//     }
// }

// function submitButtonClicked(event) {
//     $('editProfile').on('submit', function(event){
//         updateProfile(event)
//     })
// }

function updateProfile(event) {
    var x = document.forms.editProfile
    var updateProfileForm = new FormData(x)
    var emailidRegex = new RegExp('^[a-z0-9]+@vt\.edu$');
    var numberRegex = new RegExp('^[0-9]{10}');
    var passwordRegex = new RegExp('^[a-z0-9_@]{6,15}');
    if (updateProfileForm.has("email") && emailidRegex.test(updateProfileForm.get("email")) &&
        updateProfileForm.has("mobileno") && numberRegex.test(updateProfileForm.get("mobileno").replace(/[\(\)\- ]/g, "")) &&
        updateProfileForm.has("password") && passwordRegex.test(updateProfileForm.get("password"))) {
            const csrftoken = getCookie('csrftoken');
            $.ajax({
                url: '/users/update-profile',
                data: {
                    username : updateProfileForm.get('username'),
                    password : updateProfileForm.get('password'),
                    email: updateProfileForm.get("email"),
                    mobileno: updateProfileForm.get('mobileno')
                },
                type: "POST",
                dataType: "json",
                headers: { 'X-CSRFToken': csrftoken },
                context: this
            }).done(function (json) {
                if (json.success) {
                    location.reload()
                } else {
                    console.log('oops')
                }
            }).fail(function (xhr, status, errorThrown) {
                console.log('fail')
            }).always(function(){
                console.log('always')
            })
        }
    else{
        console.log('nooooooo')
        alert('There are some validation errors! Please check and update')
    }
}