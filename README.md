# 🚀 Django Login & Signup Authentication System

A complete, beginner-friendly Django authentication system with user registration, login, logout, and protected pages.

![Django Version](https://img.shields.io/badge/Django-5.2.7-green.svg)
![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)




For a comprehensive, step-by-step guide with detailed code explanations, visit:

<div align="center">
  <a href="https://shaksveo3.github.io/Login-Signup-with-Django/" target="_blank" style="
    display: inline-block;
    background: linear-gradient(45deg, #2196F3, #21CBF3);
    color: white;
    padding: 12px 24px;
    font-size: 18px;
    font-weight: bold;
    text-align: center;
    text-decoration: none;
    border-radius: 50px;
    box-shadow: 0 4px 15px rgba(33, 150, 243, 0.4);
    transition: all 0.3s ease;
    border: none;
    cursor: pointer;
  ">
    🌐 <strong>Complete Django Authentication Tutorial</strong> →
  </a>
</div>



---

## ✨ Features

- **User Registration** - Create new accounts with username, email, and password
- **User Login** - Secure authentication with session management
- **User Logout** - Clean session termination
- **Protected Pages** - Access control using `@login_required` decorator
- **Password Hashing** - Secure password storage using PBKDF2
- **CSRF Protection** - Built-in Django CSRF token security
- **Flash Messages** - User-friendly success/error notifications
- **MySQL Database** - Reliable data persistence

## 🎯 Demo

<table>
<tr>
<td width="33%" align="center">

### 📝 Signup Page

<img src="images/signup.png" alt="Signup Page" width="100%" style="border: 2px solid #667eea; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">

</td>
<td width="33%" align="center">

### 🔐 Login Page

<img src="images/login.png" alt="Login Page" width="100%" style="border: 2px solid #667eea; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">

</td>
<td width="33%" align="center">

### 🎉 Welcome Page

<img src="images/welcome_page.png" alt="Welcome Page" width="100%" style="border: 2px solid #667eea; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">

</td>
</tr>
</table>

---

## 📁 Project Structure

```
login_signup_cld/
├── manage.py                    # Django management tool
├── tutorial.html               # Complete tutorial guide
├── README.md                   # This file
│
├── accounts/                   # Authentication app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py              # User model (Django's built-in)
│   ├── views.py               # Business logic
│   ├── urls.py                # App URL routing
│   ├── tests.py
│   ├── templates/
│   │   ├── signup.html       # Registration form
│   │   ├── login.html        # Login form
│   │   └── welcome.html      # Protected dashboard
│   └── migrations/            # Database migrations
│
└── login_signup_cld/           # Project configuration
    ├── __init__.py
    ├── settings.py           # Project settings
    ├── urls.py               # Main URL router
    ├── asgi.py
    └── wsgi.py
```
