const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');

allSideMenu.forEach(item=> {
	const li = item.parentElement;

	item.addEventListener('click', function () {
		allSideMenu.forEach(i=> {
			i.parentElement.classList.remove('active');
		})
		li.classList.add('active');
	})
});




// TOGGLE SIDEBAR
const menuBar = document.querySelector('#content nav .bx.bx-menu');
const sidebar = document.getElementById('sidebar');

menuBar.addEventListener('click', function () {
	sidebar.classList.toggle('hide');
});







const searchButton = document.querySelector('#content nav form .form-input button');
const searchButtonIcon = document.querySelector('#content nav form .form-input button .bx');
const searchForm = document.querySelector('#content nav form');

searchButton.addEventListener('click', function (e) {
	if(window.innerWidth < 576) {
		e.preventDefault();
		searchForm.classList.toggle('show');
		if(searchForm.classList.contains('show')) {
			searchButtonIcon.classList.replace('bx-search', 'bx-x');
		} else {
			searchButtonIcon.classList.replace('bx-x', 'bx-search');
		}
	}
});





if(window.innerWidth < 768) {
	sidebar.classList.add('hide');
} else if(window.innerWidth > 576) {
	searchButtonIcon.classList.replace('bx-x', 'bx-search');
	searchForm.classList.remove('show');
}


window.addEventListener('resize', function () {
	if(this.innerWidth > 576) {
		searchButtonIcon.classList.replace('bx-x', 'bx-search');
		searchForm.classList.remove('show');
	}
});



const switchMode = document.getElementById('switch-mode');

switchMode.addEventListener('change', function () {
	if(this.checked) {
		document.body.classList.add('dark');
	} else {
		document.body.classList.remove('dark');
	}
});

$(document).ready(function(){
        
	$(window).scroll(function(){
		if(this.scrollY > 20){
			$('.mynav').addClass("sticky");
		}else{
			$('.mynav').removeClass("sticky");

		}
		if(this.scrollY > 500){
			$('.scroll').addClass("show");
		}else{
			$('.scroll').removeClass("show");
		}

	}); 



	$('.scroll').click(function(){
		$('html').animate({scrollTop: 0})
	});
	// navar/menu
	$('.menu-btn').click(function(){
		$('.mynav .menu').toggleClass("active");
		$('.menu-btn i').toggleClass("active"); 
	})
	// owl carousel
	$('.carousel').owlCarousel({
		margin:20,
		loop: true,
		autoPlayTimeOut: 2000,
		autoPlayHoverPause: true,
		responsive:{
			0:{
				items:1,
				nav:false
			},
			600:{
				items:2,
				nav:false
			},
			1000:{
				items:3,
				nav:false
			}
		}
	})
}) ;

// typing Animation 
var typed = new Typed(".typing",{
	strings: ["Better Doctor" ,"Better Care" , "Better Services" , "More and More"],
	typeSpeed:100,
	backSpeed:60 ,
	loop: true ,
});
var typed = new Typed(".typing-2",{
	strings: ["Better Doctor" ,"Better Care" , "Better Services" , "More and More"],
	typeSpeed:100,
	backSpeed:60 ,
	loop: true ,
});

// start loading-overlay
$(window).load(function()
{
	$("body").css("overflow","auto");

	$(".loading-overlay h1").fadeOut(2000,
	function()
	{
		$(this).parent().fadeOut(2000,
		function()
		{
			$(this).remove();
		});
	});
});

  /*------------------start Department----------*/


$('.departments div div div ul li').click(function()    {
	 $(this).parent().find('.active').removeClass();
	 $(this).addClass('active');
	 var id = $(this).attr('id');
	 $(this).parent().parent().parent().find('div .tab-content').find('div').removeClass('show');
	 $(this).parent().parent().parent().find('div .tab-content').find($("div[custom="+id+"]")).addClass('show');
 });

/*------------------end Department----------*/


$(document).ready(function(){
    $(window).scroll(function(){
        if(this.scrollY > 20){
            $('.mynav').addClass("sticky");
        }else{
            $('.mynav').removeClass("sticky");

        }
        if(this.scrollY > 500){
            $('.scroll').addClass("show");
        }else{
            $('.scroll').removeClass("show");
        }

    }); 
    $('.scroll').click(function(){
        $('html').animate({scrollTop: 0})
    });
    // navar/menu
    $('.menu-btn').click(function(){
        $('.mynav .menu').toggleClass("active");
        $('.menu-btn i').toggleClass("active"); 
    })
    // owl carousel
    $('.carousel').owlCarousel({
        margin:20,
        loop: true,
        autoPlayTimeOut: 2000,
        autoPlayHoverPause: true,
        responsive:{
            0:{
                items:1,
                nav:false
            },
            600:{
                items:2,
                nav:false
            },
            1000:{
                items:3,
                nav:false
            }
        }
    })
}) ;
// typing Animation 
var typed = new Typed(".typing",{
    strings: ["Better Doctor" ,"Better Care" , "Better Services" , "More and More"],
    typeSpeed:100,
    backSpeed:60 ,
    loop: true ,
});
var typed = new Typed(".typing-2",{
    strings: ["Better Doctor" ,"Better Care" , "Better Services" , "More and More"],
    typeSpeed:100,
    backSpeed:60 ,
    loop: true ,
});

// start loading-overlay
$(window).load(function()
{
    $("body").css("overflow","auto");

    $(".loading-overlay h1").fadeOut(2000,
    function()
    {
        $(this).parent().fadeOut(2000,
        function()
        {
            $(this).remove();
        });
    });
});