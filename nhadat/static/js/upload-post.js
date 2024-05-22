function updateFormattedPrice() {
  document.querySelector("#error-message").textContent = "";
  var inputElement = document.getElementById("id_price");
  var inputValue = inputElement.value.trim();

  if (/^\d+$/.test(inputValue)) {
    var numericValue = parseFloat(inputValue);

    if (!isNaN(numericValue)) {
      var formattedPrice = formatPrice(numericValue);
      document.getElementById("formattedPrice").innerText =
        "Giá: " + formattedPrice;
    } else {
      document.getElementById("formattedPrice").innerText =
        "Vui lòng nhập số tiền hợp lệ.";
    }
  } else {
    document.getElementById("formattedPrice").innerText =
      "Vui lòng nhập số tiền hợp lệ.";
  }
}

function formatPrice(price) {
  if (price < 1000000) {
    return price.toLocaleString() + " VNĐ";
  } else if (price < 1000000000) {
    var million = (price / 1000000)
      .toLocaleString(undefined, {
        minimumFractionDigits: 6,
        maximumFractionDigits: 6,
      })
      .replace(/\.?0+$/, "");
    return million + " triệu VNĐ";
  } else {
    var billion = (price / 1000000000)
      .toLocaleString(undefined, {
        minimumFractionDigits: 6,
        maximumFractionDigits: 6,
      })
      .replace(/\.?0+$/, "");
    return billion + " tỷ VNĐ";
  }
}

//------------

function validateForm() {
  var title = document.forms["form-upload"]["title"].value;
  var price = document.forms["form-upload"]["price"].value;
  var area = document.forms["form-upload"]["area"].value;
  var direction = document.forms["form-upload"]["direction"].value;
  var district = document.forms["form-upload"]["district"].value;
  var commune = document.forms["form-upload"]["commune"].value;
  var address = document.forms["form-upload"]["address"].value;
  var description = document.forms["form-upload"]["description"].value;
  var image = document.forms["form-upload"]["image"].value;
  var textError = document.querySelector("#error-message");

  if (
    title === "" ||
    price === "" ||
    area === "" ||
    direction === "0" ||
    district === "0" ||
    commune === "0" ||
    address === "" ||
    description === "" ||
    image === ""
  ) {
    textError.textContent = "Vui lòng điền đầy đủ thông tin vào các trường.";
    return false;
  }

  var numericValue = parseFloat(price);
  if (isNaN(numericValue) || numericValue <= 0 || /\D/.test(price)) {
    textError.textContent = "Vui lòng nhập giá tiền hợp lệ.";
    return false;
  }

  return true;
}

function clearErrorMessage() {
  document.querySelector("#error-message").textContent = "";
}

function previewImage() {
  var fileInput = document.getElementById("id_image");
  var imagePreview = document.getElementById("myImagePreview");

  // Kiểm tra nếu người dùng đã chọn ảnh
  if (fileInput.files && fileInput.files[0]) {
    var reader = new FileReader();

    // Đọc nội dung của file ảnh
    reader.onload = function (e) {
      imagePreview.src = e.target.result;
    };
    // Đặt file ảnh cho FileReader đọc
    reader.readAsDataURL(fileInput.files[0]);
    document.querySelector(".fa-image").style.display = "none";
    clearErrorMessage();
  }
}

// function getlistCommune() {
//   var district = document.forms["form-upload"]["district"].value;
//   console.log(district);
//   var xhr = new XMLHttpRequest();
//   xhr.open("POST", "C_Commune?action=getListByDistrict&id=" + district, true);
//   xhr.onload = function () {
//     if (xhr.status === 200) {
//       let data = JSON.parse(xhr.responseText);
//       var select = document.getElementById("commune");
//       var html = '<option value="0">- Chọn Phường/Xã -</option>';
//       data.forEach((commune) => {
//         html +=
//           '<option value="' +
//           commune.idCommune +
//           '">' +
//           commune.nameCommune +
//           "</option>";
//       });
//       select.innerHTML = html;
//     }
//   };
//   xhr.send();
// }

function loadDistricts(provinceId) {
  fetch(`load-districts?province_id=${provinceId}`)
    .then((response) => response.json())
    .then((data) => {
      const districtSelect = document.getElementById("id_district");
      districtSelect.innerHTML = '<option value="">---------</option>';
      data.forEach((district) => {
        const option = document.createElement("option");
        option.value = district.id;
        option.textContent = district.districtName;
        districtSelect.appendChild(option);
      });

      // Clear wards select
      const wardSelect = document.getElementById("id_ward");
      wardSelect.innerHTML = '<option value="">---------</option>';
    });
}

function loadWards(districtId) {
  fetch(`load-wards?district_id=${districtId}`)
    .then((response) => response.json())
    .then((data) => {
      const wardSelect = document.getElementById("id_ward");
      wardSelect.innerHTML = '<option value="">---------</option>';
      data.forEach((ward) => {
        const option = document.createElement("option");
        option.value = ward.id;
        option.textContent = ward.wardName;
        wardSelect.appendChild(option);
      });
    });
}
