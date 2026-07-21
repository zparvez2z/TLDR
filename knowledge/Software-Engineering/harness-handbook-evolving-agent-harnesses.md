---
source_url: https://arxiv.org/html/2607.13285v1
author: Ruhan Wang, Yucheng Shi, Zongxia Li, Zhongzhi Li, Yue Yu, Junyao Yang, Kishan Panaganti, Haitao Mi, Dongruo Zhou, Leoweiliang
date: 21-07-2026
---

# Harness Handbook: Making Evolving Agent Harnesses Readable, Navigable, and Editable

This paper tackles the bottleneck of behavior localization in evolving AI agent harnesses—the task of identifying all code locations that implement a requested behavioral change. It introduces the Harness Handbook, an automatically synthesized, behavior-centric representation that links high-level behaviors to their concrete implementations via static analysis and LLM-assisted structuring. The authors also propose Behavior-Guided Progressive Disclosure (BGPD) to guide coding agents from behavioral requests to verified code locations, plan and execute edits, and keep the handbook synchronized with repository changes. Evaluations on diverse modification requests across two open-source harnesses show improved behavior localization and edit-plan quality at lower token cost, with weaker planners sometimes matching stronger models due to better guidance. Gains are most pronounced for scattered implementation sites, rarely executed paths, and cross-module interactions, underscoring the importance of explicit behavior-to-implementation mapping.
- Defines behavior localization as systematically finding all code locations tied to a requested behavior.
- Harness Handbook organizes implementation knowledge by behaviors (not files), linking to functions, files, stages, and state transitions.
- Automated construction pipeline: static fact extraction; behavioral organization (function-as-leaf or file-as-leaf); hierarchical synthesis and packaging; state-register view.
- BGPD workflow: stage and entry selection, call-relation expansion, source verification, edit planning and execution, and handbook resynchronization.
- Evaluation metrics: plan quality, localization accuracy, and planning cost; results show better plans at lower token cost and consistent gains across request difficulty.
- Practical benefits: accelerates navigation of large, distributed harnesses; mitigates long-context limits; improves precision on scattered or rarely executed code paths.
- Includes prompt templates and LLM judging protocols supporting handbook generation, localization, and planning.