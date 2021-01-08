// Create, Update, Delete, List.
// TODO: do this task.

// AJAX method to implement CRUD.
/*
    1. Form or input of HTML.
    2. Click button to call function.
    3. Get value of object from list.
    4. AJAX data to submit to backend.
    5. Get response and show modal message.
*/

var ObjectDelegate = function() {
    // TODO: using this to update data if any AJAX function.
    this.object = {};
    this.print_object = () => return this.object;
}

var od = new ObjectDelegate();
od.convert_to = () => {
    // add a function to do deep copy for dictionary.
}

function create_object() {
}

// select/option event-driven on modal.
function create_object() {
    // insert product_profile's option into the select of model type.
    $('#modal_product_profile').empty();
    $('#modal_process_profile').empty();

    axios.get('/get_product_profile/', {
    })
    .then(function(response) {
        let product_profile_string = '<option selected>請選擇 Mode Type</option>';
        let process_profile_string = '<option selected>請選擇 Operation</option>';

        for (let i=0, max=response.data.length; i<max; i++) {
            product_profile_string += '<option value=' +
                                      response.data[i].id +
                                      '>' +
                                      response.data[i].item_name +
                                      '</option>';
        }
        $('#modal_product_profile').append(product_profile_string);
        $('#modal_process_profile').append(process_profile_string);

        // set up the select/option of operation.
        $('select#modal_product_profile').on('change', function() {
            let mpdp = $('#modal_product_profile :selected').text();
            $('#modal_process_profile').empty();
            get_operation(mpdp);
        })
    })
    .catch(function(error) {
        console.log('error', error);
    })
}
