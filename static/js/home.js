var w = Math.max(document.documentElement.clientWidth, window.innerWidth || 0)
var h = Math.max(document.documentElement.clientHeight, window.innerHeight || 0)
var images = document.getElementsByClassName('bg-fader-img');

for (i = 0; i < images.length; i++) {
    if (w/h < 16/9) {
        images[i].style.width = 'auto';
        images[i].style.height = '100%';

    }
    else {
        images[i].style.width = '100%';
        images[i].style.height = 'auto';

    }
}
