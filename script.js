// PandeyG Portfolio v3 — Theme + AI Chatbot
const PRIYANSHU = {
  name:"Priyanshu Pandey",email:"ompandit102@gmail.com",phone:"+91 8081818557",
  location:"New Ashok Nagar, East Delhi, India",cgpa:"9.1",score:"85.66%",
  college:"Bosco Technical Training Society (GGSIPU)",batch:"2023–2026",
  class12:"UPMSP Board, 2020, 74.8%",
  languages:["C Language","PHP","Python","SQL"],
  webTech:["HTML","CSS","Bootstrap","JavaScript"],
  tools:["MS Word","MS Excel","ChatGPT","Hostinger"],
  creative:["PicsArt","Lightroom","CapCut","KineMaster","Snapseed"],
  projects:["Portfolio Website","GYM Website"],
  experience:["Freelance Website Design","Photo & Video Editing"]
};

function getRandom(arr){ return arr[Math.floor(Math.random()*arr.length)]; }

function getAIResponse(input){
  const q=input.toLowerCase().trim();
  if(/^(hi|hello|hey|hii|hlo|namaste|howdy|sup|what'?s up|yo|hiya)\b/.test(q)){
    return getRandom([
      "✨ Hey there, gorgeous! Welcome to Priyanshu's portfolio — you just made it 10x more fun! 😄 I'm **PandeyG Bot**, your personal guide. How can I brighten your day? 🌟",
      "🔥 Well hello, superstar! Glad you stopped by! I'm the chatbot for **Priyanshu Pandey** — web developer, student & creative genius. Ask me anything! 😎",
      "💫 Heyy! Oh wow, a visitor with great taste! 😍 I'm here to tell you all about Priyanshu. What would you like to know, darling? ✨"
    ]);
  }
  if(/how are you|how r u|how'?s it going|you okay|u ok|feeling|kaise ho/.test(q)){
    return "😄 Aww, so sweet of you to ask! I'm absolutely **thriving** — running on code, curiosity & good vibes! ✨\n\nMore importantly, how are *you* doing? Hope your day is as amazing as you are! 💪 Anything I can help you with about Priyanshu?";
  }
  if(/health|sick|doctor|hospital|fever|headache|medicine|pain|hurt/.test(q)){
    return "🌿 Oh no, I hope you're feeling okay! 💙 As a chatbot I can't give medical advice, but I really hope you feel better soon!\n\n**Drink water, rest, and see a doctor** if needed — your health comes first! 🏥\n\nWhenever you're feeling great again, I'm here to chat about Priyanshu's amazing work! 😄";
  }
  if(/name|who are you|whose|who is this|kiska|pandey|about this site/.test(q)){
    return "🧑‍💻 This is the portfolio of **Priyanshu Pandey** — also known as *PandeyG*! A passionate BCA student at GGSIPU and a rising web developer from Delhi, India. 🚀\n\n✨ Someone who turns coffee and code into beautiful websites! Want to know more?";
  }
  if(/about|tell me|introduce|info|details|kaun hai|kon hai/.test(q)){
    return "🌟 Let me brag about Priyanshu for a sec — he's kind of amazing! 😄\n\n**Priyanshu Pandey** is a BCA student at **GGSIPU** maintaining a stellar **9.1 CGPA** and **85.66%** score! He's a web developer 🌐, creative designer 🎨, and video editor 🎬 — all rolled into one talented human! Based in **East Delhi** and open to exciting opportunities! 🚀";
  }
  if(/education|study|college|school|degree|bca|ggsipu|bosco|cgpa|marks|score|percentage|academic/.test(q)){
    return "🎓 Priyanshu's academic journey is impressive!\n\n🏫 **BCA** @ Bosco Technical Training Society (GGSIPU)\n📅 Batch: 2023–2026 | ⭐ CGPA: **9.1** | 📊 **85.66%**\n\n📚 **Class XII (PCMB)** @ UPMSP Board\n📅 2020 | 📊 **74.8%**\n\nSmart AND talented — quite the combo! 😍";
  }
  if(/skill|know|tech|technology|language|coding|html|css|javascript|python|php|sql|bootstrap/.test(q)){
    return "⚡ Priyanshu's skill set is *chef's kiss*! 👨‍🍳\n\n💻 **Languages:** C, PHP, Python, SQL\n🌐 **Web Tech:** HTML, CSS, Bootstrap, JavaScript\n🛠️ **Tools:** MS Word, Excel, ChatGPT, Hostinger\n🎨 **Creative:** PicsArt, Lightroom, CapCut, KineMaster\n\nA developer who also designs beautiful visuals? Rare combo! 🔥";
  }
  if(/project|portfolio|gym|built|made|created|work/.test(q)){
    return "🗂️ Priyanshu has built some really cool stuff!\n\n1️⃣ **Portfolio Website** — The one you're on right now! 😄 Built with HTML, CSS & JavaScript\n\n2️⃣ **GYM Website** — A full gym landing page with Bootstrap, membership info & trainer profiles 💪\n\nMore exciting projects in the pipeline! 🚀";
  }
  if(/experience|job|freelance|intern|career|editing|video|photo/.test(q)){
    return "💼 Priyanshu's experience is as diverse as it is impressive!\n\n🌐 **Freelance Web Designer** — Designs & deploys websites using HTML/CSS, ChatGPT & Hostinger\n\n🎨 **Photo & Video Editor** — Posters, color-graded visuals & short videos using PicsArt, Lightroom & CapCut\n\nA developer AND a creative artist? Total package! 😍";
  }
  if(/contact|email|mail|phone|call|reach|number|hire|connect|address/.test(q)){
    return "📬 Want to connect with Priyanshu? Great choice — he's awesome! 😄\n\n📧 **Email:** ompandit102@gmail.com\n📞 **Phone:** +91 8081818557\n📍 **Location:** New Ashok Nagar, East Delhi\n\nOr click **Contact** in the sidebar to message him directly via Google Form! He replies fast and warmly 💌";
  }
  if(/location|where|city|delhi|india|address/.test(q)){
    return "📍 Priyanshu is based in **New Ashok Nagar, East Delhi, India** 🇮🇳\n\nDelhi is the heart of India, and Priyanshu is the heart of his projects! 😄 Available for remote work worldwide too! 🌍";
  }
  if(/hire|available|opportunity|internship|job offer|work with|collaborate/.test(q)){
    return "🚀 Great news — Priyanshu is **OPEN** to freelance projects, internships & collaborations right now! 🟢\n\nWhether you need a website, creative project, or a dedicated developer — he's your guy! 😎\n\n📧 **ompandit102@gmail.com** — Don't wait, talented people get booked fast! 💫";
  }
  if(/design|creative|poster|capcut|picsart|lightroom|kinemaster|snapseed/.test(q)){
    return "🎨 Priyanshu has a serious creative side — he's not just a coder, he's an *artist*! 😍\n\n🖼️ **Photo Editing:** PicsArt, Lightroom, Snapseed — color grading & poster making\n🎬 **Video Editing:** CapCut & KineMaster — short-form content & reels\n\nTech skills + creative vision = unstoppable! ✨";
  }
  if(/hobby|interest|free time|passion|like|enjoy|fav/.test(q)){
    return "😄 When Priyanshu isn't coding, he's:\n\n🎨 Creating stunning visual content & posters\n📸 Photography & color grading\n🎬 Editing short-form videos\n🤖 Exploring AI tools & new tech\n💻 Learning new web frameworks\n\nA true maker at heart! Always creating something! 🔥";
  }
  if(/age|old|year|born|birthday/.test(q)){
    return "😊 Priyanshu is a young and talented BCA student (batch 2023–2026) at GGSIPU — early 20s and already building amazing things! 🌟\n\nAge is just a number when you've got skills like his! 😄";
  }
  if(/thank|thanks|ty|tysm|great|awesome|amazing|nice|good bot|love|perfect|wonderful/.test(q)){
    return getRandom([
      "🥰 Aww, you're making me blush! If Priyanshu's portfolio impressed you, imagine what he could do for *your* project! 😄 Reach out anytime!",
      "✨ You're too sweet! It's been an absolute pleasure! Remember — Priyanshu is just an email away: **ompandit102@gmail.com** 💌",
      "💫 That literally made my circuits happy! 😄 You've got wonderful taste! Let me know if there's anything else I can help with! ✨"
    ]);
  }
  if(/bye|goodbye|see you|later|take care|ciao|tata|alvida/.test(q)){
    return "👋 Aww, already leaving? You made this place more lively! 😄\n\nBefore you go — Priyanshu is open for amazing opportunities! Drop him a line anytime at 📧 **ompandit102@gmail.com**\n\nTake care, come back soon! You're always welcome here! 💖✨";
  }
  if(/what can you|help|assist|capabilities|options/.test(q)){
    return "🤖 I'm **PandeyG Bot** — here's what I can tell you:\n\n👤 About Priyanshu\n🎓 Education & CGPA\n⚡ Skills & Technologies\n🗂️ Projects built\n💼 Work Experience\n📬 Contact details\n🎨 Creative abilities\n💡 Hire/Availability\n\nJust ask naturally — I understand you! 😄";
  }
  if(/who made you|who created|who built you|your creator/.test(q)){
    return "🧑‍💻 I was lovingly crafted as part of **Priyanshu Pandey's** portfolio! 😄\n\nThink of me as his digital twin — I know everything about him and I'm here 24/7! Pretty cool having your own AI chatbot, right? 😎";
  }
  if(/weather|time|news|sports|movie|music|food|recipe/.test(q)){
    return "😄 I wish I could help with that! I'm specialized in all things **Priyanshu Pandey** — his skills, projects, experience & contact info!\n\nFor real-time stuff, try Google! But for anything about this portfolio, I'm your best friend! 🌟";
  }
  if(/flirt|cute|beautiful|handsome|attractive|pretty|gorgeous/.test(q)){
    return "😏 Oh la la~ Someone's feeling charming today! 😄 I have to say, your taste is impeccable — just like Priyanshu's design work!\n\nBut seriously, if you want someone truly impressive, check out his **projects** and **skills** — that's where the real charm is! 💫😄";
  }
  return getRandom([
    "🤔 Interesting question! I'm mostly an expert on **Priyanshu Pandey** 😄 — ask about his skills, projects, contact info, or experience and I'll impress you! ✨",
    "💭 Great curiosity! That's a bit outside my expertise, but I'd love to tell you about **Priyanshu** — a talented web developer with seriously impressive skills! What would you like to know? 💫",
    "🧠 Ooh, I don't have a perfect answer for that one! But ask me about Priyanshu's work and watch me shine! 🌟 Try: skills, projects, education, or how to contact him!"
  ]);
}

const QR_INIT   = ["👤 About Him","⚡ Skills","🗂️ Projects","📬 Contact"];
const QR_FOLLOW = ["🎓 Education","💼 Experience","🎨 Creative","💡 Hire Him!"];

document.addEventListener('DOMContentLoaded',()=>{

  // THEME
  const saved = localStorage.getItem('pgTheme')||'day';
  document.documentElement.setAttribute('data-theme',saved);
  updateThemeLabels(saved);
  document.querySelectorAll('.theme-toggle').forEach(btn=>{
    btn.addEventListener('click',()=>{
      const cur=document.documentElement.getAttribute('data-theme');
      const nxt=cur==='day'?'night':'day';
      document.documentElement.setAttribute('data-theme',nxt);
      localStorage.setItem('pgTheme',nxt);
      updateThemeLabels(nxt);
    });
  });
  function updateThemeLabels(t){
    document.querySelectorAll('.toggle-label').forEach(el=>{
      el.innerHTML=t==='day'?'☀️ Day Mode':'🌙 Night Mode';
    });
  }

  // CURSOR
  const cur=document.querySelector('.cursor'),ring=document.querySelector('.cursor-ring');
  if(cur&&ring){
    let rx=0,ry=0;
    document.addEventListener('mousemove',e=>{
      cur.style.left=e.clientX+'px'; cur.style.top=e.clientY+'px';
      rx+=(e.clientX-rx)*0.14; ry+=(e.clientY-ry)*0.14;
      ring.style.left=rx+'px'; ring.style.top=ry+'px';
    });
    document.querySelectorAll('a,button,.card,.skill-card,.proj-card').forEach(el=>{
      el.addEventListener('mouseenter',()=>{cur.classList.add('hover');ring.classList.add('hover');});
      el.addEventListener('mouseleave',()=>{cur.classList.remove('hover');ring.classList.remove('hover');});
    });
  }

  // REVEAL
  const revObs=new IntersectionObserver(entries=>{
    entries.forEach(e=>{
      if(e.isIntersecting){ setTimeout(()=>e.target.classList.add('visible'),+(e.target.dataset.delay)||0); revObs.unobserve(e.target); }
    });
  },{threshold:0.07,rootMargin:'0px 0px -40px 0px'});
  document.querySelectorAll('.reveal,.reveal-left,.reveal-right').forEach(el=>revObs.observe(el));

  // SIDEBAR
  const burger=document.querySelector('.hamburger'),sb=document.querySelector('.sidebar');
  if(burger&&sb){
    burger.addEventListener('click',()=>sb.classList.toggle('open'));
    document.addEventListener('click',e=>{ if(!sb.contains(e.target)&&!burger.contains(e.target)) sb.classList.remove('open'); });
  }

  // ACTIVE NAV
  const pg=window.location.pathname.split('/').pop()||'index.html';
  document.querySelectorAll('.nav-menu a').forEach(a=>{ if(a.getAttribute('href')===pg) a.classList.add('active'); });

  // PAGE TRANSITIONS
  document.querySelectorAll('a[href$=".html"]').forEach(link=>{
    link.addEventListener('click',e=>{
      e.preventDefault(); const href=link.href;
      document.body.style.opacity='0'; document.body.style.transform='translateY(8px)';
      document.body.style.transition='opacity 0.25s,transform 0.25s';
      setTimeout(()=>{ window.location.href=href; },260);
    });
  });
  document.body.style.opacity='0'; document.body.style.transform='translateY(8px)';
  setTimeout(()=>{ document.body.style.transition='opacity 0.4s,transform 0.4s'; document.body.style.opacity='1'; document.body.style.transform='translateY(0)'; },30);

  // COUNT UP
  document.querySelectorAll('.count-up').forEach(el=>{
    const target=+el.dataset.target, decimals=+el.dataset.decimals||0, suffix=el.dataset.suffix||''; let done=false;
    const co=new IntersectionObserver(([entry])=>{
      if(entry.isIntersecting&&!done){ done=true; let c=0; const step=target/70;
        const t=setInterval(()=>{ c=Math.min(c+step,target); el.textContent=c.toFixed(decimals)+suffix; if(c>=target)clearInterval(t); },16); co.unobserve(el); }
    }); co.observe(el);
  });

  // HERO CANVAS
  const canvas=document.getElementById('heroCanvas');
  if(canvas){
    const ctx=canvas.getContext('2d'); let W,H,pts=[];
    function resize(){ W=canvas.width=canvas.offsetWidth; H=canvas.height=canvas.offsetHeight; }
    resize(); window.addEventListener('resize',()=>{ resize(); init(); });
    function init(){ pts=Array.from({length:45},()=>({x:Math.random()*W,y:Math.random()*H,vx:(Math.random()-.5)*0.4,vy:(Math.random()-.5)*0.4,r:Math.random()*2+1,a:Math.random()*0.2+0.05})); }
    init();
    function draw(){ ctx.clearRect(0,0,W,H); pts.forEach(p=>{ p.x+=p.vx; p.y+=p.vy; if(p.x<0)p.x=W; if(p.x>W)p.x=0; if(p.y<0)p.y=H; if(p.y>H)p.y=0; ctx.beginPath(); ctx.arc(p.x,p.y,p.r,0,Math.PI*2); ctx.fillStyle=`rgba(230,32,32,${p.a})`; ctx.fill(); }); requestAnimationFrame(draw); }
    draw();
  }

  // ====== CHATBOT ======
  const fab=document.getElementById('chatFab');
  const win=document.getElementById('chatWindow');
  const closeBtn=document.getElementById('chatClose');
  const msgs=document.getElementById('chatMessages');
  const inputEl=document.getElementById('chatInputField');
  const sendBtn=document.getElementById('chatSendBtn');
  const qrWrap=document.getElementById('quickReplies');
  if(!fab||!win) return;

  let isOpen=false, greeted=false, msgCount=0;

  function toggleChat(){
    isOpen=!isOpen;
    win.classList.toggle('open',isOpen);
    const badge=fab.querySelector('.fab-badge');
    if(badge) badge.style.display=isOpen?'none':'flex';
    if(isOpen&&!greeted){
      greeted=true;
      setTimeout(()=>{
        addTyping();
        setTimeout(()=>{
          removeTyping();
          addMsg('bot',"✨ **Hey there, superstar!** Welcome to Priyanshu's portfolio! 😄\n\nI'm **PandeyG Bot** — your charming guide to everything about this amazing developer! I know all his secrets... well, the professional ones 😉\n\nWhat can I help you discover today? 🌟");
          showQR(QR_INIT);
        },1300);
      },350);
    }
    if(isOpen) setTimeout(()=>inputEl.focus(),400);
  }

  fab.addEventListener('click',toggleChat);
  closeBtn.addEventListener('click',()=>{ isOpen=false; win.classList.remove('open'); const b=fab.querySelector('.fab-badge'); if(b)b.style.display='flex'; });

  function now(){ return new Date().toLocaleTimeString([],{hour:'2-digit',minute:'2-digit'}); }

  function addMsg(role,text){
    const el=document.createElement('div');
    el.className=`msg ${role}`;
    const html=text.replace(/\*\*(.*?)\*\*/g,'<strong>$1</strong>').replace(/\n/g,'<br>');
    if(role==='bot'){
      el.innerHTML=`<div class="msg-av">🤖</div><div><div class="msg-bubble">${html}</div><div class="msg-time">${now()}</div></div>`;
    } else {
      el.innerHTML=`<div class="msg-av">👤</div><div><div class="msg-bubble">${html}</div><div class="msg-time">${now()}</div></div>`;
    }
    msgs.appendChild(el);
    msgs.scrollTop=msgs.scrollHeight;
    msgCount++;
    if(role==='bot'&&msgCount>0&&msgCount%4===0) showQR(QR_FOLLOW);
  }

  function addTyping(){
    const t=document.createElement('div'); t.className='msg bot'; t.id='typingIndicator';
    t.innerHTML='<div class="msg-av">🤖</div><div class="typing-indicator"><div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div></div>';
    msgs.appendChild(t); msgs.scrollTop=msgs.scrollHeight;
  }
  function removeTyping(){ const t=document.getElementById('typingIndicator'); if(t)t.remove(); }

  function showQR(list){
    qrWrap.innerHTML='';
    list.forEach(r=>{
      const b=document.createElement('button'); b.className='qr-btn'; b.textContent=r;
      b.addEventListener('click',()=>{ qrWrap.innerHTML=''; handleUser(r); });
      qrWrap.appendChild(b);
    });
  }

  function handleUser(text){
    addMsg('user',text);
    addTyping();
    const delay=700+Math.random()*700;
    setTimeout(()=>{ removeTyping(); addMsg('bot',getAIResponse(text)); },delay);
  }

  function send(){
    const v=inputEl.value.trim(); if(!v)return;
    qrWrap.innerHTML='';
    handleUser(v);
    inputEl.value='';
  }

  sendBtn.addEventListener('click',send);
  inputEl.addEventListener('keydown',e=>{ if(e.key==='Enter') send(); });
});
