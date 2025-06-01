// src/Login.js
import React, { useState } from 'react';
import { signInWithPopup } from 'firebase/auth';
import { auth, provider } from '../../firebase.config';

function Login() {
  const [user, setUser] = useState(null);

  const handleLogin = async () => {
    try {
      const result = await signInWithPopup(auth, provider);
      setUser(result.user);
    } catch (error) {
      console.error("Login error:", error);
      alert("Failed to login. Please try again.");
    }
  };

  const handleLogout = () => {
    setUser(null);
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        {!user ? (
          <>
            <h2>Login with Google</h2>
            <button onClick={handleLogin} style={styles.button}>
              Sign In with Google
            </button>
          </>
        ) : (
          <>
            <h2>Welcome, {user.displayName}</h2>
            <img src={user.photoURL} alt="Profile" style={styles.image} />
            <p>Email: {user.email}</p> 
            {console.log(user)}
            <button onClick={handleLogout} style={styles.button}>
              Logout
            </button>
          </>
        )}
      </div>
    </div>
  );
}

const styles = {
  container: {
    display: 'flex',
    height: '100vh',
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f5f5f5',
  },
  card: {
    padding: 30,
    backgroundColor: '#fff',
    borderRadius: 10,
    boxShadow: '0 4px 20px rgba(0,0,0,0.1)',
    textAlign: 'center',
  },
  button: {
    padding: '10px 20px',
    backgroundColor: '#4285F4',
    color: '#fff',
    border: 'none',
    borderRadius: 5,
    cursor: 'pointer',
    marginTop: 15,
  },
  image: {
    width: 80,
    borderRadius: '50%',
    margin: '10px 0',
  }
};

export default Login;