---
source_url: https://www.anthropic.com/research/tracing-thoughts-language-model
author: Sam Ringer, Nelson Elhage, Kamal Ndousse, Catherine Olsson, Nicholas Schiefer, Tristan Hume, Chris Olah, Zac Kenton, Nicholas Turner, Tom Henighan, and collaborators
date: 21-05-2024
---

# Tracing the “Thoughts” of a Language Model

Anthropic researchers have developed a new technique to trace how concepts evolve inside a language model as it processes information. By combining dictionary learning (which finds interpretable features) with causal tracing (which measures their impact), they can follow a concept like 'the Golden Gate Bridge' through the model's layers. This method reveals how the model activates, edits, and combines these features to construct its final output. The approach provides a more granular understanding of the model's internal reasoning, including how it corrects itself and represents abstract ideas.

- **Combined Methodology:** The technique integrates dictionary learning to identify interpretable features with causal tracing to measure their impact on the model's output.
- **Concept Tracking:** It allows researchers to follow specific concepts, such as 'the Golden Gate Bridge', through the model's layers to see how they are activated, modified, or suppressed.
- **Reveals Self-Correction:** The research demonstrates how models can self-correct by suppressing an initial incorrect association when more specific context is provided later in a prompt.
- **Scalable Interpretability:** This approach offers a scalable method for understanding the internal mechanisms of large language models, moving beyond analyzing individual neurons.
- **Hierarchical Representation:** It shows how models build abstract concepts from simpler, more concrete features that are activated in earlier layers.