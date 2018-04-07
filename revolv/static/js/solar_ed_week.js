$(document).ready(function () {
    $('a[href^="#"]').on('click', function (e) {
        $('a').each(function () {
            $(this).removeClass('active');
        })
        $(this).addClass('active');
    });

    $(".host-event").on('click', function(){
        $('.become-host-pop-up').fadeIn('slow');
    });

    $(".become-partner").on('click', function(){
        $('.become-partner-pop-up').fadeIn('slow');
    });

    $(document).keydown(function(e) {
        if (e.keyCode == 27) {
            $('.become-host-pop-up').fadeOut();
            $('.become-partner-pop-up').fadeOut();
            $(".become-sponsor-pop-up").fadeOut();
            $("#host_event_form")[0].reset();
        }
    });

    $(".partner-click-here").on('click', function (e) {
        $('.become-partner-pop-up').fadeOut();
        $(".become-sponsor-pop-up").fadeIn('slow');
    });

    var addressPicker = new AddressPicker({
        map: {
            center: new google.maps.LatLng(36.778259, -119.417931),
            id: '#map',
            displayMarker: true,
            zoom: 3
        },
        zoomForLocation: 18,
        draggable: false,
        reverseGeocoding: true,
        utocompleteService: {
            componentRestrictions: {
                country: 'US'
            }
        }
    });
       // instantiate the typeahead UI
    $('#id_address').typeahead(null, {
        displayKey: 'description',
        source: addressPicker.ttAdapter()
    });
    // add click listeners
    addressPicker.bindDefaultTypeaheadEvent($('#id_address'));
    $(addressPicker).on('addresspicker:selected', function (event, result) {
        $("#latitude").val(result.lat());
        $("#longitude").val(result.lng());
    });


    $("#host_event_form").on('submit', function(e) {
        $.ajax({
            type: "POST",
            url: "host-event/",
            data: $("#host_event_form").serialize(),
            success: function(data)
            {
                if(data.success) {
                    $(".response_message").removeClass("error");
                    $(".response_message").addClass("success");
                } else {
                    $(".response_message").removeClass("success");
                    $(".response_message").addClass("error");
                }
                $(".response_message").text(data.message);
            }
        });
        e.preventDefault();
    });

});

function chooseSponsorFile() {
    $("#sponsorFileInput").click();
    var new_image = $("#sponsorFileInput").val();
    $("#sponsorImage").attr("src", new_image);
}

function choosePartnerFile() {
    $("#fileInput").click();
    var new_image = $("#fileInput").val();
    $("#image").attr("src", new_image);
}