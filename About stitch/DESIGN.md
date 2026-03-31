# Design System Document

## 1. Overview & Creative North Star
### Creative North Star: "The Silent Terminal"
In the world of cybersecurity, precision and clarity are paramount. This design system moves away from the chaotic, "hacker-movie" tropes to embrace an aesthetic of high-end editorial tech. It treats digital space like a high-end gallery for technical intelligence. 

The system is built on **Tonal Minimalism**. We break the standard "template" look by eschewing rigid borders in favor of overlapping surface tiers and intentional asymmetry. The layout should feel like a sophisticated command center—utilizing the technical rigor of a grid while allowing for expansive whitespace that suggests authority and calm.

---

## 2. Colors
Our palette is a sophisticated dark-mode ecosystem where depth is created through luminance shifts rather than lines.

*   **Background (`#131318`):** The absolute canvas. All interfaces begin here.
*   **Primary (`#83dc5d`):** A neon emerald reserved for high-value interactions, terminal success states, and critical data points.
*   **Neutral Hierarchy:** Surfaces (`surface_container_low` to `highest`) provide the structural rhythm of the page.

### The "No-Line" Rule
**Explicit Instruction:** Do not use 1px solid borders to separate sections. Boundaries must be defined solely through background color shifts. For example, a project card (`surface_container_low`) should sit on the main `background` without an outline. The contrast in value is your divider.

### Surface Hierarchy & Nesting
Treat the UI as physical layers.
*   **Level 0:** `surface` (The foundation).
*   **Level 1:** `surface_container_low` (Section backgrounds).
*   **Level 2:** `surface_container_high` (Floating cards or interactive modules).
Each inner container must use a slightly higher or lower tier than its parent to define its importance and "lift."

### The "Glass & Gradient" Rule
To elevate the "tech" aesthetic beyond flat boxes, use **Glassmorphism**. Floating navigation bars or terminal overlays should use semi-transparent surface colors with a `backdrop-blur` (e.g., 20px). Main CTAs should utilize a subtle linear gradient from `primary` to `primary_container` (135-degree angle) to give the neon a sense of glowing "soul."

---

## 3. Typography
The typography system pairs the technical precision of **Inter** with the architectural character of **Space Grotesk**.

*   **Display & Headlines (Space Grotesk):** These are your "Editorial" voices. Use `display-lg` for hero sections with wide tracking to emphasize the "minimalist tech" vibe.
*   **Body & Titles (Inter):** The "Functional" voice. Highly legible, neutral, and clean. 
*   **Hierarchy as Identity:** Use high contrast in scale—pairing a massive `display-lg` headline with a tiny, uppercase `label-md` for metadata—to create a professional, magazine-style layout.

---

## 4. Elevation & Depth
In this system, elevation is a matter of light and tone, not drop-shadows.

### The Layering Principle
Depth is achieved by stacking surface tokens. Place a `surface_container_lowest` card on a `surface_container_low` section to create a soft, natural "recessed" effect.

### Ambient Shadows
When a floating effect is required (e.g., a modal or a primary terminal window), shadows must be extra-diffused:
*   **Blur:** 32px – 64px
*   **Opacity:** 4% – 8%
*   **Color:** Use a tinted version of `on_surface` rather than pure black to keep the shadows feeling "ambient" and integrated.

### The "Ghost Border" Fallback
If accessibility requires a container edge, use a **Ghost Border**: `outline_variant` at 15% opacity. Full-opacity borders are strictly forbidden.

---

## 5. Components

### Buttons
*   **Primary:** `primary` background with `on_primary` text. Use a `0.25rem` (DEFAULT) radius for a sharp, technical look.
*   **Tertiary:** Ghost style. No background, `primary` text, and a subtle underline only on hover.

### Terminal Blocks (Signature Component)
The core of the portfolio. 
*   **Background:** `surface_container_highest`.
*   **Typography:** `body-sm` (Monospace font recommended if available, otherwise Inter).
*   **Accents:** Use `primary` for prompts (`>`) and success messages; `error` for failed scripts.

### Cards & Lists
*   **Rule:** Forbid divider lines. 
*   **Spacing:** Use `spacing-8` (2.75rem) to separate project items. 
*   **Structure:** Place an image or terminal snippet on a `surface_container_low` card. Text should live directly on the `background` surface below it or offset to the side to break the grid's rigidity.

### Input Fields
*   **State:** Default fields use `surface_container_highest` with no border. 
*   **Focus:** Transition to a 1px `primary` ghost border (20% opacity) and a subtle `primary` outer glow.

---

## 6. Do's and Don'ts

### Do
*   **Do** use asymmetrical layouts. For example, left-align your headline and right-align the body text in a grid column to create visual tension.
*   **Do** use `primary` (emerald) sparingly. It is a "laser pointer," not a paint brush.
*   **Do** lean into `surface_container_lowest` for "cut-out" effects in the UI where content feels etched into the page.

### Don't
*   **Don't** use standard "Material" shadows. They are too heavy for this editorial aesthetic.
*   **Don't** use rounded corners above `0.75rem` (xl). We want the interface to feel architectural and sharp, not "bubbly."
*   **Don't** use pure black `#000000`. Use the `surface` token (`#131318`) to allow for tonal depth and "glow" to breathe.