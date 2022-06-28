$(document).ready(function(){

	$("#registrar").click(function(e) {       
        $('#modalRegistro').modal('show');
        e.preventDefault();    
	});

    $("#boton_login").click(function(ev) {
        // ev.preventDefault();
        $('#modalRegistro').modal('show');
    });

});
