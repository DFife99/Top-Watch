function ProductHover() {
    $(this).removeClass( "ml-5 mr-5 mt-5 mb-5" ).addClass( "ml-2 mr-2 mt-2 mb-2 pl-3 pr-3 pt-3 pb-3 product-hover" );
}

function ProductUnhover() {
    $(this).removeClass( "ml-2 mr-2 mt-2 mb-2 pl-3 pr-3 pt-3 pb-3 product-hover" ).addClass( "ml-5 mr-5 mt-5 mb-5" );
}