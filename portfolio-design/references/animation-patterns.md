# Vanilla JS Animation Patterns

Purposeful animations without frameworks. All code is copy-paste ready.

---

## Principles

1. **60 FPS:** Use `transform` and `opacity` only (GPU-accelerated)
2. **Purposeful:** Every animation should enhance UX, not distract
3. **Reduced motion:** Respect `prefers-reduced-motion`
4. **Progressive enhancement:** Site works without JS

---

## 1. Intersection Observer (Scroll Animations)

**Use for:** Fade-in, slide-in on scroll

```javascript
// Fade in elements when they enter viewport
const observerOptions = {
  threshold: 0.1, // Trigger when 10% visible
  rootMargin: '0px 0px -50px 0px' // Start animation 50px before
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      // Optional: Stop observing after animation
      // observer.unobserve(entry.target);
    }
  });
}, observerOptions);

// Observe all elements with .animate-on-scroll
document.querySelectorAll('.animate-on-scroll').forEach(el => {
  observer.observe(el);
});
```

```css
.animate-on-scroll {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.6s ease-out, transform 0.6s ease-out;
}

.animate-on-scroll.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Respect user preferences */
@media (prefers-reduced-motion: reduce) {
  .animate-on-scroll {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
```

---

## 2. Typing Effect (Terminal/Hacker Theme)

**Use for:** Terminal aesthetics, dramatic text reveals

```javascript
function typeWriter(element, text, speed = 50, callback) {
  let i = 0;
  element.innerHTML = '';
  
  function type() {
    if (i < text.length) {
      element.innerHTML += text.charAt(i);
      i++;
      setTimeout(type, speed);
    } else if (callback) {
      callback();
    }
  }
  
  type();
}

// Usage
const terminal = document.querySelector('.terminal-text');
typeWriter(terminal, 'Welcome to my portfolio...', 50);

// Multiple lines
typeWriter(terminal, 'Line 1', 50, () => {
  terminal.innerHTML += '<br>';
  typeWriter(terminal, 'Line 2', 50);
});
```

```css
/* Blinking cursor */
.cursor {
  display: inline-block;
  width: 2px;
  height: 1.2em;
  background: currentColor;
  animation: blink 1s step-end infinite;
  vertical-align: middle;
}

@keyframes blink {
  50% { opacity: 0; }
}
```

---

## 3. Smooth Scroll (Anchor Links)

**Use for:** Single-page portfolios

```javascript
// Smooth scroll to anchors
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    
    if (target) {
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  });
});

// Optional: Update active nav item on scroll
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('nav a[href^="#"]');

window.addEventListener('scroll', () => {
  let current = '';
  
  sections.forEach(section => {
    const sectionTop = section.offsetTop;
    const sectionHeight = section.clientHeight;
    if (window.pageYOffset >= sectionTop - 100) {
      current = section.getAttribute('id');
    }
  });
  
  navLinks.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === `#${current}`) {
      link.classList.add('active');
    }
  });
});
```

```css
html {
  scroll-behavior: smooth;
}

/* Fallback for browsers without smooth scroll */
@media (prefers-reduced-motion: reduce) {
  html {
    scroll-behavior: auto;
  }
}
```

---

## 4. Parallax Scroll

**Use for:** Hero sections, depth effects

```javascript
// Simple parallax on scroll
window.addEventListener('scroll', () => {
  const scrolled = window.pageYOffset;
  const parallaxElements = document.querySelectorAll('.parallax');
  
  parallaxElements.forEach(el => {
    const speed = el.dataset.speed || 0.5;
    el.style.transform = `translateY(${scrolled * speed}px)`;
  });
});
```

```html
<div class="parallax" data-speed="0.5">
  <h1>Scroll to see parallax</h1>
</div>
```

```css
.parallax {
  will-change: transform; /* Hint to browser for optimization */
}
```

---

## 5. Image Lazy Loading

**Use for:** Performance optimization

```javascript
// Native lazy loading (modern browsers)
document.querySelectorAll('img[data-src]').forEach(img => {
  img.src = img.dataset.src;
  img.removeAttribute('data-src');
});

