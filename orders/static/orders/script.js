var menuJS = {

    init:function() {
        $('#submitbtn').prop('disabled', true);
        $("table#menu tr").on('click', function (e) {
            menuJS.add($(this));
        });
    },

    add:function(item_tr) {
        $("tr#nofood").hide();
        $('#submitbtn').prop('disabled', false);

        var order = $("<tr>");
        var olddata = item_tr.data();
        var firsttd = $("<td>").html($(item_tr.children('td')[0]).html());

        var input = $("<input>").attr('type', 'hidden').attr('name', 'items[]');
        input.val(olddata['id']);
        firsttd.append(input);

        order.append(firsttd);
        order.append($("<td>").html($(item_tr.children('td')[1]).html()));
        order.append($("<td>").html($("#deleteicon").html()));
        order.data('price', olddata['price']);
        order.data('id', olddata['id']);
        order.find('.removelink').on('click', function (e) {
            menuJS.remove($(order));
        });
        $("table#ordertable tr#total").before(order);

        this.updateTotal(olddata['price']);

        item_tr.find('.ordered').append($('#okicon').html());
    },

    remove:function(item_tr) {
        this.updateTotal(-item_tr.data('price'));
        var menu_tr = $("table#menu tr[data-id='"+ item_tr.data('id') +"']");
        menu_tr.find('.ordered').children('span:first').remove();
        item_tr.remove();
    },

    updateTotal:function(delta) {
        var total = $("table#ordertable tr#total").data('total');
        total += delta
        var totalstring = (total/100).toFixed(2).replace('.', ',');
        $("table#ordertable tr#total").data('total', total);
        $("table#ordertable tr#total td").first().html('€ ' + totalstring);
        if (total == 0) {
            $('#submitbtn').prop('disabled', true);
            $("tr#nofood").show();
        }
    }
};
menuJS.init();