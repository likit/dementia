$(document).ready(function() {
    $('#amphur').empty();
    $('#district').empty();

    $('#amphur').show();
    $('#district').show();

    (function set_province() {
        $('#province').empty();
        $('#province').append('<option>Select province</option>')
        for (i in provinces_list) {
            var p = provinces_list[i];
            $('#province').append('<option value=' + p + '>' + p + '</option>')
        };
    })();

    function change_district() {
        var d = amphurs[($('#amphur').val())];
        $('#district').empty();
        for (i in d.sort()) {
            $('#district').append("<option value=" + d[i] + ">" + d[i] + "</option>");
        };
    };

    $('#province').change(function(){
        var a = provinces[$(this).val()];
        $('#amphur').empty();
        $('#district').empty();
        for (i in a.sort()) {
            $('#amphur').append("<option value=" + a[i] + ">" + a[i] + "</option>");
        };
        change_district();
    });

    $('#amphur').change(change_district);

});
