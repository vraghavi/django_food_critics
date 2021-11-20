$(document).ready(function () {
    //update values for edit form
    // updateValues();
    editPoints();
    editPointsSave();
    // event delegation for edit icon click
    $("#edit").on("click", function (event) {
        event.preventDefault();
        document.getElementById("undo").removeAttribute("hidden");
        document.getElementById('edit').setAttribute('hidden',"true")
        document.getElementById("buttons").removeAttribute("hidden");
        document.getElementById("details").firstElementChild.firstElementChild.focus();
        // console.log(event);
        // make the inputs editable 
        document.getElementById("profile-password").removeAttribute("readonly")
        document.getElementById("profile-email").removeAttribute("readonly")
        document.getElementById("profile-mobileno").removeAttribute("readonly")
    });

    $("#undo").on("click",function (event) {
        event.preventDefault();
    })
});


function editPoints() {
    $('div.blog-post button.edit-points').click(function () {
        this.setAttribute('hidden', 'true')
        this.parentElement.firstElementChild.setAttribute('hidden', 'true')
        this.parentElement.children[1].removeAttribute('hidden')
        this.parentElement.children[3].removeAttribute('hidden')
        this.parentElement.children[1].removeAttribute('readonly')
    })
}

function editPointsSave() {
    $('div.blog-post button.edit-points-save').click(function () {
        // Using the core $.ajax() method
        var blogid = $(this).attr('data-blog-id');
        var points = this.previousElementSibling.previousElementSibling.value
        var ajax_url = $(this).attr('data-ajax-url');
        const csrftoken = getCookie('csrftoken');
        // document.pa
        console.log(ajax_url)

        $.ajax({
            url: ajax_url, // The URL for the request
            data: {   // The data to send (will be converted to a query string)
                blog_id: blogid,
                points: points
            },
            type: "POST",   // Whether this is a POST or GET request
            dataType: "json",   // The type of data we expect back
            headers: { 'X-CSRFToken': csrftoken },   //csrf token in headers
            context: this
        }).done(function (json) {   // Code to run if the request succeeds (is done);
            if (json.success) {   // The response is passed to the function
                this.setAttribute('hidden', 'true')
                this.previousElementSibling.removeAttribute('hidden')
                this.previousElementSibling.previousElementSibling.setAttribute('hidden', 'true')
                this.parentElement.firstElementChild.innerText = json.points
                this.parentElement.firstElementChild.removeAttribute('hidden')
                var message = $('<p style="font-size:small;color:green">Updated points for the "'+json.title+'"</p>')
                $('#section-heading').append(message)
                $(message).appendTo($('#section-heading')).fadeOut(1600,function(){
                    this.remove()
                })
            } else {
                var message = $('<p style="font-size:small;color:red">'+json.error+'</p>')
                $('#section-heading').append(message)
                $(message).appendTo($('#section-heading')).fadeOut(1600,function(){
                    this.remove()
                })
            }
        }).fail(function (xhr, status, errorThrown) {   // Code to run if the request fails; the raw request and
            alert("Sorry, there was a problem!");       // status codes are passed to the function
            console.log("Error: " + errorThrown);
        }).always(function (xhr, status) {  // Code to run regardless of success or failure;
            // alert("The request is complete!");
        });
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function getProfile(event) {
    username = event.srcElement.innerText
    const csrftoken = getCookie('csrftoken');
    $.ajax({
        url: '/users/user-profile',
        data: {
            username: username
        },
        type: "POST",
        dataType: "json",
        headers: { 'X-CSRFToken': csrftoken },
        context: this
    }).done(function (json) {
        if (json.success) {
            event.srcElement.setAttribute('title', 'Points:' + json.points)
        } else {
            event.srcElement.setAttribute('title', 'Try after sometime. It seems to be some issue.')
        }
    }).fail(function (xhr, status, errorThrown) {
        event.srcElement.setAttribute('title', 'Try after sometime. It seems to be some issue.')
    }).always(function(){

    })
}