// OR Intersection Observer for older browsers
const imageObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      img.classList.add('loaded');
      imageObserver.unobserve(img);
    }
  });
});

document.querySelectorAll('img[data-src]').forEach(img => {
  imageObserver.observe(img);
});
```

```html
<img data-src="image.jpg" alt="Description" loading="lazy">
```

```css
img {
  opacity: 0;
  transition: opacity 0.3s;
}

img.loaded {
  opacity: 1;
}
```

---

## 6. Hover Effects (No JS)

**Use for:** Interactive elements

```css
/* Lift effect */
.card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
}

/* Underline animation */
.link {
  position: relative;
  text-decoration: none;
}

.link::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 2px;
  background: currentColor;
  transition: width 0.3s ease;
}

.link:hover::after {
  width: 100%;
}

/* Scale */
.image-hover {
  overflow: hidden;
}

.image-hover img {
  transition: transform 0.5s ease;
}

.image-hover:hover img {
  transform: scale(1.1);
}
```

---

## 7. Loading Spinner

**Use for:** Async operations

```html
<div class="spinner"></div>
```

```css
.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-top-color: #000;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

```javascript
// Show/hide spinner
function showLoading() {
  document.querySelector('.spinner').style.display = 'block';
}

function hideLoading() {
  document.querySelector('.spinner').style.display = 'none';
}
```

---

## 8. Modal / Lightbox

**Use for:** Image galleries, details

```javascript
// Simple modal
function openModal(content) {
  const modal = document.createElement('div');
  modal.className = 'modal';
  modal.innerHTML = `
    <div class="modal-content">
      <button class="modal-close">&times;</button>
      ${content}
    </div>
  `;
  
  document.body.appendChild(modal);
  document.body.style.overflow = 'hidden';
  
  // Close on click outside or X button
  modal.addEventListener('click', (e) => {
    if (e.target === modal || e.target.classList.contains('modal-close')) {
      closeModal(modal);
    }
  });
  
  // Close on Escape
  const escHandler = (e) => {
    if (e.key === 'Escape') {
      closeModal(modal);
      document.removeEventListener('keydown', escHandler);
    }
  };
  document.addEventListener('keydown', escHandler);
  
  // Animate in
  requestAnimationFrame(() => {
    modal.classList.add('visible');
  });
}

function closeModal(modal) {
  modal.classList.remove('visible');
  setTimeout(() => {
    modal.remove();
    document.body.style.overflow = '';
  }, 300);
}

// Usage
document.querySelectorAll('.gallery-img').forEach(img => {
  img.addEventListener('click', () => {
    openModal(`<img src="${img.src}" alt="${img.alt}">`);
  });
});
```

```css
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  transition: background 0.3s;
}

.modal.visible {
  background: rgba(0, 0, 0, 0.9);
}

.modal-content {
  max-width: 90%;
  max-height: 90%;
  opacity: 0;
  transform: scale(0.9);
  transition: opacity 0.3s, transform 0.3s;
}

.modal.visible .modal-content {
  opacity: 1;
  transform: scale(1);
}

.modal-close {
  position: absolute;
  top: 20px;
  right: 20px;
  font-size: 32px;
  background: none;
  border: none;
  color: white;
  cursor: pointer;
}
```

---

## 9. Glitch Effect (Cyberpunk Theme)

**Use for:** Cyberpunk, experimental aesthetics

```html
<h1 class="glitch" data-text="CYBERPUNK">CYBERPUNK</h1>
```

