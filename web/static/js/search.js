$(function(){

    $('#searchLine').keyup(function(){

        var searchText = $(this).val();

        $('ul > li').each(function(){

            var currentLiText = $(this).text(),
                showCurrentLi = currentLiText.indexOf(searchText) !== -1;

            $(this).toggle(showCurrentLi);

        });     
    });

});