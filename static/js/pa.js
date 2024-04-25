var menu=0;
var data = {
    action: 'menubuttonclick', 
    data:'helo world',
      };
function st() {
  $.ajax({
      url: "{% url 'pa_app:myworkday' %}",
      type: "POST",
      data: {
          action: 'action1', // Replace with the actual action
      },
      success: function(response) {
          // Display the data in an alert
          console.log(response);
      }
  });
}
function canceloutsource(){
    
    console.log('outsourcing ccanceled')
    var formdata = new FormData();
    formdata.append('weeklytasks','weeklytasks');
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/pa/myworkday', false);
    ajax.send(formdata);
    document.documentElement.innerHTML = ajax.responseText
}
function canceldigitalize(taskid){
    console.log(' cancel digitalize task button clicked')
    var formdata = new FormData();
    formdata.append('alltasks','alltasks');
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/pa/myworkday', false);
    ajax.send(formdata);
    document.documentElement.innerHTML = ajax.responseText
}
function digitalize(taskid){
    console.log('digitalize task button clicked')
    var formdata = new FormData();
    formdata.append('alltasks','alltasks');
    formdata.append('digitalize',taskid);
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/pa/myworkday', false);
    ajax.send(formdata);
    document.documentElement.innerHTML = ajax.responseText
}
function confirmdigitalize(taskid){
    console.log('confirm digitalize task button clicked')
    var formdata = new FormData();
    formdata.append('alltasks','alltasks');
    formdata.append('digitalize',taskid);
    formdata.append('confirmdigitalize','confirmdigitalize')
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/pa/myworkday', false);
    ajax.send(formdata);
    document.documentElement.innerHTML = ajax.responseText
}
function outsource(taskid,token){
    console.log('outsource task button clicked'+token+'now')
    var formdata = new FormData();
    formdata.append('weeklytasks','weeklytasks');
    formdata.append('outsource',taskid);
    formdata.append('token',token);
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/pa/myworkday', false);
    ajax.send(formdata);
    document.documentElement.innerHTML = ajax.responseText
}
function automate(taskid){
    console.log('automate task button clicked')
    var formdata = new FormData();
    formdata.append('dailytasks','dailytasks');
    formdata.append('automate',taskid);
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/pa/myworkday', false);
    ajax.send(formdata);
    document.documentElement.innerHTML = ajax.responseText
}
function confirmoutsource(taskid,token){
    console.log('confirm outsource task button clicked'+taskid+'now'+token)
    console.log('outsourcing confirmed')
    var formdata = new FormData();
    formdata.append('weeklytasks','weeklytasks');
    formdata.append('outsource',taskid);
    formdata.append('token',token);
    formdata.append('confirmoutsource',taskid);
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/pa/myworkday', false);
    ajax.send(formdata);
    document.documentElement.innerHTML = ajax.responseText
}
function confirmautomate(taskid){
    
    console.log('automation confirmed')
    var formdata = new FormData();
    formdata.append('dailytasks','dailytasks');
    formdata.append('automate',taskid);
    formdata.append('confirmautomate',taskid);
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/pa/myworkday', false);
    ajax.send(formdata);
    document.documentElement.innerHTML = ajax.responseText
}
function cancelautomate(){
    
    console.log('automation ccanceled')
    var formdata = new FormData();
    formdata.append('dailytasks','dailytasks');
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/pa/myworkday', false);
    ajax.send(formdata);
    document.documentElement.innerHTML = ajax.responseText
}
function addtaskbuttonclick(){
    console.log('add task button was clicked');
    menu='add task';
    var formdata = new FormData();
    formdata.append('addtask','addtask');
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/pa/myworkday', false);
    ajax.send(formdata);
   
    document.documentElement.innerHTML = ajax.responseText
    
};
function alltasksbuttonclick(){
    console.log('all tasks button was clicked');
    var formdata = new FormData();
    formdata.append('alltasks','alltasks');
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/pa/myworkday', false);
    ajax.send(formdata);
    document.documentElement.innerHTML = ajax.responseText
    
};
function menubuttonclick(){
    console.log('menu button was clicked');
    menu='hello';
    var formdata = new FormData();
    formdata.append('menu','menu');
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/pa/myworkday', false);
    ajax.send(formdata);

    document.documentElement.innerHTML = ajax.responseText
    
};
function dailytasksbuttonclick(){
    console.log('daily tasks button was clicked');
    var formdata = new FormData();
    formdata.append('dailytasks','dailytasks');
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/pa/myworkday', false);
    ajax.send(formdata);
    document.documentElement.innerHTML = ajax.responseText
    
};
function weeklytasksbuttonclick(){
    console.log('weekly tasks button was clicked');
    var formdata = new FormData();
    formdata.append('weeklytasks','weeklytasks');
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/pa/myworkday', false);
    ajax.send(formdata);
  
    document.documentElement.innerHTML = ajax.responseText
    
};
function monthlytasksbuttonclick(){
    console.log('monthly tasks button was clicked');
    var formdata = new FormData();
    formdata.append('monthlytasks','monthlytasks');
    var ajax = new XMLHttpRequest();
    ajax.open("POST", 'http://127.0.0.1:8000/pa/myworkday', false);
    ajax.send(formdata);

    document.documentElement.innerHTML = ajax.responseText
    
};



function test1(){
    console.log('test button was clicked');
}


