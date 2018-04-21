for(i=0;i<10;i++){
    var btn = document.createElement("BUTTON");  // Create a <button> element
     
    var t = document.createTextNode("my number is "+i);  // Create a text node
     
    btn.appendChild(t);  // Append the text to <button>
    document.body.appendChild(btn); 
}