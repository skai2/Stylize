$(document).ready(function () {
    $('#upload-button').click(function () {
        uploadPhoto();
    });
});

function setCheckpoint(imgNumber, checkpoint) {

    // retira o filtro das imagens
    $.each( $('.img-responsive'), function(){
        $(this).css('filter','opacity(100%)');    
    });

    $('#avatar'+imgNumber).css('filter','opacity(50%)');

    $('#checkpoint').val(checkpoint);
}