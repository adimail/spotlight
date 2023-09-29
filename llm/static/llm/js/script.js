const openPopupButton = document.getElementById("open-popup");
const closePopupButton = document.getElementById("close-popup");
const popupContainer = document.getElementById("popup-container");

openPopupButton.addEventListener("click", () => {
    popupContainer.style.display = "flex";
});

closePopupButton.addEventListener("click", () => {
    popupContainer.style.display = "none";
});
