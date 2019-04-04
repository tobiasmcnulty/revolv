// Global Variables
var map;
var bounds;
var infoWindow;
var oms;

var usStates = [
    { name: 'ALABAMA', abbreviation: 'AL'},
    { name: 'ALASKA', abbreviation: 'AK'},
    { name: 'ARIZONA', abbreviation: 'AZ'},
    { name: 'ARKANSAS', abbreviation: 'AR'},
    { name: 'CALIFORNIA', abbreviation: 'CA'},
    { name: 'COLORADO', abbreviation: 'CO'},
    { name: 'CONNECTICUT', abbreviation: 'CT'},
    { name: 'DELAWARE', abbreviation: 'DE'},
    { name: 'DISTRICT OF COLUMBIA', abbreviation: 'DC'},
    { name: 'FLORIDA', abbreviation: 'FL'},
    { name: 'GEORGIA', abbreviation: 'GA'},
    { name: 'HAWAII', abbreviation: 'HI'},
    { name: 'IDAHO', abbreviation: 'ID'},
    { name: 'ILLINOIS', abbreviation: 'IL'},
    { name: 'INDIANA', abbreviation: 'IN'},
    { name: 'IOWA', abbreviation: 'IA'},
    { name: 'KANSAS', abbreviation: 'KS'},
    { name: 'KENTUCKY', abbreviation: 'KY'},
    { name: 'LOUISIANA', abbreviation: 'LA'},
    { name: 'MAINE', abbreviation: 'ME'},
    { name: 'MARYLAND', abbreviation: 'MD'},
    { name: 'MASSACHUSETTS', abbreviation: 'MA'},
    { name: 'MICHIGAN', abbreviation: 'MI'},
    { name: 'MINNESOTA', abbreviation: 'MN'},
    { name: 'MISSISSIPPI', abbreviation: 'MS'},
    { name: 'MISSOURI', abbreviation: 'MO'},
    { name: 'MONTANA', abbreviation: 'MT'},
    { name: 'NEBRASKA', abbreviation: 'NE'},
    { name: 'NEVADA', abbreviation: 'NV'},
    { name: 'NEW HAMPSHIRE', abbreviation: 'NH'},
    { name: 'NEW JERSEY', abbreviation: 'NJ'},
    { name: 'NEW MEXICO', abbreviation: 'NM'},
    { name: 'NEW YORK', abbreviation: 'NY'},
    { name: 'NORTH CAROLINA', abbreviation: 'NC'},
    { name: 'NORTH DAKOTA', abbreviation: 'ND'},
    { name: 'OHIO', abbreviation: 'OH'},
    { name: 'OKLAHOMA', abbreviation: 'OK'},
    { name: 'OREGON', abbreviation: 'OR'},
    { name: 'PENNSYLVANIA', abbreviation: 'PA'},
    { name: 'PUERTO RICO', abbreviation: 'PR'},
    { name: 'RHODE ISLAND', abbreviation: 'RI'},
    { name: 'SOUTH CAROLINA', abbreviation: 'SC'},
    { name: 'SOUTH DAKOTA', abbreviation: 'SD'},
    { name: 'TENNESSEE', abbreviation: 'TN'},
    { name: 'TEXAS', abbreviation: 'TX'},
    { name: 'UTAH', abbreviation: 'UT'},
    { name: 'VERMONT', abbreviation: 'VT'},
    { name: 'VIRGINIA', abbreviation: 'VA'},
    { name: 'WASHINGTON', abbreviation: 'WA'},
    { name: 'WEST VIRGINIA', abbreviation: 'WV'},
    { name: 'WISCONSIN', abbreviation: 'WI'},
    { name: 'WYOMING', abbreviation: 'WY' }
];

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

    $('.close-icon').on('click',function() {
        $(this).closest('.become-host-pop-up').fadeOut();
    })

    $('.close-icon').on('click',function() {
        $(this).closest('.become-partner-pop-up').fadeOut();
    })

    $('.close-icon').on('click',function() {
        $(this).closest('.become-sponsor-pop-up').fadeOut();
    })

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
                            location.reload()
                        } else {
                            $(".response_message").removeClass("success");
                            $(".response_message").addClass("error");
                            $(".response_message").text(data.message);
                        }
                        
                    }
                });
            } else {
                alert("Unable to find the address. Please enter valid address");
                var btn = document.getElementById('host-submit');
                btn.disabled = false;
                btn.innerText = 'HOST AN EVENT '
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
    
    $(document).ready( function() {
        $(usStates).each( function(index, item) {
            var option = $('<option value="'+item.abbreviation+'">'+item.name+'</option>');
            $('#states').append(option);
        });
    });

});

jQuery(function($) {
    // Asynchronously Load the map API
    var script = document.createElement('script');
    script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyDeO2HEVcajZ2BcHnJoSfr4XFwUEpXcVkQ&sensor=false&callback=initialize";
    document.body.appendChild(script);
});

function disableButton() {
    var btn = document.getElementById('host-submit');
    btn.disabled = true;
    btn.innerText = 'Posting...'
}

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

function addMarker(title, details, latitude, longitude, date, address, city, state, link, name, email, evntime) {
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
            if ( evntime == 'None') {
                detail += "<div><span><i>Date: </i></span><b>" + date + "</b></div>";
            }
            else{
                detail += "<div><span><i>Date: </i></span><b>" + date + " , " +  evntime + "</b></div>";
            }
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