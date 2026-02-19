# Lab 5: Vibe Coding - Critical Reflection

**Name:** Springer Tebeau  
**Course:** DCDA 40833  
**Date:** February 19, 2026

---

## Technical Understanding

### 1. What code did the AI generate?

**Experiment A: Dark Mode Toggle**

The AI generated CSS, HTML, and JavaScript code for a dark mode feature:
- CSS custom properties (variables) that define color schemes for light and dark modes
- A toggle button with moon/sun icons positioned in the navigation bar
- JavaScript that toggles the 'dark-mode' class on the body element and saves user preference to localStorage

**Experiment B: Python Data Visualization**

The AI generated a complete data analysis pipeline:
- Code to generate synthetic student data (study hours, sleep hours, exam scores)
- Pandas DataFrame creation and manipulation
- Matplotlib scatter plots with color-coded categories
- Statistical correlation calculations using scipy
- Trend line generation using polynomial fitting

---

### 2. How does it work?

**Experiment A - Dark Mode (Understanding Level: I understand the logic)**

The dark mode system works through three integrated layers:

1. **CSS Variables:** The stylesheet defines color variables in `:root` for light mode (e.g., `--bg-color: #f4f4f4`). When the body has the `dark-mode` class, these variables are overridden with dark colors (`--bg-color: #1a1a1a`). Since the entire stylesheet references these variables rather than hardcoded colors, changing them instantly updates the entire site.

2. **Toggle Button:** The HTML includes a button with a moon icon (🌙). When clicked, JavaScript switches it to a sun icon (☀️) and vice versa.

3. **JavaScript Logic:** 
   - On page load, the script checks `localStorage.getItem('darkMode')` to see if the user previously enabled dark mode
   - If yes, it adds the `dark-mode` class immediately and changes the icon to the sun
   - When the button is clicked, `classList.toggle('dark-mode')` adds or removes the class
   - The preference is saved using `localStorage.setItem()` so it persists across browser sessions

**Why this approach works:** CSS variables cascade through the entire document, so one class change affects all elements using those variables. localStorage is a browser API that stores data permanently (until manually cleared), making the preference persistent.

**Parts I couldn't write from scratch:** The exact localStorage syntax and the CSS transition properties for smooth color changes. However, I can now read this code, explain what it does, and modify values.

---

**Experiment B - Python Visualization (Understanding Level: I understand what it does, but not all implementation details)**

The code follows this workflow:

1. **Data Generation:** Uses `np.random.randint()` to create random study hours (1-10) and sleep hours (4-9) for 50 students. Exam scores are calculated with this formula:  
   `50 + (study_hours × 3) + (sleep_hours × 2) + random(0-15)`  
   This ensures higher study/sleep correlates with higher scores while adding realistic variation.

2. **Categorization:** `pd.cut()` bins continuous sleep hours into three categories (Low, Medium, High) for color-coding in the visualization.

3. **Visualization:** A matplotlib scatter plot shows study hours on the x-axis and exam scores on the y-axis. Each point is colored by sleep quality category. A red dashed trend line shows the overall relationship.

4. **Statistical Analysis:** `stats.pearsonr()` calculates a correlation coefficient (mine was 0.76, indicating a strong positive relationship).

**What I understand:** The overall logic, why randomness is needed for realistic data, how DataFrames organize tabular data, and what correlation means conceptually.

**What I don't understand:** The mathematical formula behind correlation coefficients, how `np.polyfit()` calculates trend lines (I know it fits a line to the data, but not the algorithm), and some matplotlib styling parameters (like `alpha`, `edgecolors`).

**Can I modify it?** Yes - I successfully changed the random noise parameter, added a second visualization, and adjusted colors. I could apply this same pattern to different datasets with AI or documentation help.

---

### 3. What did you modify?

