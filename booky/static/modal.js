const deleteModal = document.getElementById("deleteModal");
if (deleteModal) {
  deleteModal.addEventListener("show.bs.modal", (event) => {
    // Button that triggered the modal
    const button = event.relatedTarget;
    // Extract info from data-bs-* attributes
    const id = button.getAttribute("data-bs-id");
    // If necessary, you could initiate an Ajax request here
    // and then do the updating in a callback.

    // Update the modal's content.
    const modalBodyId = deleteModal.querySelector(".modal-body #artistid");

    // modalTitle.textContent = `New message to ${recipient}`;
    artistId = id;
    modalBodyId.value = id;
    // fetch(`/artist/${artistId}/delete`, {
    //   method: "GET", // or 'POST' based on your server route
    // })
    //   .then((response) => response.text())
    //   .catch((error) => {
    //     console.error("Error:", error);
    //   });
  });
}
