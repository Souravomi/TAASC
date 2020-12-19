function getComboValues(tbName) {
    // $('#column1id')
    $.ajax({
        url: '/search/getModelsFields',
        type: 'GET',
        data: {
            "tbName": tbName,

        },
        dataType: 'json'
    }).done(function(data) {

        $('#column1id').empty()
        var $dropdown = $("#column1id");
        var i = 0
        $.each(data, function() {
            if (data[i] !== "ID" && data[i] !== "Auth_Id")

            {

                $dropdown.append($('<option></option>').val(data[i]).text(data[i]));


            }
            i++
        });

    });
}