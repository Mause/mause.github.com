$(document).ready(function() {
    $('input').each(function () {
        if ($(this).val() === '') {
            $(this).val($(this).attr('defaultvalue'));
            $(this).css({textAlign:"center"});
    }
    }).focus(function () {
        $(this).removeClass('inputerror');
        if ($(this).val() == $(this).attr('defaultvalue')) {
            $(this).val('');
            $(this).css({textAlign:"left"});
        }
    }).blur(function () {
        if ($(this).val() === '') {
            $(this).val($(this).attr('defaultvalue'));
            $(this).css({textAlign:"left"});
        }
    });


    /*GLOBAL NAVIGATION*/
    $(".post .open, .post .goto").css({opacity:0});

    $(".post").each(function(){
        var label_open = $(".open",this);
        var label_goto = $(".goto",this);
        //OPEN
        $(".avatar a", this).hover(function () {
            $(label_open).stop().animate({
                opacity: 1
                }, 'fast');
            },
            function () {
                $(label_open).stop().animate({
                    opacity: 0
                }, 'slow');
        });
        //GOTO
        $(".reblog", this).hover(function () {
            $(label_goto).stop().animate({
                opacity: 1
                }, 'fast');
            },
            function () {
                $(label_goto).stop().animate({
                    opacity: 0
                }, 'slow');
        });
    });
});