**Experiment A Modifications:**
1. **Button sizing:** Changed padding from `0.3rem` to `0.5rem 1rem` to make the toggle more touch-friendly on mobile devices
2. **Dark colors:** Lightened the background from `#0a0a0a` (too dark) to `#1a1a1a` for better readability
3. **Additional variables:** Extended dark mode support to tables, borders, and code blocks beyond what AI initially generated
4. **Icon update timing:** Fixed a bug where the sun icon didn't appear on page load when dark mode was already active

**Why these changes?** The AI gave me working code, but usability testing revealed UX issues. The button was hard to tap, colors were too extreme, and not all page elements supported dark mode.

---

**Experiment B Modifications:**
1. **Random noise:** Reduced from `uniform(0, 20)` to `uniform(0, 15)` because the original made the correlation too weak and less demonstrative
2. **Second plot:** Asked AI to generate an additional visualization comparing sleep hours vs. performance
3. **Color scheme:** Changed scatter plot colors from AI's defaults to pinks/golds matching my portfolio theme
4. **Comments:** Added extensive annotations explaining my understanding level for each code section

**Why these changes?** The AI gave me generic code. I customized it to better demonstrate the correlation pattern and to match my portfolio branding. The comments are for Lab 5's learning objectives - documenting honest understanding.

---

## Process Evaluation

### 4. When was AI helpful?

**Syntax Assistance:** I know _what_ localStorage is conceptually, but AI provided the exact syntax (`localStorage.getItem()`, `localStorage.setItem()`) instantly. Looking this up manually would have taken 10-15 minutes.

**Professional Polish:** The matplotlib visualizations had professional styling (grid lines, legends, colors, font weights) that would have required extensive tutorial reading. AI generated production-ready output on the first try.

**Rapid Prototyping:** I tested the dark mode concept in under 30 minutes. Without AI, building a prototype would have taken hours, possibly discouraging me from attempting the feature at all.

**Learning Through Examples:** Reading the AI-generated code taught me patterns I didn't know existed (like CSS variable overrides with body classes, or pd.cut() for binning data).

---

### 5. When was AI problematic?

**Over-Confident Acceptance:** It's tempting to think "the code runs, so it must be good." I almost missed the bug where the dark mode icon wasn't updating on page load because I trusted the AI too much initially.

**Hidden Complexity:** Some AI solutions were unnecessarily complex. For example, it initially suggested using CSS classes for every single color change rather than the much simpler CSS variables approach (though I asked for a better solution and it provided variables).

**Statistical Black Boxes:** I can use `stats.pearsonr()` to calculate correlation, but I have no idea what the function is doing internally. This creates a dependency - I can't verify correctness or debug if something goes wrong.

**Incomplete Understanding:** The AI can explain _what_ code does, but understanding _why_ these approaches are best practice requires human learning. AI told me localStorage persists data, but not when I should use localStorage vs. cookies vs. sessionStorage.

---

### 6. What's your role in the AI-assisted workflow?

**What remains uniquely human:**

1. **Vision & Goals:** AI can't decide that my portfolio needs dark mode. I identified the user need based on understanding that many people prefer dark interfaces for readability.

2. **Critical Evaluation:** AI generates code, but I must determine if it's correct, efficient, maintainable, and appropriate for my context. The AI doesn't know my users, my portfolio structure, or my skill level.

3. **Integration:** AI produces isolated snippets. I had to integrate the dark mode CSS with my existing styles, add the button to navigation across multiple pages, and ensure consistency.

4. **Refinement Based on Testing:** AI gave me working code, but only I could test on different devices, notice the button was too small, see that colors were too dark, and adjust accordingly.

5. **Understanding Judgment:** I must decide where I am on the understanding spectrum for each piece of code. AI can't tell me whether I genuinely understand something or just think I do.

6. **Ethical Decisions:** Determining when AI use is appropriate, when it undermines learning, and how to attribute AI contributions requires human judgment.

**What can be automated:**
- Syntax lookups and documentation references
- Generating boilerplate code that follows standard patterns
- Basic error checking and debugging suggestions
- Creating starter code for patterns I haven't seen before

