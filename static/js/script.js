// MAKING THE PRODUCT DISPLAY BOX BIGGER UPON HOVER

$(document).ready(function() {
    $(".product-display-box").hover( function() {
        $(this).removeClass("col-md-5 col-lg-3 product-margin").addClass("col-md-6 col-lg-4 product-margin-hover");
    }, function () {
        $(this).removeClass("col-md-6 col-lg-4 product-margin-hover").addClass("col-md-5 col-lg-3 product-margin");
    });
    $('#brand-filter-icon').click(function() {
        $('#brand-filters').toggle();
    });
    $('#brand-sort-icon').click(function() {
        $('#brand-sort').toggle();
    });
});
