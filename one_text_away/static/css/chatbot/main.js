var i = 0;
var choice;
var score = 0;

function getResponse() {
    var userText = $('#textInput').val();
    var userHTML = "<p class='userText'>User: <span>" + userText + "</span></p>";
    $('#textInput').val("");
    $('#chatbot').append(userHTML);
    
    if(i==0) {
        choice = userText;
    }
    
    if (choice == 'stress') {
        if (userText == 'never') {
            if(i==5 || i==6 || i==8 || i==9)
                score += 4;
            else
                score += 0;
        }
        else if (userText == 'almost never') {
            if(i==5 || i==6 || i==8 || i==9)
                score += 3;
            else
                score += 1;
        }
        else if ( userText == 'sometimes') {
            if(i==5 || i==6 || i==8 || i==9)
                score += 2;
            else
                score += 2;
        }
        else if (userText == 'fairly often') {
            if(i==5 || i==6 || i==8 || i==9)
                score += 1;
            else
                score += 3;
        }
        else if (userText == 'very often') {
            if(i==5 || i==6 || i==8 || i==9)
                score += 0;
            else
                score += 4;
        }
    }

    if(choice == 'anxiety') {
        if (userText == 'never') {
                score += 4;
        }
        else if (userText == 'almost never') {
                score += 3;
        }
        else if ( userText == 'sometimes') {
                score += 2;
        }
        else if (userText == 'fairly often') {
                score += 1;
        }
        else if (userText == 'very often') {
                score += 0;
        }
    }
    
    $.get('/chatbot/getResponse', {userMessage:userText, loopVariable:i, choice:choice, score:score}).done(function(data){
        var returnedMessage = "<p class='botText'>Chatbot: <span>"+ data +"</span></p>";
        $('#chatbot').append(returnedMessage);
    })
    i = i + 1;

}

$('#buttonInput').click(function() {
    getResponse();
    var myDiv = document.getElementById("chatbot");
    myDiv.scrollTop = myDiv.scrollHeight;
})