var socket = io.connect();
socket.close();
socket.open();
var player = 0;
$(document).ready(function () {
    socket.on('connect', function () {
        socket.emit('joined', {
            data: window.location.pathname
        });
        $('#submit').click(function () {
            console.log("Click");
            $('.container').append(`    <div class="row">
            <div class="col-md">
              <p id="middle">Loading...</p>
            </div>
          </div>`);
        });
        $("#symbol").focusout(function () {
            var value = $("#symbol").val();
            getSymbol(value);
        });
        // $(':input[type="submit"]').prop('disabled', true);
    });
});

function getSymbol(symbol) {
    socket.emit('symbolLookup', symbol)
    console.log(symbol)
};

socket.on('symbol', function (data) {
    console.log(data)
    if (data != false) {
        $('#result').html(`<div class='row'>
        <div class='col' id='notification'>
        Company: ${data[0].company_name}<br>
        Last Evaluated: ${data[0].age} ago<br>
        Score: ${data[0].score}
        </div></div><br>`)
    } else {
        $('#result').html('')
    }

})

// ${JSON.stringify(data)}

var toValidate = $('#buy_analysts, #strong_buy, #symbol'),
    valid = false;

toValidate.keyup(function () {
    if (jQuery(this).val().length > 0) {
        jQuery(this).data('valid', true);
    } else {
        jQuery(this).data('valid', false);
    }
    toValidate.each(function () {
        if (jQuery(this).data('valid') == true) {
            valid = true;
        } else {
            valid = false;
        }
    });
    if (valid === true) {
        jQuery("#Submit").prop('disabled', false);
    } else {
        jQuery("#Submit").prop('disabled', true);
    }
});