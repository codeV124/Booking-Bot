var timerInterval_message;
var timerInterval_server_time;

function start(book_mode) {
    $.ajax({
        url: '/status', // Replace with the actual URL to your backend endpoint
        method: "GET",
        success: function(response) {
            console.log(response)
            if (response == "stopped"){
                startTimer_message()
                startTimer_server_time()
                $("input, textarea, select").not(this).prop("disabled", true);

                var date_time = document.getElementById('date_time').value;
                var trans = document.getElementById('trans').value;
                var whom = document.getElementById('whom').value;
                var event = document.getElementById('event').value;
                
                fetch('/start', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({date_time, trans, whom, event, book_mode})
                })
                .then(response => {
                    if (response.ok) {
                        console.log('Script executed successfully!');
                    } else {
                        console.error('Error executing script!');
                    }
                })
                .catch(error => {
                    console.error('Error executing script:', error);
                });
                }
        },
        error: function(xhr, status, error) {
        console.log("Error:", error);
        }
    });
}

function stop(){
    clearInterval(timerInterval_message);
    clearInterval(timerInterval_server_time);
    $("#mitiDesc").html('');
    $("input, textarea, select").not(this).prop("disabled", false);
    fetch('/stop', {
        method: 'POST'
      })
      .then(response => response.text())
      .then(data => {
        console.log(data); // Variable updated successfully
      })
      .catch(error => {
        console.error('Error:', error);
      });
}

function startTimer_server_time() {
    timerInterval_server_time = setInterval(fetchData, 100); // Fetch data every 1 second
    function fetchData() {
    // Make an AJAX request to fetch data from the server
    $.ajax({
        url: '/time', // Replace with the actual URL to your backend endpoint
        method: "GET",
        success: function(response) {
        // Update the HTML container with the fetched data
        $("#server_time").html(response);
        },
        error: function(xhr, status, error) {
        console.log("Error:", error);
        }
    });
    }
};

function startTimer_message() {
    fetch('/clear', {
        method: 'POST'
      })
      .then(response => response.text())
      .then(data => {
        console.log(data); // Variable updated successfully
      })
      .catch(error => {
        console.error('Error:', error);
      });

    timerInterval_message = setInterval(fetchData, 500); // Fetch data every 1 second
    function fetchData() {
    // Make an AJAX request to fetch data from the server
    $.ajax({
        url: '/message', // Replace with the actual URL to your backend endpoint
        method: "GET",
        success: function(response) {
        // Update the HTML container with the fetched data
        $("#mitiDesc").html(response);
        if (response.includes("Done")){
            clearInterval(timerInterval_message);
            $("input, textarea, select").not(this).prop("disabled", false);
        }
        if (response.includes("started")){
            clearInterval(timerInterval_server_time);
        }
        },
        error: function(xhr, status, error) {
        console.log("Error:", error);
        }
    });
    }
}