```css
.glitch {
  position: relative;
  font-size: 64px;
  font-weight: 900;
  color: #0FF;
}

.glitch::before,
.glitch::after {
  content: attr(data-text);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.glitch:hover::before {
  animation: glitch-1 0.3s infinite;
  color: #F0F;
  z-index: -1;
}

.glitch:hover::after {
  animation: glitch-2 0.3s infinite;
  color: #FF0;
  z-index: -2;
}

@keyframes glitch-1 {
  0%, 100% { transform: translate(0); }
  20% { transform: translate(-2px, 2px); }
  40% { transform: translate(-2px, -2px); }
  60% { transform: translate(2px, 2px); }
  80% { transform: translate(2px, -2px); }
}

@keyframes glitch-2 {
  0%, 100% { transform: translate(0); }
  20% { transform: translate(2px, -2px); }
  40% { transform: translate(2px, 2px); }
  60% { transform: translate(-2px, -2px); }
  80% { transform: translate(-2px, 2px); }
}
```

---

## 10. Progress Bar (Skills Section)

**Use for:** Visualizing skill levels

```javascript
function animateProgressBars() {
  const bars = document.querySelectorAll('.progress-bar');
  
  bars.forEach(bar => {
    const targetWidth = bar.dataset.progress;
    bar.style.width = '0%';
    
    // Animate when visible
    const observer = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting) {
        setTimeout(() => {
          bar.style.width = targetWidth + '%';
        }, 100);
        observer.disconnect();
      }
    });
    
    observer.observe(bar);
  });
}

animateProgressBars();
```

```html
<div class="skill">
  <span>JavaScript</span>
  <div class="progress-container">
    <div class="progress-bar" data-progress="90"></div>
  </div>
</div>
```

```css
.progress-container {
  width: 100%;
  height: 8px;
  background: #E5E7EB;
  border-radius: 4px;
  overflow: hidden;
}

.progress-bar {
  height: 100%;
  background: #0066FF;
  transition: width 1s ease-out;
}
```

---

## 11. Copy to Clipboard

**Use for:** Code snippets, contact info

```javascript
function copyToClipboard(text, button) {
  navigator.clipboard.writeText(text).then(() => {
    const originalText = button.textContent;
    button.textContent = 'Copied!';
    button.classList.add('copied');
    
    setTimeout(() => {
      button.textContent = originalText;
      button.classList.remove('copied');
    }, 2000);
  });
}

// Usage
document.querySelectorAll('.copy-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const text = btn.dataset.copy;
    copyToClipboard(text, btn);
  });
});
```

```html
<button class="copy-btn" data-copy="email@example.com">
  Copy Email
</button>
```

---

## 12. Dark Mode Toggle

**Use for:** User preference

```javascript
const darkModeToggle = document.querySelector('.dark-mode-toggle');
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');

// Check saved preference or system preference
const currentTheme = localStorage.getItem('theme') || 
  (prefersDark.matches ? 'dark' : 'light');

document.documentElement.setAttribute('data-theme', currentTheme);

darkModeToggle.addEventListener('click', () => {
  const current = document.documentElement.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
});
```

```css
:root[data-theme="light"] {
  --bg: #FFFFFF;
  --text: #1A1A1A;
}

:root[data-theme="dark"] {
  --bg: #1A1A1A;
  --text: #FFFFFF;
}

body {
  background: var(--bg);
  color: var(--text);
  transition: background 0.3s, color 0.3s;
}
```

---

## Performance Tips

1. **Use `will-change` sparingly:**
```css
.element-that-will-animate {
  will-change: transform;
}

/* Remove after animation */
.element-that-will-animate.done {
  will-change: auto;
}
```

2. **Debounce scroll events:**
```javascript
let timeout;
window.addEventListener('scroll', () => {
  clearTimeout(timeout);
  timeout = setTimeout(() => {
    // Your scroll code
  }, 100);
});
```

3. **Use `requestAnimationFrame` for smooth animations:**
```javascript
function animate() {
  // Animation code
  requestAnimationFrame(animate);
}
animate();
```

---

## Accessibility

Always include:

```css
/* Respect user motion preferences */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

```javascript
// Skip animations if user prefers reduced motion
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (!prefersReducedMotion) {
  // Run animations
}
```