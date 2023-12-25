document.addEventListener("DOMContentLoaded", function () {
  const businessForm = document.getElementById("businessForm");
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

document.addEventListener("DOMContentLoaded", function () {
  const businessForm = document.getElementById("businessForm");
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
    const newInput = document.createElement("input");
    newInput.setAttribute("name", `package_${packageCount}`);
    newInput.setAttribute("type", "text");
    newInput.setAttribute("placeholder", "Enter package name");
    newInput.setAttribute("class", "form-control form-control-sm mb-2 mt-3");
    packageEntries.appendChild(newInput);
  });

  removePackageBtn.addEventListener("click", function () {
    if (packageCount > 0) {
      const lastInput = packageEntries.lastElementChild;
      packageEntries.removeChild(lastInput);
      packageCount--;
      updatePackageCount();
    }
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("multiStepForm");
  const fieldsets = form.querySelectorAll("fieldset");
  const prevBtn = document.getElementById("prevBtn");
  const nextBtn = document.getElementById("nextBtn");
  const saveBtns = document.querySelectorAll(".save-btn");
  let currentStep = 0;

  function showStep(step) {
    for (let i = 0; i < fieldsets.length; i++) {
      fieldsets[i].classList.remove("active-step");
    }
    fieldsets[step].classList.add("active-step");
  }

  function handleNext() {
    if (currentStep < fieldsets.length - 1) {
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
    const formData = new FormData(form);
    fetch("/new_business", {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        if (response.ok) {
          console.log("Data saved successfully!");
        } else {
          console.error("Failed to save data.");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }

  nextBtn.addEventListener("click", handleNext);
  prevBtn.addEventListener("click", handlePrev);

  saveBtns.forEach((btn) => {
    btn.addEventListener("click", handleSave);
  });

  showStep(currentStep); // Show the initial step
});
