const deleteModal = document.getElementById("deleteModal");
if (deleteModal) {
  deleteModal.addEventListener("show.bs.modal", (event) => {
    const button = event.relatedTarget;
    const id = button.getAttribute("data-bs-id");
    const modalBodyId = deleteModal
      .querySelector(".modal-footer")
      .querySelector("#artistid");

    modalBodyId.value = id;

    const deleteForm = deleteModal.querySelector("form"); // Assuming there's only one form in the modal
    deleteForm.addEventListener("submit", (e) => {
      e.preventDefault(); // Prevent the default form submission
      const artistIdValue = modalBodyId.value;
      // const actionUrl =
      //   "{{ url_for('delete_artist', artist_id='') }}" + artistIdValue;
      deleteForm.action = `artist/${artistIdValue}/delete`; // Set the form action dynamically
      deleteForm.method = "POST";
      deleteForm.submit(); // Submit the form with the updated action
    });
  });
}
