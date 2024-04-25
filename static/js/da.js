function menubuttonclick(){
    console.log('menu button was clicked');
    menu='add task';
    var formdata = new FormData();
    formdata.append('menu','menu');
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/da/', false);
    ajax.send(formdata);
    document.documentElement.innerHTML = ajax.responseText;}
function ticketsbuttonclick(){
    console.log('tickets button was clicked');
    menu='add task';
    var formdata = new FormData();
    formdata.append('tickets','tickets');
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/da/', false);
    ajax.send(formdata);
    document.documentElement.innerHTML = ajax.responseText;}
function appointmentsbuttonclick(){
    console.log('appointments button was clicked');
    menu='add task';
    var formdata = new FormData();
    formdata.append('appointments','appointments');
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/da/', false);
    ajax.send(formdata);
    document.documentElement.innerHTML = ajax.responseText;}
function projectsbuttonclick(){
    console.log('projects button was clicked');
    menu='add task';
    var formdata = new FormData();
    formdata.append('projects','projects');
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/da/', false);
    ajax.send(formdata);
    document.documentElement.innerHTML = ajax.responseText;}
function queriesbuttonclick(){
    console.log('queries button was clicked');
    menu='add task';
    var formdata = new FormData();
    formdata.append('queries','queries');
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/da/', false);
    ajax.send(formdata);
    document.documentElement.innerHTML = ajax.responseText;}
function automate(taskid){
    alert('helo world');
    
}
function bookappointment(ticket,token){
    console.log('book appointment click');
    var formdata = new FormData();
    formdata.append('tickets','tickets');
    formdata.append('token',token);
    formdata.append('ticket',ticket.value);
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/da/', false);
    ajax.send(formdata);
    document.documentElement.innerHTML = ajax.responseText;
}
function confirmbookappointment(ticket,token1){
    console.log('confirm book'+token1+ticket+' appointment click'+token1);
    var formdata = new FormData();
    formdata.append('tickets','tickets');
    formdata.append('token',token1);
    formdata.append('ticket',ticket.value);
    formdata.append('confirm','confirm');
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/da/', false);
    ajax.send(formdata);
    document.documentElement.innerHTML = ajax.responseText;
}
//    console.log('queries button was clicked');
//    menu='add task';
//    var formdata = new FormData();
//    formdata.append('queries','queries');
//    var ajax = new XMLHttpRequest();
//    ajax.open("POST", 'http://127.0.0.1:8000/da/', false);
//    ajax.send(formdata);
//    document.documentElement.innerHTML = ajax.responseText;}