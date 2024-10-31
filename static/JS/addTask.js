// * I followed a tutorial on how to make this, I commented on what each code is doing 

// Get all list items (LI) in the document
var myNodelist = document.getElementsByTagName("LI"); 
var i; // Loop variable

// Add a close button to each list item
for (i = 0; i < myNodelist.length; i++) {
  var span = document.createElement("SPAN"); // Create a span for the close button
  var txt = document.createTextNode("\u00D7"); // Create a "×" text node
  span.className = "close"; // Set the class name for styling
  span.appendChild(txt); // Add the text to the span
  myNodelist[i].appendChild(span); // Attach the span to the list item
}

// Get all close buttons
var close = document.getElementsByClassName("close"); 
var i; // Loop variable

// Set up click event for each close button
for (i = 0; i < close.length; i++) {
  close[i].onclick = function() { // When the button is clicked
    var div = this.parentElement; // Get the parent list item
    div.style.display = "none"; // Hide the list item
  }
}

// Get the unordered list (UL)
var list = document.querySelector('ul'); 

// Add click event to the list for checking items
list.addEventListener('click', function(ev) {
  if (ev.target.tagName === 'LI') { // If a list item is clicked
    ev.target.classList.toggle('checked'); // Toggle the 'checked' class
  }
}, false); // Use event bubbling (false)

// Function to add a new list item when the "Add" button is clicked
function newElement() {
  var li = document.createElement("li"); // Create a new list item
  var inputValue = document.getElementById("myInput").value; // Get input value
  var t = document.createTextNode(inputValue); // Create a text node from input
  li.appendChild(t); // Add the text to the new list item
  if (inputValue === '') { // If input is empty
    alert("You must write something!"); // Show alert
  } else {
    document.getElementById("myUL").appendChild(li); // Add the new item to the list
  }
  document.getElementById("myInput").value = ""; // Clear the input field

  var span = document.createElement("SPAN"); // Create a new close button
  var txt = document.createTextNode("\u00D7"); // Create a "×" text node
  span.className = "close"; // Set the class name for styling
  span.appendChild(txt); // Add the text to the span
  li.appendChild(span); // Attach the span to the new list item

  // Set up click event for new close buttons
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() { // When the button is clicked
      var div = this.parentElement; // Get the parent list item
      div.style.display = "none"; // Hide the list item
    }
  }
}
