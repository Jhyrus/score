$(document).on('ready',function(){
	 _V_.options.flash.swf = "/media/vendor/videjs/video-js.swf"

	initSlides();


	function initSlides(){
        $('#slider').carouFredSel({
            width: '100%',
            items: 3,
            scroll: 1,
            auto: {
                duration: 1250,
                timeoutDuration: 2500
            },
            prev: '#prev',
            next: '#next',
        });
	}    
});