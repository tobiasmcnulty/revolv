$(document).ready(function() {
    table=$('#matching_donor').DataTable({
       "dom": 'lfrtBip',
        "scrollX": true,
        buttons: [],
        "columnDefs": [ {
        "orderable": false
        } ]
    });
});