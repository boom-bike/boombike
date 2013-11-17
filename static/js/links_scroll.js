/*
 * The smooth scroll effect on a tags which having href="#.*"
 */

$(function() {
    var current_section = "#header";
    var small = false;
    var initial_nav_html = $("#home_nav").html();

    // Register the sections we want to be parallaxed
    var scroll_contents = $("[data-scroll=yes]");
    var scroll_contents_length = scroll_contents.length;

    // Set the currently viewed article
    function scrolled() {
        var window_scroll_top = $(window).scrollTop();
        var window_height = $(window).height();
        var document_height = $(document).height();
        var middle_section_coord = 0;
        var middle_window_coord = 0;

        for (var i=0; i < scroll_contents_length; i++) {

            middle_section_coord = $(scroll_contents[i]).offset().top +
                                   ($(scroll_contents[i]).height()/2);
            middle_window_coord = window_scroll_top + window_height;

            if (document_height == middle_window_coord) {
                $("#next").css("visibility", "hidden");
                $("#previous").parent()
                    .attr("href",
                          "#" + $(scroll_contents[scroll_contents_length-2]).attr("id"));
            }

            else if (middle_section_coord < middle_window_coord &&
                middle_section_coord > window_scroll_top) {
                current_section = '#' + $(scroll_contents[i]).attr("id");

                if (i-1 >= 0) {
                    $("#previous").css("visibility", "visible");
                    $("#previous").parent().attr("href", "#" + $(scroll_contents[i-1]).attr("id"));
                }
                else {
                    $("#previous").css("visibility", "hidden");
                }

                if (i+1 < scroll_contents_length) {
                    $("#next").css("visibility", "visible");
                    $("#next").parent().attr("href", "#" + $(scroll_contents[i+1]).attr("id"));
                }
                break;
            }
        }
    }

    function smooth_scroll() {
        $('a.smooth_scroll').on('click',function (e) {
            e.preventDefault();

            var target = this.hash,
            $target = $(target);

            $('html, body').stop().animate({
                'scrollTop': $target.offset().top
            }, 900, 'swing', function () {
                window.location.hash = target;
            });
            setTimeout(function() { scrolled(); }, 901);
        });
    }

    $(window).resize(function() {
        if($(window).width() <= 787) {
            small = true;
            $("#home_nav").css('top', '11px');
            $("#previous").css("visibility", "hidden");
            scrolled();
            smooth_scroll();
        }
        else {
            small = false;
            $("#home_nav").css('top', '45%');
        }
    });

    window.location.hash = "#header";

    // Trigger the resize event to make sure it is ok on load
    $(window).trigger('resize');

    $(window).scroll(function() {
        scrolled();
    });

    smooth_scroll();
    scrolled();
});
