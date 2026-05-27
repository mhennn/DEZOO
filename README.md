# DEMAL
Turn boring print() debugging into something fun — hear animals instead of reading logs.

DEMAL is a lightweight Python package that replaces traditional debugging prints with animal sounds. Instead of staring at logs, you’ll hear your program speak through playful audio cues.

### 🎯 Why DEMAL?

Debugging can get repetitive and dull. DEMAL makes it:
- 🎧 Auditory instead of visual
- 🐶 Fun and memorable
- ⚡ Fast to integrate
- 🧠 Easier to recognize debug states

### 🚀 Features
- Replace print() debugging with animal sounds
- Multiple animals for different debug levels
- Simple API with zero configuration
- Works in any Python script
- Optional fallback to normal logs

#### Installation
```bash
pip install demal
```

#### Testing the package
```bash
from demal_package import DemalSystem

demal_system = DemalSystem()
demal_system.debug_birds()
```