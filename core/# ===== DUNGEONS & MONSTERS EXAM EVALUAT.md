# ===== DUNGEONS & MONSTERS EXAM EVALUATION =====

Repository: [https://github.com/yishay-tested/RPG-OOP-SOLID_test.git](https://github.com/yishay-tested/RPG-OOP-SOLID_test.git)

## 1. File Structure

✅ All required files found: `core/player.py`, `core/orc.py`, `core/goblin.py`, `game.py`, `main.py`, `readme.md`. ([GitHub][1])

## 2. Detailed Class & Module Review

### Player (`core/player.py`)

* **Attributes**

  * `name`: yes.
  * `hp = 50` (+10 if healer): base `max_hp=50`, `hp=50` in `Alive_Entity`; healer path adds `self.hp += 10`. ✔️ ([GitHub][2])
  * `speed = random(5–10)`: ✔️ in base. ([GitHub][2])
  * `power = random(5–10)` +2 if warrior: ✔️ base + conditional `self.power += 2` for `'Warrior'`. ([GitHub][2])
  * `armor_rating = random(5–15)`: ✔️ base. ([GitHub][2])
  * `profession` is random `"Warrior"/"Healer"` and used consistently: ✔️. ([GitHub][2])
* **Methods**

  * `speak()`: implemented (prints `"I am <name>."`). (Spec asks to print name **and type**; not deducted per matrix.) ([GitHub][2])
  * `attack()`: implemented in base `Alive_Entity`, rolls a d6 using `Game.roll_dice` and returns `power + roll`. Logic works, though it oddly calls `Game.roll_dice(self, 6)` (tight coupling). ✔️ ([GitHub][2])

**Verdict**: Meets all graded Player requirements.

---

### Orc (`core/orc.py`)

* **Attributes**

  * `name`: `"Bob"`. ✔️ ([GitHub][3])
  * `hp = 50`: inherited from base (50). ✔️ ([GitHub][2])
  * `type = "Orc"`: ✔️ (capitalization acceptable if consistent). ([GitHub][3])
  * `speed = random(0–5)`: ✔️ uses `rand.randint(0,5)`. ([GitHub][3])
  * `power = random(10–15)`: **❌ Not set in Orc**; inherits 5–10 from `Alive_Entity`. (Spec requires 10–15.) ([GitHub][3])
  * `armor_rating = random(2–8)`: ✔️. ([GitHub][3])
  * `weapon`: provided via `Monsters` base as random `'Sword'/'Knife'/'Axe'`. ✔️ ([GitHub][2])
* **Methods**

  * `speak()`: ✔️ prints type & name. ([GitHub][3])
  * `attack()`: uses `Monsters.attack()` which applies weapon multipliers (0.5/1/1.5). ✔️ ([GitHub][2])

**Verdict**: Only deviation is **power range**.

---

### Goblin (`core/goblin.py`)

* **Attributes**

  * `name`: `"Gob"`. ✔️
  * `hp = 20`: ✔️ sets `max_hp=20`, `hp=20`. ([GitHub][4])
  * `type = "Goblin"`: ✔️. ([GitHub][4])
  * `speed = random(5–10)`: inherited (5–10), matches spec. ✔️ ([GitHub][2])
  * `power = random(5–10)`: inherited (5–10), matches spec. ✔️ ([GitHub][2])
  * `armor_rating = 1`: ✔️. ([GitHub][4])
  * `weapon`: via base `Monsters`. ✔️ ([GitHub][2])
* **Methods**

  * `speak()`: inherited `Monsters.speak()` (prints type & name). ✔️ ([GitHub][2])
  * `attack()`: inherited `Monsters.attack()` (includes weapon multiplier; spec calls for “standard combat” for goblin, but the matrix does not penalize this). ✔️
  * `run_away()`: **Bonus**: implemented with 30% check (returns string; not integrated into battle). ✅ bonus. ([GitHub][4])

**Verdict**: Meets graded requirements; includes bonus stub.

---

### Game (`game.py`)

* **Methods present**: `start()`, `show_menu()`, `choose_random_monster()`, `battle(...)`, `roll_dice(sides)`: ✔️ all present. ([GitHub][5])
* **Combat Logic**

  * **Initiative**: each side `d6 + speed`; if equal, player starts (tie falls to `else:` branch setting player). ✔️ ([GitHub][5])
  * **Hit check**: `d20 + speed > target.armor_rating`. ✔️ ([GitHub][5])
  * **Damage**: uses `attacker.attack()` → `d6 + power`; monsters get weapon multiplier via class logic. ✔️ ([GitHub][2])
  * **HP & death**: subtracts damage; checks `hp <= 0` and ends. ✔️ ([GitHub][5])
  * **Goblin flee**: **Not integrated** (bonus, no deduction).

**Verdict**: Combat flow matches spec.

---

## 3. Implementation Scores (70 pts)

* Files: 10/10
* Player: 20/20
* Orc: **13/15** (power not in 10–15 range). ([GitHub][3])
* Goblin: 15/15
* Game: 20/20
  **Subtotal**: **68/70**

## 4. Clean Code (30 pts)

* **Structure** (folders, separation): 5/5
* **Naming** (classes/methods consistent): 5/5
* **Readability** (logic clarity): 4/5 — heavy one-liners and prints inline make it a bit dense. ([GitHub][2])
* **Reusability** (helpers/OOP): 4/5 — good base classes, but `Player.attack()` depends on `Game.roll_dice` statically (tight coupling). ([GitHub][2])
* **Randomness** (uses `random` properly): 5/5
* **Inheritance/Design**: 5/5 — `Alive_Entity` / `Monsters` reuse is solid. ([GitHub][2])
  **Subtotal**: **28/30**

## 5. Bonus Features

* ✅ `Goblin.run_away()` stub with 30% probability (not wired into battle). ([GitHub][4])

---

**FINAL SCORE: 96 / 100**

### Strengths

1. Solid OOP layering (`Alive_Entity` → `Player`/`Monsters`) with reusable attack logic including weapon multipliers. ([GitHub][2])
2. Combat flow implements initiative, hit, damage, and death cleanly. ([GitHub][5])
3. Profession system correctly adjusts stats (healer HP bonus, warrior power bonus). ([GitHub][2])

### Weaknesses

1. Orc `power` not set to 10–15 as required (inherits 5–10). ([GitHub][3])
2. `Player.attack()` depends on `Game.roll_dice` via class call — unnecessary coupling. ([GitHub][2])
3. `speak()` for Player doesn’t include type as spec suggests (not graded, but worth noting). ([GitHub][2])

---

### Summary

All required files and core mechanics are present. The game loop, initiative, hit, and damage rules largely match the specification. Only notable spec gap is the **Orc power range**; otherwise, implementation and design are strong.

---

# ===== DUNGEONS & MONSTERS EXAM EVALUATION =====

Repository: [https://github.com/yishain11/rpg-test](https://github.com/yishain11/rpg-test)

## 1. File Structure

✅ All required files found: `core/player.py`, `core/orc.py`, `core/goblin.py`, `game.py`, `main.py`, `readme.md`. (Repository also includes helpful bases: `core/creature.py`, `core/monster.py`.) ([GitHub][6])

## 2. Detailed Class & Module Review

### Player (`core/player.py`)

* **Attributes**

  * `name`: yes (via base `Creature`). ✔️ ([GitHub][7])
  * `hp = 50` (+10 if healer): ✔️ initializes to 50; adds +10 for healer else +2 power. ([GitHub][7])
  * `speed = random(5–10)`: ✔️. ([GitHub][7])
  * `power = random(5–10)` +2 if warrior: ✔️ (`"fighter"` synonym used consistently). ([GitHub][7])
  * `armor_rating = random(5–15)`: ✔️. ([GitHub][7])
  * `profession`: random choice `"healer"/"fighter"`. ✔️ consistency maintained. ([GitHub][7])
* **Methods**

  * `speak()`: ✔️ prints identity. ([GitHub][7])
  * `attack()`: provided via base `Creature.attack(...)`; for players no weapon modifier is applied (only monsters have `type`). ✔️ ([GitHub][8])

**Verdict**: Fully meets graded Player requirements.

---

### Orc (`core/orc.py`)

* **Attributes**

  * `name`: set via constructor. ✔️ ([GitHub][9])
  * `hp = 50`: ✔️. ([GitHub][9])
  * `type = "orc"`: ✔️. ([GitHub][9])
  * `speed = random(0–5)`: **❌ Implemented as `ri(5,10)` (too fast).** ([GitHub][9])
  * `power = random(10–15)`: ✔️. ([GitHub][9])
  * `armor_rating = random(2–8)`: ✔️. ([GitHub][9])
  * `weapon`: random via `Monster`. ✔️ ([GitHub][10])
* **Methods**

  * `speak()`: ✔️ (in `Monster`). ([GitHub][10])
  * `attack()`: ✔️ weapon multiplier handled by `Creature.attack()` + `Monster.modify_damage()`. ([GitHub][10])

**Verdict**: Only deviation is **speed range**.

---

### Goblin (`core/goblin.py`)

* **Attributes**

  * `name`: set via constructor. ✔️ ([GitHub][11])
  * `hp = 20`: ✔️. ([GitHub][11])
  * `type = "goblin"`: ✔️ via `Monster.__init__`. ([GitHub][11])
  * `speed = random(5–10)`: ✔️. ([GitHub][11])
  * `power = random(5–10)`: ✔️. ([GitHub][11])
  * `armor_rating = 1`: ✔️. ([GitHub][11])
  * `weapon` random: ✔️. ([GitHub][11])
* **Methods**

  * `speak()`: ✔️ (from `Monster`). ([GitHub][10])
  * `attack()`: ✔️ (from `Creature.attack()`; currently applies weapon multiplier since goblin is a monster).
  * `run_away()`: present but `pass` (bonus; no deduction). ([GitHub][11])

**Verdict**: Meets graded requirements; bonus stub present.

---

### Game (`game.py`)

* **Methods present**: `start()`, `show_menu()`, `choose_random_monster()`, `battle(...)`, `roll_dice(sides)`: ✔️. ([GitHub][12])
* **Combat Logic**

  * **Initiative**: `d6 + speed`; tie → player starts. ✔️ ([GitHub][12])
  * **Hit**: `d20 + speed > armor_rating`. ✔️ ([GitHub][12])
  * **Damage**: `d6 + power`; **monster** damage multiplied by weapon factor (via base logic). ✔️ ([GitHub][8])
  * **HP & death**: handled via `reduce_health` and termination flags. ✔️ ([GitHub][8])
  * **Goblin flee**: not implemented (bonus).

**Verdict**: Matches spec cleanly.

---

## 3. Implementation Scores (70 pts)

* Files: 10/10
* Player: 20/20
* Orc: **13/15** (speed not in 0–5). ([GitHub][9])
* Goblin: 15/15
* Game: 20/20
  **Subtotal**: **68/70**

## 4. Clean Code (30 pts)

* **Structure**: 5/5 — neat `core/` with `creature.py` & `monster.py`. ([GitHub][6])
* **Naming**: 5/5 — consistent (“fighter” used everywhere). ([GitHub][7])
* **Readability**: 4/5 — battle state machine (returning `(True, True)` vs swapping) is a bit quirky but understandable. ([GitHub][12])
* **Reusability**: 5/5 — good extraction of shared logic. ([GitHub][8])
* **Randomness**: 5/5 — proper `randint`/`choice` usage with correct ranges (except Orc speed, graded above). ([GitHub][7])
* **Inheritance/Design**: 5/5 — clear `Creature`/`Monster` base classes; clean separation of concerns. ([GitHub][8])
  **Subtotal**: **29/30**

## 5. Bonus Features

* ✅ `run_away()` stub present on Goblin (not wired). ([GitHub][11])

---

**FINAL SCORE: 97 / 100**

### Strengths

1. Strong OOP design with reusable `Creature.attack()` and `Monster.modify_damage()` for weapon multipliers. ([GitHub][8])
2. Combat loop and initiative/hit/damage pipeline align well with spec. ([GitHub][12])
3. Clean separation of player vs monster behaviors via presence/absence of `type`. ([GitHub][8])

### Weaknesses

1. Orc `speed` range incorrect (5–10 instead of 0–5). ([GitHub][9])
2. Battle loop API (`(True, True)` sentinel) is non-idiomatic and may confuse maintainers. ([GitHub][12])
3. `readme.md` is empty (minor). ([GitHub][13])

---

### Summary

This repository closely matches the required spec with a neat, extensible OOP design. Aside from the **Orc speed range** and a slightly quirky battle loop, implementation quality and code structure are excellent.

[1]: https://github.com/yishay-tested/RPG-OOP-SOLID_test "GitHub - yishay-tested/RPG-OOP-SOLID_test"
[2]: https://github.com/yishay-tested/RPG-OOP-SOLID_test/raw/main/core/player.py "raw.githubusercontent.com"
[3]: https://github.com/yishay-tested/RPG-OOP-SOLID_test/raw/main/core/orc.py "raw.githubusercontent.com"
[4]: https://github.com/yishay-tested/RPG-OOP-SOLID_test/raw/main/core/goblin.py "raw.githubusercontent.com"
[5]: https://github.com/yishay-tested/RPG-OOP-SOLID_test/raw/main/game.py "raw.githubusercontent.com"
[6]: https://github.com/yishain11/rpg-test "GitHub - yishain11/rpg-test"
[7]: https://github.com/yishain11/rpg-test/raw/main/core/player.py "raw.githubusercontent.com"
[8]: https://github.com/yishain11/rpg-test/raw/main/core/creature.py "raw.githubusercontent.com"
[9]: https://github.com/yishain11/rpg-test/raw/main/core/orc.py "raw.githubusercontent.com"
[10]: https://github.com/yishain11/rpg-test/raw/main/core/monster.py "raw.githubusercontent.com"
[11]: https://github.com/yishain11/rpg-test/raw/main/core/goblin.py "raw.githubusercontent.com"
[12]: https://github.com/yishain11/rpg-test/raw/main/game.py "raw.githubusercontent.com"
[13]: https://github.com/yishain11/rpg-test/raw/main/readme.md "raw.githubusercontent.com"
