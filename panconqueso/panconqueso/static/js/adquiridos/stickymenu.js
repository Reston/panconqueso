$( document ).ready(function() {
	var altura_del_header = $('header').outerHeight(true);
	var altura_del_menu = $('.menuInicio').outerHeight(true);
	// Llamado cuando se cargue la página
	posicionarMenu();

	$(window).scroll(function(){
		posicionarMenu();
	});

	function posicionarMenu() {
		altura_del_menu = $('.menuInicio').outerHeight(true);
		//si el menu esta mas abajo cambiar el valor 0
		altura_del_header = $('header').outerHeight(true)+0;

		if ($(window).scrollTop() >= altura_del_header && $('.wrapper').width() >= 1000 ){
			$('.menuInicio').addClass('fixed');
			$('.contenido').css('margin-top', (altura_del_menu) + 'px');
		} else {
			$('.menuInicio').removeClass('fixed');
			$('.contenido').css('margin-top', '0');
		}
	}

	// This is a functions that scrolls to #{blah}link
	function goToByScroll(id){
	// Remove "link" from the ID
		id = id.replace("Menu", "");
	// Scroll
		$('html,body').animate({
			scrollTop: $("#"+id).offset().top - altura_del_menu}, //se altura del menu, solo si el menu continua
			'slow');
	}

	$("#menuSlow > ul > .menuopcion").click(function(e){
	// Prevent a page reload when a link is pressed
		e.preventDefault();
	// Call the scroll function
		goToByScroll($(this).attr("id"));
	});

	$("#menuSlowFooter > ul > .menuopcion").click(function(e){
	// Prevent a page reload when a link is pressed
		e.preventDefault();
	// Call the scroll function
		id = $(this).attr("id");
		id = id.replace("MenuFooter", "");
		goToByScroll(id);
	});
});

//EJEMPLO en html
//<section class="menuServicios">
//	<nav class="barraServicios" id="menuSlow">
//		<ul>
//				<li id="PreimplementMenu" class="opc1menu">Consultoría</li>
//				<li id="implementMenu" class="opc2menu">Implementación</li>
//				<li id="academyMenu" class="opc3menu">Academy</li>
//		</ul>	
//	</nav>
//</section>	