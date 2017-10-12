function onFocusVal(abc) {
    var input = $(abc).attr('name');
    var giaTri = $('#'+input).val();

    if(giaTri == ''){
        $('#'+input+'Err').css('display','inline');
        $('#'+input).focus();
        $('#'+input).css('border','solid red 1px');
    }
    else{
        $('#'+input+'Err').css('display','none');
        $('#'+input).css('border','solid  #cccccc 1px');
    }
}

/*$(document).ready(function(){
    $('#btnNext').attr('class','c_disable');
    var nguoi_daidien = $('#nguoi_daidien').val();
    var sodienthoai = $('#sodienthoai').val();
    var email = $('#email').val();
    var diachi = $('#diachi').val();
    var ten_doanhnghiep = $('#ten_doanhnghiep').val();

    var arrValue = [];
    arrValue.push(nguoi_daidien,sodienthoai,email,diachi,ten_doanhnghiep);

    $.each(arrValue, function( index, value ) {
        console.log( index + ": " + value );
        if(value==''){
            $('#infoErr').css('display','inline');
        }
        $('#btnNext').removeClass('c_disable');
        $('#infoErr').css('display','none');
        
    });
    
});
*/
