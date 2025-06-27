# EV-Vehicle


# ⚡ EV Discovery Insights – Email Subscription Project

This project allows users to subscribe to receive the latest **Electric Vehicle (EV)** updates via email. It consists of a **frontend landing page** built with HTML, CSS, and JavaScript, and a **backend email subscription system** using PHP and PHPMailer with News API integration.



## ✨ Features

- 💡 Clean EV-themed landing page with a **subscribe form**
- ✅ Validates email and sends a **verification code** to the user
- 🔒 Verifies code input by user before subscription
- 📬 Sends the latest **EV news** using [NewsAPI](https://newsapi.org/)
- ❌ Unsubscribe link included in every mail

---

## 🔧 Technologies Used

- HTML, CSS, JavaScript
- PHP 8+
- [PHPMailer](https://github.com/PHPMailer/PHPMailer)
- [NewsAPI](https://newsapi.org/)
- Optional: [XAMPP](https://www.apachefriends.org/) / [WAMP](https://www.wampserver.com/) for local server

---

## 🚀 Getting Started

### 1. Clone the Project

```bash
git clone https://github.com/your-username/ev-discovery-insights.git
````

### 2. Install PHPMailer via Composer

```bash
composer require phpmailer/phpmailer
```

### 3. Set Up `config.php`

Create a `config.php` inside `src/`:

```php
<?php
return [
  'smtp_username' => 'your-email@gmail.com',
  'smtp_password' => 'your-gmail-app-password',
  'newsapi_key' => 'your-newsapi-key'
];
```

Use a **Gmail App Password**, not your main password.

---

### 4. Run the Project

Use a local server to serve the project:

```bash
php -S localhost:8000
```

Or place the entire folder inside your XAMPP `htdocs` and visit:

```
http://localhost/Projects/EV-Vehicle/index.html
```

---

## 🔁 How the Workflow Works

1. User enters email on the landing page
2. Gets redirected to the PHP project
3. Receives verification code in email
4. After successful code entry:

   * Email is saved to `registered_emails.txt`
   * A latest EV news article is fetched using NewsAPI
   * The news article is emailed to the user

---

## 🧪 Sample NewsAPI Query

```url
https://newsapi.org/v2/everything?q=electric%20vehicles&sortBy=publishedAt&pageSize=1&apiKey=YOUR_API_KEY
```



## 🙋‍♀️ Author

Developed by [Maadwa Krishnaa](https://github.com/your-profile)
             [Keerttna Radhakrishnan](https://github.com/Keerttna)
