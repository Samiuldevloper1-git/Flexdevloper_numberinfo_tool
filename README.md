<div align="center">

# 📱 Flex devloper Number Info Tool

### 🔥 Ek Simple Aur Powerful Phone Number Information Lookup Tool

![Version](https://img.shields.io/badge/Version-1.0-blue?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Termux-green?style=for-the-badge)
![Language](https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge)
![Purpose](https://img.shields.io/badge/Purpose-Educational-red?style=for-the-badge)

> 💻 Termux Ke Liye Banaya Gaya &nbsp;|&nbsp; ⚡ Fast API Response &nbsp;|&nbsp; 🌍 India Focused

</div>

---

## 🚀 Is Tool Ke Baare Mein

**FlexDev Number Info Tool** ek lightweight Python-based tool hai jo kisi bhi phone number ki basic information fetch karta hai — Vercel par deploy ek custom API ke zariye. Ye **Termux** ke andar smoothly run karta hai aur terminal mein quick, clean output deta hai.

### 📦 Kya Kya Fetch Kar Sakta Hai:

| Info | Description |
|------|-------------|
| 📍 Country | Number se linked desh ka naam |
| 📞 Carrier | Network/Operator (e.g., Airtel, Jio, Vi) |
| 🌐 Location | Sheher/Region (agar API se available ho) |
| ✅ Validation | Basic number format validation |

---

## ⚙️ Features

- ✔️ Ek command mein easy usage
- ✔️ Lightweight aur fast API response
- ✔️ Termux ke andar perfectly kaam karta hai
- ✔️ Koi bhari dependencies nahi
- ✔️ Clean aur readable terminal output
- ✔️ Secure API key handling

---

## 🧰 Installation (Termux)

Termux mein yeh commands ek ek karke run karo:

```bash
pkg update && pkg upgrade -y
pkg install git -y
pkg install python -y
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

---

## ▶️ Kaise Run Karein

```bash
python phone.py
```

**Ya phir:**

```bash
python main.py
```

---

## 🔑 API Usage

Ye tool API ko is format mein `GET` request bhejta hai:

```
https://your-api-domain.vercel.app/api/phone?phone=XXXXXXXXXX&key=YOUR_API_KEY
```

**Example:**

```
https://your-api-domain.vercel.app/api/phone?phone=1234567890&key=YOUR_API_KEY
```

> ⚠️ **Note:** API key security reasons ke liye chhupa ke rakha gaya hai.

---

## 🧠 Kaise Kaam Karta Hai

```
User phone number enter karta hai
        ↓
Script API ko GET request bhejta hai
        ↓
API JSON response return karta hai
        ↓
Tool output ko format karke terminal mein dikhata hai
```

---

## 📸 Example Output

```
╔══════════════════════════════════╗
║     FlexDev Number Info Tool     ║
╚══════════════════════════════════╝

📱 Number   : +91 1234567890
🌍 Country  : India
📡 Carrier  : Carrier
📍 Location : Location
✅ Valid    : Yes
```

---

## ⚠️ Disclaimer

> ❗ Ye tool sirf **educational aur API testing purposes** ke liye banaya gaya hai.
> ❗ Isko kisi bhi **illegal, unethical ya harmful kaam** ke liye use mat karo.
> ❗ Kisi bhi galat use ke liye **developer zimmedar nahi hoga.**

---

## ❤️ Developer Info

| Field | Details |
|-------|---------|
| 👨‍💻 Developer | **FlexDev** |
| 📢 Telegram | [@Prime_x_Samiul](https://t.me/Prime_x_Samiul) |
| 🚀 Purpose | Learning + API Testing |
| 📌 Version | 1.0 |

---

## ⭐ Support

Agar ye project tumhare kaam aaya, toh **⭐ Star** dekar support karo aur apne doston ke saath share karo!

---

<div align="center">
Made with ❤️ by <b>Flex Devloper</b> | <a href="https://t.me/Prime_x_Samiul">@Prime_x_Samiul</a>
</div>
