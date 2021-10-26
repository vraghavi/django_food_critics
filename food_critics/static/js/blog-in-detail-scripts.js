$(document).ready(function(){
    $("#comment").on("click", function (event) {
        comment();
    });
});

function editComment(event,description){

    lielement = event.target.parentNode.parentNode;
    console.log(description)
    lielement.innerHTML = '<form method="post" action="/blogs/editcomment">{% csrf_token %}<textarea name="edited_comment">'+description+'</textarea><input hidden="true" name="blog_id" type="number" value="'+blog_id+'"><input type="submit"></form>';
}

function showForm(event,blogid){
    document.getElementById('edit-form').removeAttribute('hidden')
    document.getElementById('edit-button').setAttribute('hidden',true)
    document.getElementById('edit-button').parentElement.firstElementChild.setAttribute('hidden',true)
}

function comment(){
    var count = 1;
    var newComment = document.createElement('li');
    var blog_id = document.getElementById("blog_id").innerText;
    newComment.innerHTML='<form method="get" action="/blogs/newcomment"><input type="text" name="newComment"><input hidden="true" name="blog_id" type="number" value="'+blog_id+'"><input type="submit"></form>';
    // newComment.setAttribute("contentEditable",true);
    document.getElementById("comments").appendChild(newComment);
    // newComment.onblur(()=>{
    //     Array.from(document.getElementById("comments").children).forEach((element)=>{
    //         element.setAttribute("contentEditable",false);
    //     });
    // })
}