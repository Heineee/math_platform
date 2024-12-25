document.getElementById("loader").style.display = "none";

const check_register = document.getElementById("check-error");
const check_login = document.getElementById("login-error");
let login = document.getElementById("login");
let register = document.getElementById("register");
let form_box = document.getElementsByClassName("form-box")[0];
let register_box = document.getElementsByClassName("register-box")[0];
let login_box = document.getElementsByClassName("login-box")[0];
// 去注册按钮点击事件
register.addEventListener("click", () => {
  form_box.style.transform = "translateX(80%)";
  login_box.classList.add("hidden");
  register_box.classList.remove("hidden");
});

// 点击注册后，读取注册内容并存储在mysql数据库中
let register_button = document.querySelector(".register-box button");
register_button.addEventListener("click", async () => {
  let username = document.querySelector(
    ".register-box input:nth-of-type(1)"
  ).value;
  let email = document.querySelector(
    ".register-box input:nth-of-type(2)"
  ).value;
  let password = document.querySelector(
    ".register-box input:nth-of-type(3)"
  ).value;
  let confirm_password = document.querySelector(
    ".register-box input:nth-of-type(4)"
  ).value;
  if (
    username === "" ||
    email === "" ||
    password === "" ||
    confirm_password === ""
  ) {
    check_register.innerHTML = "请填写完整信息";
    setTimeout(() => {
      check_register.innerHTML = "";
    }, 1500);
    return;
  }
  // username长度不在3-20之间
  if (username.length < 3 || username.length > 20) {
    check_register.innerHTML = "用户名长度不在3-20之间";
    setTimeout(() => {
      check_register.innerHTML = "";
    }, 1500);
    return;
  }

  //正则表达式验证邮箱格式
  var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (emailPattern.test(email) === false) {
    check_register.innerHTML = "邮箱格式不正确";
    setTimeout(() => {
      check_register.innerHTML = "";
    }, 1500);
    return;
  }
  if (password !== confirm_password) {
    check_register.innerHTML = "两次密码不一致,请重新输入";
    setTimeout(() => {
      check_register.innerHTML = "";
    }, 1500);
    return;
  }
  // 密码长度不在10-20之间
  if (password.length < 10 || password.length > 20) {
    check_register.innerHTML = "密码长度不在10-20之间";
    setTimeout(() => {
      check_register.innerHTML = "";
    }, 1500);
    return;
  }

  const body = { username, email, password };
  const response = await fetchData("/myApp/register/", body);

  const data = await response.json();

  if (data.success === 1) {
    Swal.fire({
      title: "注册成功",
      icon: "success",
      confirmButtonText: "确定",
    });
  }else {
    if (data.message=== "用户名已存在") {
      Swal.fire({
        title: "用户名已存在",
        icon: "error",
        confirmButtonText: "确定"
      }
      );
    }else{
      Swal.fire({
        title: "邮箱已使用",
        icon: "error",
        confirmButtonText: "确定"
    });
    }
  }
  setTimeout(() => {
    check_register.innerHTML = "";
  }, 1500);
});

function fetchData(url, data) {
  return fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json;charset=utf-8",
    },
    body: JSON.stringify(data),
  });
}

// 去登录按钮点击事件
login.addEventListener("click", async () => {
  form_box.style.transform = "translateX(0%)";
  register_box.classList.add("hidden");
  login_box.classList.remove("hidden");
});

let login_button = document.querySelector(".login-box button");

login_button.addEventListener("click", async () => {
  let username = document.querySelector(
    ".login-box input:nth-of-type(1)"
  ).value;
  let password = document.querySelector(
    ".login-box input:nth-of-type(2)"
  ).value;
  let identify = document.querySelector(
    ".login-box input:nth-of-type(3)"
  ).value;
  if (username === "" || password === "") {
    check_login.innerHTML = "请填写完整信息";
    setTimeout(() => {
      check_login.innerHTML = "";
    }, 1500);
    return;
  }

  if (username.length < 3 || username.length > 20) {
    check_login.innerHTML = "用户名不存在";
    setTimeout(() => {
      check_login.innerHTML = "";
    }, 1500);
    return;
  }
  if (password.length < 10 || password.length > 20) {
    check_login.innerHTML = "密码错误";
    setTimeout(() => {
      check_login.innerHTML = "";
    }, 1500);
    return;
  }
  if (identify.length === 0) {
    document.getElementById("loader").style.display = "block";
    const body = { username, password, identify };
    console.log(body);

    const response = await fetchData("/myApp/login/", body);
    const data = await response.json();

    // 跳转到主页,同时跳转时添加动画效果
    if (data.success === 1) {
      document.getElementById("overlay").style.display = "block";
      setTimeout(() => {
        document.getElementById("loader").style.display = "none";
        window.location.href = "/myApp/homepage/";
      }, 5000);
    } else {
      document.getElementById("loader").style.display = "none";
      check_login.innerHTML = "登录失败,请检查用户名和密码";
      setTimeout(() => {
        check.innerHTML = "";
      }, 1500);
      return;
    }
  } else if (identify.length < 8 || identify.length > 8) {
    check_login.innerHTML = "身份码错误";
    setTimeout(() => {
      check_login.innerHTML = "";
    }, 1500);
    return;
  } else {
    document.getElementById("loader").style.display = "block";
    const body = { username, password, identify };
    console.log(body);

    const response = await fetchData(
      "/myApp/login_admin/",
      body
    );
    const data = await response.json();

    // 跳转到主页,同时跳转时添加动画效果
    if (data.success === 1) {
      document.getElementById("overlay").style.display = "block";
      setTimeout(() => {
        document.getElementById("loader").style.display = "none";
        window.location.href = "/myApp/get_all_text/";
      }, 1000);
    } else {
      document.getElementById("loader").style.display = "none";
      check_login.innerHTML = "登录失败,请检查用户名和密码";
      setTimeout(() => {
        check.innerHTML = "";
      }, 1500);
      return;
    }
  }
});
