// // const baseUrl = 'http://localhost:8000/api/v2/';
// //
// // function getFullPath(path) {
// //     path = path.replace(/^\/+|\/+$/g, '');
// //     path = path.replace(/\/{2,}/g, '/');
// //     return baseUrl + path + '/';
// // }
// //
// // function makeRequest(path, method, auth = true, data = null) {
// //     let settings = {
// //         url: getFullPath(path),
// //         method: method,
// //         dataType: 'json'
// //     };
// //     if (data) {
// //         settings['data'] = JSON.stringify(data);
// //         settings['contentType'] = 'application/json';
// //     }
// //     if (auth) {
// //         settings.headers = {'Authorization': 'Token ' + getToken()};
// //     }
// //     return $.ajax(settings);
// // }
// //
// // function saveToken(token) {
// //     localStorage.setItem('authToken', token);
// // }
// //
// // function getToken() {
// //     return localStorage.getItem('authToken');
// // }
// //
// // function removeToken() {
// //     localStorage.removeItem('authToken');
// // }
// //
// // function logIn(username, password) {
// //     const credentials = {username, password};
// //     let request = makeRequest('login', 'post', false, credentials);
// //     request.done(function (data, status, response) {
// //         console.log('Received token');
// //         saveToken(data.token);
// //     }).fail(function (response, status, message) {
// //         console.log('Could not get token');
// //         console.log(response);
// //     });
// // }
// //
// // $(document).ready(function () {
// //     let token = getToken();
// //     if (!token) logIn('admin', 'admin');
// // });
//
//
// /* Код с Лабораторной ESDP */
//
// function getCookie(name) {
//     var cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = cookies[i].trim();
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
//
// function favoritesAddSuccess(data) {
//     console.log(data);
//     let adPk = data.pk;
//     $('#add-to-favorites-' + adPk).addClass('d-none');
//     $('#delete-from-favorites-' + adPk).removeClass('d-none');
// }
//
// function favoritesDeleteSuccess(data) {
//     console.log(data);
//     let adPk = data.pk;
//     $('#add-to-favorites-' + adPk).removeClass('d-none');
//     $('#delete-from-favorites-' + adPk).addClass('d-none');
// }
//
// function favoritesAdd(e) {
//     e.preventDefault();
//     let link = $(e.target);
//     let href = link.attr('href');
//     let ad_pk = link.data('ad-pk');
//     $.ajax({
//         method: 'post',
//         url: href,
//         data: {'pk': ad_pk},
//         headers: {
//             'X-CSRFToken': getCookie('csrftoken')
//         }
//     })
//         .done(favoritesAddSuccess)
//         .fail(console.log);
// }
//
// function favoritesDelete(e) {
//     e.preventDefault();
//     let link = $(e.target);
//     let href = link.attr('href');
//     let ad_pk = link.data('ad-pk');
//     $.ajax({
//         method: 'post',
//         url: href,
//         data: {'pk': ad_pk},
//         headers: {
//             'X-CSRFToken': getCookie('csrftoken')
//         }
//     })
//         .done(favoritesDeleteSuccess)
//         .fail(console.log);
// }
//
// function setUpFavoriteButtons() {
//     $('.favorites-add').click(favoritesAdd);
//     $('.favorites-delete').click(favoritesDelete);
// }
//
// $(document).ready(setUpFavoriteButtons);
