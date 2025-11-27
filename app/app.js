// Simple auth logic
// - fetch users.json
// - validate credentials
// - store session in sessionStorage
// - protect dashboard by checking session

const USERS_JSON = 'users.json';

// Utility: show message on login page
function showMsg(text, el='#msg') {
  const node = document.querySelector(el);
  if(node) node.textContent = text;
}

// Attempt login (used on index.html)
async function attemptLogin(evt){
  if(evt) evt.preventDefault();
  showMsg('');
  const user = document.getElementById('username').value.trim();
  const pass = document.getElementById('password').value;

  if(!user || !pass){ showMsg('Rellena usuario y contraseña'); return; }

  try{
    const res = await fetch(USERS_JSON, {cache: "no-store"});
    if(!res.ok){ showMsg('No se pudo cargar el archivo users.json (sirve desde un servidor).'); return; }
    const data = await res.json();

    const found = data.users.find(u => u.username === user && u.password === pass);
    if(found){
      // create minimal session
      const session = { username: found.username, name: found.name, email: found.email, ts: Date.now() };
      sessionStorage.setItem('sena_session', JSON.stringify(session));
      // redirect to dashboard
      window.location.href = 'dashboard.html';
    } else {
      showMsg('Credenciales inválidas');
    }
  }catch(err){
    console.error(err);
    showMsg('Error leyendo users.json');
  }
}

// Protect the dashboard — run on dashboard.html
function protectDashboard(){
  const raw = sessionStorage.getItem('sena_session');
  if(!raw){
    // no session -> redirect to login
    window.location.href = 'index.html';
    return;
  }
  try{
    const s = JSON.parse(raw);
    document.getElementById('welcome').textContent = `Hola, ${s.name || s.username}`;
    document.getElementById('emailArea').textContent = s.email ? `Email: ${s.email}` : '';
  }catch(e){
    sessionStorage.removeItem('sena_session');
    window.location.href = 'index.html';
  }
}

// Logout handler
function setupLogout(){
  const btn = document.getElementById('logoutBtn');
  if(btn){ btn.addEventListener('click', ()=>{
    sessionStorage.removeItem('sena_session');
    window.location.href = 'index.html';
  })}
}

// Bind events depending on page
document.addEventListener('DOMContentLoaded', ()=>{
  const loginForm = document.getElementById('loginForm');
  if(loginForm) loginForm.addEventListener('submit', attemptLogin);

  // If on dashboard, protect and wire logout
  if(document.getElementById('logoutBtn')){
    protectDashboard();
    setupLogout();
  }
});
