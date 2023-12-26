document.addEventListener("DOMContentLoaded", function () {
  const saveBtn = document.getElementById("saveBtn");

  function handleSave() {
    const formData = new FormData(document.querySelector("#businessname"));
    fetch("/businessname", {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        // Handle the response if needed
        if (response.ok) {
          console.log("Signal sent to Flask");
          window.location.replace("/business");
        }
      })
      .catch((error) => {
        console.error("Error sending signal to Flask:", error);
      });
    // window.location.replace("/business");
  }

  saveBtn.addEventListener("click", handleSave);
});
