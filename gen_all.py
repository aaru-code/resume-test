import os

SIDEBAR = """<aside class="sidebar">
  <div class="sidebar-logo">
    <div class="logo-circle"><span class="logo-text-inner">PG</span></div>
    <div class="logo-wordmark"><div class="logo-name">PandeyG</div><div class="logo-tagline">Portfolio 2024</div></div>
  </div>
  <ul class="nav-menu">
    <li><a href="index.html"><span class="nav-icon">🏠</span>Home</a></li>
    <li><a href="about.html"><span class="nav-icon">👤</span>About</a></li>
    <li><a href="skills.html"><span class="nav-icon">⚡</span>Skills</a></li>
    <li><a href="projects.html"><span class="nav-icon">🗂️</span>Projects</a></li>
    <li><a href="experience.html"><span class="nav-icon">💼</span>Experience</a></li>
    <li><a href="contact.html"><span class="nav-icon">✉️</span>Contact</a></li>
  </ul>
  <div class="theme-toggle-wrap">
    <button class="theme-toggle" aria-label="Toggle theme">
      <span class="toggle-label">☀️ Day Mode</span>
      <div class="toggle-track"><div class="toggle-thumb"></div></div>
    </button>
  </div>
  <div class="sidebar-footer">📍 Delhi, India<br><span>Open to Freelance</span></div>
</aside>
<button class="hamburger"><span></span><span></span><span></span></button>"""

CHATBOT = """<button class="chat-fab" id="chatFab">
  <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.37 5.07L2 22l5.09-1.35A9.92 9.92 0 0 0 12 22c5.52 0 10-4.48 10-10S17.52 2 12 2zm0 18c-1.66 0-3.21-.49-4.5-1.33l-.32-.2-3.02.8.82-2.96-.21-.33A7.95 7.95 0 0 1 4 12c0-4.41 3.59-8 8-8s8 3.59 8 8-3.59 8-8 8zm4.17-5.24c-.23-.12-1.35-.67-1.56-.74s-.36-.12-.51.12-.59.74-.72.9-.26.18-.49.06c-.23-.12-.97-.36-1.85-1.14-.68-.61-1.14-1.36-1.27-1.59s-.01-.35.1-.47c.1-.1.23-.26.34-.39s.15-.23.23-.38.04-.29-.02-.41-.51-1.22-.7-1.68-.37-.38-.51-.39-.28-.01-.43-.01-.39.06-.6.29-.78.76-.78 1.85.8 2.15.91 2.3c.12.15 1.58 2.41 3.82 3.38.53.23.95.37 1.27.47.54.17 1.03.15 1.41.09.43-.07 1.35-.55 1.54-1.08.19-.53.19-.99.13-1.08-.06-.1-.22-.16-.46-.28z"/></svg>
  <div class="fab-badge">AI</div>
</button>
<div class="chat-window" id="chatWindow">
  <div class="chat-header">
    <div class="chat-av">🤖</div>
    <div class="chat-hinfo">
      <div class="chat-hname">PandeyG Bot ✨</div>
      <div class="chat-hstatus">Online — Always here for you!</div>
    </div>
    <button class="chat-close" id="chatClose">✕</button>
  </div>
  <div class="chat-messages" id="chatMessages"></div>
  <div class="quick-replies" id="quickReplies"></div>
  <div class="chat-input-row">
    <input type="text" class="chat-input" id="chatInputField" placeholder="Ask me anything about Priyanshu... 😊" maxlength="200">
    <button class="chat-send" id="chatSendBtn">
      <svg viewBox="0 0 24 24"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
    </button>
  </div>
</div>"""

