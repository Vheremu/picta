function pn(number){
    console.log('pages number button clicked')
    var formdata = new FormData();
    formdata.append('alltasks','alltasks');
    formdata.append('digitalize',taskid);
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/sa', false);
    ajax.send(formdata);
    document.documentElement.innerHTML = ajax.responseText
}