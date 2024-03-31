import React, { useState } from 'react';
import { useNavigate  } from 'react-router-dom';
import './Auth.css';

import user_icon from '../Assets/person.png';
import email_icon from '../Assets/email.png';
import password_icon from '../Assets/password.png';

const Auth = () => {
    const navigate = useNavigate ();
    const [action, setAction] = useState('Sign Up');
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        password: ''
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async () => {
        try {
            let url = "signup"
            if (action === "Login") {
                url = "login"
            }
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });
            const data = await response.json();
            if (data.status === 'success'){
                navigate('/upload', {state: {data}});
            }
            else {
                console.log("no auth")
            }
        } catch (error) {
            console.error('Error submitting data:', error);
        }
    };

    const handleActionChange = (newAction) => {
        setAction(newAction);
    };

    const handleButtonClick = (clickedAction) => {
        if (action === clickedAction) {
            handleSubmit();
        } else {
            handleActionChange(clickedAction);
        }
    };

    return (
        <div className='container'>
            <div className="header">
                <div className="text">
                    {action}
                </div>
                <div className="underline"></div>
            </div>
            <div className="inputs">
                {action === "Login" ? null : <div className="input">
                    <img src={user_icon} alt="" />
                    <input type="text" name="name" placeholder='Name' value={formData.name} onChange={handleChange} />
                </div>}
                <div className="input">
                    <img src={email_icon} alt="" />
                    <input type="email" name="email" placeholder='Email' value={formData.email} onChange={handleChange} />
                </div>
                <div className="input">
                    <img src={password_icon} alt="" />
                    <input type="password" name="password" placeholder='Password' value={formData.password} onChange={handleChange} />
                </div>
            </div>
            <div className="submit-container">
                <div className={action === "Login" ? "submit gray" : "submit"} onClick={() => handleButtonClick("Sign Up")}>Sign Up</div>
                <div className={action === "Sign Up" ? "submit gray" : "submit"} onClick={() => handleButtonClick("Login")}>Login</div>
            </div>
        </div>
    );
};

export default Auth;
