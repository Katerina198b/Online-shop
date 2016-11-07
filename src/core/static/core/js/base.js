    $(function () {

    function load_comments () {
        var url =  $("#comments").data('update-from');
        $("#comments").load(url);
    }
    window.setInterval(load_comments, 10000);


    $(document).on('click', '[data-click-action]', function() {
        var url = $(this).data('click-action');
        var element = $(this).find('.like_count');
        $.getJSON(url, {}, function(data) {
            element.text(data.like);
            element.text(data.dislike);
            console.log(data);
        })
        return false;
    });

    $('.chosen-select').chosen();
    

});
