let searchdata = document.querySelector('.formSearch');

document.querySelector('#search').onclick = () =>{
    searchdata.classList.toggle('active');
}
let accountdata = document.querySelector('.loginForm');

document.querySelector('#user').onclick = () =>{
    accountdata.classList.toggle('active');
}
let iconnav = document.querySelector('.nav');

document.querySelector('#menu').onclick = () =>{
    iconnav.classList.toggle('active');
}

var swiper = new Swiper(".teamslider", {
    loop:true,
    spaceBetween:20,
    autoplay:{
        delay:3500,
        disableOnInteraction: false,
    },
    centetredSlides: true,
    breakpoints:{
        0:{
            slidesPerView:1,
           
        },
        768:{
            slidesPerView:2,
          
        },
        1020:{
            slidesPerView:3,
            
        },
    },

    
  });
