// fade in  course container
// window.addEventListener('DOMContentLoaded', function() {
//      var card = this.document.getElementsByClassName('.card-body');
//      card.style.animation = 'fade-in 0.5s ease-in-out forwards';
// });

//zoom course container
function zoomCard() {
    var card = document.querySelector('.card-body');
                     card.classList.add('zoomed');
}

//testimonials slide
const slides = document.querySelectorAll('.testimonial');

let currentSlide = 0;
slides[0].classList.add('active');

function goToSlide(slideIndex) {
     slides[currentSlide].classList.remove('active');
     slides[slideIndex].classList.add('active');
     currentSlide = slideIndex;
}

function nextSlide() {
    const nextSlideIndex = (currentSlide + 1) % slides.length;
    goToSlide(nextSlideIndex);

}
setInterval(() => {
    nextSlide();
}, 6000);