$(document).ready(function () {
    let donation_report = $('#donation_report'), date1, date2, search_value, report_length;
    let table = donation_report.DataTable({
        "processing": true,
        "serverSide": true,
        "aLengthMenu": [[10, 25, 50, -4, -3, -2], [10, 25, 50, "Active Donors", "Active Donors and Manual Reinvestors", "All Donors"]],
        "dom": 'lfrtBip',
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
                orientation: 'landscape',
            },
            {
                extend: 'csvHtml5',
                orientation: 'landscape',
            },
            {
                text: 'Export Filtered Category Report CSV',
                className: 'export-button',
                action: function ( e, dt, node, config ) {
                    report_length = $("select[name=donation_report_length]").val();
                    location.replace('/export_csv?from_date=' + date1 + '&to_date=' + date2 + '&search_value=' + search_value + '&report_length=' + report_length);
                }
            },

        ],
        "order": [[4, "desc"]],
        "ajax": {
            url: '/payment_ajax_url/',
            "data": function (d) {
                $('.dataTables_length select').on('change', function () {
                    $(".container, footer, header").css("display", "none");
                    $(".donationTableLoader").css("display", "block");
                });
                date1 = $('#datepicker-1').val();
                date2 = $('#datepicker-2').val();

                d.datepicker1 = date1;
                d.datepicker2 = date2;
                d.reportLength = $("select[name=donation_report_length]").val();
                d.search_value = search_value = $('input[type=search]').val();

            },
            "dataSrc": function (data) {
                $(".container, footer, header").css("display", "block");
                $(".donationTableLoader").css("display", "none");
                return data["data"];
            },

        },
        "columns": [
            {"data": "first_name"},
            {"data": "last_name"},
            {"data": "username"},
            {"data": "email"},
            {"data": "date"},
            {"data": "project"},
            {"data": "amount"},
            {"data": "user_reinvestment"},
            {"data": "admin_reinvestment"},
            {"data": "tip"},
            {"data": "total"}
        ],
        "columnDefs": [
            {
                "targets": 8,
                "orderable": false
            },
            {
                "targets": 10,
                "orderable": false
            },
        ]

    });
    if ($("select[name=donation_report_length]").val() > 0) {
        $('.export-button').css("display", "none");
    }
    $("select[name=donation_report_length]").change(function (e) {
        if (e.target.value < 0) {
            $('.export-button').css("display", "inline-block");
        }
        else {
            $('.export-button').css("display", "none");
        }
        let targetValue = e.target.value;
        donation_report.DataTable().page.len(targetValue);
        if (parseInt(targetValue) < 0) {
            $('#donation_report').DataTable().page.len(10);
            $("select[name=donation_report_length]").val(targetValue);
        }
    });
    $(function () {
        $("#datepicker-1").datepicker({
            dateFormat: 'yy-mm-dd',
            onSelect: function () {
            }
        }).keyup(function (e) {
            if (e.keyCode === 8 || e.keyCode === 46) {

                if (!$(this).value) {
                    $.datepicker._clearDate(this);
                    table.draw();
                }


            }
        });
        $("#datepicker-2").datepicker({
            dateFormat: 'yy-mm-dd',
            onSelect: function () {
            }
        }).keyup(function (e) {
            if (e.keyCode === 8 || e.keyCode === 46) {

                if (!$(this).value) {
                    $.datepicker._clearDate(this);
                }
            }
        });
    });

    $("#search_button").click(function () {
        let fromDate = new Date($("#datepicker-1").val());
        let toDate = new Date($("#datepicker-2").val());
        if (fromDate.toString() !== 'Invalid Date' && toDate.toString() !== 'Invalid Date') {

            if (fromDate.getTime() > toDate.getTime()) {
                alert("The From date is greater then To date!");
            } else {
                table.draw();
            }

        }
        else {
            alert("Invalid Date Range");
        }
    });
    // $('#export-button').on('click', function () {
    //     report_length = $("select[name=donation_report_length]").val();
    //     location.replace('/export_csv?from_date=' + date1 + '&to_date=' + date2 + '&search_value=' + search_value + '&report_length=' + report_length);
    // });
    $('#export-excel-btn').on('click', function () {
        location.replace('/export_excel?from_date=' + date1 + '&to_date=' + date2 + '&search_value=' + search_value);
    });
    $("input[type=search]").keyup(function (e) {
        let search_input = e.target.value.trim();
        if (search_input === 0) {
            e.target.value = search_input;
        }
    });
});