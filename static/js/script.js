/* ==========================================
   AITEDS — Government AI Tender System
   script.js
   ========================================== */

/* =====================
   1. NETWORK CANVAS ANIMATION
   ===================== */
(function initCanvas() {
  const canvas = document.getElementById('networkCanvas');
  const ctx    = canvas.getContext('2d');
  let W, H, nodes = [], animId;

  const NUM_NODES = 55;
  const MAX_DIST  = 150;
  const NODE_COLOR = 'rgba(15,110,140,';
  const LINE_COLOR = 'rgba(15,110,140,';

  function resize() {
    W = canvas.width  = window.innerWidth;
    H = canvas.height = window.innerHeight;
  }

  function createNodes() {
    nodes = [];
    for (let i = 0; i < NUM_NODES; i++) {
      nodes.push({
        x:  Math.random() * W,
        y:  Math.random() * H,
        vx: (Math.random() - 0.5) * 0.45,
        vy: (Math.random() - 0.5) * 0.45,
        r:  Math.random() * 2 + 1.2,
      });
    }
  }
  // Role Modal Functions
function openRoleModal(action) {
    const modal = document.getElementById('roleModal');
    const modalContent = modal.querySelector('.role-modal-content h2');
    
    // Update modal title based on action
    if (action === 'login') {
        modalContent.textContent = 'Login - Select Your Role';
    } else {
        modalContent.textContent = 'Register - Select Your Role';
    }
    
    modal.style.display = 'flex';
    
    // Store the action for later use
    modal.setAttribute('data-action', action);
}

function closeRoleModal() {
    const modal = document.getElementById('roleModal');
    modal.style.display = 'none';
}

function redirectRole(role, action) {
    let url = '';
    
    if (role === 'officer') {
        if (action === 'login') {
            url = "{% url 'officer_login' %}";  // Will be replaced by Django template
        } else {
            url = "{% url 'officer_register' %}";  // Will be replaced by Django template
        }
    } else if (role === 'bidder') {
        if (action === 'login') {
            url = "{% url 'company_login' %}";  // Will be replaced by Django template
        } else {
            url = "{% url 'company_register' %}";  // Will be replaced by Django template
        }
    }
    
    window.location.href = url;
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('roleModal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}

// Rest of your existing JavaScript code remains the same

  function draw() {
    ctx.clearRect(0, 0, W, H);

    // Move nodes
    nodes.forEach(n => {
      n.x += n.vx;
      n.y += n.vy;
      if (n.x < 0 || n.x > W) n.vx *= -1;
      if (n.y < 0 || n.y > H) n.vy *= -1;
    });

    // Draw lines
    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        const dx   = nodes[i].x - nodes[j].x;
        const dy   = nodes[i].y - nodes[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < MAX_DIST) {
          const alpha = (1 - dist / MAX_DIST) * 0.35;
          ctx.beginPath();
          ctx.moveTo(nodes[i].x, nodes[i].y);
          ctx.lineTo(nodes[j].x, nodes[j].y);
          ctx.strokeStyle = LINE_COLOR + alpha + ')';
          ctx.lineWidth = 0.8;
          ctx.stroke();
        }
      }
    }

    // Draw nodes
    nodes.forEach(n => {
      ctx.beginPath();
      ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
      ctx.fillStyle = NODE_COLOR + '0.5)';
      ctx.fill();
    });

    animId = requestAnimationFrame(draw);
  }

  window.addEventListener('resize', () => {
    resize();
    createNodes();
  });

  resize();
  createNodes();
  draw();
})();


/* =====================
   2. NAVBAR SCROLL EFFECT
   ===================== */
const navbar    = document.getElementById('navbar');
const hamburger = document.getElementById('hamburger');
const navLinks  = document.querySelector('.nav-links');

window.addEventListener('scroll', () => {
  if (window.scrollY > 30) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

// Force scrolled on load since hero is dark
navbar.classList.add('scrolled');

// Hamburger
hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('open');
});

