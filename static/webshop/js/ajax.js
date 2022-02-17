$(document).ready(function (){
    searchQuery();
});

$('#searchBar').submit(function (e) {
    searchQuery();
    e.preventDefault();
});

function searchQuery(page_number) {
    query = document.getElementById('searchQuery').value
    orderBy = $("#orderBy :selected").val();
    $.ajax({
        url: "/search",
        type: "GET",
        data: {
            "query": query,
            "order": orderBy,
            "page": page_number,
        },
        success: function (data) {
            $("#searchResults").html(data);
        }
    });
}

