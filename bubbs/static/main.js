$(function() {
    $('#generate-btn').click(function() {
        var requested = $('#requested').val();
        $.get('/bubbs/bid/generate/' + requested + '/', function(data) {
            $('#generated').val(JSON.parse(data).join('\n'));
        });
    });
    $('#requested').InputSpinner();
});