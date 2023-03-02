const images = document.querySelectorAll('.slider .slider-line img');
const sliderLine = document.querySelector('.slider-line');
let count = 0;
let width;

function init (){
    width = document.querySelector('.slider').offsetWidth;
    sliderLine.style.width = width*images.length + 'px';
    images.forEach(item =>{
        item.style.width = width + 'px';
        item.style.height = 'auto';
    })
    rollSlider();
}

window.addEventListener('resize', init);
init();


document.querySelector('.slider__btn_prev').addEventListener('click',function (){
    count--;
    if (count < 0) {
        count = images.length - 1;
    }
    rollSlider();
})

document.querySelector('.slider__btn_next').addEventListener('click',function (){
    count++;
    if (count >= images.length) {
        count = 0;
    }
    rollSlider();
})

function rollSlider() {
    sliderLine.style.transform = 'translate(-' + count * width + 'px)';
}

let timer = setInterval(function(){
    count++;
    if (count >= images.length) {
        count = 0;
    }
    rollSlider();
  },5000);
