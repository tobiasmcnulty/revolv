$(window).load(function(){
    $('#user_record_loader').fadeOut();
});
$(document).ready(function() {
    table=$('#donation_report').DataTable({
       "dom": 'lfrtBip',
        "scrollX": true,
        buttons: [,
            'excelHtml5',
            'csvHtml5'
        ],
        "columnDefs": [
        {"className": "dt-center", "targets": "_all"}
        ],
        "aaSorting": []
    });
});