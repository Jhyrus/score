$(document).on('ready', function(){

	$("#jquery_jplayer_1").jPlayer({
		ready: function () {
			$(this).jPlayer("setMedia", {
				m4v: "/media/uploads/videos/v1.webm",
				poster: "/media/uploads/videos/preloads/p4.jpg"
			});
		},
		swfPath: "js/jplayer",
		supplied: "m4v",
		size: {
			width: "372px",
			height: "210px",
			cssClass: "jp-video-360p"
		}
	});



	$('#botonprueba').click(function(){
		initSlides();
	});
	
	
	initSlides('#semana');
	initSlides('#chicas');

	// mini_news();
	// mini_central();
	// mini_posts();

	$('#contact_button').click(function(){
		openDialog();
	});

	$('#c1').click(function(){ ChangeColor('#c1'); });
	$('#c2').click(function(){ ChangeColor('#c2'); });
	$('#c3').click(function(){ ChangeColor('#c3'); });
	$('#c4').click(function(){ ChangeColor('#c4'); });
	$('#c5').click(function(){ ChangeColor('#c5'); });
	$('#c6').click(function(){ ChangeColor('#c6'); });
	$('#c7').click(function(){ ChangeColor('#c7'); });
	$('#c8').click(function(){ ChangeColor('#c8'); });
	$('#c9').click(function(){ ChangeColor('#c9'); });
	$('#c10').click(function(){ ChangeColor('#c10'); });
	$('#c11').click(function(){ ChangeColor('#c11'); });
	$('#c12').click(function(){ ChangeColor('#c12'); });
});


function limite(chart, size){
	var cad_min = chart.substring(0, size);
	return cad_min = cad_min + " ... ";
}


function mini_news(){
	var ant = $('#priority-news article p').text();
	$('#priority-news article p').text(limite(ant, 77));
}

function mini_posts(){
	var ant = $('#posts article p').text();
	$('#posts .post p').text(limite(ant, 240));
	$('#posts .mini-post p').text(limite(ant, 169));

}

function mini_central(){
	var ant = $('#main-new figure figcaption p').text();
	$('#main-new figure figcaption p').text(limite(ant, 128));

}



function initSlides(media){
    $(media).carouFredSel({
        width: 'null',
        items: 4,
        direction   : "left",
        scroll: 1,
        auto: {
            duration: 5000,
                timeoutDuration: 4000
            },
        prev: media + ' .prev',
        next: media + ' .next',
    });
}

function openDialog() {
	Avgrund.show( "#default-popup" );
}

function closeDialog() {
	Avgrund.hide();
}


function ChangeColor(element){
	$('body header').css('background-color',$(element).css('background-color'));
}