$(document).ready(function () {
     table = $('#donation_report').DataTable({
        "lengthMenu": [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]],
        "processing": true,
        "serverSide": true,
        "dom": 'lBfrtip',
        "scrollX": true,
        "bSort": true,
        "ajax": {
            url: '/monthly_repayment_table/',

            "dataSrc": "data"

        },
        "columns": [
            {"data": "year"},
            {"data": "month"},
            {"data": "project_name"},
            {"data": "repayment_amount"}

        ],
        "columnDefs": [
        {
            "targets": [1, 2, 3],
            "orderable": false
        }
        ],
        buttons: [
            {
                extend: 'excelHtml5',
                orientation: 'landscape'
            },
            {
                extend: 'csvHtml5',
                orientation: 'landscape'
            }

        ]

    });

});