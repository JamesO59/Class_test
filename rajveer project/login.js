const loginForm = document.getElementById('loginForm');
const errorMsg = document.getElementById('errorMsg');

loginForm.addEventListener('submit', (event) => {
  event.preventDefault(); 

  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  const users = {
    'rajveer23@gmail.com': 'Rajveer123','mriganka11@gmail.com':'Mriganka1119' , 'suraj@gmail.com':'Suraj123','riya@gmail.com':'riya123'
  };

  if (users[email] === password) {
    window.location.href = 'second.html';
  } else {
    errorMsg.textContent = 'Invalid email or password.';
  }
});