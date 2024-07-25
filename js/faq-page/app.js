const questions = [
    "What is your return policy?",
    "How can I track my order?",
    "What payment methods do you accept?"
];

const answers = [
    "Our return policy allows you to return most items within 30 days of purchase for a full refund or exchange. To be eligible for a return, items must be unused and in the same condition that you received them. They must also be in the original packaging. To start a return, please contact our customer service team with your order number and reason for return. We will provide you with a return shipping label and instructions on how to send your item back to us.",
    "To track your order, log in to your account on our website and go to the 'My Orders' section. Click on the order you want to track, and you will find the tracking number along with the shipping carrier's website. You can also track your order by entering the tracking number directly on the carrier's website. If you have any issues tracking your order, please contact our customer service team for assistance.",
    "We accept a variety of payment methods for your convenience. These include major credit cards such as Visa, MasterCard, American Express, and Discover. We also accept payments through PayPal, Apple Pay, and Google Pay. If you prefer, you can use bank transfers or purchase with store gift cards. Please note that the available payment methods may vary depending on your location."
];

const questionsList = document.getElementById("questions");

questions.forEach((question, index) => {
    const li = document.createElement("li");
    li.setAttribute("class", "question");
    const questionId = "question-" + index;
    li.setAttribute("id", questionId);
    li.appendChild(document.createTextNode(question));
    questionsList.appendChild(li);
    
    const div = document.createElement("div");
    div.setAttribute("class", "answer");
    div.appendChild(document.createTextNode(answers[index]));
    li.appendChild(div);
    
    li.addEventListener('click', toggleChild);
});

function toggleChild(event) {
    const answerDiv = event.currentTarget.querySelector(".answer");
    if (answerDiv.style.display === "none"){
        answerDiv.style.display = "block";
    } else {
        answerDiv.style.display = "none";
    }
}

document.querySelectorAll(".answer").forEach(answer => {
    answer.style.display = "none";
});