const result = document.getElementById("data-div");

document
  .querySelector("#sendDefaultData")
  .addEventListener("click", function (e) {
    var but = document.querySelector("#sendDefaultData");
    but.classList.toggle("sending");
    but.blur();
    // send a POST request to the server
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "http://localhost:8081", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify({ type: "union", content: [1, 2, 3] }));
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

document.querySelector("#unionData").addEventListener("click", function (e) {
  var but = document.querySelector("#unionData");
  but.classList.toggle("sending");
  but.blur();
  // send a POST request to the server
  let message = document.querySelector("#union_message").value;
  console.log("message: ", message);
  message = message
    .split(",")
    .map((x) => parseInt(x))
    .sort((a, b) => a - b);
  console.log(message);
  console.log(typeof message);

  const xhr = new XMLHttpRequest();
  xhr.open("POST", "http://localhost:8081", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(JSON.stringify({ type: "union", content: message }));
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

// create an array with nodes
var nodes = new vis.DataSet([
  { id: 1, label: "Node 1" },
  { id: 2, label: "Node 2" },
  { id: 3, label: "Node 3" },
  { id: 4, label: "Node 4" },
]);

// create an array with edges
var edges = new vis.DataSet([
  { from: 1, to: 2, label: "10" },
  { from: 1, to: 3, label: "4" },
  { from: 3, to: 4, label: "10" },
]);

// create a network
var container = document.getElementById("mynetwork");
var data = {
  nodes: nodes,
  edges: edges,
};
var options = {
  edges: {
    arrows: {
      to: { enabled: true, scaleFactor: 0.75, type: "arrow" },
    },
    color: "black",
    font: {
      align: "middle",
    },
    smooth: false,
  },
};
var network = new vis.Network(container, data, options);


