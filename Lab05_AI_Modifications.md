# AI Original Output vs. My Modifications

**Student:** Springer Tebeau  
**Lab 5:** Vibe Coding

This document shows examples of AI-generated code BEFORE my modifications, and what I changed.

---

## Example 1: Dark Mode CSS Variables

### AI's Original Output:

```css
:root {
    --primary-color: #f4a6c8;
    --bg-color: #f4f4f4;
    --text-color: #333;
}

body.dark-mode {
    --bg-color: #0a0a0a;
    --text-color: #e5e5e5;
}
```

### What I Changed and Why:

**Problem:** The AI only created variables for background and text, but my portfolio uses colors for cards, borders, tables, and code blocks.

**My Modified Version:**

```css
:root {
    --primary-color: #f4a6c8;
    --bg-color: #f4f4f4;
    --text-color: #333;
    --card-bg: #ffffff;        /* ADDED */
    --section-bg: #ffffff;     /* ADDED */
    --border-color: #e2e8f0;   /* ADDED */
    --code-bg: #2d2d2d;        /* ADDED */
}

body.dark-mode {
    --bg-color: #1a1a1a;       /* CHANGED from #0a0a0a (too dark) */
    --text-color: #e5e5e5;
    --card-bg: #2d2d2d;        /* ADDED */
    --section-bg: #2d2d2d;     /* ADDED */
    --border-color: #404040;   /* ADDED */
    --code-bg: #1e1e1e;        /* ADDED */
}
```

