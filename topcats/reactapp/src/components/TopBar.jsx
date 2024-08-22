import React from 'react';
import '../styles/TopBar.css';


const TopBar = () => {
    return (
        <div>
            <div className="top-bar">
                <div className="left-section">
                    <h1>Active Recall</h1>
                </div>
                <div className="right-section">
                    <a href="/register">Sign Up</a>
                    <a href="/login">Log In</a>
                </div>
            </div>
        </div>
    );
};

export default TopBar;