// Close menu on nav link click
document.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');

    // Active link
    document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
    link.classList.add('active');
  });
});


/* =====================
   3. TENDER FILTER FUNCTIONALITY
   ===================== */
const filterBtns = document.querySelectorAll('.filter-btn');
const tenderCards = document.querySelectorAll('.tender-card');

filterBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    // Remove active class from all buttons
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    
    // Filter functionality (demo - just for UI)
    const filter = btn.textContent;
    // In a real app, you'd filter the cards here
    // For demo, we'll just show a console message
    console.log(`Filtering by: ${filter}`);
    
    // Simulate filter animation
    tenderCards.forEach((card, index) => {
      card.style.opacity = '0.5';
      setTimeout(() => {
        card.style.opacity = '1';
      }, index * 100);
    });
  });
});


/* =====================
   4. TENDER VIEW BUTTONS
   ===================== */
document.querySelectorAll('.tender-view-btn').forEach(btn => {
  btn.addEventListener('click', (e) => {
    e.preventDefault();
    const card = btn.closest('.tender-card');
    const title = card.querySelector('.tender-title').textContent;
    alert(`Viewing details for: ${title}\n(This is a demo - full tender details would open in a new page)`);
  });
});


/* =====================
   5. INTERSECTION OBSERVER (animations)
   ===================== */
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const delay = el.dataset.delay || 0;
      setTimeout(() => {
        el.classList.add('visible');
      }, parseInt(delay));
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('[data-animate]').forEach(el => observer.observe(el));


/* =====================
   6. COUNTER ANIMATION
   ===================== */
const counters = document.querySelectorAll('.stat-num');
const countObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      animateCounter(entry.target);
      countObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.5 });

counters.forEach(c => countObserver.observe(c));

function animateCounter(el) {
  const target   = parseInt(el.dataset.count);
  const duration = 1800;
  const step     = Math.ceil(target / (duration / 16));
  let current    = 0;

  const timer = setInterval(() => {
    current += step;
    if (current >= target) {
      current = target;
      clearInterval(timer);
    }
    el.textContent = current.toLocaleString();
  }, 16);
}


/* =====================
   7. SMOOTH SCROLL NAV ACTIVE
   ===================== */
const sections = document.querySelectorAll('section[id]');
const navLinkEls = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(sec => {
    if (window.scrollY >= sec.offsetTop - 120) {
      current = sec.getAttribute('id');
    }
  });

  navLinkEls.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === '#' + current) {
      link.classList.add('active');
    }
  });
});


/* =====================
   8. 3D CARD MOUSE TILT
   ===================== */
const odishaCard = document.querySelector('.odisha-3d-card');
if (odishaCard) {
  odishaCard.addEventListener('mousemove', (e) => {
    const rect   = odishaCard.getBoundingClientRect();
    const x      = e.clientX - rect.left - rect.width  / 2;
    const y      = e.clientY - rect.top  - rect.height / 2;
    const rotateX = -(y / rect.height) * 15;
    const rotateY =  (x / rect.width)  * 15;

    odishaCard.style.transform = `perspective(1200px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.02)`;
  });

  odishaCard.addEventListener('mouseleave', () => {
    odishaCard.style.transform = 'perspective(1200px) rotateX(0) rotateY(0) scale(1)';
  });

  odishaCard.style.transition = 'transform 0.25s ease';
}


/* =====================
   9. DASHBOARD MOCK BARS HOVER
   ===================== */
document.querySelectorAll('.mock-bar-v').forEach(bar => {
  bar.addEventListener('mouseenter', () => {
    if (!bar.classList.contains('l1')) {
      bar.style.background = 'rgba(15,110,140,0.6)';
    }
  });
  bar.addEventListener('mouseleave', () => {
    if (!bar.classList.contains('l1')) {
      bar.style.background = 'rgba(15,110,140,0.3)';
    }
  });
});


/* =====================
   10. RIPPLE EFFECT ON BUTTONS
   ===================== */
