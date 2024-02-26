// Function to verify the grammar
function verifyGrammar(text) {
    axios.post('http://localhost:5000/grammar', { text })
    .then((response) => {
      return response.data.edited_text === text;
    })
    .catch((error) => {
      console.error(error.message);
      return false;
    });

    return false;
}

// Event listener for text input
document.addEventListener("input", function(event) {
  const text = event.target.value;
  const isGrammarCorrect = verifyGrammar(text);
  
  if (isGrammarCorrect) {
    console.log("Grammar is correct");
  } else {
    console.log("Grammar is incorrect");
  }
});
