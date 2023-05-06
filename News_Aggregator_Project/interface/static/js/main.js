// nav background
let navbar = document.getElementsByClassName(".navbar");

window.addEventListener("scroll", () => {
    navbar.classList.toggle("shadow", window.scrollY > 0)
})

//Filter
$(document).ready(function () {
    $(".filter-item").click(function () {
        const value = $(this).attr("data-filter");
        if (value == "all"){
            $(".post-box").show("1000")
        } else{
            $(".post-box")
                .not("." + value)
                .hide(1000);
            $(".post-box")
            .filter("." + value)
            .show("1000")
        }
    });
    $(".filter-item").click(function () {
        $(this).addClass("active-filter").siblings().removeClass("active-filter")
    });
});


window.addEventListener('load', function() {
    var modals = document.getElementsByClassName('modal');
    var btns = document.getElementsByClassName('post-box');
    var spans = document.getElementsByClassName("close");
    var postContainer = document.querySelector('.post');

    postContainer.addEventListener('click', function(event) {
        console.log('post clicked');
        if(event.target.classList.contains('post-box')) {
            var index = Array.from(postContainer.children).indexOf(event.target);
            console.log(modals);
            console.log(index);
            console.log(modals.item(index));
            modals[index].style.display = 'flex';
        }    
    });

    for (var i = 0; i < spans.length; i++) {
        spans[i].addEventListener('click', function() {
    
          // Get the parent modal element of the clicked close button
          var modal = this.parentElement;
    
          // Hide the modal
          modal.style.display = 'none';
        });
      }
    
    // Add a click event listener to the window object to close the modal if the user clicks outside of it
    window.addEventListener('click', function(event) {
        if (event.target.classList.contains('modal')) {
            // Hide the modal
            event.target.style.display = 'none';
        }
    });
});



