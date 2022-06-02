$(function(){
    $('.menu-button').click(function(){
        $(this).toggleClass('active');
        $('.mobile-menu').toggleClass('open');
    });
    $('.mobile-menu-inner > ul > li > a').click(function(){
        $('.menu-button').removeClass('active');
        $('.mobile-menu').removeClass('open');
    });
    $('.edit1').click(function(){
        $('.form1').toggleClass('none');
    });
    $('.edit2').click(function(){
        $('.form2').toggleClass('none');
    });
    $('.edit3').click(function(){
        $('.form3').toggleClass('none');
    });
    $('.edit4').click(function(){
        $('.form4').toggleClass('none');
    });

    $('.mobile-menu ul > li').has('ul').addClass('down');
    $('.mobile-menu .down > ul').before('<span class="dropdown-button"></span>');    
    $('.mobile-menu .dropdown-button').click(function(){
        $(this).toggleClass('active');
        if($(this).siblings('ul').is(':visible')){
            $(this).siblings('ul').slideUp();
        }else{
            $(this).siblings('ul').slideDown();
        }
        
    });
    $('.top-menu  ul > li').has('ul').addClass('down');
    $('.top-menu  .down > ul').before('<span class="dropdown-button"></span>');    

	$(".header-img-wrap").slick({
        dots: true,
        infinite: true,
        speed: 300,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        adaptiveHeight: true,
        autoplaySpeed: 2000
      });
      $(".participant-slider").slick({
    	infinite: true,
    	speed: 300,
        arrows: false,
    	slidesToShow: 3,
    	slidesToScroll: 1,
    	autoplay: true,
    	swipeToSlide: true,
    	adaptiveHeight: true,
    	autoplaySpeed: 6000,
        responsive: [
		     {
		       breakpoint: 700,
		       settings: { slidesToShow: 2 },
		     },
             {
                breakpoint: 550,
                settings: { slidesToShow: 1 },
            }
		  ]
      });
      $(".prize-wrap-slider").slick({
        dots: false,
        infinite: true,
        speed: 300,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        adaptiveHeight: true,
        autoplaySpeed: 2000
      });
      
	// fancybox
	    $('.fancybox').fancybox({
	        padding: 0,
	        openEffect  : 'none',
	        closeEffect : 'none',
	        nextEffect  : 'none',
	        prevEffect  : 'none',
	        helpers: {
	            overlay: {
	              locked: false
	            }
	        }
	    });

        $('.signin').fancybox({
	        padding: 0,
	        openEffect  : 'none',
	        closeEffect : 'none',
	        nextEffect  : 'none',
	        prevEffect  : 'none',
	        helpers: {
	            overlay: {
	              locked: false
	            }
	        }
	    });
        $('.regist').fancybox({
	        padding: 0,
	        openEffect  : 'none',
	        closeEffect : 'none',
	        nextEffect  : 'none',
	        prevEffect  : 'none',
	        helpers: {
	            overlay: {
	              locked: false
	            }
	        }
	    });

        $('.fancyboxModal').fancybox({
            autoResize:true,            
            padding: 0,
            openEffect  : 'fade',
            closeEffect : 'fade',
            nextEffect  : 'none',
            prevEffect  : 'none',
            fitToView : false, 
            maxWidth: '100%',
            scrolling : "no",
            helpers: {
            overlay: {
              locked: false
            }
            }
        });
	 //----------------------------ЦИФРЫ!!!!!!!!-----------------------------------------------------
	     $('.num1').viewportChecker({
            classToAdd: 'visible animated fadeInUp',
            offset: 100,
            callbackFunction: function(){
                $('#num1').animateNumber({ number: 205 },2500); //КОЛЛИЧЕСТВО ПРОЕКТОВ
            }
        });
        
        $('.num2').viewportChecker({
            classToAdd: 'visible animated fadeInUp',
            offset: 100,
            callbackFunction: function(){
                $('#num2').animateNumber({ number: 105 },2500);  //КОЛЛИЧЕСТВО ЧЕЛОВЕК
            }
        });
        
        $('.num3').viewportChecker({
            classToAdd: 'visible animated fadeInUp',
            offset: 100,
            callbackFunction: function(){
                $('#num3').animateNumber({ number: 3 },1200);//СКОЛЬКО ЛЕТ
            }
        });

          // validation
        
          $('.rf').each(function(){
            var item = $(this),
            
            btn = item.find('.btn');
            
            
            function checkInput(){
                item.find('select.required').each(function(){
                    if($(this).val() == '0'){
                        
                        // Если поле пустое добавляем класс-указание
                        $(this).parents('.form-group').addClass('error');
                        $(this).parents('.form-group').find('.error-message').show();

                    } else {
                        // Если поле не пустое удаляем класс-указание
                        $(this).parents('.form-group').removeClass('error');
                    }
                });
                
                
                
                
                
                item.find('input[type=text].required').each(function(){
                    if($(this).val() != ''){
                        // Если поле не пустое удаляем класс-указание
                        $(this).removeClass('error');
                    } else {
                        // Если поле пустое добавляем класс-указание
                        $(this).addClass('error');
                        $(this).parent('.form-group').find('.error-message').show();
                        
                    }
                });
                
                
                item.find('input[type=password].required').each(function(){
                    if($(this).val() != ''){
                        // Если поле не пустое удаляем класс-указание
                        $(this).removeClass('error');
                    } else {
                        // Если поле пустое добавляем класс-указание
                        $(this).addClass('error');
                        $(this).parent('.form-group').find('.error-message').show();
                        
                    }
                });
                
                
                if($('.pass1',item).length != 0){
                    var pass01 = item.find('.pass1').val();
                    var pass02 = item.find('.pass2').val();
                    if(pass01 != pass02){
                        $('.pass1, .pass2',item).addClass('error');
                        
                        
                        $('.pass1').parent('.form-group').find('.error-message').show();
                        $('.pass2').parent('.form-group').find('.error-message').show();
                    }
                }
                
                
                
                item.find('textarea.required').each(function(){
                    if($(this).val() != ''){
                        // Если поле не пустое удаляем класс-указание
                        $(this).removeClass('error');
                    } else {
                        // Если поле пустое добавляем класс-указание
                        $(this).addClass('error');
                        $(this).parent('.form-group').find('.error-message').show();
                        
                    }
                });
                
                item.find('input[type=email]').each(function(){
                    var regexp = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/i;
                    var $this = $(this);
                    if($this.hasClass('required')){
                        
                        if (regexp.test($this.val())) {
                            $this.removeClass('error');
                        }else {
                            // Если поле пустое добавляем класс-указание
                            $this.addClass('error');
                            $(this).parent('.form-group').find('.error-message').show();
                        }
                    }else{
                        
                        if($this.val() != ''){
                            if (regexp.test($this.val())) {
                                $this.removeClass('error');
                            }else {
                            
                            $this.addClass('error');
                            $(this).parent('.form-group').find('.error-message').show();
                            }
                        }else{
                            $this.removeClass('error');
                        }
                    }
                    
                    
                });
                
             
            
            }

            btn.click(function(){
                checkInput();
                var sizeEmpty = item.find('.error:visible').size();
                if(sizeEmpty > 0){
                    return false;
                } else {
                    // Все хорошо, все заполнено, отправляем форму
                    
                    item.submit();
                    $.fancybox.close();
                }
            });

        });
        
        
        $('.required:not(.pass1, .pass2)').change(function(){
            if($(this).val() != ''){
                $(this).removeClass('error');
                $(this).parents('.form-group').find('.error-message').hide();
                $(this).parents('.form-group').find('.t-tip').tooltip('hide');
            }
            
        });
        
        $('.pass1').change(function(){
            if($(this).val() != ''){
                
                var pass1Val = $('.pass1').val();
                var pass2Val = $(this).parents('.rf').find('.pass2').val();
                
                if(pass1Val == pass2Val){
                    $('.pass1, .pass2').removeClass('error');
                    $('.pass1, .pass2').parents('.form-group').find('.error-message').hide();
                    $('.pass1, .pass2').parents('.form-group').find('.t-tip').tooltip('hide');
                }

            }
            
        });
        
        $('.pass2').change(function(){
            if($(this).val() != ''){
                
                var pass2Val = $('.pass2').val();
                var pass1Val = $(this).parents('.rf').find('.pass1').val();
                
                if(pass1Val == pass2Val){
                    $('.pass1, .pass2').removeClass('error');
                    $('.pass1, .pass2').parents('.form-group').find('.error-message').hide();
                    $('.pass1, .pass2').parents('.form-group').find('.t-tip').tooltip('hide');
                }

            }
            
        });
        
        
        $('select').change(function(){
            if($(this).val() == ''){     
                // Если значение empty
                $(this).parents('.form-group').removeClass('selected');

            } else {
                // Если значение не empty
                $(this).parents('.form-group').addClass('selected');
                $(this).parents('.form-group').removeClass('error');
            }
        });
        
        // end validation

}); // end document ready



