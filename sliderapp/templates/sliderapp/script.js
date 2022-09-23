window.addEventListener('load', setUpSliders);


function setUpSliders() {
    var prevBtns = document.getElementsByClassName('prev-button');
    var nextBtns = document.getElementsByClassName('next-button');

    for (var i = 0; i < prevBtns.length; i++)
        prevBtns[i].addEventListener('click', function(e) {slide(e, 'prev')});
    
    for (var i = 0; i < nextBtns.length; i++)
        nextBtns[i].addEventListener('click', function(e) {slide(e, 'next')});
};


function slide(e, to) {
    var sliderId = e.target.getAttribute('data-target');
    var sliderInner = document.querySelector('#' + sliderId + ' .slider-inner');
    var activeSlide = sliderInner.querySelector('.active');

    var toSlide;

    if (to === 'prev') {
        toSlide = activeSlide.previousElementSibling;
        if (!toSlide)
            toSlide = activeSlide.parentElement.lastElementChild;
    } else {
        toSlide = activeSlide.nextElementSibling;
        if (!toSlide)
            toSlide = activeSlide.parentElement.firstElementChild;
    }

    activeSlide.classList.remove('active');
    toSlide.classList.add('active');
};
