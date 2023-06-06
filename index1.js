const result = document.getElementById("data-div");

document.querySelector("form").addEventListener("submit", function (e) {
  e.preventDefault();

  var but = this.querySelector('[type="submit"]');
  but.classList.toggle("sending");
  but.blur();
  // send a POST request to the server
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "http://localhost:8080", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(JSON.stringify([1, 2, 5]));
  xhr.onload = () => {
    if (xhr.status === 200) {
      console.log(xhr.response);
      setTimeout(() => {}, 2000);
      result.innerHTML = xhr.response;
      result.className = "visible floating-div";
      but.classList.remove("sending");
      but.blur();
    }
  };
});
