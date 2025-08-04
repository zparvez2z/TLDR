---
source_url: https://refactoring.guru/refactoring/how-to
author: Unknown
date: 04-08-2025
---

# How to Refactor

Refactoring should be done as a series of small, incremental changes, each making the existing code slightly better while leaving the program in a working state. It is crucial not to introduce new functionality during the refactoring process and to ensure that all existing tests pass upon completion. If tests fail, it's either due to an error in refactoring or because the tests themselves were too low-level and need to be refactored.

- **Incremental Changes:** Refactor in small steps to maintain a working program at all times.
- **No New Features:** Do not mix refactoring with the development of new functionality; keep these processes separate.
- **Passing Tests:** All existing tests must pass after refactoring is complete.
- **Code Improvement:** The primary goal is to make the code cleaner and more efficient.