function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function privatesAddSuccess(data) {
    console.log(data);
    let userPk = data.pk;
    $('#add-to-privates-' + userPk).addClass('d-none');
    $('#delete-from-privates-' + userPk).removeClass('d-none');
}

function privatesDeleteSuccess(data) {
    console.log(data);
    let userPk = data.pk;
    $('#add-to-privates-' + userPk).removeClass('d-none');
    $('#delete-from-privates-' + userPk).addClass('d-none');
}

function privatesAdd(e) {
    e.preventDefault();
    let link = $(e.target);
    let href = link.attr('href');
    let ad_pk = link.data('user-pk');
    $.ajax({
        method: 'post',
        url: href,
        data: {'pk': user_pk},
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
        .done(privatesAddSuccess)
        .fail(console.log);
}

function privatesDelete(e) {
    e.preventDefault();
    let link = $(e.target);
    let href = link.attr('href');
    let user_pk = link.data('user-pk');
    $.ajax({
        method: 'post',
        url: href,
        data: {'pk': user_pk},
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
        .done(favoritesDeleteSuccess)
        .fail(console.log);
}

function setUpPrivatesButtons() {
    $('.privates-add').click(privatesAdd);
    $('.privates-delete').click(privatesDelete);
}

$(document).ready(setUpPrivatesButtons);
