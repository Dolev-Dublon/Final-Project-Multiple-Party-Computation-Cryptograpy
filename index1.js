const result = document.getElementById("data-div");

document
  .querySelector("#sendDefaultData")
  .addEventListener("click", function (e) {
    var but = document.querySelector("#sendDefaultData");
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
  xhr.open("POST", "http://localhost:8080", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(JSON.stringify({ type: "union", content: message }));
  xhr.onload = () => {
    if (xhr.status === 200) {
      console.log(xhr.response);
      result.innerHTML = xhr.response;
      result.className = "visible floating-div";
      but.classList.remove("sending");
      but.blur();
    }
  };
});

const networkResultContainer = document.getElementById("mynetworkresult");

const sendGraphBtn = document
  .querySelector("#sendGraph")
  .addEventListener("click", function (e) {
    console.log("sendGraphBtn clicked");
    const sendGraphBtn = document.querySelector("#sendGraph");
    sendGraphBtn.classList.toggle("sending");
    const edgesData = Object.entries(network.body.edges).map((edge) => {
      console.log("edge : ", edge);
      return {
        fromId: edge[1].fromId,
        toId: edge[1].toId,
        label: parseInt(edge[1].labelModule.elementOptions.label),
      };
    });
    console.log("edgesData : ", edgesData);

    const xhr = new XMLHttpRequest();
    xhr.open("POST", "http://localhost:8080", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify({ type: "apsp", content: edgesData }));
    xhr.onload = () => {
      if (xhr.status === 200) {
        console.log(xhr.response);
        sendGraphBtn.classList.remove("sending");
        sendGraphBtn.blur();

        const responseData = JSON.parse(xhr.response);
        let responseEdges = responseData.map((edge) => ({
          from: edge.fromId,
          to: edge.toId,
          label: String(edge.label),
        }));
        let responseNodes = [];
        responseData.forEach((edge) => {
          responseNodes.push({ id: edge.fromId, label: "Node " + edge.fromId });
          responseNodes.push({ id: edge.toId, label: "Node " + edge.toId });
        });

        // Remove duplicate nodes
        responseNodes = responseNodes.filter(
          (node, index, self) =>
            index === self.findIndex((n) => n.id === node.id)
        );

        const responseNetworkData = {
          nodes: new vis.DataSet(responseNodes),
          edges: new vis.DataSet(responseEdges),
        };
        const options = {
          nodes: {
            color: {
              background: "#ff80ff",
              border: "#ffccff",
            },
          },
        };
        new vis.Network(networkResultContainer, responseNetworkData, options);
      }
    };
  });

var nodesArray = [
  { id: 1, label: "Node 1" },
  { id: 2, label: "Node 2" },
  { id: 3, label: "Node 3" },
];
var edgesArray = [
  { from: 1, to: 2, label: "5" }, // weight 5
  { from: 1, to: 3, label: "3" }, // weight 3
];
var nodes = new vis.DataSet(nodesArray);
var edges = new vis.DataSet(edgesArray);

var container = document.getElementById("mynetwork");
var data = {
  nodes: nodes,
  edges: edges,
};
var options = {
  nodes: {
    color: {
      background: "#ffcccc",
      border: "#ff0000",
    },
  },
};
var network = new vis.Network(container, data, options);

var lastClickedNodes = [];

network.on("click", function (params) {
  if (params.nodes.length > 0) {
    lastClickedNodes.unshift(params.nodes[0]);
    if (lastClickedNodes.length > 2) {
      lastClickedNodes.pop();
    }
  }
});

function addNode() {
  var newNodeId = nodesArray.length + 1;
  var newNode = { id: newNodeId, label: "Node " + newNodeId };
  nodesArray.push(newNode);
  nodes.add(newNode);
}

function addEdge() {
  if (nodesArray.length > 1) {
    var fromNode, toNode;
    if (lastClickedNodes.length >= 2) {
      fromNode = lastClickedNodes[0];
      toNode = lastClickedNodes[1];
    } else {
      fromNode = nodesArray.length;
      toNode = nodesArray.length - 1;
    }
    var weight = prompt("Please enter the weight for the edge", "1");

    if (weight !== null) {
      var newEdge = {
        from: fromNode,
        to: toNode,
        label: weight,
      };
      edgesArray.push(newEdge);
      edges.add(newEdge);
    }
  }
}

function removeNode() {
  if (lastClickedNodes.length > 0) {
    // Remove associated edges
    var nodeId = lastClickedNodes[0];
    var associatedEdges = edges.get({
      filter: function (edge) {
        return edge.from === nodeId || edge.to === nodeId;
      },
    });
    associatedEdges.forEach(function (edge) {
      edges.remove(edge.id);
    });

    // Remove the node
    nodes.remove(nodeId);

    // Update nodesArray
    nodesArray = nodesArray.filter((node) => node.id !== nodeId);

    // Remove the node from the lastClickedNodes array
    lastClickedNodes = lastClickedNodes.filter((node) => node !== nodeId);
  }
}

function removeEdge() {
  if (edgesArray.length > 0) {
    // Remove the last edge from the edges DataSet
    var lastEdge = edgesArray[edgesArray.length - 1];
    edges.remove(lastEdge.id);

    // Update the edgesArray
    edgesArray.pop();
  }
}
