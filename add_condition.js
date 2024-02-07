function addCondition() {
    var conditionName = document.getElementById("conditionName").value;
    var subcategoryName = document.getElementById("subcategoryName").value;
    var subtypeName = document.getElementById("subtypeName").value;
  
    var newCondition = {
      name: conditionName,
      subcategories: [
        {
          name: subcategoryName,
          subtype: [{ name: subtypeName }]
        }
      ]
    };
  
    // Send the new condition data to the backend
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/add_condition", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify(newCondition));
  
    xhr.onload = function () {
      if (xhr.status == 200) {
        alert("Condition added successfully!");
      } else {
        alert("Error adding condition.");
      }
    };
  }
  