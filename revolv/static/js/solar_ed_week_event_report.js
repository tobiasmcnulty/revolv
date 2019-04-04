$(document).ready(function () {
    table = $('#matching_donor').DataTable({
        "dom": 'lfrtBip',
        "scrollX": true,
        buttons: [],
        "columnDefs": [{
            "targets": 3,
            "orderable": false
        }],
        aoColumnDefs: [
            {
                bSortable: false,
                aTargets: [3, 4]
            }]
    })

    $(document).on("click", ".close-btn", function () {
        id = $(this).attr('data-id');
        var tr = $(this).closest('tr');
        if (confirm("Are you sure you want to delete this?")) {
            $.ajax({
                type: "GET",
                url: '/delete_event/',
                data: { id: id },
                success: function () {
                    tr.fadeOut(1000, function () {
                        $(this).remove();
                        table.row(tr).remove().draw();
                    });

                }
            });
        }
    });


    $(document).on("click", ".edit", function () {
        var id = $(this).attr('data-id');
        $(this).closest('td').data()
        $.ajax({
            type: "GET",
            url: '/edit_event/',
            data: { id: id },
            success: function (response) {
                matchingDonor = JSON.parse(response.emp);
                $('#name').val(matchingDonor[0].fields.name);
                $('#title').val(matchingDonor[0].fields.title);
                $('#email').val(matchingDonor[0].fields.email);
                $('#evntime').val(matchingDonor[0].fields.evntime);
                $('#date').val(matchingDonor[0].fields.date);
                $('#address').val(matchingDonor[0].fields.address);
                $('#city').val(matchingDonor[0].fields.city);
                $('#state').val(matchingDonor[0].fields.state);
                $('#zip_code').val(matchingDonor[0].fields.zip_code);
                $('#detail').val(matchingDonor[0].fields.detail);
                $('#facebook_link').val(matchingDonor[0].fields.facebook_link);
                $('#id').val(matchingDonor[0].pk);
                $('#matching_donor_modal').modal('toggle');
                $("#matching-donor-save").removeAttr('disabled');
            }

        });
    });

    $('#matching-donor-save').click(function () { 
        var $frm = $('#add_matching_donor');
        $.ajax({
            type: "POST",
            url: '/add_events_form/',
            data: $frm.serialize(),
            success: function (data) {
                var id = $("#id").val();
                location.reload()
            }
        });
    });
    $("input[type=search]").keyup(function (e) {
        let search_input = e.target.value.trim();
        if (search_input === 0) {
            e.target.value = search_input;
        }
    });
});