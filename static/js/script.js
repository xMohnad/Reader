function loadImagesSequentially(images, index) {
    if (index < images.length) {
        var img = new Image();
        img.onload = function() {
            // عرض الصورة بعد تحميلها
            document.getElementById('readerarea').appendChild(img);
            // تحميل الصورة التالية
            loadImagesSequentially(images, index + 1);
        };
        img.onerror = function() {
            // في حالة فشل تحميل الصورة، قم بالمحاولة لتحميل الصورة التالية
            console.log('Failed to load image: ' + images[index]);
            loadImagesSequentially(images, index + 1);
        };
        img.src = images[index];
    }
}

var floatingDialog = document.getElementById('floatingDialog');
function closeDialog() {
    floatingDialog.style.display = "none";
}
function toggleDialog() {
if (floatingDialog.style.display === 'block') {
  floatingDialog.style.display = 'none';
} else {
  floatingDialog.style.display = 'block';
}
}

var buttons = document.getElementById('Buttons');
function optionsDialog() {
    buttons.classList.toggle('show'); /* تبديل الفئة show */
}

var btns = document.getElementById('allbut');
var lastScrollTop = 0;
window.addEventListener('scroll', function() {
    var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    if (scrollTop > lastScrollTop) {
        btns.style.opacity = "0";
    } else {
        btns.style.opacity = "1";
    }
    lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
});


document.getElementById("readerarea").addEventListener("click", function(event) {
    if(event.clientY < window.innerHeight / 2) {
        window.scrollTo(0, window.scrollY - window.innerHeight * 0.5);
    }
    else {
        window.scrollTo(0, window.scrollY + window.innerHeight * 0.5);
    }
});


function scrollToTop() {
  window.scrollTo(0, 0);
}
window.onscroll = function() {scrollFunction()};
function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById('scroll-top').style.display = "block";
    } else {
        document.getElementById('scroll-top').style.display = "none";
    }
}

function scrollToDown() {
  window.scrollTo(0, document.body.scrollHeight);
}


function toggleFullScreen() {
    var element = document.documentElement;
    if (!document.fullscreenElement && !document.webkitFullscreenElement && !document.msFullscreenElement) {
        if (element.requestFullscreen) {
            element.requestFullscreen();
        } else if (element.webkitRequestFullscreen) { /* Chrome, Safari & Opera */
            element.webkitRequestFullscreen();
        } else if (element.msRequestFullscreen) { /* IE/Edge */
            element.msRequestFullscreen();
        }
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        } else if (document.webkitExitFullscreen) { /* Chrome, Safari & Opera */
            document.webkitExitFullscreen();
        } else if (document.msExitFullscreen) { /* IE/Edge */
            document.msExitFullscreen();
        }
    }
}
