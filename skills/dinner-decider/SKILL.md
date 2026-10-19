---
name: dinner-decider
description: Help a couple decide tonight's dinner together. Suggests cheap, hearty meals a two-year-old will also eat, plus easy separate toddler backups, then produces a voting link the partner can open on any phone (no Claude account needed). Use when the user asks "what's for dinner", "help us pick dinner", "dinner ideas tonight", or mentions what's in the fridge.
---

# Dinner Decider

Goal: get from "I don't know, what do you want?" to a decided dinner in a few minutes, with both
adults having an equal say and the toddler covered.

The voting page is at https://kalston96.github.io/dinner/. Both people vote 👍 / 🤷 / 👎 on each
option. Anything either person vetoes is out, and the best mutual match wins (ties go to cheaper,
then faster). The whole vote lives in the link, so it works by text message with no login.

## House rules (always apply)

- **Time is the main constraint.** Cooking starts at 7:00 PM, or 6:30 PM at the earliest, and
  everyone eats between 8:00 and 8:30. Every dinner must take **60 minutes or less** from start to
  table. Nothing that needs a morning slow-cooker start or overnight marinating.
- **Prefer what's already at home**, then things that are easy to grab on the way home.
- **Budget:** about **$3 per serving or less**. Plan **4 servings**: 2 adults, the toddler, and about
  one leftover lunch. That's roughly $12 for the whole meal.
- **Hearty:** a protein, a filling starch (pasta, rice, potatoes, bread, tortillas) and a vegetable
  or fruit, so nobody's hungry an hour later.
- **No mushrooms**, ever. Watch for hidden ones in frozen stir-fry mixes and cream-of-mushroom soup.

## Steps

1. **Ask at most two quick questions** (skip any the user already answered):
   - Anything in the fridge or pantry that needs using up?
   - Starting at 6:30 or 7:00 tonight?

2. **Suggest 3–5 dinners** that fit the house rules. For each, give the cook time and the time
   you'll eat (for example, "35 min, eat ~7:40") and a short shopping list for 4 servings.
   Each one must also be:
   - **Toddler-friendly**: soft, mild, and easy to cut up. For each, add one line on how to adapt it
     for a 2-year-old (pull a portion before adding spice, cut small, sauce on the side).

   Also suggest 2–3 **separate toddler backups** that take 10 minutes or less (buttered noodles + peas,
   eggs + toast fingers, quesadilla triangles) in case he won't eat the main dinner.

   Toddler safety, always: quarter grapes, cherry tomatoes and hot dogs lengthwise; no whole nuts or
   popcorn; spread nut butter thin.

3. **Make the voting link** with the bundled script:

   ```bash
   # Add tonight's ideas on top of the standard menu (17 staples + 10 toddler options)
   python3 scripts/make_link.py "Chicken & veggie stir fry" "Chili mac with the leftover chili"

   # Or vote on ONLY tonight's ideas (shorter list, faster decision)
   python3 scripts/make_link.py --only "Chicken stir fry" "Breakfast burritos" "Baked potato bar"
   ```

   Use `--only` when the user has a specific short list (for example, the fridge clean-out).
   Otherwise add to the standard menu.

4. **Give the user a message they can paste**, ready for a text:

   > Dinner vote! Tap, vote yes/maybe/no, and it'll show what we both want: <link>

   Remind them: they vote first, then send the link; the partner votes second and sees the matches
   immediately, then can send the result back. If the Gmail connector is available and the user asks,
   you can draft the email for them, but texting the link is usually fastest.

## Without the script

If the script can't run (for example, on the Claude mobile app), give the plain link
https://kalston96.github.io/dinner/ and tell the user to add tonight's ideas with the
"Craving something else?" box before they vote. Those ideas travel with the link.
