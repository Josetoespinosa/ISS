import React from 'react';
import '../css/Top.css';
import "../../assets/logoMYS.png";
import '../css/Top.css'; 
import { useNavigate } from 'react-router-dom';

const Top = () => {
  // Retrieve the user from local storage
  const user = localStorage.getItem('user');
  const isLoggedIn = user !== null; // Check if the user is logged in

  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('user'); // Remove user from local storage
    navigate('/'); // Navigate to the login page// Reload the page to update the UI
  }

  return (
    <div className="top-header">
      <img src={require("../../assets/logoMYS.png")} alt="Logo" className="logo" style={{ width: '60px', height: '60px' }} />
      <div className="title">Match Your Style</div>
      <div className="auth-buttons">
        {isLoggedIn ? (
          <>
            <button className="login-logout-btn" onClick={handleLogout}>
              Logout
            </button>
          </>
        ) : (
          <>
            <button className="login-logout-btn" onClick={() => navigate('/')}>
              Login
            </button>
            <button className="login-logout-btn" onClick={() => navigate('/signup')}>
              Sign Up
            </button>
          </>
        )}
      </div>
    </div>
  );
}

export default Top;
