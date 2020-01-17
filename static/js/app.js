
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect(document.protocol + '//' + document.domain + ':' + location.port + '/random');
    var numbers_received = [];

    //receive details from server
    socket.on('new_number', function(msg) {
        console.log("Received number " + msg.number);
        //maintain a list of ten numbers
        if (numbers_received.length >= 5){
            numbers_received.shift()
        }            
        numbers_received.push(msg.number);
        numbers_string = '';
        for (var i = 0; i < numbers_received.length; i++){
            numbers_string = numbers_string + '<p>' + numbers_received[i].toString() + '</p>';
        }
        $('#log').html(numbers_string);
    });

});