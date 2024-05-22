function validateForm() {
  var username = document.forms["form-sign-up"]["username"].value;
  var password = document.forms["form-sign-up"]["password"].value;
  var retypepassword = document.forms["form-sign-up"]["retypepassword"].value;
  var fullName = document.forms["form-sign-up"]["fullName"].value;
  var phone = document.forms["form-sign-up"]["phone"].value;
  var textError = document.querySelector("#error-message");
  if (
    username === "" ||
    password === "" ||
    retypepassword === "" ||
    fullName === "" ||
    phone === ""
  ) {
    textError.textContent = "Vui lòng điền đầy đủ thông tin vào các trường.";
    return false;
  }
  if (password != retypepassword) {
    textError.textContent = "Mật khẩu nhập lại không trùng.";
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
