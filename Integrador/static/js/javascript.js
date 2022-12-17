var btn =document.querySelector("#Moore");
var More = document.querySelector('li.More');

btn.addEventListener('click',function() {
    if(More.style.display === 'block'){
        More.style.display = 'none';
    }
    else{
        More.style.display = 'block';
    }

});

var bnt0 = document.querySelector("#Uusers");
var User = document.querySelector('li.Users');

bnt0.addEventListener('click', function(){
    if(User.style.display === 'block'){
        User.style.display = 'None';
        User.style.background='None';
    }else{
        User.style.display = 'block';
    }


});
