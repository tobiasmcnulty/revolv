$(document).ready(function () {
    $("#schedule_repayment").on('submit', function (e) {
        toastr.options = {
            "positionClass": "toast-bottom-right"
        };
        $.ajax({
            type: "POST",
            data: $('#schedule_repayment').serialize(),
            success: function (data) {
                if (data.success) {
                    $(".response_message").addClass("error");
                    $(".response_message").addClass("success");
                    $(".response_message").show();
                    $("#reset-button").click();
                    toastr.success(data.message)
                } else {
                    $(".response_message").addClass("success");
                    $(".response_message").addClass("error");
                    toastr.error(data.message)
                }
            }
        });
        e.preventDefault();

    });
    $('#repayment_entry').hide();
    $('#button1').hide();
    $("#button, #button1").click(function () {
        $('#repayment_entry, #repayment_table').toggle(600);
        $('#button, #button1').toggle();
    });
    $('#search_button').remove();
    $('#repayment-schedule').hide();
    $('#end_date_toggle').hide();
    $('#end_date').click (function () {
        $('#end_date_toggle').show(500);
        $('#end_date').hide();
    });
    var d = new Date(),
        month = d.getMonth() + 2,
        year = d.getFullYear();
    if (month > 12)
        month = 1;
    if (month < 10)
        min = (year + '-' + '0' + month);
    else
        min = (year + '-' + month);
    $("#start-date").attr({
        "min": min
    });
    $(".project-name").change(function () {
        $('#repayment-schedule').show();
        var repayment_schedule = '#repayment-schedule';
        if ($.fn.dataTable.isDataTable(repayment_schedule)) {
            $(repayment_schedule).DataTable().ajax.reload();
        } else {
            table = $('#repayment-schedule').DataTable({
                // "processing": true,
                // "serverSide": true,
                "dom": 'lfrtip',
                "scrollX": true,
                buttons: [
                    'print',
                    {
                        extend: 'pdfHtml5',
                        orientation: 'landscape',
                        pageSize: 'LEGAL'
                    },
                    {
                        extend: 'excelHtml5',
                        orientation: 'landscape'
                    },
                    {
                        extend: 'csvHtml5',
                        orientation: 'landscape'
                    }

                ],
                // "order": [[ 4, "desc" ]],
                "ajax": {
                    url: '/repayment_config/',
                    "data": function (d) {
                        project_id = $('.project-name')[0].value;
                        d.project_id = project_id;
                    },
                    "dataSrc": "data"
                },
                "columns": [
                    {"data": "year"},
                    {"data": "month"},
                    {"data": "amount"}

                ]
            });
        }
    });
});
