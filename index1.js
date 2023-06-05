const SubmitButton = document.querySelector("#SubmitList");
const ListInput = document.querySelector("#ListInput");
const result = document.querySelector("#result");

// add event listener to the ListInput on input change so when it has input the submit button is no longer disabled
ListInput.addEventListener("input", () => {
  if (ListInput.value.trim() !== "") {
    // Check if input is not empty
    SubmitButton.disabled = false;
  } else {
    SubmitButton.disabled = true;
  }
});

SubmitButton.addEventListener("click", () => {
  SubmitButton.style.color = "blue";
  SubmitButton.style.backgroundColor = "red";
  // get the value of the input
  const ListInputValue = ListInput.value;
  // the value is a string of 1,2,3 seperated by comma so we need to convert it to an array
  const ListInputValueArray = ListInputValue.split(",");
  // we need to convert the array of strings to an array of numbers
  const ListInputValueArrayNumbers = ListInputValueArray.map((item) => {
    return parseInt(item);
  });
  // we need to sort the array of numbers
  const ListInputValueArrayNumbersSorted = ListInputValueArrayNumbers.sort(
    (a, b) => {
      return a - b;
    }
  );
  // send a POST request to the server
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "http://localhost:8080", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(JSON.stringify(ListInputValueArrayNumbersSorted));
  xhr.onload = () => {
    if (xhr.status === 200) {
      console.log(xhr.response);
      result.innerHTML = xhr.response;
    }
  };
});
