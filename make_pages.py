# Helper to generate pages with shared sidebar/chatbot snippets

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
<button class="hamburger" aria-label="Menu"><span></span><span></span><span></span></button>"""

CHATBOT = """<!-- AI CHATBOT FAB -->
<button class="chat-fab" id="chatFab" aria-label="Chat">
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
    <input type="text" class="chat-input" id="chatInputField" placeholder="Ask me anything... 😊" maxlength="200">
    <button class="chat-send" id="chatSendBtn">
      <svg viewBox="0 0 24 24"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
    </button>
  </div>
</div>"""

print("snippet helper ready")
