contentdiv = document.getElementById("markdownfilecontent");

fetch("markdownfilepath")
  .then((response) => response.text())
  .then((markdown) => {
    // set the div with id content to marked.parse
    contentdiv.innerHTML = marked.parse(markdown);
  })
  .catch((error) => {
    contentdiv.innerText =
      "Failed to load markdown content probably file paths off";
    console.error(error);
  });
