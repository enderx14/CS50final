// Handle artists input
document.addEventListener("DOMContentLoaded", function () {
  const artistEntries = document.getElementById("artistEntries");
  const addArtistBtn = document.getElementById("addArtistBtn");
  const removeArtistBtn = document.getElementById("removeArtistBtn");

  let artistCount = 0;
  function updateArtistCount() {
    const artistCountField = document.getElementById("artistCount");
    artistCountField.value = artistCount;
  }

  addArtistBtn.addEventListener("click", function () {
    artistCount++;
    updateArtistCount();
    const newInput1 = document.createElement("input");
    newInput1.setAttribute("name", `artist_name_${artistCount}`);
    newInput1.setAttribute("type", "text");
    newInput1.setAttribute("placeholder", "Enter artist name");
    newInput1.setAttribute("class", "form-control form-control-sm mb-2 mt-3");
    artistEntries.appendChild(newInput1);
    const newInput2 = document.createElement("input");
    newInput2.setAttribute("name", `artist_number_${artistCount}`);
    newInput2.setAttribute("type", "text");
    newInput2.setAttribute("placeholder", "Enter artist number");
    newInput2.setAttribute("class", "form-control form-control-sm mb-2");
    artistEntries.appendChild(newInput2);
  });

  removeArtistBtn.addEventListener("click", function () {
    if (artistCount > 0) {
      const lastInput1 = artistEntries.lastElementChild;
      artistEntries.removeChild(lastInput1);
      const lastInput2 = artistEntries.lastElementChild;
      artistEntries.removeChild(lastInput2);
      artistCount--;
      updateArtistCount();
    }
  });
});

// Handle schedules input
document.addEventListener("DOMContentLoaded", function () {
  const scheduleEntries = document.getElementById("scheduleEntries");
  const addScheduleBtn = document.getElementById("addScheduleBtn");
  const removeScheduleBtn = document.getElementById("removeScheduleBtn");

  let scheduleCount = 0;
  function updateScheduleCount() {
    const scheduleCountField = document.getElementById("scheduleCount");
    scheduleCountField.value = scheduleCount;
  }

  addScheduleBtn.addEventListener("click", function () {
    scheduleCount++;
    updateScheduleCount();
    const newInput = document.createElement("input");
    newInput.setAttribute("name", `schedule_${scheduleCount}`);
    newInput.setAttribute("type", "text");
    newInput.setAttribute("class", "form-control form-control-sm");
    newInput.setAttribute(
      "placeholder",
      "Enter Schedule like this 9AM - 12PM "
    );
    scheduleEntries.appendChild(newInput);
  });

  removeScheduleBtn.addEventListener("click", function () {
    if (scheduleCount > 0) {
      const lastInput = scheduleEntries.lastElementChild;
      scheduleEntries.removeChild(lastInput);
      scheduleCount--;
      updateScheduleCount();
    }
  });
});

// Handle packages input
document.addEventListener("DOMContentLoaded", function () {
  const packageEntries = document.getElementById("packageEntries");
  const addPackageBtn = document.getElementById("addPackageBtn");
  const removePackageBtn = document.getElementById("removePackageBtn");

  let packageCount = 0;
  function updatePackageCount() {
    const packageCountField = document.getElementById("packageCount");
    packageCountField.value = packageCount;
  }

  addPackageBtn.addEventListener("click", function () {
    packageCount++;
    updatePackageCount();
    const newInput1 = document.createElement("input");
    newInput1.setAttribute("name", `package_${packageCount}`);
    newInput1.setAttribute("type", "text");
    newInput1.setAttribute("placeholder", "Enter package name");
    newInput1.setAttribute("class", "form-control form-control-sm mb-2 mt-3");
    packageEntries.appendChild(newInput1);
    const newInput2 = document.createElement("input");
    newInput2.setAttribute("name", `package_detail_${packageCount}`);
    newInput2.setAttribute("type", "text");
    newInput2.setAttribute("placeholder", "Enter package details");
    newInput2.setAttribute("class", "form-control form-control-sm mb-2 mt-3");
    packageEntries.appendChild(newInput2);
  });

  removePackageBtn.addEventListener("click", function () {
    if (packageCount > 0) {
      const lastInput1 = packageEntries.lastElementChild;
      packageEntries.removeChild(lastInput1);
      const lastInput2 = packageEntries.lastElementChild;
      packageEntries.removeChild(lastInput2);
      packageCount--;
      updatePackageCount();
    }
  });
});

