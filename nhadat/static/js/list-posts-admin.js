function validateForm() {
  var oldPassword = document.forms["form-change-password"]["oldPassword"].value;
  var newPassword = document.forms["form-change-password"]["newPassword"].value;
  var newPasswordAgain =
    document.forms["form-change-password"]["newPasswordAgain"].value;
  var textError = document.querySelector("#error-message");
  if (oldPassword === "" || newPassword === "" || newPasswordAgain === "") {
    textError.textContent =
      "Vui lòng điền đầy đủ thông tin vào các trường mật khẩu.";
    return false;
  }

  return true;
}

function clearErrorMessage() {
  document.querySelector("#error-message").textContent = "";
}

function togglePasswordVisibility(inputId) {
  const passwordInput = document.getElementById(inputId);
  const togglePassword = passwordInput.nextElementSibling;

  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    togglePassword.innerHTML = '<i class="fas fa-eye"></i>';
  } else {
    passwordInput.type = "password";
    togglePassword.innerHTML = '<i class="fas fa-eye-slash"></i>';
  }
}

const disableBtn = document.querySelectorAll(".disable-btn");
for (var i = 0; i < disableBtn.length; i++) {
  const disableTagA = disableBtn[i].querySelector("a");
  disableTagA.onclick = function (e) {
    e.preventDefault();
  };
}