def page(title, extra_css, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Priyanshu Pandey</title>
<link rel="stylesheet" href="style.css">
<style>{extra_css}</style>
</head>
<body>
<div class="cursor"></div><div class="cursor-ring"></div><div class="page-bg"></div>
{SIDEBAR}
<main class="main">
{body}
</main>
{CHATBOT}
<script src="script.js"></script>
</body>
</html>"""

# ============ ABOUT ============
about_css = """
.about-layout{display:grid;grid-template-columns:290px 1fr;gap:2.5rem;align-items:start;}
.profile-card{background:var(--card);border:1px solid var(--border-lt);border-radius:22px;overflow:hidden;position:sticky;top:1.5rem;box-shadow:0 4px 24px var(--shadow2);}
.profile-banner{height:110px;background:linear-gradient(135deg,var(--red),#ff6b6b);position:relative;overflow:hidden;}
.profile-banner::before{content:'';position:absolute;inset:0;background:repeating-linear-gradient(-45deg,transparent,transparent 18px,rgba(255,255,255,0.07) 18px,rgba(255,255,255,0.07) 36px);}
.banner-logo{position:absolute;top:1rem;right:1rem;width:38px;height:38px;border-radius:50%;background:rgba(255,255,255,0.2);border:1.5px solid rgba(255,255,255,0.4);display:flex;align-items:center;justify-content:center;font-family:'Bebas Neue',sans-serif;font-size:0.9rem;color:#fff;animation:logoPulse 4s ease-in-out infinite;}
.profile-avatar{width:80px;height:80px;border-radius:50%;background:var(--cream);border:4px solid var(--surface);display:flex;align-items:center;justify-content:center;font-size:2.6rem;margin:-40px auto 0;position:relative;z-index:2;box-shadow:0 4px 16px var(--shadow);animation:avFloat 4s ease-in-out infinite;}
@keyframes avFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-5px)}}
.profile-body{padding:0.8rem 1.5rem 1.5rem;text-align:center;}
.profile-name{font-family:'Bebas Neue',sans-serif;font-size:1.4rem;letter-spacing:0.5px;color:var(--text);margin:0.4rem 0 0.1rem;}
.profile-role{font-size:0.78rem;color:var(--red);font-weight:600;margin-bottom:1rem;}
.p-divider{height:1px;background:var(--border-lt);margin:1rem 0;}
.info-list{display:flex;flex-direction:column;gap:0.6rem;text-align:left;}
.info-row{display:flex;align-items:center;gap:0.6rem;font-size:0.82rem;color:var(--muted);}
.info-ico{width:28px;height:28px;border-radius:7px;background:var(--cream);border:1px solid var(--border-lt);display:flex;align-items:center;justify-content:center;font-size:0.82rem;flex-shrink:0;}
.info-row a{color:var(--muted);text-decoration:none;transition:color 0.2s;}
.info-row a:hover{color:var(--red);}
.about-body{display:flex;flex-direction:column;gap:2.5rem;}
.intro-text{color:var(--muted);font-size:0.96rem;line-height:1.85;}
.intro-text p+p{margin-top:1rem;}
.intro-text strong{color:var(--text);font-weight:700;}
.intro-text .red{color:var(--red);font-weight:700;}
.edu-list{display:flex;flex-direction:column;gap:1rem;}
.edu-card{background:var(--card);border:1px solid var(--border-lt);border-radius:16px;padding:1.4rem 1.6rem;display:flex;gap:1.2rem;align-items:flex-start;transition:all 0.25s;box-shadow:0 2px 10px var(--shadow2);}
.edu-card:hover{border-color:var(--border);transform:translateX(6px);box-shadow:0 6px 24px var(--shadow);}
.edu-ico{width:48px;height:48px;border-radius:13px;background:var(--red-soft);display:flex;align-items:center;justify-content:center;font-size:1.4rem;flex-shrink:0;}
.edu-degree{font-weight:700;font-size:0.95rem;margin-bottom:0.15rem;color:var(--text);}
.edu-inst{font-size:0.8rem;color:var(--red);font-weight:600;margin-bottom:0.6rem;}
.edu-chips{display:flex;flex-wrap:wrap;gap:0.35rem;}
.interest-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:0.8rem;}
.interest-tile{background:var(--card);border:1px solid var(--border-lt);border-radius:14px;padding:1.2rem 1rem;text-align:center;transition:all 0.25s;font-size:0.82rem;font-weight:600;color:var(--muted);box-shadow:0 2px 8px var(--shadow2);}
.interest-tile:hover{border-color:var(--border);color:var(--red);transform:translateY(-4px);box-shadow:0 8px 24px var(--shadow);}
.interest-tile .ico{font-size:1.8rem;display:block;margin-bottom:0.5rem;}
@media(max-width:900px){.about-layout{grid-template-columns:1fr;}.profile-card{position:static;}.interest-grid{grid-template-columns:1fr 1fr;}}
"""
about_body = """  <div class="page-header">
    <div class="page-eyebrow">// Who I Am</div>
    <h1 class="page-title">About <span class="accent">Me.</span></h1>
  </div>
  <div class="content">
    <div class="about-layout">
      <div class="reveal-left">
        <div class="profile-card">
          <div class="profile-banner"><div class="banner-logo">PG</div></div>
          <div class="profile-avatar">🧑‍💻</div>
          <div class="profile-body">
            <div class="profile-name">Priyanshu Pandey</div>
            <div class="profile-role">BCA Student &amp; Web Developer</div>
            <a href="contact.html" class="btn btn-primary" style="width:100%;justify-content:center;font-size:0.82rem;">💬 Hire Me</a>
            <div class="p-divider"></div>
            <div class="info-list">
              <div class="info-row"><span class="info-ico">📍</span>New Ashok Nagar, East Delhi</div>
              <div class="info-row"><span class="info-ico">📧</span><a href="mailto:ompandit102@gmail.com">ompandit102@gmail.com</a></div>
              <div class="info-row"><span class="info-ico">📞</span><a href="tel:+918081818557">+91 8081818557</a></div>
              <div class="info-row"><span class="info-ico">🎓</span>BCA — GGSIPU (2023–26)</div>
              <div class="info-row"><span class="info-ico">⭐</span>CGPA 9.1 · 85.66%</div>
            </div>
          </div>
        </div>
      </div>
      <div class="about-body">
        <div class="reveal">
          <div class="s-label">// Introduction</div>
          <div class="s-title">Hello, I'm Priyanshu 👋</div>
          <div class="intro-text">
            <p>I'm a <strong>BCA student</strong> at Bosco Technical Training Society (GGSIPU) — maintaining a strong <span class="red">9.1 CGPA</span> and <span class="red">85.66%</span> score while actively building real-world web projects.</p>
            <p>I love turning ideas into beautiful, functional websites. From writing clean HTML/CSS to deploying live on Hostinger — I handle the full process. My creative background in <strong>photo &amp; video editing</strong> gives me a designer's eye that elevates everything I build.</p>
            <p>Always learning. Always building. Always growing — that's my motto. 🚀</p>
          </div>
        </div>
        <div class="reveal" data-delay="80">
          <div class="s-label">// Education</div>
          <div class="s-title">Academic Journey</div>
          <div class="edu-list">
            <div class="edu-card"><div class="edu-ico">🎓</div><div><div class="edu-degree">Bachelor of Computer Applications (BCA)</div><div class="edu-inst">Bosco Technical Training Society — GGSIPU</div><div class="edu-chips"><span class="chip chip-red">2023–2026</span><span class="chip chip-red">CGPA: 9.1</span><span class="chip chip-red">85.66%</span></div></div></div>
            <div class="edu-card"><div class="edu-ico">📚</div><div><div class="edu-degree">Class XII — PCMB</div><div class="edu-inst">UPMSP Board</div><div class="edu-chips"><span class="chip chip-dark">2020</span><span class="chip chip-dark">74.8%</span></div></div></div>
          </div>
        </div>
        <div class="reveal" data-delay="160">
          <div class="s-label">// Beyond Code</div>
          <div class="s-title">Interests &amp; Hobbies</div>
          <div class="interest-grid">
            <div class="interest-tile"><span class="ico">🌐</span>Web Dev</div>
            <div class="interest-tile"><span class="ico">🎨</span>Graphic Design</div>
            <div class="interest-tile"><span class="ico">🎬</span>Video Editing</div>
            <div class="interest-tile"><span class="ico">📸</span>Photography</div>
            <div class="interest-tile"><span class="ico">🤖</span>AI &amp; Tech</div>
            <div class="interest-tile"><span class="ico">📱</span>Social Media</div>
          </div>
        </div>
      </div>
    </div>
  </div>"""

# ============ SKILLS ============
skills_css = """
.skills-summary{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;margin-bottom:3rem;}
.sum-box{background:var(--card);border:1px solid var(--border-lt);border-radius:14px;padding:1.4rem;text-align:center;box-shadow:0 2px 10px var(--shadow2);transition:all 0.25s;position:relative;overflow:hidden;}
.sum-box::after{content:'';position:absolute;bottom:0;left:0;right:0;height:3px;background:var(--red);transform:scaleX(0);transition:transform 0.3s;}
.sum-box:hover::after{transform:scaleX(1);}
.sum-box:hover{transform:translateY(-3px);box-shadow:0 8px 24px var(--shadow);}
.sum-num{font-family:'Bebas Neue',sans-serif;font-size:2.4rem;color:var(--red);line-height:1;}
.sum-lbl{font-size:0.76rem;color:var(--muted);font-weight:600;margin-top:0.3rem;}
.skill-cat{margin-bottom:3rem;}
.skill-cat-hdr{display:flex;align-items:center;gap:1rem;margin-bottom:1.4rem;padding-bottom:1rem;border-bottom:2px solid var(--border-lt);}
.cat-ico{width:46px;height:46px;border-radius:12px;background:var(--red-soft);border:1px solid var(--border);display:flex;align-items:center;justify-content:center;font-size:1.3rem;flex-shrink:0;}
.cat-name{font-family:'Bebas Neue',sans-serif;font-size:1.3rem;letter-spacing:0.5px;color:var(--text);}
.cat-desc{font-size:0.78rem;color:var(--muted);font-weight:500;}
.skill-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(165px,1fr));gap:1rem;}
.skill-card{background:var(--card);border:1px solid var(--border-lt);border-radius:16px;padding:1.4rem 1rem 1.2rem;text-align:center;transition:all 0.3s cubic-bezier(0.4,0,0.2,1);cursor:default;position:relative;overflow:hidden;box-shadow:0 2px 8px var(--shadow2);}
.skill-card:hover{transform:translateY(-7px) scale(1.02);border-color:var(--border);box-shadow:0 14px 36px var(--shadow);}
.sk-icon{font-size:2.2rem;display:block;margin-bottom:0.6rem;}
.sk-name{font-weight:700;font-size:0.88rem;color:var(--text);margin-bottom:0.6rem;}
.sk-bar{height:3px;border-radius:100px;background:var(--red-soft);overflow:hidden;margin-top:0.6rem;}
.sk-fill{height:100%;border-radius:100px;background:linear-gradient(90deg,var(--red),#ff6b6b);transform:scaleX(0);transform-origin:left;transition:transform 0.9s cubic-bezier(0.4,0,0.2,1) 0.2s;}
.skill-card.animate .sk-fill{transform:scaleX(1);}
.sk-sub{font-size:0.7rem;color:var(--muted);margin-top:0.35rem;}
@media(max-width:600px){.skills-summary{grid-template-columns:1fr 1fr;}}
"""
skills_body = """  <div class="page-header">
    <div class="page-eyebrow">// What I Know</div>
    <h1 class="page-title">Technical <span class="accent">Skills.</span></h1>
  </div>
  <div class="content">
    <div class="skills-summary reveal">
      <div class="sum-box"><div class="sum-num">4</div><div class="sum-lbl">Languages</div></div>
      <div class="sum-box"><div class="sum-num">4</div><div class="sum-lbl">Web Tech</div></div>
      <div class="sum-box"><div class="sum-num">4</div><div class="sum-lbl">Tools</div></div>
      <div class="sum-box"><div class="sum-num">4</div><div class="sum-lbl">Creative Apps</div></div>
    </div>
    <div class="skill-cat reveal">
      <div class="skill-cat-hdr"><div class="cat-ico">💻</div><div><div class="cat-name">Programming Languages</div><div class="cat-desc">Core languages I code in</div></div></div>
      <div class="skill-grid">
        <div class="skill-card"><span class="sk-icon">⚙️</span><div class="sk-name">C Language</div><div class="sk-bar"><div class="sk-fill"></div></div><div class="sk-sub">Fundamentals</div></div>
        <div class="skill-card"><span class="sk-icon">🐘</span><div class="sk-name">PHP</div><div class="sk-bar"><div class="sk-fill"></div></div><div class="sk-sub">Backend Dev</div></div>
        <div class="skill-card"><span class="sk-icon">🐍</span><div class="sk-name">Python</div><div class="sk-bar"><div class="sk-fill"></div></div><div class="sk-sub">Scripting</div></div>
        <div class="skill-card"><span class="sk-icon">🗄️</span><div class="sk-name">SQL</div><div class="sk-bar"><div class="sk-fill"></div></div><div class="sk-sub">Databases</div></div>
      </div>
    </div>
    <div class="skill-cat reveal">
      <div class="skill-cat-hdr"><div class="cat-ico">🌐</div><div><div class="cat-name">Web Technologies</div><div class="cat-desc">Front-end development stack</div></div></div>
      <div class="skill-grid">
        <div class="skill-card"><span class="sk-icon">🏗️</span><div class="sk-name">HTML5</div><div class="sk-bar"><div class="sk-fill"></div></div><div class="sk-sub">Markup</div></div>
        <div class="skill-card"><span class="sk-icon">🎨</span><div class="sk-name">CSS3</div><div class="sk-bar"><div class="sk-fill"></div></div><div class="sk-sub">Styling</div></div>
        <div class="skill-card"><span class="sk-icon">🅱️</span><div class="sk-name">Bootstrap</div><div class="sk-bar"><div class="sk-fill"></div></div><div class="sk-sub">Framework</div></div>
        <div class="skill-card"><span class="sk-icon">⚡</span><div class="sk-name">JavaScript</div><div class="sk-bar"><div class="sk-fill"></div></div><div class="sk-sub">Interactivity</div></div>
      </div>
    </div>
    <div class="skill-cat reveal">
      <div class="skill-cat-hdr"><div class="cat-ico">🛠️</div><div><div class="cat-name">Tools &amp; Platforms</div><div class="cat-desc">Productivity and deployment</div></div></div>
      <div class="skill-grid">
        <div class="skill-card"><span class="sk-icon">📝</span><div class="sk-name">MS Word</div><div class="sk-bar"><div class="sk-fill"></div></div><div class="sk-sub">Documentation</div></div>
        <div class="skill-card"><span class="sk-icon">📊</span><div class="sk-name">MS Excel</div><div class="sk-bar"><div class="sk-fill"></div></div><div class="sk-sub">Spreadsheets</div></div>
        <div class="skill-card"><span class="sk-icon">🤖</span><div class="sk-name">ChatGPT</div><div class="sk-bar"><div class="sk-fill"></div></div><div class="sk-sub">AI-Assisted Dev</div></div>
        <div class="skill-card"><span class="sk-icon">🚀</span><div class="sk-name">Hostinger</div><div class="sk-bar"><div class="sk-fill"></div></div><div class="sk-sub">Web Hosting</div></div>
      </div>
    </div>
    <div class="skill-cat reveal">
      <div class="skill-cat-hdr"><div class="cat-ico">🎨</div><div><div class="cat-name">Creative Suite</div><div class="cat-desc">Photo &amp; video editing</div></div></div>
      <div class="skill-grid">
        <div class="skill-card"><span class="sk-icon">🖼️</span><div class="sk-name">PicsArt</div><div class="sk-bar"><div class="sk-fill"></div></div><div class="sk-sub">Photo Editing</div></div>
        <div class="skill-card"><span class="sk-icon">🌅</span><div class="sk-name">Lightroom</div><div class="sk-bar"><div class="sk-fill"></div></div><div class="sk-sub">Color Grading</div></div>
        <div class="skill-card"><span class="sk-icon">🎬</span><div class="sk-name">CapCut</div><div class="sk-bar"><div class="sk-fill"></div></div><div class="sk-sub">Video Editing</div></div>
        <div class="skill-card"><span class="sk-icon">📽️</span><div class="sk-name">KineMaster</div><div class="sk-bar"><div class="sk-fill"></div></div><div class="sk-sub">Mobile Editing</div></div>
      </div>
    </div>
  </div>
  <script>
  const so=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('animate');so.unobserve(e.target);}});},{threshold:0.15});
  document.querySelectorAll('.skill-card').forEach(c=>so.observe(c));
  </script>"""

# ============ PROJECTS ============
projects_css = """
.proj-intro{color:var(--muted);font-size:0.97rem;max-width:600px;margin-bottom:2.5rem;line-height:1.8;}
.proj-grid{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-bottom:2.5rem;}
.proj-card{background:var(--card);border:1px solid var(--border-lt);border-radius:22px;overflow:hidden;transition:all 0.38s cubic-bezier(0.4,0,0.2,1);display:flex;flex-direction:column;box-shadow:0 3px 14px var(--shadow2);cursor:default;}
.proj-card:hover{transform:translateY(-9px);border-color:var(--border);box-shadow:0 22px 50px var(--shadow);}
.proj-preview{height:200px;position:relative;display:flex;align-items:center;justify-content:center;overflow:hidden;}
.prev-portfolio{background:linear-gradient(135deg,var(--cream),var(--bg2));}
.prev-gym{background:linear-gradient(135deg,#1a0a0a,#2d1010);}
.proj-preview::before{content:'';position:absolute;inset:0;background:repeating-linear-gradient(-55deg,transparent,transparent 18px,rgba(230,32,32,0.04) 18px,rgba(230,32,32,0.04) 36px);}
.proj-emoji{font-size:5rem;position:relative;z-index:1;transition:transform 0.38s cubic-bezier(0.34,1.56,0.64,1);filter:drop-shadow(0 6px 16px rgba(0,0,0,0.1));}
.proj-card:hover .proj-emoji{transform:scale(1.15) translateY(-6px);}
.proj-badge{position:absolute;top:1rem;right:1rem;background:var(--red);color:#fff;font-size:0.68rem;font-weight:700;padding:0.25rem 0.7rem;border-radius:100px;letter-spacing:0.05em;text-transform:uppercase;z-index:2;}
.proj-body{padding:1.6rem;flex:1;display:flex;flex-direction:column;}
.proj-name{font-family:'Bebas Neue',sans-serif;font-size:1.4rem;letter-spacing:0.5px;color:var(--text);margin-bottom:0.6rem;transition:color 0.25s;}
.proj-card:hover .proj-name{color:var(--red);}
.proj-desc{font-size:0.86rem;color:var(--muted);line-height:1.78;flex:1;margin-bottom:1rem;}
.proj-tags{display:flex;flex-wrap:wrap;gap:0.35rem;}
.proj-footer{display:flex;align-items:center;justify-content:space-between;margin-top:1.2rem;padding-top:1rem;border-top:1px solid var(--border-lt);}
.proj-cat{font-size:0.74rem;color:var(--muted);font-family:'DM Mono',monospace;}
.proj-arr{width:36px;height:36px;border-radius:50%;background:var(--cream);border:1px solid var(--border-lt);display:flex;align-items:center;justify-content:center;color:var(--muted);font-size:0.95rem;transition:all 0.25s;}
.proj-card:hover .proj-arr{background:var(--red);color:#fff;transform:rotate(45deg);border-color:var(--red);}
.proj-card.soon{opacity:0.45;border-style:dashed;}
.proj-card.soon:hover{transform:none;box-shadow:none;border-color:var(--border-lt);}
.proj-stats{display:grid;grid-template-columns:repeat(3,1fr);background:var(--red);border-radius:18px;padding:2rem;text-align:center;gap:1px;overflow:hidden;position:relative;}
.proj-stats::before{content:'';position:absolute;inset:0;background:repeating-linear-gradient(-45deg,transparent,transparent 20px,rgba(255,255,255,0.04) 20px,rgba(255,255,255,0.04) 40px);}
.ps-item{position:relative;z-index:1;}
.ps-num{font-family:'Bebas Neue',sans-serif;font-size:2.5rem;color:#fff;line-height:1;}
.ps-lbl{font-size:0.76rem;color:rgba(255,255,255,0.75);margin-top:0.2rem;font-weight:600;}
@media(max-width:700px){.proj-grid{grid-template-columns:1fr;}.proj-stats{grid-template-columns:1fr;gap:1.5rem;}}
"""
projects_body = """  <div class="page-header">
    <div class="page-eyebrow">// What I've Built</div>
    <h1 class="page-title">My <span class="accent">Projects.</span></h1>
  </div>
  <div class="content">
    <p class="proj-intro reveal">Showcase of academic and freelance work — built with attention to detail, responsive design, and a focus on creating great user experiences.</p>
    <div class="proj-grid">
      <div class="proj-card reveal">
        <div class="proj-preview prev-portfolio"><div class="proj-emoji">🗂️</div><span class="proj-badge">Academic</span></div>
        <div class="proj-body">
          <div class="proj-name">Portfolio Website</div>
          <div class="proj-desc">A personal portfolio to showcase skills, education, projects and contact info. Built with clean HTML/CSS and modern design — fully responsive.</div>
          <div class="proj-tags"><span class="chip chip-red">HTML</span><span class="chip chip-red">CSS</span><span class="chip chip-red">JavaScript</span><span class="chip chip-dark">Responsive</span></div>
          <div class="proj-footer"><span class="proj-cat">web-development</span><div class="proj-arr">↗</div></div>
        </div>
      </div>
      <div class="proj-card reveal" data-delay="120">
        <div class="proj-preview prev-gym"><div class="proj-emoji">💪</div><span class="proj-badge" style="background:var(--text)">Academic</span></div>
        <div class="proj-body">
          <div class="proj-name">GYM Website</div>
          <div class="proj-desc">Full gym landing page with membership plans, class schedules, trainer profiles, and a contact section. Bold, energetic visual design.</div>
          <div class="proj-tags"><span class="chip chip-red">HTML</span><span class="chip chip-red">CSS</span><span class="chip chip-red">Bootstrap</span><span class="chip chip-dark">UI Design</span></div>
          <div class="proj-footer"><span class="proj-cat">web-development</span><div class="proj-arr">↗</div></div>
        </div>
      </div>
      <div class="proj-card soon reveal" data-delay="240">
        <div class="proj-preview" style="background:var(--cream)"><div class="proj-emoji" style="opacity:0.3">🔮</div></div>
        <div class="proj-body"><div class="proj-name" style="opacity:0.4">Coming Soon</div><div class="proj-desc">New project in development. Stay tuned!</div><div class="proj-footer"><span class="proj-cat">🚧 in progress</span></div></div>
      </div>
      <div class="proj-card soon reveal" data-delay="360">
        <div class="proj-preview" style="background:var(--cream)"><div class="proj-emoji" style="opacity:0.3">✨</div></div>
        <div class="proj-body"><div class="proj-name" style="opacity:0.4">Coming Soon</div><div class="proj-desc">Another exciting project in the pipeline!</div><div class="proj-footer"><span class="proj-cat">🚧 planning</span></div></div>
      </div>
    </div>
    <div class="proj-stats reveal">
      <div class="ps-item"><div class="ps-num">2</div><div class="ps-lbl">Completed Projects</div></div>
      <div class="ps-item"><div class="ps-num">100%</div><div class="ps-lbl">Academic Grade</div></div>
      <div class="ps-item"><div class="ps-num">∞</div><div class="ps-lbl">More In Progress</div></div>
    </div>
  </div>"""

# ============ EXPERIENCE ============
exp_css = """
.exp-layout{display:grid;grid-template-columns:1fr 270px;gap:2.5rem;align-items:start;}
.timeline{position:relative;}
.timeline::before{content:'';position:absolute;left:22px;top:0;bottom:0;width:2px;background:linear-gradient(180deg,var(--red),rgba(230,32,32,0.1));}
.tl-entry{display:flex;gap:2rem;margin-bottom:2.5rem;position:relative;padding-left:0.5rem;}
.tl-dot-wrap{flex-shrink:0;position:relative;z-index:1;}
.tl-dot{width:44px;height:44px;border-radius:50%;background:var(--card);border:2px solid var(--red);display:flex;align-items:center;justify-content:center;font-size:1.1rem;box-shadow:0 3px 12px var(--shadow);transition:all 0.3s;}
.tl-entry:hover .tl-dot{transform:scale(1.12);box-shadow:0 6px 20px var(--shadow);}
.tl-card{background:var(--card);border:1px solid var(--border-lt);border-radius:18px;padding:1.7rem;flex:1;transition:all 0.3s;box-shadow:0 2px 10px var(--shadow2);position:relative;overflow:hidden;}
.tl-card::before{content:'';position:absolute;top:0;left:0;bottom:0;width:3px;background:var(--red);transform:scaleY(0);transition:transform 0.3s;transform-origin:top;}
.tl-entry:hover .tl-card{border-color:var(--border);transform:translateX(8px);box-shadow:0 8px 28px var(--shadow);}
.tl-entry:hover .tl-card::before{transform:scaleY(1);}
.tl-top{display:flex;align-items:flex-start;justify-content:space-between;flex-wrap:wrap;gap:0.5rem;margin-bottom:0.8rem;}
.tl-role{font-family:'Bebas Neue',sans-serif;font-size:1.2rem;letter-spacing:0.5px;color:var(--text);}
.tl-badge{font-size:0.72rem;font-weight:700;padding:0.25rem 0.7rem;border-radius:100px;letter-spacing:0.04em;text-transform:uppercase;}
.badge-fr{background:var(--red-soft);color:var(--red);border:1px solid var(--border);}
.badge-cr{background:rgba(26,10,10,0.06);color:var(--text);border:1px solid var(--border-lt);}
.badge-ed{background:var(--red-soft);color:var(--red);border:1px solid var(--border);}
.tl-desc{font-size:0.87rem;color:var(--muted);line-height:1.8;margin-bottom:1rem;}
.tl-ul{list-style:none;display:flex;flex-direction:column;gap:0.4rem;margin-bottom:1rem;}
.tl-ul li{display:flex;align-items:flex-start;gap:0.6rem;font-size:0.85rem;color:var(--muted);}
.tl-ul li::before{content:'▸';color:var(--red);flex-shrink:0;margin-top:0.1rem;font-weight:700;}
.tl-tools-lbl{font-size:0.68rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--muted);font-family:'DM Mono',monospace;margin-bottom:0.5rem;}
.tl-tools{display:flex;flex-wrap:wrap;gap:0.35rem;}
.exp-sidebar{display:flex;flex-direction:column;gap:1.3rem;}
.side-card{background:var(--card);border:1px solid var(--border-lt);border-radius:16px;padding:1.4rem;box-shadow:0 2px 10px var(--shadow2);position:relative;overflow:hidden;}
.side-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:var(--red);}
.side-title{font-family:'Bebas Neue',sans-serif;font-size:1rem;letter-spacing:0.5px;margin-bottom:1rem;color:var(--text);}
.stat-row2{display:flex;justify-content:space-between;align-items:center;font-size:0.83rem;margin-bottom:0.6rem;color:var(--muted);}
.stat-val{font-family:'Bebas Neue',sans-serif;font-size:1.15rem;color:var(--red);}
.soft-list{display:grid;grid-template-columns:1fr 1fr;gap:0.5rem;}
.soft-i{display:flex;align-items:center;gap:0.4rem;font-size:0.78rem;color:var(--muted);background:var(--cream);border-radius:8px;padding:0.45rem 0.6rem;}
@media(max-width:900px){.exp-layout{grid-template-columns:1fr;}}
"""
exp_body = """  <div class="page-header">
    <div class="page-eyebrow">// My Journey</div>
    <h1 class="page-title">Work <span class="accent">Experience.</span></h1>
  </div>
  <div class="content">
    <div class="exp-layout">
      <div class="timeline">
        <div class="tl-entry reveal">
          <div class="tl-dot-wrap"><div class="tl-dot">🌐</div></div>
          <div class="tl-card">
            <div class="tl-top"><div class="tl-role">Freelancer — Website Design</div><span class="tl-badge badge-fr">Freelance</span></div>
            <p class="tl-desc">Independently designed and deployed websites for clients using AI-assisted workflows and reliable hosting. Managed complete project lifecycle from design to deployment.</p>
            <ul class="tl-ul"><li>Designed responsive, mobile-first websites for clients</li><li>Used ChatGPT to accelerate development and solve challenges</li><li>Deployed on Hostinger with custom domain configuration</li><li>Managed client communication and revision cycles</li></ul>
            <div class="tl-tools-lbl">Tools</div>
            <div class="tl-tools"><span class="chip chip-red">HTML/CSS</span><span class="chip chip-red">JavaScript</span><span class="chip chip-dark">ChatGPT</span><span class="chip chip-dark">Hostinger</span></div>
          </div>
        </div>
        <div class="tl-entry reveal" data-delay="120">
          <div class="tl-dot-wrap"><div class="tl-dot">🎨</div></div>
          <div class="tl-card">
            <div class="tl-top"><div class="tl-role">Photo &amp; Video Editor</div><span class="tl-badge badge-cr">Creative</span></div>
            <p class="tl-desc">Created professional visual content including poster design, color-graded photo series, and polished short-form video edits for social media and personal projects.</p>
            <ul class="tl-ul"><li>Created eye-catching posters and digital artwork in PicsArt</li><li>Applied professional color grading in Lightroom &amp; Snapseed</li><li>Edited engaging short-form videos in CapCut and KineMaster</li></ul>
            <div class="tl-tools-lbl">Tools</div>
            <div class="tl-tools"><span class="chip chip-red">PicsArt</span><span class="chip chip-red">Lightroom</span><span class="chip chip-red">Snapseed</span><span class="chip chip-red">CapCut</span><span class="chip chip-dark">KineMaster</span></div>
          </div>
        </div>
        <div class="tl-entry reveal" data-delay="240">
          <div class="tl-dot-wrap"><div class="tl-dot">🎓</div></div>
          <div class="tl-card">
            <div class="tl-top"><div class="tl-role">BCA Student — GGSIPU</div><span class="tl-badge badge-ed">2023 – Present</span></div>
            <p class="tl-desc">Pursuing BCA at Bosco Technical Training Society (GGSIPU) with consistent 9.1 CGPA. Studying core computing, web technologies, databases, and software development.</p>
            <ul class="tl-ul"><li>Maintaining 85.66% overall score with 9.1 CGPA</li><li>Built academic projects: Portfolio Website &amp; GYM Website</li><li>Studying: C, PHP, Python, SQL, HTML/CSS, JavaScript</li></ul>
            <div class="tl-tools-lbl">Focus Areas</div>
            <div class="tl-tools"><span class="chip chip-red">Web Development</span><span class="chip chip-dark">Databases</span><span class="chip chip-gray">Programming</span></div>
          </div>
        </div>
      </div>
      <div class="exp-sidebar">
        <div class="side-card reveal-right">
          <div class="side-title">Quick Stats</div>
          <div class="stat-row2"><span>Freelance Projects</span><span class="stat-val">3+</span></div>
          <div class="stat-row2"><span>Creative Works</span><span class="stat-val">50+</span></div>
          <div class="stat-row2"><span>CGPA</span><span class="stat-val">9.1</span></div>
          <div class="stat-row2"><span>Tools Known</span><span class="stat-val">15+</span></div>
        </div>
        <div class="side-card reveal-right" data-delay="100">
          <div class="side-title">Creative Software</div>
          <div class="soft-list">
            <div class="soft-i"><span>🖼️</span>PicsArt</div><div class="soft-i"><span>🌅</span>Lightroom</div>
            <div class="soft-i"><span>🎬</span>CapCut</div><div class="soft-i"><span>📽️</span>KineMaster</div>
            <div class="soft-i"><span>📱</span>Snapseed</div>
          </div>
        </div>
        <div class="side-card reveal-right" data-delay="200">
          <div class="side-title">Open To</div>
          <p style="font-size:0.83rem;color:var(--muted);line-height:1.75;margin-bottom:1rem;">Freelance web projects, internships, and collaborative creative opportunities.</p>
          <a href="contact.html" class="btn btn-primary" style="width:100%;justify-content:center;font-size:0.82rem;">Get In Touch →</a>
        </div>
      </div>
    </div>
  </div>"""

# ============ CONTACT ============
contact_css = """
.contact-layout{display:grid;grid-template-columns:1fr 1.4fr;gap:2.5rem;align-items:start;}
.contact-intro{font-size:0.96rem;color:var(--muted);line-height:1.85;margin-bottom:1.5rem;}
.avail-bar{display:flex;align-items:center;gap:0.75rem;background:var(--red-soft);border:1px solid var(--border);border-radius:12px;padding:1rem 1.2rem;margin-bottom:1.5rem;font-size:0.84rem;}
.avail-dot{width:8px;height:8px;border-radius:50%;background:var(--red);flex-shrink:0;animation:blinkDot 2s ease-in-out infinite;}
@keyframes blinkDot{0%,100%{opacity:1}50%{opacity:0.3}}
.avail-text{color:var(--muted);}.avail-text strong{color:var(--red);}
.c-cards{display:flex;flex-direction:column;gap:0.8rem;}
.c-card{display:flex;align-items:center;gap:0.9rem;padding:1rem 1.2rem;background:var(--card);border:1px solid var(--border-lt);border-radius:14px;text-decoration:none;color:var(--text);font-size:0.87rem;transition:all 0.25s;box-shadow:0 2px 8px var(--shadow2);}
.c-card:hover{border-color:var(--border);transform:translateX(6px);box-shadow:0 6px 20px var(--shadow);}
.c-ico{width:40px;height:40px;border-radius:10px;background:var(--red-soft);display:flex;align-items:center;justify-content:center;font-size:1.1rem;flex-shrink:0;}
.c-lbl{font-size:0.68rem;color:var(--muted);text-transform:uppercase;letter-spacing:0.08em;}
.c-val{font-weight:600;font-size:0.88rem;color:var(--text);}
.c-arr{margin-left:auto;color:var(--muted);transition:all 0.2s;}
.c-card:hover .c-arr{color:var(--red);transform:translateX(3px);}
.map-box{margin-top:1rem;background:var(--card);border:1px solid var(--border-lt);border-radius:14px;height:130px;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:0.4rem;font-size:0.82rem;color:var(--muted);position:relative;overflow:hidden;box-shadow:0 2px 8px var(--shadow2);}
.map-box::before{content:'';position:absolute;inset:0;background:repeating-linear-gradient(0deg,transparent,transparent 28px,var(--red-soft) 28px,var(--red-soft) 29px),repeating-linear-gradient(90deg,transparent,transparent 28px,var(--red-soft) 28px,var(--red-soft) 29px);}
.map-pin{font-size:1.8rem;position:relative;z-index:1;animation:pinBounce 2.5s ease-in-out infinite;}
@keyframes pinBounce{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
.gform-wrap{background:var(--card);border:1px solid var(--border-lt);border-radius:22px;overflow:hidden;box-shadow:0 4px 24px var(--shadow2);position:relative;}
.gform-top{background:var(--red);padding:1.6rem 2rem;position:relative;overflow:hidden;}
.gform-top::before{content:'';position:absolute;inset:0;background:repeating-linear-gradient(-45deg,transparent,transparent 16px,rgba(255,255,255,0.06) 16px,rgba(255,255,255,0.06) 32px);}
.gform-logo{position:absolute;top:1rem;right:1.5rem;width:42px;height:42px;border-radius:50%;background:rgba(255,255,255,0.2);border:2px solid rgba(255,255,255,0.35);display:flex;align-items:center;justify-content:center;font-family:'Bebas Neue',sans-serif;font-size:0.95rem;color:#fff;animation:logoPulse 4s ease-in-out infinite;}
.gform-title{font-family:'Bebas Neue',sans-serif;font-size:1.5rem;letter-spacing:1px;color:#fff;position:relative;z-index:1;}
.gform-sub{font-size:0.8rem;color:rgba(255,255,255,0.75);margin-top:0.2rem;position:relative;z-index:1;}
.form-tabs{display:flex;border-bottom:1px solid var(--border-lt);background:var(--cream);}
.tab-btn{flex:1;padding:0.9rem;font-size:0.83rem;font-weight:700;font-family:'Outfit',sans-serif;color:var(--muted);border:none;background:transparent;cursor:pointer;transition:all 0.25s;border-bottom:2px solid transparent;margin-bottom:-1px;}
.tab-btn.active{color:var(--red);border-bottom-color:var(--red);background:var(--card);}
.tab-btn:hover:not(.active){color:var(--text);background:var(--red-soft);}
.tab-content{display:none;}.tab-content.active{display:block;}
.gform-iframe{width:100%;height:580px;border:none;display:block;}
.gform-note{padding:0.8rem 1.5rem;background:var(--red-soft);border-top:1px solid var(--border-lt);font-size:0.74rem;color:var(--muted);display:flex;align-items:center;gap:0.5rem;}
.direct-form{padding:1.5rem 2rem;}
.direct-form p.note{font-size:0.82rem;color:var(--muted);background:var(--red-soft);border:1px solid var(--border);border-radius:10px;padding:0.9rem 1rem;margin-bottom:1.2rem;line-height:1.65;}
.direct-form p.note strong{color:var(--red);}
.form-group{display:flex;flex-direction:column;gap:0.4rem;margin-bottom:1rem;}
label{font-size:0.75rem;font-weight:700;color:var(--muted);letter-spacing:0.06em;text-transform:uppercase;}
.form-row2{display:grid;grid-template-columns:1fr 1fr;gap:1rem;}
.submit-row{display:flex;align-items:center;justify-content:space-between;gap:1rem;margin-top:0.5rem;}
.submit-note{font-size:0.74rem;color:var(--muted);}
.success-box{display:none;text-align:center;padding:3rem 2rem;}
.success-box.show{display:block;}
.succ-icon{font-size:3rem;animation:popIn 0.5s cubic-bezier(0.175,0.885,0.32,1.275) both;}
@keyframes popIn{from{transform:scale(0);opacity:0}to{transform:scale(1);opacity:1}}
.succ-title{font-family:'Bebas Neue',sans-serif;font-size:1.5rem;margin:0.8rem 0 0.4rem;color:var(--red);}
.succ-text{font-size:0.86rem;color:var(--muted);}
.soc-row{display:flex;gap:0.6rem;margin-top:1.2rem;flex-wrap:wrap;}
.soc-btn{display:inline-flex;align-items:center;gap:0.5rem;padding:0.55rem 1rem;border-radius:10px;font-size:0.8rem;font-weight:700;text-decoration:none;border:1.5px solid var(--border-lt);color:var(--muted);background:var(--card);transition:all 0.22s;}
.soc-btn:hover{border-color:var(--red);color:var(--red);transform:translateY(-2px);}
@media(max-width:900px){.contact-layout{grid-template-columns:1fr;}.form-row2{grid-template-columns:1fr;}}
"""
contact_body = """  <div class="page-header">
    <div class="page-eyebrow">// Let's Connect</div>
    <h1 class="page-title">Get In <span class="accent">Touch.</span></h1>
  </div>
  <div class="content">
    <div class="contact-layout">
      <div>
        <p class="contact-intro reveal">Have a project, a freelance opportunity, or just want to say hello? I'd love to hear from you. Choose your preferred way to reach out!</p>
        <div class="avail-bar reveal"><div class="avail-dot"></div><div class="avail-text"><strong>Currently Available</strong> — Open to freelance &amp; internship opportunities</div></div>
        <div class="c-cards">
          <a href="mailto:ompandit102@gmail.com" class="c-card reveal"><div class="c-ico">📧</div><div><div class="c-lbl">Email</div><div class="c-val">ompandit102@gmail.com</div></div><span class="c-arr">→</span></a>
          <a href="tel:+918081818557" class="c-card reveal" data-delay="60"><div class="c-ico">📞</div><div><div class="c-lbl">Phone</div><div class="c-val">+91 8081818557</div></div><span class="c-arr">→</span></a>
          <div class="c-card reveal" data-delay="120" style="cursor:default;"><div class="c-ico">📍</div><div><div class="c-lbl">Location</div><div class="c-val">New Ashok Nagar, East Delhi</div></div></div>
        </div>
        <div class="soc-row reveal" data-delay="180">
          <a href="mailto:ompandit102@gmail.com" class="soc-btn">📬 Email Me</a>
          <a href="tel:+918081818557" class="soc-btn">📞 Call Me</a>
        </div>
        <div class="map-box reveal" data-delay="240"><span class="map-pin">📍</span><span>Delhi, India</span></div>
      </div>
      <div class="reveal-right">
        <div class="gform-wrap">
          <div class="gform-top">
            <div class="gform-logo">PG</div>
            <div class="gform-title">Send a Message</div>
            <div class="gform-sub">Powered by Google Forms — responses go straight to Priyanshu</div>
          </div>
          <div class="form-tabs">
            <button class="tab-btn active" onclick="switchTab('google',this)">🔗 Google Form</button>
            <button class="tab-btn" onclick="switchTab('direct',this)">✏️ Direct Form</button>
          </div>
          <div class="tab-content active" id="tab-google">
            <iframe class="gform-iframe"
              src="https://docs.google.com/forms/d/e/YOUR_GOOGLE_FORM_ID/viewform?embedded=true"
              frameborder="0" marginheight="0" marginwidth="0" title="Contact Form" loading="lazy">
              Loading Google Form...
            </iframe>
            <div class="gform-note">🔒 Secured by Google &nbsp;|&nbsp;
              <a href="https://docs.google.com/forms/d/e/YOUR_GOOGLE_FORM_ID/viewform" target="_blank" style="color:var(--red);font-weight:600;text-decoration:none;">Open in new tab ↗</a>
            </div>
          </div>
          <div class="tab-content" id="tab-direct">
            <div class="direct-form">
              <p class="note"><strong>📌 Setup:</strong> Replace <code>YOUR_GOOGLE_FORM_ID</code> above with your actual Google Form ID. Until then, use this form — it pre-fills your email client!</p>
              <div id="directFormContent">
                <div class="form-row2">
                  <div class="form-group"><label>First Name</label><input type="text" id="fn" placeholder="Rahul" required></div>
                  <div class="form-group"><label>Last Name</label><input type="text" id="ln" placeholder="Sharma"></div>
                </div>
                <div class="form-group"><label>Email Address</label><input type="email" id="em" placeholder="rahul@example.com" required></div>
                <div class="form-group"><label>Subject</label>
                  <select id="subj"><option>Freelance Web Project</option><option>Collaboration</option><option>Internship Opportunity</option><option>Feedback</option><option>Just Saying Hello</option><option>Other</option></select>
                </div>
                <div class="form-group"><label>Message</label><textarea id="msg" placeholder="Tell me about your project or opportunity..." required></textarea></div>
                <div class="submit-row"><span class="submit-note">🔒 Opens your email client</span><button class="btn btn-primary" onclick="sendEmail()">Send Message →</button></div>
              </div>
              <div class="success-box" id="successBox">
                <div class="succ-icon">✅</div>
                <div class="succ-title">Email Ready!</div>
                <div class="succ-text">Your email client opened with the message pre-filled. Just hit send!</div>
                <button class="btn btn-outline" onclick="resetDirect()" style="margin-top:1rem;">Send Another</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <script>
  function switchTab(id,btn){
    document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(c=>c.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById('tab-'+id).classList.add('active');
  }
  function sendEmail(){
    const fn=document.getElementById('fn').value.trim(),ln=document.getElementById('ln').value.trim(),em=document.getElementById('em').value.trim(),subj=document.getElementById('subj').value,msg=document.getElementById('msg').value.trim();
    if(!fn||!em||!msg){alert('Please fill in your name, email, and message.');return;}
    const name=fn+' '+ln,subject=encodeURIComponent('[Portfolio] '+subj+' — from '+name),body=encodeURIComponent('Hi Priyanshu,\\n\\n'+msg+'\\n\\nBest,\\n'+name+'\\n'+em);
    window.location.href='mailto:ompandit102@gmail.com?subject='+subject+'&body='+body;
    document.getElementById('directFormContent').style.display='none';
    document.getElementById('successBox').classList.add('show');
  }
  function resetDirect(){
    document.getElementById('successBox').classList.remove('show');
    document.getElementById('directFormContent').style.display='block';
    ['fn','ln','em','msg'].forEach(id=>document.getElementById(id).value='');
  }
  </script>"""

# Generate all pages
pages = {
    "about.html":      ("About",      about_css,    about_body),
    "skills.html":     ("Skills",     skills_css,   skills_body),
    "projects.html":   ("Projects",   projects_css, projects_body),
    "experience.html": ("Experience", exp_css,      exp_body),
    "contact.html":    ("Contact",    contact_css,  contact_body),
}

for fname, (title, css, body) in pages.items():
    content = page(title, css, body)
    with open(f"/home/claude/portfoliov3/{fname}", "w") as f:
        f.write(content)
    print(f"Written: {fname}")

print("All pages done!")
