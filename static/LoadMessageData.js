function LoadMessages()
{
      $.getJSON("http://127.0.0.1:8000/static/MessageData.json", function(json) {
            for (var i = 0; i < Object.keys(json.Messages).length; i++)
            {
                  var container = document.createElement("div");
                  document.body.appendChild(container);

                  var username = document.createElement("span");
                  container.appendChild(username);
                  username.style.color = "gray";
                  username.textContent = json.Messages[i].username + ": ";

                  var message = document.createElement("span");
                  container.appendChild(message);
                  message.style.color = "black";
                  message.textContent = json.Messages[i].message;
            }
      });
}

LoadMessages()