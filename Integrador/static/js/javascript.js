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

/*'''$(document).ready(function(){

        var jsonArrObj=[{Quem Criou: "",Titulo: "",Data Termino: "",Status:"",Link:""}

        ];

        }
});


$("#tab_filter_btn").click(function(){
    current_index=1;
    start_index =1;
    displayIndexButtons();
})

function displayIndexButtons(){
    preLoadCalculations();
    $(".index_buttons button").remove();
    $(".index_buttons").append('<button onclick="prev();">Previous</button>');
    for(var i=1; i<=max_index;i++){
        $(".index_buttons").append('<button onclick="indexPagination('+i+')"index="'+i+'">'+i+'</button>');
    }
    $(".index_buttons").append('<button onclick="next();">Next</button>')
    highlightIndexButton();
}

function preLoadCalculations(){
    filterRankList();
    array=rankList;
    array_length = array.length;
    max_index = ParseInt(array_length/table_size);

    if((array_length%table_size)>0){
        max_index++;
    }


}

function filterRankList(){
    var tab_filter_text = $('@tab_filter_text').val();
    if(tab_filter_text != ''){
        var temp_array = rankList.filter(function(object){
            return object.rank.toString().includes(tab_filter_text);
        })
        array = temp_array;
    }else{
        array=rankList
    }

}*/