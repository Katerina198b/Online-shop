    $(function () {

    function load_comments () {
        var url =  $("#comments").data('update-from');
        $("#comments").load(url);
    }
    window.setInterval(load_comments, 1000);

    $('.chosen-select').chosen();


});
