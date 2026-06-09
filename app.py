<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask

app = Flask(__name__)

# ================= HOME PAGE =================
@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>RohanK | Instagram Content Creator</title>

<!-- SEO -->
<meta name="description" content="RohanK - Marathi Instagram Content Creator. Viral Reels, Comedy, Daily Life Content.">
<meta name="keywords" content="RohanK, instagram reels, marathi creator, viral reels">
<meta name="author" content="RohanK">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
body{
    margin:0;
    font-family: 'Segoe UI', sans-serif;
    background:#0f0f0f;
    color:white;
    text-align:center;
}
header{
    padding:80px 20px;
}
h1{
    font-size:56px;
    color:#ffcc00;
    margin-bottom:10px;
}
.tagline{
    font-size:20px;
    color:#ccc;
    margin-bottom:35px;
}
.btn{
    display:inline-block;
    margin:10px;
    padding:14px 36px;
    background:linear-gradient(45deg,#ff0050,#ff7a18);
    color:white;
    text-decoration:none;
    border-radius:40px;
    font-size:17px;
    font-weight:bold;
}
.btn:hover{
    transform:scale(1.05);
}
.section{
    padding:60px 20px;
}
.section h2{
    color:#ffcc00;
    margin-bottom:25px;
}
.reels{
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:20px;
}
iframe{
    border-radius:18px;
}
footer{
    padding:25px;
    font-size:14px;
    color:#aaa;
    background:#111;
}
</style>
</head>

<body>

<header>
    <h1>RohanK</h1>
    <div class="tagline">
        Instagram Content Creator | Viral Reels | Marathi Creator
    </div>

    <a class="btn" href="https://www.instagram.com/" target="_blank">📸 Follow on Instagram</a>
    <a class="btn" href="/blog">📝 SEO Blog</a>
</header>

<!-- Instagram Reels Section -->
<div class="section">
    <h2>🔥 My Viral Reels</h2>

    <div class="reels">
        <iframe src="https://www.instagram.com/reel/DUF9bkqCH4h/embed"
        width="320" height="400" frameborder="0"></iframe>
    </div>
</div>

<footer>
© 2026 RohanK | All Rights Reserved
</footer>

</body>
</html>
"""

# ================= BLOG PAGE =================
@app.route("/blog")
def blog():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>RohanK Blog | Instagram Growth</title>

<meta name="description" content="Learn Instagram Reels growth tips by RohanK">
<meta name="keywords" content="instagram reels viral tips, marathi creator blog">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
body{
    font-family:Arial, sans-serif;
    background:#0f0f0f;
    color:white;
    padding:30px;
    line-height:1.7;
}
h1,h2{
    color:#ffcc00;
}
a{
    color:#ff7a18;
    text-decoration:none;
}
.container{
    max-width:800px;
    margin:auto;
}
</style>
</head>

<body>
<div class="container">

<h1>How I Grow Instagram Reels Organically 🚀</h1>

<p>
Instagram reels viral honya sathi **shortcut nahi** aahe,
pan correct strategy follow keli tar growth nakki milte.
</p>

<h2>1️⃣ Strong Hook</h2>
<p>
First 3 seconds madhe viewer थांबला पाहिजे.
Text + action immediately start kara.
</p>

<h2>2️⃣ Consistency</h2>
<p>
Daily 1 reel (minimum 5 reels per week) takla tar
Instagram algorithm favour karto.
</p>

<h2>3️⃣ SEO + Hashtags</h2>
<p>
Caption madhe keywords + niche hashtags vapra.
Random hashtags टाळ.
</p>

<p>
Follow <b>RohanK</b> for more Instagram growth tips 🔥
</p>

<a href="/">⬅ Back to Home</a>

</div>
</body>
</html>
"""

# ================= RUN APP =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)