// Handle Event Type input
document.addEventListener("DOMContentLoaded", function () {
  const eventTypeEntries = document.getElementById("eventTypeEntries");
  const addEventTypeBtn = document.getElementById("addEventTypeBtn");
  const removeEventTypeBtn = document.getElementById("removeEventTypeBtn");

  let eventTypeCount = 0;
  function updateEventTypeCount() {
    const eventTypeCountField = document.getElementById("eventTypeCount");
    eventTypeCountField.value = eventTypeCount;
  }

  addEventTypeBtn.addEventListener("click", function () {
    eventTypeCount++;
    updateEventTypeCount();
    const newInput = document.createElement("input");
    newInput.setAttribute("name", `event_type_${eventTypeCount}`);
    newInput.setAttribute("type", "text");
    newInput.setAttribute("placeholder", "Enter Event Type name");
    newInput.setAttribute("class", "form-control form-control-sm mb-2 mt-3");
    eventTypeEntries.appendChild(newInput);
  });

  removeEventTypeBtn.addEventListener("click", function () {
    if (eventTypeCount > 0) {
      const lastInput = eventTypeEntries.lastElementChild;
      eventTypeEntries.removeChild(lastInput);
      eventTypeCount--;
      updateEventTypeCount();
    }
  });
});

// Handle Payment Methods input
document.addEventListener("DOMContentLoaded", function () {
  const paymentMethodEntries = document.getElementById("paymentMethodEntries");
  const addPaymentMethodBtn = document.getElementById("addPaymentMethodBtn");
  const removePaymentMethodBtn = document.getElementById(
    "removePaymentMethodBtn"
  );

  let paymentMethodCount = 0;
  function updatePaymentMethodCount() {
    const paymentMethodCountField =
      document.getElementById("paymentMethodCount");
    paymentMethodCountField.value = paymentMethodCount;
  }

  addPaymentMethodBtn.addEventListener("click", function () {
    paymentMethodCount++;
    updatePaymentMethodCount();
    const newInput = document.createElement("input");
    newInput.setAttribute("name", `payment_method_${paymentMethodCount}`);
    newInput.setAttribute("type", "text");
    newInput.setAttribute("placeholder", "Enter Payment Method name");
    newInput.setAttribute("class", "form-control form-control-sm mb-2 mt-3");
    paymentMethodEntries.appendChild(newInput);
  });

  removePaymentMethodBtn.addEventListener("click", function () {
    if (paymentMethodCount > 0) {
      const lastInput = paymentMethodEntries.lastElementChild;
      paymentMethodEntries.removeChild(lastInput);
      paymentMethodCount--;
      updatePaymentMethodCount();
    }
  });
});

// Function to display Multi-Step form and handle its input
document.addEventListener("DOMContentLoaded", function () {
  const formsdiv = document.getElementById("multi_forms");
  const forms = formsdiv.querySelectorAll("form");
  const prevBtn = document.getElementById("prevBtn");
  const nextBtn = document.getElementById("nextBtn");
  const saveBtns = document.querySelectorAll(".save-btn");
  let currentStep = 0;

  function showStep(step) {
    for (let i = 0; i < forms.length; i++) {
      forms[i].classList.remove("active-step");
    }
    forms[step].classList.add("active-step");
  }

  function handleNext() {
    if (currentStep < forms.length - 1) {
      currentStep++;
      showStep(currentStep);
    }
  }

  function handlePrev() {
    if (currentStep > 0) {
      currentStep--;
      showStep(currentStep);
    }
  }

  function handleSave() {
    // Perform AJAX request to save form data
    const activeStep = document.querySelector(".active-step");
    const url = `/${activeStep.id}`;
    if (activeStep) {
      const formData = new FormData(activeStep);
      fetch(url, {
        method: "POST",
        body: formData,
      })
        .then((response) => {
          if (response.ok) {
            console.log("Data from the active step saved successfully!");
            handleNext;
          } else {
            console.error("Failed to save data from the active step.");
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    } else {
      console.error("No active step form found.");
    }
  }

  nextBtn.addEventListener("click", handleNext);
  prevBtn.addEventListener("click", handlePrev);

  saveBtns.forEach((btn) => {
    btn.addEventListener("click", handleSave);
  });

  showStep(currentStep); // Show the initial step
});
