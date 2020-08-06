var current = 0;


function LoadMessages()
{
      console.log("Hello World!");
      $.getJSON("http://127.0.0.1:8000/static/MessageData.json", function(json) {
            const messageList = json.Messages.reverse();

            if (json.Messages[0])
            {
                  if (current != messageList[0].id)
                  {
                        for (var i = 0; i < Object.keys(messageList).length; i++)
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
                        current = messageList[0].id;
                  }
            }
            

            if (current == 0)
            {
                  if (json.Messages[0])
                  {
                        current = messageList[0].id;
                  }
            }
      });
}

LoadMessages();

function PageReload() {
      setInterval(function()
      {
            LoadMessages()
      }, 5000);
}

PageReload();