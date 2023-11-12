$(document).ready(function() {
    $('#calcular').on('click', function() {
        var num1 = $('#edad').val();
        var num2 = $('#anemia').val();
        var operation = $('#operation').val();

        // Perform the calculation on the server
        $.post('/calculate', {num1: num1, num2: num2, operation: operation}, function(response) {
            // Update the result in the personalized div
            $('#result').text(response);
        });
    });
});