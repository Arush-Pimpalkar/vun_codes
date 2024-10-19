const userInput = "<script>alert('XSS')</script>";
document.getElementById('output').innerHTML = userInput;
