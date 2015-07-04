$(function() {
    $("select#receipts").change(function() {
        var id = $("select#receipts").val();
        $("div.receipt:not(div#receipt"+id+")").hide();
        $("div#receipt"+id).show();
    });
    $("select#receipts").change();
});

