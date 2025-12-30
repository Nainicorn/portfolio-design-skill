# Resume Input Format

Structured template for users to provide portfolio content. **Detail = Quality.**

---

## Template

Copy this template and fill it out. More detail = better transformation.

```markdown
# PORTFOLIO CONTENT

## PERSONAL INFO
Name: [Your Name]
Title: [e.g., Full-Stack Developer, UX Designer, Software Engineer]
Location: [City, State/Country]
Tagline: [1-2 sentences about what you do and what you are looking for]

---

## ABOUT ME (Optional but recommended)

[2-3 paragraphs about you beyond the resume. What drives you? What are you curious about? What's your story? This is where personality shines. Can mention hobbies, interests, side projects, what you're currently learning, etc.]

Example:
"I've been coding since I was 12, starting with Python to automate boring tasks. Now I build full-stack applications that help people solve real problems. I'm particularly interested in developer tools and AI-powered workflows.

When I'm not coding, I'm probably hiking, reading sci-fi, or experimenting with new coffee brewing methods. I'm currently learning Rust and exploring how to build more performant web applications."

---

## ADDITIONAL INFO (Optional)

**Currently Learning:** [What are you studying/working on right now?]

**Open to:** [Types of roles, locations, remote/hybrid/onsite]

**Languages:** [English (native), Spanish (conversational), etc.]

**Awards:** [If notable]

---

## EDUCATION

### Degree, Major
**School:** [University Name]
**Graduation:** [Month Year or Expected Month Year]
**GPA:** [If 3.5+ and recent grad]
**Relevant Coursework:** [Only if relevant and space permits]
**Achievements:** [Dean's List, scholarships, honors]

---

## SKILLS

### Languages
[JavaScript, Python, Java, TypeScript, etc.]

### Frontend
[React, Vue, HTML/CSS, etc.]

### Backend
[Node.js, Django, FastAPI, etc.]

### Database
[PostgreSQL, MongoDB, Redis, etc.]

### Cloud/DevOps
[AWS, Docker, Kubernetes, CI/CD, etc.]

### Tools/Other
[Git, Figma, Jira, etc.]

---

[Optional: Organize differently if you prefer, e.g., by proficiency level]

---

## CERTIFICATIONS (Optional)

- [Certification Name - Issuing Organization - Year]
- [AWS Certified Solutions Architect - Amazon - 2024]

---

## PROJECTS

### Project Name

**One-line summary:** [What is it? [personal projects, open source contributions, hackathons, research publications, etc]]

**Company/Location:** [if applicable only]

**Problem:** [What problem did this solve?]

**Solution:** [How did you solve it? Include approach, key decisions]

**Tech Stack:** [React, Node.js, PostgreSQL, AWS, etc.]

**Results/Impact:** [Metrics if available: "Increased X by Y%", "Reduced Z by 50%", "Used by N users"]

**Link:** [GitHub repo or live demo URL]

**Your Role:** [Solo project? Team? What did YOU specifically do?]

**Interesting Details:** [Any technical challenges, cool features, lessons learned]

---

[Repeat project format above for any remaining projects]
[Add important projects. More = better portfolio depth]

---

## WORK EXPERIENCE

### Job Title at Company Name

**Dates:** [Month Year - Month Year or "Present"]

**Your Responsibilities:** [What did you work on specifically [frontend, backend, etc.] ? What was your scope?]

**Key Achievements:**
- [Achievement 1 with impact/metrics]
- [Achievement 2 with impact/metrics]
- [Achievement 3 with impact/metrics]

**Tech Stack:** [Technologies you used in this role]

**Interesting Details:** [Cool projects, challenges overcome, growth]

---

[Repeat work experience format above for all important career points]

---

## CONTACT
Email: [email@example.com]
LinkedIn: [linkedin.com/in/username]
GitHub: [github.com/username]
Other: [Twitter, etc.]

---

END OF TEMPLATE
```

---

## Content Transformation Rules

After user provides content, transform it for web:

### Projects Section

**Resume version:**
> "Built a task management app with React and Node.js. Implemented user authentication and real-time updates."

**Web version:**
> "TaskFlow: Real-Time Collaborative Task Management
> 
> I built TaskFlow to solve a problem my team faced: juggling multiple project management tools that didn't talk to each other. Using React for the frontend and Node.js with WebSockets for real-time sync, I created a lightweight alternative that focuses on speed and simplicity.
>
> The app handles 500+ concurrent users with sub-100ms update latency. Authentication uses JWT with refresh tokens, and I implemented optimistic UI updates to make it feel instant."

**Key differences:**
- Added context (why it was built)
- Explained technical decisions
- Included metrics
- More narrative, less bullets

---

### Experience Section

**Resume version:**
> "• Developed microservices in Go
> • Improved API performance by 40%
> • Mentored junior developers"

**Web version:**
> "As a backend engineer at TechCorp, I architected and built three microservices in Go that handle millions of requests daily. The most impactful was our caching layer redesign, which reduced API latency from 200ms to 120ms—a 40% improvement that directly affected 2 million users.
>
> I also mentored two junior developers, helping them grow from writing basic CRUD operations to owning entire service deployments. One of them is now a mid-level engineer on another team."

**Key differences:**
- Context about company/team
- Specific numbers and impact
- Storytelling about the work
- Shows growth and leadership

---

### Skills Section

**Transform from list to narrative if appropriate for theme:**

Instead of:
> JavaScript, React, Node.js, Python...

Consider (for some themes):
> "I work across the full stack, with JavaScript/TypeScript as my primary language. On the frontend, I build with React and have experience with Vue and Svelte. Backend work is usually Node.js or Python (FastAPI/Django). I'm comfortable with PostgreSQL and MongoDB, and I deploy to AWS using Docker and GitHub Actions."

**Or keep it visual/organized:**
```
Frontend          Backend           DevOps
━━━━━━━━━━━━━     ━━━━━━━━━━━━━    ━━━━━━━━━━━━━
React             Node.js           AWS
TypeScript        Python            Docker
Vue               PostgreSQL        CI/CD
HTML/CSS          MongoDB           Kubernetes
```

---

## Minimum Requirements

To proceed with portfolio generation, user must provide:

**Essential:**
- Name and title
- Contact info (at least email)
- 2+ projects OR 2+ work experiences

**Highly Recommended:**
- 3-5 projects
- Work experience details
- Skills list
- About section

**Optional but valuable:**
- Education
- Certifications
- Currently learning
- Personal interests

---

## What NOT to Include

❌ **Personal info:** SSN, full address
❌ **Irrelevant jobs:** High school summer job (unless fresh grad with limited experience)
❌ **Obvious skills:** "Microsoft Word", "Email", "Teamwork"
❌ **Buzzwords without context:** "Synergized cross-functional deliverables"
❌ **Unverifiable claims:** "Best developer in the city"

---

## Tips for Quality Content

1. **Be specific:** "Reduced load time by 60%" > "Made it faster"
2. **Show impact:** "Used by 10K+ students" > "Built an app"
3. **Explain decisions:** "Chose PostgreSQL for ACID compliance" > "Used PostgreSQL"
4. **Tell stories:** How you solved a problem, not just what you built
5. **Quantify:** Numbers make achievements real
6. **Be honest:** Don't inflate or lie. Authenticity matters.

---

Users can provide less detail in final format, but reminder that **detail = quality**.