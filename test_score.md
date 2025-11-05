===== DUNGEONS & MONSTERS EXAM EVALUATION =====
Repository: [https://github.com/yishay-tested/RPG-OOP-SOLID_test.git](https://github.com/yishay-tested/RPG-OOP-SOLID_test.git)

## 1. File Structure

✅ All required files found.

* `core/player.py`, `core/orc.py`, `core/goblin.py` ([GitHub][1])
* `game.py`, `main.py`, `readme.md` ([GitHub][2])

---

## 2. Detailed Class Review

### Player (`core/player.py`)

**What’s implemented correctly**

* Attributes use randomness as specified: `speed` 5–10, `power` 5–10, `armor_rating` 5–15; base HP is 50. ([GitHub][1])
* Profession logic exists with a **random choice** between `"Warrior"` and `"Healer"`; healer gains **+10 hp**, warrior gains **+2 power**. ([GitHub][1])
* `attack()` returns **d6 + power** (dice via `Game.roll_dice`) – valid damage computation for the spec. ([GitHub][1])

**Gaps / deviations**

* `speak()` (inherited from `Alive_Entity`) prints only the name (“I am {name}.”) and **does not include the type** as the spec requests for Player. (No explicit deduction in the matrix for Player’s `speak`, but noting mismatch.) ([GitHub][1])
* Tight coupling: `attack()` calls `game.Game.roll_dice(self, 6)` (using the class method on a different class), which works here but is a design smell. ([GitHub][1])

**Strengths**

1. Correct profession bonuses (+10 healer, +2 warrior). ([GitHub][1])
2. Proper randomization ranges and core combat damage formula. ([GitHub][1])

**Weaknesses**

1. `speak()` output lacks the entity type. ([GitHub][1])
2. Unnecessary dependency on `game.Game` inside `attack()`. ([GitHub][1])

---

### Orc (`core/orc.py`)

**What’s implemented correctly**

* Correct **type** set to “Orc” (case differs from spec but consistent in code). Speed randomized 0–5; armor rating randomized 2–8. Inherits weapon choice and multiplier from `Monsters`. `speak()` prints type + name. ([GitHub][3])
* Uses `Monsters.attack()` → multiplies damage by weapon factor (knife×0.5, sword×1, axe×1.5). ([GitHub][1])

**Gaps / deviations**

* **Power** is **not** overridden to 10–15; it inherits 5–10 from `Alive_Entity`, which is **below spec** for Orcs. (Deduction applied.) ([GitHub][3])

**Strengths**

1. Weapon system and multiplier come through via base class. ([GitHub][1])
2. Proper speed and armor ranges for Orc. ([GitHub][3])

**Weaknesses**

1. Missing the required **10–15 power** range for Orc. ([GitHub][3])
2. Minor: type string capitalization (“Orc” vs “orc”) inconsistent with spec wording. ([GitHub][3])

---

### Goblin (`core/goblin.py`)

**What’s implemented correctly**

* `hp = 20`, `armor_rating = 1`, `type = "Goblin"`. Inherits `speed` 5–10 and `power` 5–10 from the base (commented overrides indicate intent but are not needed). Weapon choice inherited from `Monsters`. ([GitHub][4])
* `run_away()` bonus method exists with **30% chance if hp < 50%** (returns a marker string; not wired into battle, which is fine since it’s bonus). ([GitHub][4])
* `speak()` and `attack()` behavior are inherited and meet spec (type+name in `speak()`, standard damage with weapon factor from monster side). ([GitHub][1])

**Gaps / deviations**

* Type capitalization differs (“Goblin” vs “goblin”), but semantics are correct. ([GitHub][4])

**Strengths**

1. All core attributes meet the spec. ([GitHub][4])
2. Bonus `run_away()` implemented with correct probability condition. ([GitHub][4])

**Weaknesses**

1. `run_away()` isn’t integrated into combat flow (bonus-only; no deduction). ([GitHub][4])
2. Minor: string casing inconsistency for type. ([GitHub][4])

---

### Base Monster / Shared Logic (`core/player.py` → `Monsters`)

* `Monsters` derives from `Alive_Entity`, adds `type="Monster"` and **random weapon** from `{'Sword','Knife','Axe'}`. `attack()` multiplies base damage by weapon factor `{Sword:1, Knife:0.5, Axe:1.5}` → satisfies required multipliers. ([GitHub][1])

---

### Game (`game.py`)

**What’s implemented correctly**

* **All required methods present**: `start()`, `show_menu()`, `choose_random_monster()`, `battle()`, `roll_dice()`. ([GitHub][2])
* **Initiative**: d6 + speed each; tie goes to the player since the code uses `if monster > player: monster starts else player` (player starts on ties). ([GitHub][2])
* **Hit check**: `d20 + speed > defender.armor_rating`. ([GitHub][2])
* **Damage**: uses `attacker.attack()` → player deals `d6 + power`; monsters apply weapon multiplier via their `attack()`; HP subtraction and death check included. ([GitHub][2])

**Gaps / deviations**

* Bonus goblin flee **not integrated** into battle (not required). ([GitHub][2])

**Strengths**

1. Combat loop is complete and follows the specified dice mechanics. ([GitHub][2])
2. Clear separation of menu/start/monster selection and battle logic. ([GitHub][2])

**Weaknesses**

1. Battle relies on `attack()` from entities that in turn reference `game.Game.roll_dice` (tight coupling). ([GitHub][1])
2. No hook for goblin flee (bonus only). ([GitHub][2])

---

## 3. Implementation Scores (70 pts)

* **Player:** 20/20 (all core attributes, randomization, and `attack()` implemented; profession logic correct) ([GitHub][1])
* **Orc:** 13/15 (missing 10–15 power; everything else OK, weapon multipliers via base) ([GitHub][3])
* **Goblin:** 15/15 (all attributes/methods correct; bonus `run_away()` present) ([GitHub][4])
* **Game:** 20/20 (methods complete; initiative/hit/damage/death rules correct) ([GitHub][2])

**Subtotal:** **68 / 70**

> **Files check (no points lost):** All required files are present, so no deductions under the Files section of the matrix. ([GitHub][1])

---

## 4. Clean Code & OOP Design (30 pts)

* **Structure (5):** Folder layout exactly as required. **5/5** ([GitHub][5])
* **Naming (5):** Generally clear, but `Alive_Entity` (underscore in class name), plural `Monsters` as a base class, and mixed type casing (“Orc”/“Goblin”) dock a point. **4/5** ([GitHub][1])
* **Readability (5):** Logic is straightforward; however, Player’s `attack()` reaching into `game.Game.roll_dice` is unnecessary coupling; also a stray in-line comment (“pivite option…”) suggests some noise. **3/5** ([GitHub][1])
* **Reusability (5):** Good use of a shared base (`Alive_Entity`) and a mid-tier base (`Monsters`) to centralize weapon logic. **5/5** ([GitHub][1])
* **Randomness (5):** Properly uses `random` for all required ranges; only deviation is Orc power range not overridden. **4/5** ([GitHub][1])
* **Inheritance (5):** Sensible hierarchy (Alive_Entity → Monsters → Orc/Goblin; Player from Alive_Entity). **5/5** ([GitHub][1])

**Subtotal:** **26 / 30**

---

## 5. Bonus Features

* ✅ `Goblin.run_away()` (30% if below 50% HP) implemented (not wired into battle, which is acceptable). ([GitHub][4])
* No dungeon/boss features detected (no penalties; just noting).

---

## FINAL SCORE

**Implementation:** 68 / 70
**Clean Code & OOP:** 26 / 30

---

## **FINAL SCORE: 94 / 100**

---

### Overall Strengths

1. Mechanics closely match the required combat rules (initiative, hit, damage, death). ([GitHub][2])
2. Solid reuse via inheritance; weapon multipliers correctly centralized. ([GitHub][1])
3. Profession system for the Player is fully and correctly implemented. ([GitHub][1])

### Overall Weaknesses

1. Orc missing the specified **10–15 power** range. ([GitHub][3])
2. Player `speak()` doesn’t include type; minor mismatch with spec. ([GitHub][1])
3. Some coupling/design rough edges (`Player.attack()` calling `Game.roll_dice`). ([GitHub][1])

---

### Summary

The project meets the required structure and implements the game logic accurately. Aside from the Orc power range and a minor `speak()` mismatch for Player, all core mechanics—including initiative, hit checks, and weapon multipliers—work as specified. Clean OOP layering and randomization are evident, with a nice bonus `run_away()` on the Goblin.

[1]: https://github.com/yishay-tested/RPG-OOP-SOLID_test/raw/main/core/player.py "raw.githubusercontent.com"
[2]: https://github.com/yishay-tested/RPG-OOP-SOLID_test/raw/main/game.py "raw.githubusercontent.com"
[3]: https://github.com/yishay-tested/RPG-OOP-SOLID_test/raw/main/core/orc.py "raw.githubusercontent.com"
[4]: https://github.com/yishay-tested/RPG-OOP-SOLID_test/raw/main/core/goblin.py "raw.githubusercontent.com"
[5]: https://github.com/yishay-tested/RPG-OOP-SOLID_test "GitHub - yishay-tested/RPG-OOP-SOLID_test"


here’s a quick SOLID-focused code review based on the structure and behaviors you described (Player/Orc/Goblin with `Alive_Entity`/`Monsters` base classes and a `Game` orchestrator):

# SOLID assessment

### S — Single Responsibility: **mostly good (✔︎)**

* **What works:**

  * Domain entities (Player, Orc, Goblin) appear to own their *state* and combat-specific behaviors (`attack`, `speak`).
  * `Game` coordinates flow (menu, battle loop, dice), separate from entity definitions.
* **Smells:**

  * If `Player.attack()` (or monster `attack()`) reaches into `Game.roll_dice`, that’s a cross-module dependency and mixes concerns (entities shouldn’t need to know *where* randomness comes from).
  * Any shared base like `Alive_Entity` doing too much (hp, speed, armor, randomization, and possibly printing) can become a “kitchen-sink” class.

**Suggestion:** pass a `roller` (callable) into combat methods or inject it at construction. Keep printing/logging out of entities (return messages; let `Game` print).

---

### O — Open/Closed: **decent, but can improve (△)**

* **What works:**

  * Adding a new monster by subclassing `Monsters` should work without touching `Game`.
  * Weapon multipliers centralized (e.g., a dict) avoids scattering logic.
* **Smells:**

  * If weapon types & multipliers live in a single dict inside the base class, adding a new weapon still requires editing that class (not fully closed for modification).
  * If `Game` branches on concrete types (e.g., special-case goblin flee) instead of polymorphism, that erodes OCP.

**Suggestion:** model weapons as strategy objects (`Weapon.multiplier()` or `Weapon.damage(base)`) and let each monster choose a weapon instance. For goblin flee, prefer `monster.pre_attack(player, ctx)` hook the `Game` calls—so new behaviors plug in without `Game` edits.

---

### L — Liskov Substitution: **solid (✔︎)**

* **What works:**

  * Orc and Goblin substitute for a Monster in `battle()` without breaking expectations (they share `hp`, `speed`, `armor_rating`, `attack`).
* **Watchouts:**

  * Ensure interface and return types are consistent (e.g., `attack()` always returns a numeric damage; `speak()` returns string vs prints).
  * Special rules (goblin flee) should not change required postconditions (e.g., “an attacker either deals damage or declares an explicit ‘no-attack’ result”).

**Suggestion:** standardize method contracts: `attack(attacker, defender, roller) -> int` and optional `pre_attack(...) -> bool` (continue?).

---

### I — Interface Segregation: **okay for Python, room to tune (△)**

* **What works:**

  * Not forcing classes to implement irrelevant methods (simple class set).
* **Smells:**

  * If a base mixes printing, random generation, and combat in the same surface, consumers must depend on methods they don’t need.

**Suggestion:** split roles conceptually: “talkers” (`speak()`), “combatants” (`attack()`, `armor_rating`, `hp`), and “rollable” behavior (dice). In Python, you can keep it lightweight with mixins or duck-typed protocols (no heavy interface ceremony).

---

### D — Dependency Inversion: **weakest area (✖︎)**

* **What hurts:**

  * Entities calling `Game.roll_dice` hard-wires them to a concrete class.
  * `Game` likely constructs monsters/players directly and owns the RNG—hard to test.

**Suggestion (high impact):**

* Inject a `Dice`/`RNG` dependency (or pass a `roller: Callable[[int], int]`) into `Game` and forward to entities.
* Have `Game` depend on abstractions: factories like `MonsterFactory` and `PlayerFactory` (or callables) so tests can swap implementations easily.
* Keep I/O (print/input) at the edges; return data from core methods.

---

## Quick SOLID score (informal)

* **S:** 8/10
* **O:** 7/10
* **L:** 9/10
* **I:** 7/10
* **D:** 5/10
  **Overall:** **7.2 / 10** → good foundations, with **Dependency Inversion** as the main upgrade path.

---

## Concrete refactors (bite-sized)

1. **Dice strategy**

   ```python
   class Dice:
       def roll(self, sides: int) -> int: return random.randint(1, sides)
   ```

   Pass `dice` into `Game` and `attack()` instead of calling `Game.roll_dice`.

2. **Weapon strategy**

   ```python
   class Weapon: 
       def damage(self, base: int) -> int: return base
   class Knife(Weapon): 
       def damage(self, base): return int(base * 0.5)
   class Sword(Weapon): 
       pass
   class Axe(Weapon): 
       def damage(self, base): return int(base * 1.5)
   ```

   Monsters hold a `weapon: Weapon`. No central multiplier dict needed.

3. **Pre-attack hook**

   ```python
   class Monster(...):
       def pre_attack(self, opponent, dice) -> bool: return True

   class Goblin(Monster):
       def pre_attack(self, opponent, dice) -> bool:
           return not (self.hp < self.max_hp * 0.5 and dice.roll(10) <= 3)  # 30% flee
   ```

   `Game` calls `if not monster.pre_attack(player, dice): ...`—no branching on types.

4. **Factories / injection**

   ```python
   class MonsterFactory:
       def random(self) -> Monster: ...
   game = Game(dice=Dice(), monsters=MonsterFactory())
   ```

   Improves testability and OCP.

---

## TL;DR

* **Strengths:** clear entity boundaries, polymorphic monsters, centralized combat rules → **S/L in good shape**.
* **Main weakness:** **tight coupling to `Game` for dice/random and construction** → invest in **Dependency Inversion** via injected dice/factories; consider weapon strategies and a `pre_attack` hook for special behaviors.
* With those tweaks, you’d move from “good OO” to **textbook SOLID**.
