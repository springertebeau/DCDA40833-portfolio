# AI Prompts Log - Lab 5: Vibe Coding

**Student:** Springer Tebeau  
**Course:** DCDA 40833  
**Date:** February 19, 2026

---

## Experiment A: Dark Mode Toggle

### Initial Research Prompt:
**Prompt 1:** "How do I add a dark mode toggle to my website using CSS and JavaScript?"

**AI Response Summary:**
Suggested using CSS custom properties (variables) with a toggle class on the body element, plus JavaScript to switch between modes.

---

### CSS Implementation Prompts:

**Prompt 2:** "Create CSS custom properties for a dark mode color scheme that works with my existing pink theme (primary: #f4a6c8). Include variables for text, background, and card backgrounds."

**AI Response Summary:**
Generated `:root` variables for light mode and `body.dark-mode` overrides for dark mode. Included colors for text, backgrounds, borders, and code blocks.

**What I used:** Most of the color values, with modifications to the dark background (I lightened it from #0a0a0a to #1a1a1a).

---

**Prompt 3:** "Create a moon/sun toggle button for dark mode that sits in the navigation bar using CSS positioned absolutely to the right"

**AI Response Summary:**
Generated HTML structure with button element containing icon span, plus CSS with position:absolute, flexbox centering, and hover effects.

**What I used:** Button structure and positioning logic. Modified padding for better mobile usability.

---

### JavaScript Implementation Prompts:

**Prompt 4:** "Write JavaScript that toggles dark mode on button click, changes the icon between moon and sun, and saves the preference in localStorage"

**AI Response Summary:**
Generated complete JavaScript with:
- querySelector to get button and icon elements
- classList.toggle() to add/remove dark-mode class
- localStorage.setItem() and getItem() for persistence
- Icon switching logic with Unicode emojis
- Page load check for saved preference

**What I used:** All of this logic. Fixed a bug where icon didn't update on page load when dark mode was already enabled.

---

### Debugging Prompt:

**Prompt 5:** "My dark mode icon shows moon emoji on page load even when dark mode is active. Fix the code so it shows sun when dark mode is enabled on page load."

**AI Response Summary:**
Suggested moving the icon update (`icon.textContent = '☀️'`) inside the localStorage check that runs on page load, not just in the click handler.

**What I used:** This fix worked perfectly - it was exactly what I needed.

---

## Experiment B: Python Data Visualization

### Main Generation Prompt:

**Prompt 6:** "Create Python code that generates a sample dataset of 50 students with columns for study_hours (1-10), sleep_hours (4-9), and exam_score (0-100). Then create a scatter plot showing the relationship between study hours and exam scores, with points colored by sleep quality. Add a trend line and proper labels."

**AI Response Summary:**
Generated complete Jupyter notebook code including:
- numpy for random data generation
- pandas DataFrame construction
- sleep_hours binning into Low/Medium/High categories using pd.cut()
- matplotlib scatter plot with color-coded groups
- trend line using np.polyfit() and np.poly1d()
- correlation calculation using scipy.stats.pearsonr()
- Professional styling (labels, title, grid, legend)

**What I used:** Entire structure, modified random noise parameter and added comments.

---

### Follow-up Prompts:

**Prompt 7:** "Explain what np.polyfit() and np.poly1d() do in simple terms"

**AI Response Summary:**
"np.polyfit() finds the line (or curve) that best fits your data points. np.poly1d() turns the equation of that line into a function you can use to calculate y-values for plotting."

**Understanding Level:** I understand what it does conceptually (line of best fit), but not the mathematical algorithm.

---

**Prompt 8:** "Add a second visualization showing sleep_hours vs exam_score with the same styling"

**AI Response Summary:**
Generated parallel code following the same pattern but with sleep_hours on x-axis, different color scheme, and separate correlation calculation.

**What I used:** All of it, changed colors to match my portfolio theme.

---

**Prompt 9:** "What does the 'alpha' parameter in plt.scatter() do?"

**AI Response Summary:**
"Controls transparency. alpha=0.6 means 60% opaque / 40% transparent, useful when points overlap so you can see density."

**Understanding Level:** Now I fully understand this parameter and can use it independently.

---

## General Learning Prompts:

**Prompt 10:** "What's the difference between localStorage, sessionStorage, and cookies in web development?"

**AI Response Summary:**
- localStorage: persists indefinitely across sessions
- sessionStorage: cleared when browser tab closes
- cookies: sent with HTTP requests, has expiration dates, smaller storage limit

**Understanding:** This helped me understand why localStorage was the right choice for dark mode preference.

---

**Prompt 11:** "What is a Pearson correlation coefficient and what do the values mean?"

**AI Response Summary:**
- Ranges from -1 to +1
- +1 = perfect positive correlation (both increase together)
- -1 = perfect negative correlation (one increases, other decreases)
- 0 = no linear relationship
- 0.7-1.0 = strong, 0.3-0.7 = moderate, 0.0-0.3 = weak

**Understanding:** Conceptually clear, but I don't know the mathematical formula for calculating it.

---

## Prompts I Decided NOT To Use:

**Rejected Prompt:** "Generate a complete dark mode system with automatic time-based switching and user preference detection"

**Why I rejected this:**
Too complex for my current understanding level. I wanted to understand each piece (CSS variables, localStorage, toggle button) before combining them. AI's output would have been a black box.

---

**Rejected Prompt:** "Write Python code to scrape real student data from a university database"

**Why I rejected this:**
1. Ethical concerns about scraping real student data
2. Too advanced for my current Python skills
3. The lab objective was about AI-assisted coding, not web scraping
4. Synthetic data serves the learning purpose just as well

---

## Reflection on Prompting Strategy:

**What worked well:**
- Starting with conceptual questions ("How do I...") before requesting code
- Breaking complex features into smaller prompts (CSS, then HTML, then JS separately)
- Asking AI to explain unfamiliar terms and functions
- Following up when I didn't understand something

**What I would improve:**
- I should have asked for accessibility considerations upfront (keyboard navigation, ARIA labels)
- Could have requested responsive design guidance for mobile vs. desktop
- Would be more specific about coding style preferences (tabs vs spaces, bracket style)

**Key insight:**
The quality of AI output depends heavily on prompt clarity. Vague prompts ("make it look good") produce generic code. Specific prompts with constraints ("using CSS custom properties, maintain my pink theme, position in navigation bar") produce tailored, usable code.

---

**Total Prompts Used:** 11 prompts (plus several follow-ups not listed)

**Most Valuable Prompt:** #4 (localStorage implementation) - This gave me a complete pattern I can now reuse for other user preferences.

**Prompt I Learned Most From:** #6 (Python visualization) - Seeing a complete data pipeline helped me understand how numpy/pandas/matplotlib work together.