**Reason for changes:**
1. Extended dark mode support to all page elements (not just body and text)
2. Lightened dark background because pure black (#0a0a0a) was too harsh and hard to read
3. Ensured all CSS that used hardcoded colors now references variables

---

## Example 2: Dark Mode Toggle Button

### AI's Original Output:

```css
.dark-mode-toggle {
    position: absolute;
    right: 1rem;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(255, 255, 255, 0.2);
    border: 2px solid rgba(255, 255, 255, 0.3);
    border-radius: 20px;
    padding: 0.3rem;           /* ORIGINAL */
    cursor: pointer;
    font-size: 1.2rem;
}
```

### What I Changed and Why:

**Problem:** The button was too small (0.3rem padding) and hard to tap on mobile devices. Also lacked spacing for the icon.

**My Modified Version:**

```css
.dark-mode-toggle {
    position: absolute;
    right: 1rem;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(255, 255, 255, 0.2);
    border: 2px solid rgba(255, 255, 255, 0.3);
    border-radius: 20px;
    padding: 0.5rem 1rem;      /* CHANGED for better touch targets */
    cursor: pointer;
    font-size: 1.2rem;
    display: flex;              /* ADDED */
    align-items: center;        /* ADDED */
    gap: 0.5rem;               /* ADDED for icon spacing */
}
```

**Reason for changes:**
- Increased padding to meet iOS minimum touch target size (44x44px)
- Added flexbox properties for better icon centering
- Made button more visible and easier to interact with

---

## Example 3: localStorage JavaScript

### AI's Original Output:

```javascript
const darkModeToggle = document.querySelector('.dark-mode-toggle');
const body = document.body;

darkModeToggle.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
    
    if (body.classList.contains('dark-mode')) {
        localStorage.setItem('darkMode', 'enabled');
    } else {
        localStorage.setItem('darkMode', 'disabled');
    }
});
```

### What I Changed and Why:

**Problem 1:** No icon switching logic  
**Problem 2:** Doesn't check localStorage on page load, so preference isn't persistent

**My Modified Version:**

```javascript
const darkModeToggle = document.querySelector('.dark-mode-toggle');
const body = document.body;
const icon = darkModeToggle.querySelector('.icon');  // ADDED

// Check saved preference on page load (ADDED ENTIRE BLOCK)
if (localStorage.getItem('darkMode') === 'enabled') {
    body.classList.add('dark-mode');
    icon.textContent = '☀️';
}

darkModeToggle.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
    
    // Update icon based on mode (ADDED)
    if (body.classList.contains('dark-mode')) {
        icon.textContent = '☀️';  // ADDED
        localStorage.setItem('darkMode', 'enabled');
    } else {
        icon.textContent = '🌙';  // ADDED
        localStorage.setItem('darkMode', 'disabled');
    }
});
```

**Reason for changes:**
1. Added `const icon` to select the icon element
2. Added page load check to apply saved preference immediately
3. Added icon switching logic so users see visual feedback
4. This makes the feature actually functional (AI's version saved preference but didn't use it)

---

## Example 4: Python Data Generation

### AI's Original Output:

```python
# Generate exam scores
data['exam_score'] = (
    50 +
    (data['study_hours'] * 3) +
    (data['sleep_hours'] * 2) +
    np.random.uniform(0, 20, n_students)  # ORIGINAL: 0-20 range
)
```

### What I Changed and Why:

**Problem:** Random noise of 0-20 points made the correlation too weak (r=0.52 instead of 0.76). The point of the visualization is to demonstrate correlation, so too much randomness obscures the pattern.

**My Modified Version:**

```python
# Generate exam scores
data['exam_score'] = (
    50 +
    (data['study_hours'] * 3) +
    (data['sleep_hours'] * 2) +
    np.random.uniform(0, 15, n_students)  # CHANGED: 0-15 range
)
```

**Reason for change:**
- Reduced noise from 0-20 to 0-15 to make the correlation clearer
- Still maintains realistic variation (no perfect correlation)
- Better demonstrates the study-performance relationship for educational purposes
- Resulted in correlation of 0.76 (strong positive) vs 0.52 (moderate)

---

## Example 5: Matplotlib Scatter Plot Colors

### AI's Original Output:

```python
colors = {'Low': 'red', 'Medium': 'yellow', 'High': 'green'}
```

### What I Changed and Why:

**Problem:** Generic color names don't match my portfolio's pink/gold theme.

**My Modified Version:**

```python
colors = {
    'Low (≤5h)': '#ff6b6b',      # Coral red (matches pink theme)
    'Medium (6-7h)': '#ffd93d',  # Gold (matches accent color)
    'High (8+h)': '#6bcf7f'      # Mint green (complementary)
}
```

**Reason for changes:**
1. Used hex codes for precise color matching with portfolio
2. Updated category labels to include hour ranges for clarity
3. Chose colors that work well together and maintain visual hierarchy

---

## Example 6: What I DIDN'T Change

### AI's Trend Line Code:

```python
z = np.polyfit(df['study_hours'], df['exam_score'], 1)
p = np.poly1d(z)
plt.plot(df['study_hours'], p(df['study_hours']), "r--", linewidth=2)
```

**Why I kept this unchanged:**
- It works correctly
- I understand what it does conceptually (creates line of best fit)
- I don't know enough about polynomial fitting to improve it
- Modifying code I don't fully understand could introduce bugs

**My Understanding Spectrum:** "I know what it does but not how"

This is honest self-assessment - I use this code but acknowledge I couldn't write it from scratch yet.

---

## Summary of Modification Patterns

### Types of Changes I Made:
1. **Usability improvements** (button sizing for mobile)
2. **Visual consistency** (colors matching portfolio theme)
3. **Bug fixes** (icon not updating on page load)
4. **Feature extensions** (adding more CSS variables)
5. **Parameter tuning** (adjusting random noise for clearer correlation)

### What I Left Unchanged:
- Advanced algorithms I don't fully understand (polyfit, correlation calculation)
- Code that works correctly and doesn't need improvement
- Professional styling that's already polished

### Key Insight:
I modified approximately 30-40% of the AI-generated code. This balance shows:
- I'm not blindly copying (I evaluated and improved)
- I'm also not over-engineering (I accepted good solutions)
- I know where my understanding ends (left complex algorithms alone)

This is evidence of **collaborative coding** rather than passive acceptance or unnecessary modification.

