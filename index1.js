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
  xhr.send(JSON.stringify({ type: "union", content: [1, 2, 5] }));
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
const nodes = new vis.DataSet([
  { id: 1, label: "Node 1" },
  { id: 2, label: "Node 2" },
  { id: 3, label: "Node 3" },
  { id: 4, label: "Node 4" },
]);

// create an array with edges
const edges = new vis.DataSet([
  { from: 1, to: 2, label: "5" },
  { from: 2, to: 3, label: "4" },
  { from: 3, to: 4, label: "5" },
]);

// create a network
const container = document.getElementById("mynetwork");
const data = {
  nodes: nodes,
  edges: edges,
};
const options = {
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
const network = new vis.Network(container, data, options);

const sendGraphBtn = document.getElementById("sendGraph");
sendGraphBtn.addEventListener("click", () => {
  console.log("sendGraphBtn clicked");
  sendGraphBtn.classList.toggle("sending");
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "http://localhost:8080", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(JSON.stringify({ type: "apsp", content: edges.get() }));
  xhr.onload = () => {
    if (xhr.status === 200) {
      console.log(xhr.response);
      setTimeout(() => {}, 2000);
      // result.innerHTML = xhr.response;
      // result.className = "visible floating-div";
      sendGraphBtn.classList.remove("sending");
      sendGraphBtn.blur();
    }
  };
});
