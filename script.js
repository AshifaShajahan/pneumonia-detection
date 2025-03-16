document.getElementById("fileInput").addEventListener("change", function () {
    let file = this.files[0];
    if (!file) return;

    let formData = new FormData();
    formData.append("file", file);

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        alert("Prediction: " + data.prediction);
    })
    .catch(error => {
        console.error("Error:", error);
    });
});
