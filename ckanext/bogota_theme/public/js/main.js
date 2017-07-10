$(function(){
    $(window).bind("load resize", function(){
        _winWidth = $(window).width();
        _winHeight= $(window).height();

        // Setting Width
        $('.side-1').css({'width':_winWidth * 0.15}); // 0.15 = 15%
        console.log('Width: ' + _winWidth);
        $('.side-2').css({'width':_winWidth * 0.15}); // 0.15 = 15%
        
        _wTop = 5; 
        
        if ( _winWidth > 1700) {
            _wTop = 5;
        } else if (_winWidth > 1000 ) {
            _wTop = 13;
        }
        
        $('.logo object').css({'width':_winWidth * 0.15, 'margin-top': _wTop}); // 0.15 = 15%
        
    });
});