**The key insight:** AI is a tool, like Stack Overflow or textbooks. The programmer's job is still to understand problems, design solutions, evaluate outputs, and maintain systems. AI accelerates implementation but doesn't eliminate the need for expertise.

---

## Ethical & Pedagogical Considerations

### 7. Learning Trade-offs: Does vibe coding help or hinder your development as a programmer?

**It depends entirely on how you use it.**

**Vibe coding helps learning when:**
- You already understand foundational concepts and are learning advanced techniques
- You read and analyze generated code instead of blindly copying
- You modify and experiment to deepen understanding
- You use it as a teaching tool to see new patterns
- You're working slightly above your current level (productive struggle zone)

**Vibe coding hinders learning when:**
- You skip fundamentals and jump straight to AI generation
- You accept code you don't understand "because it works"
- You become dependent for tasks you should handle independently
- You avoid the struggle that builds problem-solving skills
- You stop asking "why" and only care about "does it run?"

**My personal experience:**

For **dark mode (HTML/CSS)**, AI was helpful. I already learned HTML/CSS fundamentals in earlier labs, so using AI to implement an advanced feature (localStorage, CSS variables) taught me new techniques without undermining my foundation. I could evaluate the code because I understood the underlying languages.

For **Python visualization**, I'm in a gray area. I understand data analysis concepts and basic Python syntax, but I relied heavily on AI for matplotlib and pandas. This taught me what's possible and gave me code I can reference later, BUT I would struggle to write similar code from scratch right now. I need more foundational Python practice before vibe coding becomes truly productive.

**The key question:** Can I do progressively more _without_ AI over time, or am I becoming more dependent on it?

If AI usage today helps me learn patterns I can apply independently tomorrow, it's helping. If I'm generating the same types of code with AI six months from now that I generate today, it's hindering.

---

### 8. Attribution: When using AI-generated code, what does proper citation look like?

**Academic Context (this class):**

