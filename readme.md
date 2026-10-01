# 🌐 Defeat the Evil Wizard

A turn-based Python battle game built with Object-Oriented Programming. Choose your hero class, customize your strategy, and defeat the Dark Wizard through combat, special abilities, and tactical healing.

## 🎮 How to Play

1. Run `python main.py` (or whatever you name the file)
2. Select a character class: Warrior, Mage, Archer, or Paladin
3. Enter your hero's name
4. Battle the Evil Wizard using the turn-based menu:
   - **1** — Attack with randomized damage
   - **2** — Use a special ability (unique to your class)
   - **3** — Heal (restores up to 15 HP, capped at max health)
   - **4** — View current stats (does not consume a turn)

The Evil Wizard regenerates 5 HP each round and attacks after every player action. Reduce their health to zero to win.

## ⚔️ Character Classes

| Class       | HP  | Base ATK | Special Abilities                                                                                                        |
| ----------- | --- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Warrior** | 140 | 25       | Two-Hand Strike (bonus damage), Berserker Rage (self-damage for massive attack)                                          |
| **Mage**    | 100 | 35       | Overcast (life-force spell, huge damage), Enfeeblement (permanently reduces wizard ATK)                                  |
| **Archer**  | 125 | 25       | Shoot & Scoot (reduced ATK damage + chance to evade wizardt attack), Quick Shot (double attack with accuracy check)      |
| **Paladin** | 150 | 20       | Divine Shield (blocks wizard's attack + conditional heal/damage based on favor), Holy Strike (costs HP for bonus damage) |

## 🛠️ Technical Details

- **Language:** Python 3
- **Paradigm:** Object-Oriented Programming with inheritance and polymorphism
- **Key Concepts Used:**
  - Base `Character` class with shared methods (`attack`, `heal_mechanic`, `display_stats`)
  - Child classes override `special_ability()` with unique logic
  - Turn-based game loop with input validation
  - Randomized damage scaling per attack
  - State tracking for evasion, shields, and debuffs

## 📦 Dependencies

None. Uses only Python standard library modules: `os`, `subprocess`, `random`.

## 📝 Notes

- Health values may display as decimals due to randomized damage scaling
- Special abilities use class-specific mechanics (probability checks, temporary stat changes, debuffs)
- Viewing stats does not trigger the wizard's turn
- If character already at full health and try to heal will receive an error message. Wizard will not perform any actions.
