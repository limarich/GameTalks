document.addEventListener("DOMContentLoaded", function () {
  const statisticsContainer = document.querySelector("#statistics-container");
  const formsContainer = document.querySelector("#forms-container");
  const userHasProfile = document.querySelector("#userHasProfile").value;
  const editBtn = document.querySelector("#user-edit");

  console.log(userHasProfile);

  if (userHasProfile === "True") {
    statisticsContainer.style.display = "flex";
    formsContainer.style.display = "none";
  } else {
    statisticsContainer.style.display = "none";
    formsContainer.style.display = "flex";
  }

  editBtn.addEventListener("click", () => {
    if (statisticsContainer.style.display === "flex") {
      statisticsContainer.style.display = "none";
      formsContainer.style.display = "flex";
    } else {
      statisticsContainer.style.display = "flex";
      formsContainer.style.display = "none";
    }
  });
});
