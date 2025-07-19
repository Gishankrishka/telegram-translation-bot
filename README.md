# 🌐 Telegram Translation Bot

<div align="center">
  
![Telegram Translation Bot](https://img.shields.io/badge/Telegram-Translation%20Bot-blue?style=for-the-badge&logo=telegram)
![Python](https://img.shields.io/badge/Python-3.7+-brightgreen?style=for-the-badge&logo=python)
![Gemini AI](https://img.shields.io/badge/Powered%20by-Gemini%20AI-orange?style=for-the-badge&logo=google)

**🚀 A powerful Telegram bot that auto-translates messages from source channels using Google's Gemini AI**

![License](https://img.shields.io/github/license/yourusername/telegram-translation-bot?style=flat-square)
![Stars](https://img.shields.io/github/stars/yourusername/telegram-translation-bot?style=flat-square)
![Forks](https://img.shields.io/github/forks/yourusername/telegram-translation-bot?style=flat-square)
![Issues](https://img.shields.io/github/issues/yourusername/telegram-translation-bot?style=flat-square)

[🚀 Quick Deploy](#-deploy-now) • [📖 Documentation](#-setup-guide) • [🤝 Contributing](#-contributing) • [💬 Support](#-support)

</div>

---

## ✨ Features

<div align="center">

| Feature | Description |
|---------|-------------|
| 🔄 **Real-time Translation** | Automatically translates messages as they arrive |
| 🤖 **Gemini AI Powered** | Uses Google's advanced AI for accurate translations |
| 🌍 **Multi-language Support** | Supports 100+ languages with ISO codes |
| ⚡ **Cloud Deployment** | Easy deployment on Railway, Heroku, or any VPS |
| 🔒 **Secure & Private** | Your credentials stay safe with you |
| 📱 **Mobile Friendly** | Works seamlessly on all Telegram clients |

</div>

---

## 🚀 Deploy Now

<div align="center">

## One-Click Deployment

<!---[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/github/Gishankrishka/telegram-translation-bot) -->

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Gishankrishka/telegram-translation-bot)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Gishankrishka/telegram-translation-bot)

## Additional Deployment Options

### Vercel
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Gishankrishka/telegram-translation-bot)

### Netlify
[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/Gishankrishka/telegram-translation-bot)

</div>

---

## 🛠️ Prerequisites

Before getting started, make sure you have:

- 🐍 **Python 3.7+** installed
- 📱 **Telegram account**
- 🔑 **Google account** for Gemini API access
- ☁️ **Cloud platform account** (Railway/Heroku/Render) for deployment

---

## 📋 Setup Guide

### 🤖 Step 1: Create Telegram Bot

1. Open [@BotFather](https://t.me/BotFather) on Telegram
2. Send `/newbot` and follow the prompts
3. Choose a unique name and username for your bot
4. 📝 Copy the **Bot Token** (format: `123456789:ABCDEF...`)

<div align="center">
<img src="https://img.shields.io/badge/BotFather-@BotFather-blue?style=for-the-badge&logo=telegram" alt="BotFather">
</div>

### 🔐 Step 2: Get Telegram API Credentials

1. Visit [my.telegram.org](https://my.telegram.org)
2. Log in with your phone number
3. Click **API Development Tools**
4. Fill in the application details
5. 📝 Note your `API_ID` and `API_HASH`

### 📢 Step 3: Configure Destination Chat

1. Add your bot as an **administrator** to the source chat
2. Give it permission to read messages
3. add [@MissRose_bot](https://t.me/MissRose_bot) to the chat and send /id
4. 📝 Copy the Channel ID (format: `-100xxxxxxxxxx`)

### 🌐 Step 4: Choose Target Language

Select your preferred language using [ISO 639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes):

| Language | Code | Language | Code |
|----------|------|----------|------|
| English | `en` | Spanish | `es` |
| French | `fr` | German | `de` |
| Sinhala | `si` | Tamil | `ta` |
| Hindi | `hi` | Arabic | `ar` |

### 🧠 Step 5: Get Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **Create API Key**
4. 📝 Copy your Gemini API key

<div align="center">
<img src="https://img.shields.io/badge/Google%20AI-Studio-orange?style=for-the-badge&logo=google" alt="Google AI Studio">
</div>

---

## ⚙️ Configuration

Create a `config.py` file in your project root:

```python
class Config:
    # Telegram Bot Configuration
    BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
    API_ID = "YOUR_API_ID_HERE"
    API_HASH = "YOUR_API_HASH_HERE"
    
    # Channel Configuration
    SOURCE_CHANNEL = -1001234567890  # Your destination channel ID
    
    # Translation Configuration
    LANGUAGE_CODE = "en"  # Target language (ISO 639-1)
    
    # AI Configuration
    GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
    
    # Optional: Advanced Settings
    MAX_MESSAGE_LENGTH = 4096
    TRANSLATION_TIMEOUT = 30
    RATE_LIMIT_DELAY = 1
```

---

## 🚀 Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/telegram-translation-bot.git
   cd telegram-translation-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your settings**
   ```bash
   cp .env.example. .env
   # Edit .env with your credentials
   ```

4. **Run the bot**
   ```bash
   python3 -m Bot
   ```

---

## 🌟 Features in Detail

### 🔄 Real-time Translation
The bot monitors your source channel 24/7 and instantly translates new messages using Google's Gemini AI, ensuring you never miss important updates.

### 🎯 Smart Context Understanding
Gemini AI doesn't just translate words—it understands context, idioms, and cultural nuances for more accurate translations.

### 🛡️ Error Handling
Built-in retry mechanisms and error handling ensure your bot stays online even during network issues or API rate limits.

### 📊 Performance Monitoring
Optional logging and monitoring features to track translation accuracy and bot performance.

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

<div align="center">

[![Contributors](https://img.shields.io/badge/Contributors-Welcome-brightgreen?style=for-the-badge)](CONTRIBUTING.md)
[![Good First Issues](https://img.shields.io/badge/Good%20First%20Issues-Available-blue?style=for-the-badge)](https://github.com/yourusername/telegram-translation-bot/labels/good%20first%20issue)

</div>

### 🐛 Report Bugs
Found a bug? [Open an issue](https://github.com/yourusername/telegram-translation-bot/issues/new?template=bug_report.md) with detailed information.

### 💡 Suggest Features
Have an idea? [Open a feature request](https://github.com/yourusername/telegram-translation-bot/issues/new?template=feature_request.md) and let's discuss it!

### 🔧 Submit Pull Requests
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👥 Contributors

<div align="center">

Thanks to all the amazing people who have contributed to this project:

<a href="https://github.com/yourusername/telegram-translation-bot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=yourusername/telegram-translation-bot" alt="Contributors" />
</a>

Made with [contributors-img](https://contrib.rocks).

</div>

---

## 📄 License

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

</div>

---

## 💬 Support

<div align="center">

Need help? We're here for you!

[![Telegram Support](https://img.shields.io/badge/Telegram-Support%20Chat-blue?style=for-the-badge&logo=telegram)](https://t.me/your_support_channel)
[![Discord](https://img.shields.io/badge/Discord-Join%20Server-7289da?style=for-the-badge&logo=discord)](https://discord.gg/your_server)
[![GitHub Issues](https://img.shields.io/badge/GitHub-Issues-red?style=for-the-badge&logo=github)](https://github.com/yourusername/telegram-translation-bot/issues)

</div>

### 🆘 Common Issues

| Issue | Solution |
|-------|----------|
| Bot not responding | Check if bot token is correct and bot is added to channel |
| Translation errors | Verify Gemini API key and check rate limits |
| Channel ID issues | Ensure channel ID format is correct (-100xxxxxxxxxx) |
| Deployment failures | Check all environment variables are set correctly |

---

## 🌟 Star History

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=Gishankrishka/telegram-translation-bot&type=Date)](https://star-history.com/#yourusername/telegram-translation-bot&Date)

</div>

---

## 🚀 What's Next?

- [ ] 🎨 Web dashboard for bot management
- [ ] 📊 Translation analytics and statistics
- [ ] 🔄 Support for multiple source channels
- [ ] 🎯 Custom translation prompts
- [ ] 📱 Mobile app companion
- [ ] 🌐 Support for more AI providers

---

<div align="center">

**⭐ Star this repo if you found it helpful! ⭐**

[![GitHub stars](https://img.shields.io/github/stars/GishanKrishka/telegram-translation-bot?style=social)](https://github.com/yourusername/telegram-translation-bot/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Gishankrishka/telegram-translation-bot?style=social)](https://github.com/yourusername/telegram-translation-bot/network/members)

Made with ❤️ by [Gishan Krishka](https://github.com/GishanKrishka)

</div>
