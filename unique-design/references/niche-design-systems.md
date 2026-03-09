# Niche Design Systems

Industry-specific design intelligence. Each niche has its own visual language, UX patterns, animation approach, and anti-patterns. Use this to make every design feel native to its industry.

---

## Healthcare / Medical

### Visual Identity
- **Colors:** Soft blues (#4A90D9, #E8F4FD), calming greens (#34A853, #E8F5E9), clean whites
- **Typography:** Clean sans-serif (Inter, Source Sans Pro), generous line height (1.6+), 16px+ body text
- **Imagery:** Real people, not stock. Warm, empathetic photography. Illustrations for complex medical concepts
- **Spacing:** Generous — reduce cognitive load. 80-120px section padding

### Layout Patterns
- **Patient portals** — dashboard with appointment cards, health metrics, medication reminders
- **Provider directories** — filterable grid with specialty tags, ratings, availability
- **Symptom checkers** — step-by-step flow with progressive disclosure, never overwhelming
- **Telehealth interfaces** — video-first with minimal surrounding UI during calls
- **Health data visualization** — heart rate, blood pressure, BMI charts with gentle animations

### Animation Approach
Subtle and calming. Never jarring.
- Gentle fade-ins on scroll (0.6s ease-out)
- Soft pulse animations for vital signs and status indicators
- Smooth transitions between form steps
- Loading states with breathing/pulse animation (not spinners)
- Progress bars for multi-step flows

### UX Essentials
- HIPAA-aware form patterns (secure input indicators, session timeouts)
- Emergency information always visible/accessible
- Multi-language support patterns
- Accessibility is non-negotiable (WCAG AA minimum, AAA preferred)
- Large touch targets for elderly/impaired users (48px+)
- Clear error states on medical forms (never ambiguous)

### Anti-Patterns
- Dark themes (feels clinical/cold — unless specifically a health-tech dashboard)
- Complex animations that delay access to critical information
- Generic stock photos of doctors with stethoscopes
- Tiny text or low-contrast elements
- Autoplay video/audio (triggers anxiety)

### Signature Ideas
- Heartbeat animation in the loading screen
- Gradient that shifts from anxious warm tones to calming cool tones as user progresses through booking
- Breathing exercise micro-interaction (expandable circle) as a loading state
- Health metric cards that animate data in like a gentle wave

---

## Legal / Law Firms

### Visual Identity
- **Colors:** Navy (#1B2A4A), charcoal (#2C3E50), deep burgundy (#722F37), gold accents (#C9A84C), cream (#FAF8F5)
- **Typography:** Serif headings (Playfair Display, Cormorant Garamond), clean sans body (Inter, DM Sans), authoritative weights
- **Imagery:** Custom photography of the actual team, architectural shots of offices, city skylines. Never stock
- **Spacing:** Dignified — not cramped, not wasteful. 60-80px section padding

### Layout Patterns
- **Practice area showcases** — card grid or accordion with subtle reveals
- **Attorney profiles** — full pages with headshots, credentials, case highlights
- **Case results** — metrics-driven ($ recovered, cases won) with dramatic number counters
- **Consultation booking** — progressive disclosure form (never show 20 fields at once)
- **Resource library** — filterable articles, whitepapers, legal guides
- **Testimonials** — rotating quotes with client initials (privacy-aware)

### Animation Approach
Dignified and intentional. Confidence, not flash.
- Slow, weighted fade-ins (0.8s ease)
- Text reveals that feel like unveiling (clip-path or opacity)
- Subtle parallax on hero images
- Gold accent line that draws across section dividers
- Number counters for case results that tick up deliberately

### UX Essentials
- Trust signals prominent (bar association badges, awards, years in practice)
- Clear CTAs for free consultations
- Phone number clickable and prominent on mobile
- Fast load times (potential clients are stressed, don't make them wait)
- Content should address client pain points, not firm credentials

### Anti-Patterns
- Sliders/carousels (feel dated, reduce trust)
- Flashy animations (undermines authority)
- Generic "Lady Justice" imagery
- Bright, playful colors (wrong tone)
- Auto-playing background videos
- Cluttered navigation (too many practice areas in top nav)

### Signature Ideas
- Gavel animation on page load — subtle, single strike
- Scales of justice SVG that balances on scroll
- Section transitions that feel like turning pages in a leather-bound book
- Gold foil shimmer effect on key headings
- Testimonial cards that flip like legal documents

---

## Fintech / Finance

### Visual Identity
- **Colors:** Deep purples (#5B21B6), teals (#0D9488), dark mode backgrounds (#0F172A), electric accents
- **Typography:** Geometric sans (DM Sans, Space Grotesk), monospace for numbers/data (JetBrains Mono, IBM Plex Mono)
- **Imagery:** Abstract data visualizations, geometric patterns, minimal photography
- **Spacing:** Dense but organized — dashboard-like information density with clear hierarchy

### Layout Patterns
- **Dashboard layouts** — metric cards, charts, transaction lists, real-time data
- **Product landing pages** — progressive feature reveals, pricing calculators
- **Onboarding flows** — step-by-step with ID verification, KYC patterns
- **Transaction feeds** — real-time updates with smooth list animations
- **Portfolio views** — charts, allocation breakdowns, performance metrics
- **Pricing tables** — comparison with interactive toggles (monthly/yearly)

### Animation Approach
Precise, data-driven. Every animation should feel intentional and numeric.
- Number counters that tick up/down with easing
- Chart animations that draw data progressively (line charts trace, bar charts grow)
- Smooth transitions between financial views/tabs
- Celebration micro-animations for milestones (confetti on first deposit, etc.)
- Real-time data pulse (subtle glow on updated values)
- Card flip animations for before/after comparisons

### UX Essentials
- Security signals everywhere (lock icons, encryption badges, compliance certifications)
- Clear transaction states (pending, processing, completed, failed)
- Biometric auth patterns (Face ID, fingerprint prompts)
- Progressive disclosure for complex products
- Accessible number formatting (commas, decimals, currency symbols)
- Zero-state guidance (empty portfolio → educational content)

### Anti-Patterns
- Playful/casual tone (money is serious)
- Unclear fee structures
- Animations that delay transaction confirmations
- Dark patterns (hidden fees, manipulative urgency)
- Generic "money growing" stock photos

### Signature Ideas
- Money flow animation — value visually moves from one account to another
- Portfolio allocation pie chart that morphs when you adjust percentages
- Ticker-tape animation in the header with real-time market feel
- Card that flips to reveal transaction details
- Success animation: coins falling into a vault on payment confirmation

---

## Marine Life / Ocean Themes

### Visual Identity
- **Colors:** Deep ocean (#0C2340), teal (#008B8B), aqua (#00CED1), bioluminescent cyan (#00FFFF), coral (#FF6F61), sandy beige (#F4E4C1)
- **Typography:** Flowing, organic — rounded sans (Nunito, Quicksand) or elegant serif (Cormorant)
- **Imagery:** Underwater photography, ocean textures, coral patterns, watercolor marine illustrations
- **Spacing:** Flowing — sections blend into each other like water, not sharply divided

### Layout Patterns
- **Full-bleed ocean photography** with text overlays
- **Wave-shaped section dividers** (SVG clip-paths between content blocks)
- **Depth-based parallax** — multiple layers simulating ocean depth (surface → mid-water → deep sea)
- **Card layouts** that feel like floating specimens or diving into exhibits
- **Interactive maps** — ocean/reef/dive site locations
- **Species galleries** — filterable, zoomable, with rich detail panels

### Animation Approach
Everything should feel like water — organic, flowing, never rigid.
- **Wave section dividers** — SVG wave paths that gently animate
- **Bubble particles** — rising from bottom of viewport
- **Underwater parallax** — elements drift at different speeds like ocean currents
- **Bioluminescent glow** — elements subtly glow on hover (box-shadow with cyan/teal)
- **Tidal rhythm** — elements that ebb and flow on a gentle interval
- **Fish/marine silhouettes** — SVG creatures that swim across on scroll
- **Liquid/blob effects** — CSS filter blur + contrast for metaball shapes
- **Current drift** — idle elements gently sway as if in water

### CSS Techniques
```css
/* Wave section divider */
.wave-divider {
  clip-path: url(#wave-path);
  /* or */ clip-path: polygon(0 0, 100% 0, 100% 85%, 75% 95%, 50% 85%, 25% 95%, 0 85%);
}

/* Bioluminescent glow on hover */
.glow-element:hover {
  box-shadow: 0 0 20px rgba(0, 255, 255, 0.4), 0 0 60px rgba(0, 255, 255, 0.1);
  transition: box-shadow 0.6s ease;
}

/* Underwater drift animation */
@keyframes drift {
  0%, 100% { transform: translateX(0) translateY(0) rotate(0deg); }
  25% { transform: translateX(5px) translateY(-3px) rotate(1deg); }
  75% { transform: translateX(-5px) translateY(3px) rotate(-1deg); }
}

/* Bubble rising */
@keyframes bubble-rise {
  0% { transform: translateY(100vh) scale(0.5); opacity: 0; }
  10% { opacity: 0.6; }
  100% { transform: translateY(-10vh) scale(1); opacity: 0; }
}
```

### Anti-Patterns
- Rigid geometric layouts (feels wrong for ocean themes)
- Sharp corners and hard edges
- Neon colors without ocean context (this isn't cyberpunk)
- Static, non-flowing page structure
- Cartoonish clip art marine life

### Signature Ideas
- Site loads with a "dive" animation — viewport descends into the ocean
- Cursor leaves a trail of tiny bubbles
- Scroll triggers depth changes — background shifts from light surface water to dark deep sea
- Jellyfish that pulse gently in the background using CSS animations
- Section headers have watercolor splash SVG behind them
- Interactive coral reef where hovering reveals species info

---

## Government / Civic Tech

### Visual Identity
- **Colors:** Official palettes — navy (#112E51), white, red/blue per nation. Maximum contrast
- **Typography:** System fonts or accessible web fonts (Public Sans, Source Sans Pro). Never decorative
- **Imagery:** Minimal, purposeful. Icons over photos. Clear infographics
- **Spacing:** Structured, predictable. Standard grid. 8px base unit

### Layout Patterns
- **Service directory** — clear categories, search, step-by-step guides
- **Mega menus** — organized by department/service type
- **Step-by-step flows** — progress indicators, save-and-return, clear next actions
- **Alert banners** — emergency/critical info always visible at top
- **Data tables** — sortable, filterable, exportable, responsive
- **FAQ/Accordion** — searchable, organized by topic

### Animation Approach
Minimal and purposeful. Accessibility over creativity.
- Subtle state transitions only (focus, hover, active)
- Loading indicators for async government services
- Progress bar animations for multi-step forms
- Smooth accordion open/close
- **Must respect `prefers-reduced-motion`** — this is non-negotiable

### Accessibility Requirements (MANDATORY)
- WCAG 2.2 AA minimum (AAA preferred)
- Focus indicators clearly visible (not just browser default)
- Touch targets ≥ 44x44px (48px preferred)
- Color contrast ≥ 4.5:1 everywhere
- Screen reader tested with NVDA/VoiceOver
- Cognitive accessibility (plain language, predictable navigation)
- Resizable to 200% without horizontal scroll
- Captions on all video/audio
- No time limits on forms without extension option

### Reference Frameworks
- **USWDS** (designsystem.digital.gov) — U.S. Web Design System
- **GOV.UK Design System** — UK government patterns
- **Canada.ca Web Experience Toolkit** — Canadian government

### Anti-Patterns
- Creative/artistic layouts (unpredictable navigation confuses users)
- Decorative animations (wastes time, fails accessibility)
- Small text or low contrast
- Complex navigation hierarchies
- Jargon without explanation
- PDFs as the primary content delivery

### Signature Ideas (Subtle)
- Smooth, confidence-inspiring form interactions
- Data visualizations that build as you scroll (census data, budget breakdowns)
- Interactive service finder ("What do you need help with?" → guided flow)
- Progress saved automatically with visual confirmation

---

## AI Applications

### Visual Identity
- **Colors:** Dark backgrounds (#0A0A0F, #111827), electric accents — cyan (#06B6D4), purple (#8B5CF6), electric blue (#3B82F6), neon green (#22C55E)
- **Typography:** Mix of clean sans (Inter, Space Grotesk) + monospace for code/data (Fira Code, JetBrains Mono)
- **Imagery:** Abstract geometric patterns, node graphs, gradient meshes, data streams
- **Spacing:** Moderate — dashboard-density for tools, generous for marketing pages

### Layout Patterns
- **Chat/conversational interfaces** — message bubbles, streaming text, suggested prompts
- **Dashboard with AI insights** — prediction cards, confidence meters, anomaly alerts
- **Pipeline visualizations** — data flow from input → processing → output
- **Model comparison** — side-by-side outputs, performance metrics
- **Prompt playgrounds** — input/output split view, parameter sliders
- **Documentation** — searchable, with interactive code examples

### Animation Approach
Futuristic, data-driven, intelligent-feeling.
- **Token-by-token text generation** — text appears word-by-word or character-by-character
- **Neural network nodes** — pulsing dots connected by animated lines
- **Data flow lines** — animated dashes flowing between pipeline stages
- **Processing indicators** — not just spinners, but animated brain/circuit patterns
- **Confidence meters** — bars/circles that fill with spring physics
- **Streaming data** — values updating in real-time with fade transitions
- **Gradient mesh backgrounds** — slowly morphing color fields
- **Particle systems** — representing data being processed

### CSS/JS Techniques
```css
/* Neural network node pulse */
@keyframes node-pulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(6, 182, 212, 0.4); }
  50% { box-shadow: 0 0 0 10px rgba(6, 182, 212, 0); }
}

/* Data flow dash animation */
@keyframes data-flow {
  0% { stroke-dashoffset: 20; }
  100% { stroke-dashoffset: 0; }
}

/* Gradient mesh shift */
@keyframes mesh-shift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
```

### Anti-Patterns
- Robot/android imagery (cliché)
- "HAL 9000" red eye aesthetic (overused)
- Matrix-style falling code (dated)
- Overly complex visualizations that obscure the actual AI functionality
- Generic chatbot UI with no personality

### Signature Ideas
- Background of slowly pulsing neural network that responds to mouse position
- Text generation animation where response "types" with a subtle glow cursor
- Pipeline visualization: data visually flows through processing stages
- Confidence gauge that bounces with spring physics before settling
- "Thinking" animation — abstract shapes morphing while AI processes
- Interactive demo where user can drag parameters and see AI output change live

---

## Automotive

### Visual Identity
- **Colors:** Premium blacks (#000, #111), metallic silver (#C0C0C0), white (#FFF), brand-specific accent (Ferrari red, BMW blue, etc.)
- **Typography:** Thin sans-serif (Montserrat Thin, Raleway), elegant letter-spacing (0.1-0.2em), all-caps for headings
- **Imagery:** Full-bleed hero photography, dramatic lighting, studio shots on dark backgrounds
- **Spacing:** Cinematic — large hero sections (100vh), generous section padding (100-150px)

### Layout Patterns
- **Hero with video/3D** — full-screen automotive hero with ambient video or WebGL model
- **Configurator** — color picker, wheel selector, interior options with live preview
- **Specs comparison** — side-by-side with animated metric bars
- **Gallery** — full-bleed image sequences, lightbox with detail zoom
- **Performance metrics** — 0-60 counters, HP/torque gauges, range indicators
- **Booking/test drive** — premium form design with minimal fields

### Animation Approach
Smooth, premium, cinematic. Every animation should feel expensive.
- **Slow cinematic reveals** — content fades in over 1-1.5s
- **Horizontal scroll** — car lineup scrolling horizontally within a pinned section
- **Performance counters** — 0-60 time ticking up dramatically, HP numbers counting
- **Car rotation** — 360° spin interaction (drag or auto-rotate)
- **Parallax hero** — car image with depth layers (foreground detail + background blur)
- **Color transition** — car image cross-fades when user selects different color
- **Garage door reveal** — page loads with a vertical split or roll-up revealing the car

### Garage Door Concept (User Requested)
```css
/* Garage door opening animation */
.garage-door {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: #111;
  z-index: 9999;
  transform-origin: top center;
  animation: garage-open 2s cubic-bezier(0.65, 0, 0.35, 1) forwards;
}

@keyframes garage-open {
  0% { transform: translateY(0); }
  100% { transform: translateY(-100%); }
}

/* Segmented garage door (more realistic) */
.garage-segment {
  height: 20%;
  background: linear-gradient(180deg, #222 0%, #111 50%, #222 100%);
  border-bottom: 2px solid #333;
}
```

### Anti-Patterns
- Cluttered layouts (premium = space)
- Small imagery (cars need to be BIG)
- Generic car dealership vibe (this should feel like a brand experience)
- Aggressive CTAs (premium is understated)
- Slow-loading hero images without optimization

### Signature Ideas
- Garage door split-open → car revealed with dramatic lighting
- Engine sound wave visualization that pulses in the background
- Speedometer-style loading animation
- Headlight sweep effect on scroll (light beams animate across section)
- Dashboard instrument cluster as the navigation (RPM = scroll progress)

---

## E-Commerce / Product

### Visual Identity
- **Colors:** Depends on brand. Clean whites for luxury, bold colors for youth/streetwear, earth tones for artisan
- **Typography:** Product names in display fonts, prices in monospace or bold weight, body in readable sans
- **Imagery:** High-quality product photography is EVERYTHING. White background for clarity, lifestyle shots for context
- **Spacing:** Product-focused — images are hero, text supports

### Layout Patterns
- **Product grid** — responsive, filterable, with quick-view modals
- **Product detail** — image gallery + sticky add-to-cart + accordion details
- **Cart** — slide-out drawer or dedicated page with quantity controls
- **Checkout** — minimal distractions, progress steps, trust signals
- **Collections** — curated grids with editorial header images
- **Lookbook** — editorial-style product storytelling

### Animation Approach
Smooth, conversion-focused. Animations should guide toward purchase.
- Product image zoom on hover
- Add-to-cart confirmation with micro-animation (item flies to cart icon)
- Cart count badge bounce when updated
- Smooth filter/sort transitions (layout animation)
- Image gallery swipe with spring physics
- Quick-view modal slide-in
- Skeleton loading for product grids

### Anti-Patterns
- Slow page loads (every second costs conversions)
- Animations that block interaction
- Hiding the price
- Complex checkout flows
- Missing trust signals (shipping, returns, security)

---

## Restaurant / Food

### Visual Identity
- **Colors:** Warm tones — amber (#F59E0B), terracotta (#C2703C), olive (#7C8C3B), cream (#FFF8E7), espresso (#3C1F0A)
- **Typography:** Display serif for restaurant name (Playfair, Cormorant), clean sans for menus (DM Sans), handwritten for specials
- **Imagery:** Professional food photography with warm lighting, close-up textures, ambiance shots
- **Spacing:** Generous — let the food breathe. No clutter

### Layout Patterns
- **Menu** — categorized, with item descriptions and dietary icons. Responsive
- **Reservation booking** — date/time picker, party size, special requests
- **Gallery** — food + interior + events
- **Location** — interactive map, hours, contact
- **Events/specials** — featured banner or rotating section

### Animation Approach
Warm, sensory, inviting.
- Menu items fade in with stagger (appetizers → mains → desserts)
- Food images zoom slightly on hover (inviting closer look)
- Smooth parallax on hero food photography
- Reservation form steps slide smoothly
- Specials banner with gentle auto-rotation

### Signature Ideas
- Menu that unfolds like a physical menu card
- Plate presentation animation — dish assembles on scroll
- Steam rising from food images (CSS animation)
- Time-of-day adaptive design (breakfast menu in morning, dinner in evening)

---

## Personal Brand / Portfolio

### Visual Identity
- **Entirely personality-driven** — no one-size-fits-all. This is where the user's personality shines
- Ask extensive questions about who they are, what makes them unique, their personal aesthetic

### The Key Difference
Unlike generic portfolio templates, a personal brand site should feel like walking into someone's space. Every choice reflects them.

### Layout Patterns
- **About section** — not just a bio, but a story
- **Work/projects** — case study format with problem → solution → impact
- **Skills** — visualized in a way that matches their aesthetic (not progress bars)
- **Contact** — clear CTA, personality in the copy
- **Blog/thoughts** — if they create content

### Animation Approach
Match the person's energy:
- **Calm creative** → Minimal fades, subtle parallax, clean transitions
- **Bold developer** → Terminal typing, code-block aesthetics, glitch effects
- **Playful designer** → Bouncy physics, color explosions, interactive cursor
- **Elegant professional** → Slow reveals, sophisticated easing, gold accents

### Signature Ideas (Unique Per Person)
- Site that looks like their actual desk/workspace
- Interactive timeline of their career (scroll through years)
- Project case studies with before/after sliders
- Cursor that reveals hidden content (flashlight effect in dark mode)
- Easter eggs that reflect their personality (Konami code, click counter, hidden page)
- Loading screen that tells a micro-story about them

---

## Education / EdTech

### Visual Identity
- **Colors:** Engaging but not overwhelming — blue (#2563EB) for trust, green (#16A34A) for progress, warm accents
- **Typography:** Readable above all. Large body text (18px+), generous line height (1.7+)
- **Imagery:** Diverse, inclusive, real learners (not stock). Illustrations for concepts
- **Spacing:** Comfortable — learning is already hard, don't add visual stress

### Layout Patterns
- **Course catalog** — filterable grid with difficulty level, duration, ratings
- **Lesson view** — sidebar navigation, main content area, progress indicator
- **Dashboard** — progress tracking, recommended next steps, streaks/achievements
- **Interactive exercises** — embedded code editors, quizzes, drag-and-drop
- **Discussion** — threaded comments, peer interaction

### Animation Approach
Encouraging, clear, gamified.
- Progress bars that fill with celebration
- Achievement badge reveal animations
- Smooth transitions between lesson steps
- Correct/incorrect feedback animations
- Streak counter with fire animation
- Confetti on course completion

---

## Fashion / Luxury

### Visual Identity
- **Colors:** Monochrome base (black + white) with one statement accent. Or all-black with gold
- **Typography:** High-fashion display fonts (Didot, Bodoni), extreme weights (ultra-thin or ultra-bold)
- **Imagery:** Full-bleed editorial photography, dramatic lighting, no borders
- **Spacing:** Extreme — luxury = space. Let images dominate

### Layout Patterns
- **Lookbook** — full-screen image sequences, minimal text overlay
- **Product grid** — clean, image-forward, minimal UI
- **Editorial** — magazine-style layouts, multi-column text
- **Campaign** — full-screen video hero, immersive storytelling

### Animation Approach
Elegant, editorial, confident.
- Slow image reveals (clip-path expanding)
- Text that fades in with dramatic timing (1.5s+)
- Smooth page transitions (crossfade or slide)
- Parallax on editorial images
- Hover zoom on product images (subtle, smooth)

### Signature Ideas
- Runway-style scroll — images slide in like models on a catwalk
- Magazine page-turn transitions between sections
- Cursor becomes a magnifying glass over product images
- Background music toggle for full immersive experience (optional, user-controlled)

---

## Gaming

### Visual Identity
- **Colors:** Bold, high-energy — neons, dark backgrounds, RGB-inspired gradients
- **Typography:** Bold display fonts (Bungee, Press Start 2P for retro, Orbitron for sci-fi)
- **Imagery:** Game art, character renders, dynamic action shots, particle effects
- **Spacing:** Tight and energetic — dense with information but organized

### Layout Patterns
- **Game showcase** — hero with trailer video/gameplay, key features
- **Character/class selection** — interactive cards with stats
- **Leaderboards** — real-time rankings with animated updates
- **News/updates** — blog-style with category tags
- **Community** — forums, fan art, event calendars

### Animation Approach
Bold, energetic, immersive.
- Glitch effects on hover
- Particle effects on interaction
- Achievement unlock animations
- Health bar / stat bar fills
- Screen shake on impactful actions
- Loading screens with mini-games or lore

### Signature Ideas
- Character selection screen as the landing page
- XP bar as the scroll progress indicator
- Achievement toasts for completing site interactions (read 3 articles = "Lore Master" badge)
- Boss health bar depleting as user scrolls through feature list
- Retro pixel art loading screen

---

## Music / Audio

### Visual Identity
- **Colors:** Dark/moody with vibrant accents. Or genre-specific (jazz = warm browns, EDM = neons, classical = cream + gold)
- **Typography:** Display fonts matching genre. Graffiti for hip-hop, elegant serif for classical, geometric for electronic
- **Imagery:** Artist photography, album art, concert shots, audio waveforms
- **Spacing:** Album-cover proportions — square grids, cinematic widths

### Layout Patterns
- **Artist page** — hero with latest release, discography, tour dates, merch
- **Album/EP view** — track list with play buttons, lyrics, credits
- **Tour dates** — location list with venue info and ticket links
- **Music player** — persistent bottom bar or fullscreen experience

### Animation Approach
Rhythmic, audio-visual.
- Audio waveform visualizations
- Album art that pulses or morphs
- Beat-synced animations (if audio is playing)
- Vinyl record spin on track pages
- Equalizer bars in navigation or headers
- Concert-style light show background effects

### Signature Ideas
- Audio waveform as the site's main visual motif
- Vinyl record that spins while a track plays, needle drops on play
- Equalizer bars hidden in the logo or header
- Genre-specific UI skins (switch between acoustic/electric modes)
- Interactive mixing board where sliders control UI elements

---

## Real Estate

### Visual Identity
- **Colors:** Warm neutrals (beige, cream, taupe), trust blue, green for eco-properties
- **Typography:** Elegant sans or serif for listings, clean sans for data
- **Imagery:** Professional property photography, virtual tours, neighborhood shots
- **Spacing:** Image-forward — properties need visual space to impress

### Layout Patterns
- **Property grid** — large images, key details (price, beds, baths, sqft), favorites
- **Property detail** — image gallery, virtual tour, floor plan, neighborhood data
- **Search/filter** — map-based search, advanced filters, saved searches
- **Agent profiles** — headshot, credentials, listings, reviews
- **Market data** — price trends, neighborhood comparisons

### Animation Approach
Smooth, premium, trust-building.
- Property card hover with slight lift and detail reveal
- Image gallery smooth transitions
- Map markers that pop in as results load
- Price range slider with smooth interaction
- Virtual tour transitions between rooms

### Signature Ideas
- Property cards that "open the door" on click (door swing animation revealing details)
- Map-centric design where the map IS the homepage
- Floor plan that builds itself as you scroll
- Neighborhood data that reveals in concentric circles from the property
