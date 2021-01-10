// MAKING THE PRODUCT DISPLAY BOX BIGGER UPON HOVER

$(document).ready(function() {
    $(".product-display-box").hover( function() {
        $(this).removeClass("col-lg-3 product-margin").addClass("col-lg-4 product-margin-hover");
    }, function () {
        $(this).removeClass("col-lg-4 product-margin-hover").addClass("col-lg-3 product-margin");
    });
    $('#brand-filter-icon').click(function() {
        $('#brand-filters').toggle();
    });
    $('#brand-sort-icon').click(function() {
        $('#brand-sort').toggle();
    });
});
