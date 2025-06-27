# EVionix – Discover EV insights with AI Chatbot

EVionix is a dynamic web-based platform developed to educate users about Electric Vehicles (EVs) and promote sustainable transportation. The project combines informative content, real-time chatbot assistance, and a subscription system to deliver a complete learning experience.

## 🌱 Features

- **Landing Page**  
  A visually appealing introduction to EV technology highlighting benefits like zero emissions, energy efficiency, and reduced maintenance.

- **Blog Section**  
  In-depth, well-researched articles on EV topics including:
  - Latest innovations
  - Environmental impact
  - Cost and performance comparisons
  - Transition to green mobility

- **AI-Powered Chatbot (Groq API)**  
  Integrated chatbot answers common questions such as:
  - Battery range & life
  - Charging options and infrastructure
  - EV vs. traditional vehicle comparisons

- **Email Subscription System**  
  Users can subscribe to receive regular updates and articles. The backend:
  - Built using **PHP**
  - Utilizes **PHPMailer** with **Gmail SMTP**
  - Sends verification emails to confirm subscriptions

## 🛠️ Tech Stack

| Frontend         | Backend          | AI Integration | Email |
|------------------|------------------|----------------|-------|
| HTML, CSS, JS    | PHP              | Groq API       | PHPMailer (SMTP) |

## 🔧 Installation & Setup

### Prerequisites
- PHP (>= 7.4)
- Composer
- Valid Gmail SMTP credentials
- Groq API key

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/maadwa/EV-Vehicle.git
   ```
   

2. **Install PHPMailer**

   ```bash
   composer require phpmailer/phpmailer
   ```

3. **Configure Environment**

   * Create a `.env` file or configure credentials in `config.php`

   ```env
   GROQ_API_KEY=your_groq_api_key
   SMTP_EMAIL=your_email@gmail.com
   SMTP_PASSWORD=your_email_password
   ```

4. **Database Setup**

   * Update DB credentials in `config.php`.

5. **Run the Application**

   * Use a local server (e.g., XAMPP, WAMP) or deploy on a live server.

## 🤖 Chatbot API

The chatbot uses the [Groq API](https://groq.com/) to handle user queries related to EVs in real time.

```php
// Example: Sending query to Groq
$response = $client->chat()->create([
  'model' => 'mixtral-8x7b-32768',
  'messages' => [
    ['role' => 'user', 'content' => 'What is the range of an EV?'],
  ],
]);
```

## 📬 Email Subscription Flow

1. User enters email on the site.
2. A 6-digit code is sent via Gmail SMTP using PHPMailer.
3. User verifies the code to complete subscription.

## 📸 Demo

> [View the project demo here](https://drive.google.com/file/d/1PBPdHrf4hjAPPi4N13C7LALtAnQ-Fcow/view?usp=sharing)

## 🎯 Purpose

This project aims to:

* Educate the public about electric vehicles
* Provide real-time assistance via AI
* Encourage informed, eco-friendly transportation choices

## 🧠 Skills Gained

* Full-stack web development (PHP, JS, HTML/CSS)
* API integration (Groq)
* Email verification workflows
* Understanding of EV tech and green mobility trends

## 📄 License

MIT License

---

### 🚀 Developed by [Maadwa Krishnaa](https://github.com/maadwa) and [Keerttna Radhakrishnan](https://github.com/Keerttna)
