var path = location.protocol + "//" + location.host
var vueItem

function createItem() {
    var id = $('#id').val()
    var requestData = {
        name: $('#name').val(),
        amount: $('#amount').val()
    }
    $.ajax({
            url: path + '/api/1.0.0/item/' + id,
            type: 'POST',
            data: requestData
        })
        .done((item) => {
            vueItem.items.push(JSON.parse(item))
            $('#createModal').modal('hide')
        })
}

function showUpdateModal(item) {
    $('#createModal').modal('show')
}

$(document).ready(function() {
    vueItem = new Vue({
        el: '#item_list',
        data: {
            items: []
        },
        methods: {
            deleteelement: function(id) {
                $.ajax({
                        url: '/api/1.0.0/item/' + id,
                        type: 'DELETE'
                    })
                    .done((result) => {
                        if (result === "success") {
                            var i = this.items.findIndex((v) => v.id === id);
                            this.items.splice(i, 1)
                        }
                    })
            }
        }
    })
    $.ajax({
            url: path + '/api/1.0.0/items',
            type: 'GET'
        })
        .done((data) => {
            vueItem.items = data["items"];
        })

});