document.querySelectorAll('.btn-primary, .btn-submit, .btn-demo, .btn-outline, .tender-view-btn').forEach(btn => {
  btn.addEventListener('click', function (e) {
    const circle = document.createElement('span');
    const diameter = Math.max(btn.clientWidth, btn.clientHeight);
    const radius = diameter / 2;
    const rect = btn.getBoundingClientRect();

    circle.style.cssText = `
      width:  ${diameter}px;
      height: ${diameter}px;
      left:   ${e.clientX - rect.left  - radius}px;
      top:    ${e.clientY - rect.top   - radius}px;
      position: absolute;
      border-radius: 50%;
      background: rgba(255,255,255,0.25);
      transform: scale(0);
      animation: ripple 0.5s linear;
      pointer-events: none;
    `;

    // Ensure relative positioning
    btn.style.position = 'relative';
    btn.style.overflow = 'hidden';
    btn.appendChild(circle);
    setTimeout(() => circle.remove(), 500);
  });
});

// Inject ripple keyframes
const rippleStyle = document.createElement('style');
rippleStyle.textContent = `
  @keyframes ripple {
    to { transform: scale(2.5); opacity: 0; }
  }
`;
document.head.appendChild(rippleStyle);


/* =====================
   11. LOADING SCREEN
   ===================== */
(function createLoader() {
  const loader = document.createElement('div');
  loader.id = 'loader';
  loader.innerHTML = `
    <div class="loader-inner">
      <div class="loader-emblem"><i class="fas fa-landmark"></i></div>
      <div class="loader-text">AITEDS</div>
      <div class="loader-bar"><div class="loader-progress"></div></div>
      <div class="loader-sub">Government of Odisha · Tender Evaluation System</div>
    </div>
  `;

  const loaderStyle = document.createElement('style');
  loaderStyle.textContent = `
    #loader {
      position: fixed; inset: 0;
      background: #0B1F3A;
      z-index: 9999;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-direction: column;
      transition: opacity 0.6s ease, visibility 0.6s;
    }
    #loader.hidden { opacity: 0; visibility: hidden; }

    .loader-inner { text-align: center; }

    .loader-emblem {
      width: 72px; height: 72px;
      background: linear-gradient(135deg, #0F6E8C, #C9922A);
      border-radius: 18px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 1.8rem;
      color: white;
      margin-bottom: 1.2rem;
      animation: loaderPulse 1.5s ease-in-out infinite;
      box-shadow: 0 10px 40px rgba(15,110,140,0.4);
    }

    @keyframes loaderPulse {
      0%,100% { transform: scale(1);    box-shadow: 0 10px 40px rgba(15,110,140,0.4); }
      50%      { transform: scale(1.07); box-shadow: 0 16px 50px rgba(15,110,140,0.6); }
    }

    .loader-text {
      font-family: 'Sora', sans-serif;
      font-size: 1.6rem;
      font-weight: 800;
      color: white;
      letter-spacing: 4px;
      margin-bottom: 1.5rem;
    }

    .loader-bar {
      width: 200px;
      height: 3px;
      background: rgba(255,255,255,0.1);
      border-radius: 2px;
      margin: 0 auto 1rem;
      overflow: hidden;
    }

    .loader-progress {
      height: 100%;
      background: linear-gradient(90deg, #0F6E8C, #E8B84B);
      border-radius: 2px;
      animation: loaderFill 1.6s ease forwards;
    }

    @keyframes loaderFill {
      from { width: 0%; }
      to   { width: 100%; }
    }

    .loader-sub {
      font-family: 'DM Sans', sans-serif;
      font-size: 0.78rem;
      color: rgba(255,255,255,0.4);
      letter-spacing: 0.5px;
    }
  `;

  document.head.appendChild(loaderStyle);
  document.body.appendChild(loader);

  window.addEventListener('load', () => {
    setTimeout(() => {
      loader.classList.add('hidden');
      setTimeout(() => loader.remove(), 700);
    }, 1800);
  });
  
})();