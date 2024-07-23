const buttonIncrease = document.getElementById("increase-btn");
const buttonDecrease = document.getElementById("decrease-btn");
const buttonReset = document.getElementById("reset-btn");

const counterContainer = document.getElementById("counter-container");

const increaseCounter = function() {
    const currentCount = Number(counterContainer.innerText);
    const newCount = currentCount + 1;
    counterContainer.innerText = newCount;
}

const decreaseCounter = function() {
    const currentCount = Number(counterContainer.innerText);
    const newCount = currentCount - 1;
    counterContainer.innerText = newCount;
}

const resetCounter = function() {
    const newCount = 0;
    counterContainer.innerText = newCount;
}

buttonIncrease.addEventListener('click', increaseCounter);
buttonDecrease.addEventListener('click', decreaseCounter);
buttonReset.addEventListener('click', resetCounter);