var deleteList = document.querySelectorAll(".delete-post");
for (let i = 0; i < deleteList.length; i++) {
  deleteList[i].onclick = function (event) {
    event.preventDefault();
    console.log(deleteList[i].href);
    document.getElementById("id01").style.display = "block";

    const form = document.querySelector(".modal-content");
    var modal = document.getElementById("id01");
    console.log(form);
    window.onclick = function (event) {
      if (event.target == modal) {
        closeModal();
      }
    };

    var cancel = document.getElementById("cancelBtn");
    cancel.addEventListener("click", (event) => {
      event.stopPropagation();
      closeModal();
    });

    var ok = document.getElementById("okBtn");
    ok.addEventListener("click", (event) => {
      event.stopPropagation();
      form.method = "POST";
      form.action = deleteList[i].href;
      form.submit();
    });

    function closeModal() {
      modal.classList.add("fade-out");
      setTimeout(function () {
        modal.style.display = "none";
        modal.classList.remove("fade-out");
      }, 500);
    }
  };
}

const disableBtn = document.querySelectorAll(".disable-btn");
for (var i = 0; i < disableBtn.length; i++) {
  const disableTagA = disableBtn[i].querySelector("a");
  disableTagA.onclick = function (e) {
    e.preventDefault();
  };
}
