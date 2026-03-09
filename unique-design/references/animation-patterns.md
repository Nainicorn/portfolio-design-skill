# Animation Patterns — Multi-Stack Reference

Purposeful animations for every frontend stack. Copy-paste ready patterns organized by technique and framework.

---

## Principles (All Stacks)

1. **60 FPS:** Animate only `transform` and `opacity` (GPU-accelerated). Avoid animating `width`, `height`, `top`, `left`, `margin`, `padding`
2. **Purposeful:** Every animation enhances UX. If it doesn't help the user understand or navigate, remove it
3. **Reduced motion:** Always respect `prefers-reduced-motion`. Non-negotiable
4. **Progressive enhancement:** Site must work without JS. Animations are the cherry on top

---

## Stack Selection Guide

| Stack | Best Animation Tools | When to Use |
|-------|---------------------|-------------|
| Vanilla JS/CSS | CSS animations, Intersection Observer, GSAP (CDN) | Simple sites, landing pages, zero-dependency requirement |
| React | Framer Motion, GSAP + React, ReactBits, Aceternity UI | SPAs, complex interactions, component-based |
| Next.js | Framer Motion, GSAP, View Transitions API | Full apps with routing transitions |
| Vue | Vue transitions, Motion One, GSAP + Vue | Vue ecosystem projects |
| Svelte | Built-in transitions/animations, GSAP | Svelte ecosystem, simple + powerful |

---

## SECTION 1: Vanilla CSS/JS Patterns

### 1.1 Scroll-Triggered Fade-In (Intersection Observer)

```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

document.querySelectorAll('.animate-on-scroll').forEach(el => observer.observe(el));
```

```css
.animate-on-scroll {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease-out, transform 0.6s ease-out;
}
.animate-on-scroll.visible { opacity: 1; transform: translateY(0); }

/* Stagger children */
.stagger-group .animate-on-scroll:nth-child(1) { transition-delay: 0s; }
.stagger-group .animate-on-scroll:nth-child(2) { transition-delay: 0.1s; }
.stagger-group .animate-on-scroll:nth-child(3) { transition-delay: 0.2s; }
.stagger-group .animate-on-scroll:nth-child(4) { transition-delay: 0.3s; }

@media (prefers-reduced-motion: reduce) {
  .animate-on-scroll { opacity: 1; transform: none; transition: none; }
}
```

### 1.2 Typing Effect

```javascript
function typeWriter(element, text, speed = 50, callback) {
  let i = 0;
  element.textContent = '';
  function type() {
    if (i < text.length) {
      element.textContent += text.charAt(i);
      i++;
      setTimeout(type, speed);
    } else if (callback) callback();
  }
  type();
}

// Chain multiple lines
function typeLines(element, lines, speed = 50) {
  let lineIndex = 0;
  function nextLine() {
    if (lineIndex < lines.length) {
      const line = document.createElement('div');
      element.appendChild(line);
      typeWriter(line, lines[lineIndex], speed, () => {
        lineIndex++;
        nextLine();
      });
    }
  }
  nextLine();
}
```

### 1.3 Parallax Scroll

```javascript
// Performance-optimized with requestAnimationFrame
let ticking = false;
window.addEventListener('scroll', () => {
  if (!ticking) {
    requestAnimationFrame(() => {
      const scrolled = window.pageYOffset;
      document.querySelectorAll('[data-parallax]').forEach(el => {
        const speed = parseFloat(el.dataset.parallax) || 0.5;
        el.style.transform = `translateY(${scrolled * speed}px)`;
      });
      ticking = false;
    });
    ticking = true;
  }
});
```

```html
<div data-parallax="0.3">Slow layer</div>
<div data-parallax="0.6">Medium layer</div>
<div data-parallax="1.0">Fast layer</div>
```

### 1.4 Smooth Scroll + Active Nav

```javascript
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
});

// Active nav tracking
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('nav a[href^="#"]');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(link => {
        link.classList.toggle('active', link.getAttribute('href') === `#${entry.target.id}`);
      });
    }
  });
}, { threshold: 0.3 });
sections.forEach(s => observer.observe(s));
```

### 1.5 CSS-Only Hover Effects

```css
/* Card lift */
.card { transition: transform 0.3s ease, box-shadow 0.3s ease; }
.card:hover { transform: translateY(-8px); box-shadow: 0 12px 24px rgba(0,0,0,0.15); }