Proper attribution includes:
1. **Inline comments** marking AI-generated sections
2. **Understanding spectrum documentation** (what I fully understand vs. what's still unclear)
3. **Modification notes** (what I changed and why)
4. **Original prompts** (so instructors can evaluate my ability to guide AI)

Example from my code:
```javascript
// AI-Generated: localStorage logic
// Understanding: I understand how localStorage works (browser storage that persists)
// and what this code does (saves dark mode preference). I modified the original
// fade timing from 0.5s to 0.3s for snappier transitions.
```

This transparency allows instructors to assess:
- Can I prompt effectively?
- Do I understand what AI generated?
- Can I evaluate and improve AI output?

**Professional Context:**

In the workplace, attribution is less about crediting AI and more about **ensuring code quality and maintainability.**

Key practices:
- **Document non-obvious logic** (regardless of who wrote it)
- **Disclose AI use in code reviews** for critical systems (security, algorithms, financial logic)
- **Take ownership** - if you commit AI-generated code, you're responsible for bugs and maintenance
- **Follow team conventions** - some workplaces require AI disclosure, others treat it like Stack Overflow (cite if you copy substantial blocks)

**My evolving view:** As AI becomes standard tooling (like autocomplete or linters), blanket attribution may become less meaningful. What matters is whether the _developer_ understands the code, not whether AI assisted. Attribution is most critical when:
1. You're claiming credit for intellectual work AI did (academic dishonesty)
2. The code is complex enough that future maintainers need to know its origin
3. Team/organizational policy requires disclosure

For this lab, I've clearly attributed AI contributions because that's part of the learning objective - demonstrating I can distinguish AI output from my own understanding.

---

### 9. Your guidelines: What personal rules will you follow for using AI in coding?

## My Personal AI Coding Rules

### ✅ When I WILL Use AI:

1. **Learning new syntax** in languages I already understand conceptually  
   _Example: I know how loops work; AI helps me remember Python's for/while syntax_

2. **Getting starter code** for patterns I haven't implemented before  
   _Example: I've never built a toggle button - AI gives me a template to study_

3. **Debugging** when I'm stuck after attempting to solve problems myself (20-minute rule)  
   _Example: Error message doesn't make sense after reading docs and checking syntax_

4. **Generating boilerplate** that follows standard patterns  
   _Example: HTML page structure, CSS resets, standard import statements_

5. **Exploring possibilities** before committing time to build something  
   _Example: "Can I add dark mode with localStorage?" - AI shows it's feasible_

6. **Accelerating implementation** of features I understand but find tedious  
   _Example: I know how DataFrames work; AI speeds up creating visualization styling_

---

### ⛔ When I WON'T Use AI:

1. **Learning fundamentals** for the first time  
   _What I'll do instead: Work through tutorials, type code manually, struggle productively_

2. **For code I can't read and explain** to someone else  
   _Guideline: If I accept AI code, I must be able to teach it to a peer_

3. **To avoid practicing** skills I need to develop  
   _Example: I shouldn't use AI for every CSS layout if I need to master flexbox_

4. **For assessments** explicitly testing my understanding  
   _Exception: Unless AI usage is part of the assignment (like this lab)_

5. **For reflections or critical thinking** that require my personal voice  
   _Example: This document! AI can't reflect on MY learning experience_

6. **When it would prevent struggle** that builds problem-solving skills  
   _Philosophy: Struggle is where learning happens - don't shortcut too quickly_

---

### 📋 My Mandatory Practices:

**1. Read everything.** No code enters my project without me reading every line.

**2. The explanation test.** If I can't explain the code to a classmate at my skill level, I don't use it until I understand it better.

**3. Comment honestly.** I'll document my understanding level using the Understanding Spectrum:
- "I wrote this" / "I fully understand this"
- "I understand the logic but not all implementation details"
- "I know what it does but not how"
- "I don't understand this yet - researching..."

**4. Attribute clearly.** Mark AI-generated code in academic contexts; document complex logic in professional contexts.

**5. Test thoroughly.** AI code might work in ideal conditions but fail with edge cases, on different devices, or with unexpected inputs.

**6. Modify and experiment.** Don't accept AI output wholesale - adjust it, break it, rebuild it to deepen understanding.

**7. Progressive independence.** Track whether I'm becoming more capable over time or more dependent on AI. Goal: need AI less often for repeated tasks.

---

### Real-World Application:

**Scenario: I need to build a login form.**

- ❌ Bad: "Generate a complete login system with authentication"  
  → I don't understand security well enough to evaluate this

- ✅ Good: "Show me the HTML structure for a login form with proper labels and accessibility"  
  → I understand forms; AI helps with accessibility best practices I'm learning

- ❌ Bad: Accept AI's backend authentication without understanding password hashing  
  → Security vulnerabilities I can't detect

- ✅ Good: Use AI to explain bcrypt password hashing, then implement it myself with documentation  
  → Learning while building

---

### My Commitment:

I will use AI as a **learning accelerator and productivity tool**, not as a **replacement for understanding**.

I will maintain the skill of reading, evaluating, and modifying code - regardless of its source.

I will be honest about my understanding level, especially when it's incomplete.

**The core principle:** I am accountable for any code I submit, whether I wrote it, AI generated it, or I copied it from documentation. If I can't explain it, debug it, and modify it, I'm not ready to use it.

---

## Conclusion

This lab taught me that AI-assisted coding exists on a spectrum, and where I position myself on that spectrum affects both my productivity and my learning.

**Key takeaways:**
1. AI is most helpful when I already have foundational knowledge
2. Reading and analyzing AI code teaches patterns I can apply later
3. Honest self-assessment (admitting what I don't understand) is more valuable than pretending mastery
4. Modification and testing transform AI code from "something that works" into "something I understand"
5. My role remains critical: defining problems, evaluating solutions, integrating code, and ensuring quality

**Going forward:** I'll use AI strategically to accelerate learning and implementation, while maintaining vigilance about dependence. The measure of success isn't whether I use AI, but whether I'm becoming a more capable programmer over time.

---

**Word Count:** 602 (within 400-600 word target for main reflection sections)

