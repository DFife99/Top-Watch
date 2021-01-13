// MAKING THE PRODUCT DISPLAY BOX BIGGER UPON HOVER

$(document).ready(function() {
    $('#brand-filter-icon').click(function() {
        $('#brand-filters').toggle();
    });
    $('#brand-sort-icon').click(function() {
        $('#brand-sort').toggle();
    });
});

$(document).ready(function() {
    $(".product-display-box").hover(function() {
        $(this).removeClass("col-md-5 col-lg-3 product-margin").addClass("col-md-6 col-lg-4 product-margin-hover");
    }, function () {
        $(this).removeClass("col-md-6 col-lg-4 product-margin-hover").addClass("col-md-5 col-lg-3 product-margin");
    });
});

$(document).ready(function() {
    $('#sort-selector').change(function() {
    var selector = $(this);
    var currentUrl = new URL(window.location);

    var selectedValue = selector.val();
    if(selectedValue != 'reset'){
        var sort = selectedValue.split('_')[0];
        var direction = selectedValue.split('_')[1];

        currentUrl.searchParams.set('sort', sort);
        currentUrl.searchParams.set('direction', direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete('sort');
        currentUrl.searchParams.delete('direction');

        window.location.replace(currentUrl)
    }
})
})