$(document).ready(function () {
    //event for search task
    checkQueryString();
});

function checkQueryString() {
    var queryString = window.location.search;
    var urlParam = new URLSearchParams(queryString);
    if (urlParam.has('search-keyword')) {
        var searchKeyword = urlParam.get("search-keyword").toLowerCase();

        switch (searchKeyword) {
            default:
                document.getElementById("no-results").hidden = false;
                document.getElementById("gillie").hidden = true;
                document.getElementById("plaka").hidden = true;
                document.getElementById("chauncey").hidden = true;
                document.getElementById("tacos").hidden = true;
                break;
            case "blacksburg":
                document.getElementById("no-results").hidden = true;
                document.getElementById("gillie").hidden = false;
                document.getElementById("plaka").hidden = true;
                document.getElementById("chauncey").hidden = true;
                document.getElementById("tacos").hidden = true;
                break;
            case "ncr":
                document.getElementById("no-results").hidden = true;
                document.getElementById("gillie").hidden = true;
                document.getElementById("plaka").hidden = false;
                document.getElementById("chauncey").hidden = false;
                document.getElementById("tacos").hidden = true;
                break;
            case "mexican":
                document.getElementById("no-results").hidden = true;
                document.getElementById("gillie").hidden = true;
                document.getElementById("plaka").hidden = true;
                document.getElementById("chauncey").hidden = true;
                document.getElementById("tacos").hidden = false;
                break;
            case "family":
                document.getElementById("no-results").hidden = true;
                document.getElementById("gillie").hidden = true;
                document.getElementById("plaka").hidden = true;
                document.getElementById("chauncey").hidden = false;
                document.getElementById("tacos").hidden = true;
                break;
            case "food":
                document.getElementById("no-results").hidden = true;
                document.getElementById("gillie").hidden = false;
                document.getElementById("plaka").hidden = false;
                document.getElementById("chauncey").hidden = false;
                document.getElementById("tacos").hidden = false;
        }
    }
}