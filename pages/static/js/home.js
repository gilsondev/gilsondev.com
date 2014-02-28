$(document).ready(function() {
    $('.navbar li').click(function(e) {
        $('.navbar li.active').removeClass('active');
        var $this = $(this);
        var section = $($this.attr('href'));
        if (!$this.hasClass('active')) {
            $this.addClass('active');
        }

        $('html, body').animate({scrollTop: section.offset().top}, 2000);
        e.preventDefault();
    });
});
