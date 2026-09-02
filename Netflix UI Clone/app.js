// DOM ELEMENTS
const faqItems = document.querySelectorAll(".faq");

// EVENT LISTENER
for (let i = 0; i < faqItems.length; i++) {
    faqItems[i].addEventListener("click", function() {
        toggleFAQ(faqItems[i]);
    });
}

// FUNCTIONS
function toggleFAQ(faqEl) {
    // Toggle "open" class on the clicked faq item for icon change
    faqEl.classList.toggle("open");

    // Find the answer container which is the next sibling element
    const answer = faqEl.nextElementSibling;

    if (answer) {
        // Check if it's already open (using max-height)
        if (answer.style.maxHeight && answer.style.maxHeight !== "0px") {
            answer.style.maxHeight = null;
            answer.style.opacity = 0;
            answer.style.display = "none";
        } else {
            answer.style.display = "block";
            answer.style.maxHeight = answer.scrollHeight + "px";
            answer.style.opacity = 1;
        }
    }
}