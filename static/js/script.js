// MAKING THE PRODUCT DISPLAY BOX BIGGER UPON HOVER

$( document ).ready(function() {
    $(".product-display-box").hover( function() {
        $(this).removeClass("col-3 ml-5 mr-4 mt-5 mb-5").addClass("col-4 ml-0 mr-0 mt-1 mb-1");
    }, function () {
        $(this).removeClass("col-4 ml-0 mr-0 mt-1 mb-1").addClass("col-3 ml-5 mr-4 mt-5 mb-5");
    });
});