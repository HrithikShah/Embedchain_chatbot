
// we get BOT resposne with this function


function getBotResponse() 
{
    //  here we put our query to bot to get response
    var rawText = $("#textInput").val();
    var userHtml = '<p class="userText"><span>' + rawText + "</span></p>";
    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document
      .getElementById("userInput")
      .scrollIntoView({ block: "start", behavior: "smooth" }); // this give scrolling effect to our chat.

    //  we get bot response for the query and show it on bothtml or on bot side

    $.get("/get", { msg: rawText }).done(function(data)
     {
      var botHtml = '<p class="botText"><span>' + data + "</span></p>";
      $("#chatbox").append(botHtml);
      document
        .getElementById("userInput")
        .scrollIntoView({ block: "start", behavior: "smooth" });
    });
  }

 