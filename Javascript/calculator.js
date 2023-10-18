var screen = document.getElementById("screen");

function addToDisplay(value) {
  var calculatorValue = screen.value;
  var operatorSign = ["+", "-", "%", "/", "*"];
  var last = calculatorValue[calculatorValue.length - 1];
  var newInput = value;

  if (
    operatorSign.indexOf(last) !== -1 &&
    operatorSign.indexOf(newInput) !== -1
  ) {
    calculatorValue = calculatorValue.slice(0, -1) + newInput;
  } else {
    calculatorValue += newInput;
  }

  screen.value = calculatorValue;
}

function clearScreen() {
  document.getElementById("screen").value = "";
}
function singleDelete() {
  var inputElement = document.getElementById("screen");
  var inputValue = inputElement.value;
  if (inputValue.length > 0) {
    var updatedValue = inputValue.slice(0, -1);
    inputElement.value = updatedValue;
  }
}

function calculate() {
  if (screen.value !== "") {
    var result = eval(document.getElementById("screen").value);
    document.getElementById("screen").value = result;
  }
}
