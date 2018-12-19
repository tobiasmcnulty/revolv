$(document).ready(function () {
    var table = $('#donation_report').DataTable({
        "aLengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
        "processing": true,
        "serverSide": true,
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

        ],
        "order": [[4, "desc"]],
        "ajax": {
            url: '/ambassador_data_table/',
            "data": function (d) {
                date1 = $('#datepicker-1').val();
                date2 = $('#datepicker-2').val();

                d.datepicker1 = date1;
                d.datepicker2 = date2;
            },
            "dataSrc": "all-data",

        },
        "columns": [
            {"data": "firstname"},
            {"data": "lastname"},
            {"data": "username"},
            {"data": "email"},
            {"data": "date"},
            {"data": "project"},
            {"data": "amount"},
            {"data": "user_reinvestment"},
            {"data": "tip"},
            {"data": "total"},
        ],

    });

    var allDataTable = $('#all_donation_report').DataTable({
        "aLengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
        "processing": true,
        "serverSide": true,
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

        ],
        "ajax": {
            url: '/ambassador_data_table_auto_reinvestors/',
            "data": function (d) {
                date3 = $('#datepicker-3').val();
                date4 = $('#datepicker-4').val();

                d.datepicker1 = date3;
                d.datepicker2 = date4;
            },
            "dataSrc": "auto-reinvestors-data",
        },
        "order": [[6, "asc"]],
        "aaSorting": [[6, "desc"]],
        "columns": [
            {"data": "firstname"},
            {"data": "lastname"},
            {"data": "username"},
            {"data": "email"},
            {"data": "date"},
            {"data": "project"},
            {"data": "admin_reinvestment"},
        ],

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
        $("#datepicker-3").datepicker({
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
        $("#datepicker-4").datepicker({
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
        var fromDate = new Date($("#datepicker-1").val());
        var toDate = new Date($("#datepicker-2").val());
        if (fromDate !== 'Invalid Date' && toDate !== 'Invalid Date') {

            if (fromDate.getTime() > toDate.getTime()) {
                window.alert("The From date is greater the To date!");
            } else {
                table.draw();
            }

        }
        else {
            window.alert('Invalid date');
        }
    });

    $("#search_button2").click(function () {
        var fromDate = new Date($("#datepicker-3").val());
        var toDate = new Date($("#datepicker-4").val());
        if (fromDate !== 'Invalid Date' && toDate !== 'Invalid Date') {

            if (fromDate.getTime() > toDate.getTime()) {
                window.alert("The From date is greater the To date!");
            } else {
                allDataTable.draw();
            }

        }
        else {
            window.alert('Invalid date');
        }
    });

    $('.switch-view-ambassador-financial-rp').on('click', function () {
        $('.container.after-header').toggleClass("hidden");
        table.columns.adjust().draw();
        allDataTable.columns.adjust().draw();
    });
});