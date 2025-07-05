// gets the first element in the document that matches this
const subs = document.querySelector(".bi-substack");

const isAnimating = subs.classList.contains("animating");

subs.addEventListener("mouseenter", () => {
  if (!isAnimating) {
    subs.classList.add("animating");
    subs.classList.add("animated-substack");
  }
});

// listens for when the animation ends
subs.addEventListener("animationend", () => {
  subs.classList.remove("animated-substack");
  subs.classList.remove("animating");
});
