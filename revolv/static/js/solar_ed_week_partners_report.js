$(document).ready(function () {
    let donation_report = $('#donation_report');
    let table = donation_report.DataTable({
        "processing": true,
        "serverSide": true,
        "dom": 'lfrtBip',
        "scrollX": true,
        "aLengthMenu": [[10, 25, 50, 100, 150, -1], [10, 25, 50, 100, 150, "All"]],
        "ordering": true,
        buttons: [
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

        ],
        "ajax": {
            url: '/partner_data_table/',
            "data": function (d) {
                $('.dataTables_length select').on('change', function () {
                    $(".container, footer, header").css("display", "none");
                    $(".donationTableLoader").css("display", "block");
                });
                d.search_value = $('input[type=search]').val();
            },
            "dataSrc": function (data) {
                $(".container, footer, header").css("display", "block");
                $(".donationTableLoader").css("display", "none");
                return data["all-data"];
            },
        },
        "columns": [
            {"data": "name"},
            {"data": "email"},
            {"data": "organization"},
            {"data": "promoting_way"},
        ],
    });
    $("input[type=search]").keyup(function (e) {
        let search_input = e.target.value.trim();
        if (search_input === 0) {
            e.target.value = search_input;
        }
    });
});