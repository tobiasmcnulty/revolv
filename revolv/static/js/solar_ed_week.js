// Global Variables
var map;
var bounds;
var infoWindow;
var oms;

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
            closeHostEventPopup();
            closeBecomePartnerPopup();
            closeBecomeSponsorPopup();
        }
    });

    $(".partner-click-here").on('click', function (e) {
        closeBecomePartnerPopup();
        $(".become-sponsor-pop-up").fadeIn('slow');
    });

    $("#host_event_form").on('submit', function(e) {
        var geocoder = new google.maps.Geocoder();
        var address = $("#address").val() + " " + $("#city").val() + " " + $("#state"). val() + " " + $("#zipcode").val();
        geocoder.geocode( { 'address': address}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                var latitude = results[0].geometry.location.lat();
                var longitude = results[0].geometry.location.lng();
                $("#latitude").val(latitude);
                $("#longitude").val(longitude);

                $.ajax({
                    type: "POST",
                    url: "host-event/",
                    data: $("#host_event_form").serialize(),
                    success: function(data)
                    {
                        if(data.success) {
                            $(".response_message").removeClass("error");
                            $(".response_message").addClass("success");

                            var title = $("#event-title").val();
                            var details = $("#details").val();
                            var date = $("#date").val();
                            var address = $("#address").val();
                            var city = $("#city").val();
                            var state = $("#state").val();
                            var link = $("#link").val();
                            var name = $("#name").val();
                            var email = $("#email").val();
                            addMarker(title, details, latitude, longitude, date, address, city, state, link, name, email);
                            closeHostEventPopup();
                        } else {
                            $(".response_message").removeClass("success");
                            $(".response_message").addClass("error");
                            $(".response_message").text(data.message);
                        }

                    }
                });
            } else {
                alert("Unable to find the address. Please enter valid address");
            }
        });
        e.preventDefault();
    });

    $("#become_partner_form").on('submit', function(e) {
        var form = $("#become_partner_form")[0];
        var formData = new FormData(form);

        $.ajax({
            type: "POST",
            url: "become-partner/",
            data: formData,
            processData: false,
            contentType: false,
            success: function(data)
            {
                if(data.success) {
                    $(".partner_response_message").removeClass("error");
                    $(".partner_response_message").addClass("success");
                    closeBecomePartnerPopup();
                } else {
                    $(".partner_response_message").removeClass("success");
                    $(".partner_response_message").addClass("error");
                    $(".partner_response_message").text(data.message);
                }
            }
        });
        e.preventDefault();
    });

    $("#become_sponsor_form").on('submit', function(e) {
        var form = $("#become_sponsor_form")[0];
        var formData = new FormData(form);

        $.ajax({
            type: "POST",
            url: "become-sponsor/",
            data: formData,
            processData: false,
            contentType: false,
            success: function(data)
            {
                if(data.success) {
                    $(".sponsor_response_message").removeClass("error");
                    $(".sponsor_response_message").addClass("success");
                    closeBecomeSponsorPopup();
                } else {
                    $(".sponsor_response_message").removeClass("success");
                    $(".sponsor_response_message").addClass("error");
                    $(".sponsor_response_message").text(data.message);
                }
            }
        });
        e.preventDefault();
    });

    $("#partnerLogoImage").on("click", function(){
        $("#partnerFileInput").click();
    });

    $("#sponsorLogoImage").on("click", function(){
        $("#sponsorFileInput").click();
    });

    $("#partnerFileInput").on("change", function(){
        readURL(this, "partnerLogoImage");
    });

    $("#sponsorFileInput").on("change", function(){
        readURL(this, "sponsorLogoImage");
    });

});


jQuery(function($) {
    // Asynchronously Load the map API
    var script = document.createElement('script');
    script.src = "//maps.googleapis.com/maps/api/js?key=AIzaSyDeO2HEVcajZ2BcHnJoSfr4XFwUEpXcVkQ&sensor=false&callback=initialize";
    document.body.appendChild(script);
    var markerSpiderfierScript = document.createElement('script');
    markerSpiderfierScript.src = "//cdnjs.cloudflare.com/ajax/libs/OverlappingMarkerSpiderfier/1.0.3/oms.min.js";
    document.body.appendChild(markerSpiderfierScript);
});

function initialize() {
    bounds = new google.maps.LatLngBounds();
    var mapOptions = {
        mapTypeId: 'roadmap',
        center: new google.maps.LatLng(36.778259, -119.417931),
        zoom: 7
    };

    // Display a map on the page
    map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
    map.setTilt(45);

    oms = new OverlappingMarkerSpiderfier(map, {
        markersWontMove: true,
        markersWontHide: true,
        basicFormatEvents: true
      });

    // Display multiple markers on a map
    infoWindow = new google.maps.InfoWindow();
    initializeMarker();
}

function addMarker(title, details, latitude, longitude, date, address, city, state, link, name, email) {
    var position = new google.maps.LatLng(latitude, longitude);
    bounds.extend(position);
    var marker = new google.maps.Marker({
        position: position,
        map: map,
        title: title,
    });

    // Allow each marker to have an info window
    google.maps.event.addListener(marker, 'spider_click', (function(marker) {
        return function() {
            var detail = "<div>";
            detail += "<div><h4>" + title + "</h4></div>";
            detail += "<div><span><i>Date: </i></span><b>" + date + "</b></div>";
            detail += "<div><span><i>Address: </i></span><b>" + address + "</b></div>";
//            detail += "<div><span><i>City: </i></span><b>" + city + "</b></div>";
//            detail += "<div><span><i>State: </i></span><b>" + state + "</b></div>";
            detail += "<div><span><i>Details: </i></span><b>" + details + "</b></div>";
            detail += "<div><span><i>Link: </i></span><b><a href='" + link + "'>" + link + "</a></b></div>";
            detail += "<div><span><i>Name: </i></span><b>" + name + "</b></div>";
            detail += "<div><span><i>Email: </i></span><b>" + email + "</b></div>";
            detail += "</div>";
            infoWindow.setContent(detail);
            infoWindow.open(map, marker);
        }
    })(marker));

    oms.addMarker(marker);

    // Automatically center the map fitting all markers on the screen
    map.fitBounds(bounds);
}

function readURL(input, id) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#'+id).attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }
}

function closeHostEventPopup() {
    $('.become-host-pop-up').fadeOut();
    $("#host_event_form")[0].reset();
    $(".response_message").text("");
}

function closeBecomePartnerPopup() {
    $('.become-partner-pop-up').fadeOut();
    $("#become_partner_form")[0].reset();
    $(".partner_response_message").text("");
    $("#partnerFileInput").val('');
    $('#partnerLogoImage').attr('src', '/static/images/upload_image@1x.png');
}

function closeBecomeSponsorPopup() {
    $(".become-sponsor-pop-up").fadeOut();
    $("#become_sponsor_form")[0].reset();
    $(".sponsor_response_message").text("");
    $("#sponsorFileInput").val('');
    $('#sponsorLogoImage').attr('src', '/static/images/upload_image@1x.png');
}