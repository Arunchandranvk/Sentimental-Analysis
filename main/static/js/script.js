let menu_state = true

function menu_bar(){
    const nav = document.querySelector('.bottom ul')

    if(menu_state){
        nav.classList.add('active')
        menu_state = !menu_state
    }
    
    else {
        nav.classList.remove('active')
        menu_state = !menu_state
    }
}

window.onscroll = () => {
    const header = document.querySelector('.bottom')

    if(window.scrollY > 120){
        header.classList.add('bottom_fixed')
    }
    else {
        header.classList.remove('bottom_fixed')
    }

}

var swiper = new Swiper(".mySwiper", {
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    loop : true,
    onchange : false,
    allowTouchMove: false,
    speed : 1200,
    autoplay : true
  });

var swiper2 = new Swiper(".mySwiper2", {
    slidesPerView: 1,
    clickable: true,
    loop : true,
    autoplay : true,
    breakpoints : {
        651 : {slidesPerView : 2}
    }
});

var swiper3 = new Swiper(".mySwiper3", {
    slidesPerView: 1,
    clickable: true,
    loop : true,
    autoplay : true,
    breakpoints : {
        650 : {slidesPerView : 2},
        1000 : {slidesPerView : 4}
    }
});