/* Underline reveal */
.link { position: relative; text-decoration: none; }
.link::after {
  content: ''; position: absolute; bottom: -2px; left: 0;
  width: 0; height: 2px; background: currentColor; transition: width 0.3s ease;
}
.link:hover::after { width: 100%; }

/* Image zoom in container */
.img-zoom { overflow: hidden; }
.img-zoom img { transition: transform 0.5s ease; }
.img-zoom:hover img { transform: scale(1.1); }

/* Magnetic button (JS needed) */
.magnetic-btn { transition: transform 0.2s ease; }
```

```javascript
// Magnetic button effect
document.querySelectorAll('.magnetic-btn').forEach(btn => {
  btn.addEventListener('mousemove', (e) => {
    const rect = btn.getBoundingClientRect();
    const x = (e.clientX - rect.left - rect.width / 2) * 0.3;
    const y = (e.clientY - rect.top - rect.height / 2) * 0.3;
    btn.style.transform = `translate(${x}px, ${y}px)`;
  });
  btn.addEventListener('mouseleave', () => {
    btn.style.transform = 'translate(0, 0)';
  });
});
```

### 1.6 Glitch Effect

```css
.glitch { position: relative; font-size: 64px; font-weight: 900; color: #0FF; }
.glitch::before, .glitch::after {
  content: attr(data-text); position: absolute; top: 0; left: 0; width: 100%; height: 100%;
}
.glitch:hover::before { animation: glitch-1 0.3s infinite; color: #F0F; z-index: -1; }
.glitch:hover::after { animation: glitch-2 0.3s infinite; color: #FF0; z-index: -2; }

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

### 1.7 Dark Mode Toggle

```javascript
const toggle = document.querySelector('.theme-toggle');
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');
const theme = localStorage.getItem('theme') || (prefersDark.matches ? 'dark' : 'light');
document.documentElement.setAttribute('data-theme', theme);

toggle.addEventListener('click', () => {
  const current = document.documentElement.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
});
```

### 1.8 Modal / Lightbox

```javascript
function openModal(content) {
  const modal = document.createElement('div');
  modal.className = 'modal';
  modal.innerHTML = `<div class="modal-content"><button class="modal-close" aria-label="Close">&times;</button>${content}</div>`;
  document.body.appendChild(modal);
  document.body.style.overflow = 'hidden';
  requestAnimationFrame(() => modal.classList.add('visible'));

  const close = () => { modal.classList.remove('visible'); setTimeout(() => { modal.remove(); document.body.style.overflow = ''; }, 300); };
  modal.addEventListener('click', (e) => { if (e.target === modal || e.target.classList.contains('modal-close')) close(); });
  document.addEventListener('keydown', function handler(e) { if (e.key === 'Escape') { close(); document.removeEventListener('keydown', handler); } });
}
```

### 1.9 Clip-Path Reveal (Page/Section Transitions)

```css
/* Circle reveal from center */
.reveal-circle {
  clip-path: circle(0% at 50% 50%);
  transition: clip-path 1s cubic-bezier(0.65, 0, 0.35, 1);
}
.reveal-circle.visible { clip-path: circle(150% at 50% 50%); }

/* Diagonal wipe */
.reveal-diagonal {
  clip-path: polygon(0 0, 0 0, 0 100%, 0 100%);
  transition: clip-path 0.8s cubic-bezier(0.65, 0, 0.35, 1);
}
.reveal-diagonal.visible { clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%); }

/* Garage door open (vertical slide up) */
.garage-door {
  position: fixed; top: 0; left: 0; width: 100%; height: 100%;
  background: #111; z-index: 9999;
  animation: garage-open 1.5s cubic-bezier(0.65, 0, 0.35, 1) 0.5s forwards;
}
@keyframes garage-open {
  0% { transform: translateY(0); }
  100% { transform: translateY(-100%); }
}
```

### 1.10 Number Counter Animation

```javascript
function animateCounter(element, target, duration = 2000) {
  const start = 0;
  const startTime = performance.now();

  function update(currentTime) {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
    const current = Math.round(start + (target - start) * eased);
    element.textContent = current.toLocaleString();
    if (progress < 1) requestAnimationFrame(update);
  }
  requestAnimationFrame(update);
}

// Trigger on scroll
const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const target = parseInt(entry.target.dataset.target);
      animateCounter(entry.target, target);
      counterObserver.unobserve(entry.target);
    }
  });
});
document.querySelectorAll('[data-target]').forEach(el => counterObserver.observe(el));
```

### 1.11 Wave Section Divider

```html
<div class="wave-divider">
  <svg viewBox="0 0 1200 120" preserveAspectRatio="none">
    <path d="M0,60 C200,120 400,0 600,60 C800,120 1000,0 1200,60 L1200,120 L0,120 Z" fill="currentColor"/>
  </svg>
</div>
```

```css
.wave-divider { width: 100%; overflow: hidden; line-height: 0; color: var(--next-section-bg); }
.wave-divider svg { width: 100%; height: 80px; }

/* Animated wave */
.wave-divider svg path {
  animation: wave-morph 8s ease-in-out infinite alternate;
}
@keyframes wave-morph {
  0% { d: path("M0,60 C200,120 400,0 600,60 C800,120 1000,0 1200,60 L1200,120 L0,120 Z"); }
  100% { d: path("M0,80 C200,20 400,100 600,40 C800,100 1000,20 1200,80 L1200,120 L0,120 Z"); }
}
```

### 1.12 Custom Cursor

```javascript
const cursor = document.createElement('div');
cursor.className = 'custom-cursor';
document.body.appendChild(cursor);

document.addEventListener('mousemove', (e) => {
  cursor.style.left = e.clientX + 'px';
  cursor.style.top = e.clientY + 'px';
});

// Grow cursor on interactive elements
document.querySelectorAll('a, button, [role="button"]').forEach(el => {
  el.addEventListener('mouseenter', () => cursor.classList.add('cursor-hover'));
  el.addEventListener('mouseleave', () => cursor.classList.remove('cursor-hover'));
});
```

```css
.custom-cursor {
  position: fixed; width: 20px; height: 20px;
  border: 2px solid var(--accent); border-radius: 50%;
  pointer-events: none; z-index: 99999;
  transform: translate(-50%, -50%);
  transition: width 0.2s, height 0.2s, background 0.2s;
}
.custom-cursor.cursor-hover {
  width: 50px; height: 50px;
  background: rgba(var(--accent-rgb), 0.1);
}
/* Hide default cursor */
* { cursor: none; }
/* Restore on touch devices */
@media (hover: none) { * { cursor: auto; } .custom-cursor { display: none; } }
```

---

## SECTION 2: React + Framer Motion Patterns

### 2.1 Scroll-Triggered Fade-In

```jsx
import { motion, useInView } from 'framer-motion';
import { useRef } from 'react';

function FadeInOnScroll({ children, delay = 0 }) {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: '-50px' });

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 30 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.6, delay, ease: 'easeOut' }}
    >
      {children}
    </motion.div>
  );
}
```

### 2.2 Staggered Children

```jsx
const containerVariants = {
  hidden: {},
  visible: {
    transition: { staggerChildren: 0.1, delayChildren: 0.2 }
  }
};

const itemVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.5 } }
};

function StaggeredList({ items }) {
  return (
    <motion.ul variants={containerVariants} initial="hidden" whileInView="visible" viewport={{ once: true }}>
      {items.map((item, i) => (
        <motion.li key={i} variants={itemVariants}>{item}</motion.li>
      ))}
    </motion.ul>
  );
}
```

### 2.3 Page Transitions (AnimatePresence)

```jsx
import { AnimatePresence, motion } from 'framer-motion';

const pageVariants = {
  initial: { opacity: 0, x: -20 },
  animate: { opacity: 1, x: 0 },
  exit: { opacity: 0, x: 20 }
};

function PageTransition({ children, key }) {
  return (
    <AnimatePresence mode="wait">
      <motion.div
        key={key}
        variants={pageVariants}
        initial="initial"
        animate="animate"
        exit="exit"
        transition={{ duration: 0.3 }}
      >
        {children}
      </motion.div>
    </AnimatePresence>
  );
}
```

### 2.4 Scroll-Linked Parallax

```jsx
import { motion, useScroll, useTransform } from 'framer-motion';

function ParallaxHero() {
  const { scrollY } = useScroll();
  const y = useTransform(scrollY, [0, 500], [0, 150]);
  const opacity = useTransform(scrollY, [0, 300], [1, 0]);

  return (
    <motion.div style={{ y, opacity }} className="hero">
      <h1>Scroll to see parallax</h1>
    </motion.div>
  );
}
```

### 2.5 Layout Animations (Shared Elements)

```jsx
import { motion, LayoutGroup } from 'framer-motion';

function TabContent({ activeTab, tabs }) {
  return (
    <LayoutGroup>
      <div className="tab-bar">
        {tabs.map(tab => (
          <button key={tab.id} onClick={() => setActive(tab.id)}>
            {tab.label}
            {activeTab === tab.id && (
              <motion.div className="tab-indicator" layoutId="tab-indicator" />
            )}
          </button>
        ))}
      </div>
    </LayoutGroup>
  );
}
```

### 2.6 Gesture Interactions

```jsx
function DraggableCard() {
  return (
    <motion.div
      drag
      dragConstraints={{ left: -100, right: 100, top: -50, bottom: 50 }}
      dragElastic={0.2}
      whileHover={{ scale: 1.05 }}
      whileTap={{ scale: 0.95 }}
      whileDrag={{ cursor: 'grabbing' }}
    >
      Drag me
    </motion.div>
  );
}
```

### 2.7 Reduced Motion Hook

```jsx
import { useReducedMotion } from 'framer-motion';

function AnimatedComponent() {
  const prefersReduced = useReducedMotion();

  return (
    <motion.div
      initial={prefersReduced ? false : { opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={prefersReduced ? { duration: 0 } : { duration: 0.6 }}
    >
      Content
    </motion.div>
  );
}
```

---

## SECTION 3: GSAP Patterns (Any Stack)

### 3.1 ScrollTrigger — Section Pin + Reveal

```javascript
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger);

// Pin a section while content animates
gsap.to('.hero-content', {
  y: -100,
  opacity: 0,
  scrollTrigger: {
    trigger: '.hero',
    start: 'top top',
    end: 'bottom top',
    scrub: 1,
    pin: true
  }
});
```

### 3.2 ScrollTrigger — Horizontal Scroll

```javascript
// Convert vertical scroll to horizontal movement
const sections = gsap.utils.toArray('.horizontal-section');
gsap.to(sections, {
  xPercent: -100 * (sections.length - 1),
  ease: 'none',
  scrollTrigger: {
    trigger: '.horizontal-container',
    pin: true,
    scrub: 1,
    end: () => '+=' + document.querySelector('.horizontal-container').offsetWidth
  }
});
```

### 3.3 Text Split Animation

```javascript
// Character-by-character reveal
function splitTextAnimation(selector) {
  const element = document.querySelector(selector);
  const text = element.textContent;
  element.innerHTML = text.split('').map(char =>
    char === ' ' ? ' ' : `<span class="char">${char}</span>`
  ).join('');

  gsap.from(`${selector} .char`, {
    opacity: 0,
    y: 20,
    stagger: 0.03,
    duration: 0.5,
    ease: 'back.out(1.7)',
    scrollTrigger: { trigger: selector, start: 'top 80%' }
  });
}
```

### 3.4 SVG Path Drawing

```javascript
// Draw SVG path on scroll
const path = document.querySelector('.draw-path');
const pathLength = path.getTotalLength();
path.style.strokeDasharray = pathLength;
path.style.strokeDashoffset = pathLength;

gsap.to(path, {
  strokeDashoffset: 0,
  duration: 2,
  ease: 'power2.inOut',
  scrollTrigger: { trigger: path, start: 'top 80%', end: 'bottom 20%', scrub: true }
});
```

### 3.5 GSAP + React Pattern

```jsx
import { useEffect, useRef } from 'react';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

function GSAPSection() {
  const sectionRef = useRef(null);
  const contentRef = useRef(null);

  useEffect(() => {
    const ctx = gsap.context(() => {
      gsap.from(contentRef.current.children, {
        opacity: 0, y: 50, stagger: 0.15, duration: 0.8,
        scrollTrigger: { trigger: sectionRef.current, start: 'top 70%' }
      });
    }, sectionRef);

    return () => ctx.revert(); // Cleanup
  }, []);

  return (
    <section ref={sectionRef}>
      <div ref={contentRef}>
        <h2>Animated heading</h2>
        <p>Animated paragraph</p>
      </div>
    </section>
  );
}
```

### 3.6 Pinned Section with Progress

```javascript
gsap.to('.progress-fill', {
  width: '100%',
  ease: 'none',
  scrollTrigger: {
    trigger: '.pinned-section',
    start: 'top top',
    end: 'bottom bottom',
    scrub: true,
    pin: '.pinned-content'
  }
});
```

---

## SECTION 4: Creative/Signature Animations

### 4.1 Garage Door Opening

```html
<div class="garage-door" id="garageDoor">
  <div class="garage-segment"></div>
  <div class="garage-segment"></div>
  <div class="garage-segment"></div>
  <div class="garage-segment"></div>
  <div class="garage-segment"></div>
</div>
<main class="site-content"><!-- Your actual site --></main>
```

```css
.garage-door {
  position: fixed; top: 0; left: 0; width: 100%; height: 100%;
  z-index: 9999; display: flex; flex-direction: column;
  animation: garage-lift 2s cubic-bezier(0.65, 0, 0.35, 1) 1s forwards;
}
.garage-segment {
  flex: 1;
  background: linear-gradient(180deg, #2a2a2a 0%, #1a1a1a 50%, #2a2a2a 100%);
  border-bottom: 2px solid #333;
}
@keyframes garage-lift {
  0% { transform: translateY(0); }
  100% { transform: translateY(-100vh); }
}
```

### 4.2 Underwater Bubble Particles

```javascript
function createBubbles(container, count = 20) {
  for (let i = 0; i < count; i++) {
    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    bubble.style.cssText = `
      left: ${Math.random() * 100}%;
      width: ${4 + Math.random() * 12}px;
      animation-duration: ${4 + Math.random() * 6}s;
      animation-delay: ${Math.random() * 5}s;
    `;
    bubble.style.height = bubble.style.width;
    container.appendChild(bubble);
  }
}
```

```css
.bubble {
  position: absolute; bottom: -20px;
  border-radius: 50%; background: rgba(255,255,255,0.1);
  border: 1px solid rgba(255,255,255,0.2);
  animation: bubble-rise linear infinite;
}
@keyframes bubble-rise {
  0% { transform: translateY(0) translateX(0) scale(0.5); opacity: 0; }
  10% { opacity: 0.6; }
  90% { opacity: 0.3; }
  100% { transform: translateY(-100vh) translateX(20px) scale(1); opacity: 0; }
}
```

### 4.3 Terminal Boot Sequence

```javascript
async function bootSequence(container) {
  const lines = [
    { text: '> Initializing system...', delay: 300 },
    { text: '> Loading modules... OK', delay: 500 },
    { text: '> Connecting to server... OK', delay: 400 },
    { text: '> Rendering interface...', delay: 600 },
    { text: '> Welcome.', delay: 200 },
  ];

  for (const line of lines) {
    const div = document.createElement('div');
    div.className = 'terminal-line';
    container.appendChild(div);
    await typeText(div, line.text, 30);
    await sleep(line.delay);
  }
  // Transition to main site
  container.classList.add('boot-complete');
}

function typeText(el, text, speed) {
  return new Promise(resolve => {
    let i = 0;
    const interval = setInterval(() => {
      el.textContent += text[i]; i++;
      if (i >= text.length) { clearInterval(interval); resolve(); }
    }, speed);
  });
}
function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }
```

### 4.4 Bioluminescent Glow

```css
.bioluminescent {
  position: relative;
}
.bioluminescent::after {
  content: '';
  position: absolute; inset: -2px;
  border-radius: inherit;
  background: linear-gradient(45deg, #00FFFF, #0088FF, #00FFAA, #00FFFF);
  background-size: 300% 300%;
  animation: glow-shift 4s ease infinite;
  z-index: -1; opacity: 0;
  transition: opacity 0.5s ease;
  filter: blur(10px);
}
.bioluminescent:hover::after { opacity: 0.6; }

@keyframes glow-shift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
```

### 4.5 Bridgerton / Period Drama Aesthetic

```css
/* Ornate border that draws itself */
.ornate-border {
  border: 2px solid transparent;
  background:
    linear-gradient(var(--bg), var(--bg)) padding-box,
    linear-gradient(135deg, #D4AF37, #F5E6A3, #D4AF37) border-box;
  position: relative;
}

/* Gold filigree corner SVG animations */
.filigree-corner {
  position: absolute; width: 60px; height: 60px;
  stroke: #D4AF37; fill: none; stroke-width: 1.5;
  stroke-dasharray: 200; stroke-dashoffset: 200;
  animation: draw-filigree 2s ease forwards;
}
@keyframes draw-filigree {
  to { stroke-dashoffset: 0; }
}

/* Parchment texture */
.parchment {
  background-color: #FAF3E0;
  background-image:
    radial-gradient(ellipse at 20% 50%, rgba(139,90,43,0.05) 0%, transparent 50%),
    radial-gradient(ellipse at 80% 50%, rgba(139,90,43,0.03) 0%, transparent 50%);
}

/* Elegant serif typography */
.period-heading {
  font-family: 'Cormorant Garamond', serif;
  font-weight: 300; letter-spacing: 0.15em;
  text-transform: uppercase;
  background: linear-gradient(90deg, #D4AF37, #F5E6A3, #D4AF37);
  background-size: 200% 100%;
  -webkit-background-clip: text; color: transparent;
  animation: gold-shimmer 3s ease infinite;
}
@keyframes gold-shimmer {
  0% { background-position: -200% 50%; }
  100% { background-position: 200% 50%; }
}
```

### 4.6 Neural Network Background

```javascript
function createNeuralNetwork(canvas) {
  const ctx = canvas.getContext('2d');
  const nodes = [];
  const nodeCount = 40;

  for (let i = 0; i < nodeCount; i++) {
    nodes.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      vx: (Math.random() - 0.5) * 0.5,
      vy: (Math.random() - 0.5) * 0.5,
      radius: 2 + Math.random() * 2
    });
  }

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Update positions
    nodes.forEach(node => {
      node.x += node.vx; node.y += node.vy;
      if (node.x < 0 || node.x > canvas.width) node.vx *= -1;
      if (node.y < 0 || node.y > canvas.height) node.vy *= -1;
    });

    // Draw connections
    nodes.forEach((a, i) => {
      nodes.slice(i + 1).forEach(b => {
        const dist = Math.hypot(a.x - b.x, a.y - b.y);
        if (dist < 150) {
          ctx.strokeStyle = `rgba(6, 182, 212, ${1 - dist / 150})`;
          ctx.lineWidth = 0.5;
          ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
        }
      });
    });

    // Draw nodes
    nodes.forEach(node => {
      ctx.fillStyle = '#06B6D4';
      ctx.beginPath(); ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2); ctx.fill();
    });

    requestAnimationFrame(animate);
  }
  animate();
}
```

### 4.7 Page Transition — Book Turn

```css
.page-turn-enter {
  transform-origin: left center;
  animation: page-turn-in 0.6s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}
@keyframes page-turn-in {
  0% { transform: perspective(1200px) rotateY(-90deg); opacity: 0; }
  100% { transform: perspective(1200px) rotateY(0deg); opacity: 1; }
}

.page-turn-exit {
  transform-origin: right center;
  animation: page-turn-out 0.6s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}
@keyframes page-turn-out {
  0% { transform: perspective(1200px) rotateY(0deg); opacity: 1; }
  100% { transform: perspective(1200px) rotateY(90deg); opacity: 0; }
}
```

---

## SECTION 5: Performance & Accessibility

### Performance Checklist
- Animate only `transform` and `opacity`
- Use `will-change` sparingly (remove after animation completes)
- Debounce scroll events (or use Intersection Observer / GSAP ScrollTrigger)
- Use `requestAnimationFrame` for JS animations
- Lazy-load heavy animation libraries (GSAP, Three.js)
- Test on low-end devices (throttle CPU in DevTools)
- Avoid animating during page load (defer to after `DOMContentLoaded`)

### Accessibility — Reduced Motion

**Always include this globally:**

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

```javascript
// Check in JS before running animations
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!prefersReduced) {
  // Initialize animations
}
```

### Focus Management
- Never animate away focus indicators
- Ensure animated content is reachable by keyboard
- Use `aria-live` for dynamically animated content changes
- Don't auto-scroll users away from their current focus

---

## Quick Reference: Which Animation For Which Niche

| Niche | Go-To Animations |
|-------|-----------------|
| Healthcare | Gentle fades, pulse, breathing circle, progress bars |
| Law | Slow reveals, gold line draws, dignified fades |
| Fintech | Number counters, chart draws, data pulses, confetti milestones |
| Marine | Waves, bubbles, drift, bioluminescent glow, parallax depth |
| Government | Minimal fades only, progress indicators, state transitions |
| AI/Tech | Neural nodes, data flow, typing generation, gradient mesh |
| Automotive | Cinematic reveals, horizontal scroll, performance counters, garage door |
| Restaurant | Warm fades, menu unfold, food zoom, parallax |
| Fashion | Clip-path reveals, slow image transitions, editorial scroll |
| Gaming | Glitch, particles, screen shake, health bars, achievements |
| Music | Waveforms, vinyl spin, equalizer bars, beat sync |
| Personal | Match the person's energy — anything goes |
