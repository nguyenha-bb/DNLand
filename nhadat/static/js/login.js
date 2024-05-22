function validateForm() {
  var username = document.forms["form-login"]["username"].value;
  var password = document.forms["form-login"]["password"].value;
  var textError = document.querySelector("#error-message");
  if (username === "" || password === "") {
    textError.textContent = "Vui lòng điền đầy đủ thông tin vào các trường.";
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
