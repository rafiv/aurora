/**
 * Created by dan on 1/29/14.
 *
 * simple functions should include modifications, that are done via single click
 * e.g. vote up/down, promote, bookmark
 */

var COMMENTS = (function (my, $) {
    "use strict";

    my.post = function(url, data) {
        $.ajax({
            url: url,
            data: data,
            type: 'POST',
            dataType: 'json',
            beforeSend: function (xhr) {
                var csrftoken = my.getCsrfToken();
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        });
    };

    my.getCsrfToken = function() {
        return $('[name=csrfmiddlewaretoken]').first().val();
    };

    my.registerPromoteLinksForCommentList = function($comment_list) {
        $comment_list.find('.comment_promote').click(function(event) {
            var $this = $(this);
            promote($this, event);
        });

        $comment_list.find('.comment_demote').click(function(event) {
            var $this = $(this);
            demote($this, event);
        });

        function promote($this, event) {
            event.preventDefault();
            event.stopPropagation();

            if(typeof my.POLLING !== 'undefined') {
                my.POLLING.resetTimer();
            }

            var comment_number = $this.data('comment_number');
            my.post(COMMENTS.PROMOTE_URL, {comment_id: comment_number, value: true});

            $this.off();
            $this.click(function(event){
                demote($this, event);
            });
            $this.toggleClass('comment_demote comment_promote');
            $this.find('i').toggleClass('gold ungold');

            return false;
        }

        function demote($this, event) {
            event.preventDefault();
            event.stopPropagation();

            if(typeof my.POLLING !== 'undefined') {
                my.POLLING.resetTimer();
            }

            var comment_number = $this.data('comment_number');
            my.post(COMMENTS.PROMOTE_URL, {comment_id: comment_number, value: false});

            $this.off();
            $this.click(function(event) {
                promote($this, event);
            });
            $this.toggleClass('comment_demote comment_promote');
            $this.find('i').toggleClass('gold ungold');

            return false;
        }
    };

    my.registerBookmarkLinksForCommentList = function($comment_list) {
        $comment_list.find('.comment_bookmark').click(function(event) {
            var $this = $(this);
            bookmark($this, event);
        });

        $comment_list.find('.comment_unbookmark').click(function(event) {
            var $this = $(this);
            unbookmark($this, event);
        });

        var url = my.BOOKMARK_URL;

        function bookmark($this, event) {
            event.preventDefault();

            if(typeof my.POLLING !== 'undefined') {
                my.POLLING.resetTimer();
            }

            var comment_number = $this.data('comment_number');
            var data = {
                comment_id: comment_number,
                bookmark: true
            };
            my.post(url, data);

            $this.off();
            $this.click(unbookmark);
            $this.toggleClass('comment_unbookmark comment_bookmark');
            $this.text('unbookmark');

            return false;
        }

        function unbookmark($this, event) {
            event.preventDefault();

            if(typeof my.POLLING !== 'undefined') {
                my.POLLING.resetTimer();
            }

            var comment_number = $this.data('comment_number');
            var data = {
                comment_id: comment_number,
                bookmark: false
            };
            my.post(url, data);

            $this.off();
            $this.click(bookmark);
            $this.toggleClass('comment_unbookmark comment_bookmark');
            $this.text('bookmark');

            return false;
        }
    };

    my.registerSeenLinksForCommentList = function($comment_list) {
        $comment_list.find('.mark_seen_link').click(function(event) {
            var $this = $(this);
            markSeen($this, event);
        });

        var url = my.MARK_SEEN_URL;

        function markSeen($this, event) {
            event.preventDefault();

            if(typeof my.POLLING !== 'undefined') {
                my.POLLING.resetTimer();
            }

            var comment_ids = [];

            $this.parents(".comment_with_responses").find(".comment, .response").each(function() {
                comment_ids.push($(this).data('comment_number'));
            });

            var data = {
                comment_ids: comment_ids
            };

            my.post(url, data);

            $this.off();
            $this.removeClass('mark_seen_link').addClass('seen_link');
            $this.text('(seen)');

            return false;
        }
    };

    return my;
}(COMMENTS || {}, jQuery));
