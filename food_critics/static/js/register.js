$(document).ready(function() {

})

function addUser(event) {
    var registerForm = new FormData(document.forms.register)
    console.log('hello')
    const csrftoken = getCookie('csrftoken');
    $.ajax({
        url: '/blogs/registration',
        data: {
            username: registerForm.username,
            password: registerForm.password,
            mobileno: registerForm.mobileno
        },
        type: "POST",
        dataType: "json",
        headers: { 'X-CSRFToken': csrftoken },
        context: this
    }).done(function (json) {
        if (json.success) {
            console.log(json.username)
        } else {
            console.log('oops')
        }
    }).fail(function (xhr, status, errorThrown) {
        console.log('fail')
    }).always(function(){
        console.log('always')
    })
}
