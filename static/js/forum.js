// function postComment() {
//     var commentInput = document.getElementById('commentInput');
//     var commentText = commentInput.value;
//     var userNickname = document.getElementById('userNickname').textContent;
//
//     if (commentText) {
//         var currentDate = new Date().toISOString().slice(0, 19).replace('T', ' ');
//
//         // 创建评论元素
//         var commentDiv = document.createElement('div');
//         commentDiv.className = 'comment';
//         commentDiv.innerHTML = `
//             <div class="header">
//                 <div class="avatar"></div>
//                 <span>${userNickname} ${currentDate}</span>
//             </div>
//             <p>${commentText}</p>
//             <div class="actions">
//                 <span>👍 0</span> <span>👎 0</span> <span class="reply">回复</span>
//             </div>
//         `;
//
//         // 将新评论添加到评论区域
//         document.getElementById('commentsSection').appendChild(commentDiv);
//
//         // 清空输入框
//         commentInput.value = '';
//     } else {
//         alert('请输入评论内容！');
//     }
// }
//
// function updateComments() {
//     // 清空当前评论区域
//     document.getElementById('commentsSection').innerHTML = '';
//     // 示例：添加新的评论
//     const newCommentDiv = document.createElement('div');
//     newCommentDiv.className = 'comment';
//     newCommentDiv.innerHTML = `
//         <div class="header">
//             <div class="avatar"></div>
//             <span>用户 ${new Date().toISOString().slice(0, 19).replace('T', ' ')}</span>
//         </div>
//         <p>这是更新后的示例评论!</p>
//         <div class="actions">
//             <span>👍 0</span> <span>👎 0</span> <span class="reply">回复</span>
//         </div>
//     `;
//     document.getElementById('commentsSection').appendChild(newCommentDiv);
// }
