$(document).ready(function () {
    $("#manual_payment_form").on('submit', function(e) {
        $.ajax({
            type: "POST",
            data: $('#manual_payment_form').serialize(),
            success: function(data)
            {
                if(data.success) {
                    $(".response_message").addClass("error");
                    $(".response_message").addClass("success");
                    $(".response_message").text(data.message);
                    $(':input[type="submit"]').prop('disabled', true);
                } else {
                    $(".response_message").addClass("success");
                    $(".response_message").addClass("error");
                    $(".response_message").text(data.message);
                }
            }
        });
        e.preventDefault();

    });
});