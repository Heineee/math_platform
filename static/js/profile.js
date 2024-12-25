function fetchData(url, data) {
  return fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json;charset=utf-8",
    },
    body: JSON.stringify(data),
  });
}

let saveProfileButton = document.querySelector(".profile-section button");
saveProfileButton.addEventListener('click', async () => {

    var nickname = document.getElementById('nickname').value;
    var gender = document.getElementById('gender').value;
    var birthday = document.getElementById('birthday').value;
    var address = document.getElementById('address').value;
    var email = document.getElementById('email').value;
    const body = { nickname, gender, birthday,address,email };
    const response = await fetchData("/myApp/profile/", body);
    const data = await response.json();
     // 最关键的几步
    if (data.success === 1) {
    Swal.fire({
      title: "保存成功",
      icon: "success",
      confirmButtonText: "确定",
    });
        }
});
// function saveProfileData() {
//
//
//   const body = { nickname, gender, birthday,address,email };
//   const feedback=fetch("/myApp/profile/",{method: "POST",headers: {
//       "Content-Type": "application/json;charset=utf-8",
//     },
//     body: JSON.stringify(body),});
//
//
//     alert('基本信息已保存！\n\n昵称: ' + nickname + '\n性别: ' + gender + '\n生日: ' + birthday + '\n地址: ' + address + '\n邮箱: ' + email+'\n'+"反馈"+feedback);
// }

function updateChallengeData() {
    document.getElementById('completed-questions').innerText = Math.floor(Math.random() * 100);
    document.getElementById('ranking').innerText = '第' + Math.floor(Math.random() * 100) + '名';
    alert('挑战数据已更新！');
}

function updateDiscussionData() {
    document.getElementById('post-count').innerText = Math.floor(Math.random() * 20);
    document.getElementById('likes-count').innerText = Math.floor(Math.random() * 100);
    document.getElementById('replies-count').innerText = Math.floor(Math.random() * 50);
    alert('讨论数据已更新！');
}
