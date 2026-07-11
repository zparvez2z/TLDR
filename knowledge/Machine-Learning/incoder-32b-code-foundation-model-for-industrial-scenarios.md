---
source_url: https://arxiv.org/html/2603.16790v3
author: Jian Yang, Wei Zhang, Jiajun Wu, Junhang Cheng, Shawn Guo, Haowen Wang, Weicheng Gu, Yaxin Du, Joseph Li, Fanglin Xu, Yizhi Li, Lin Jing, Yuanbo Wang, Yuhan Gao, Ruihao Gong, Chuan Hao, Ran Tao, Aishan Liu, Tuney Zheng, Ganqu Cui, Zhoujun Li, Mingjie Tang, Chenghua Lin, Wayne Xin Zhao, Xianglong Liu, Ming Zhou, Bryan Dai
date: 11-07-2026
---

# InCoder-32B: Code Foundation Model for Industrial Scenarios

This paper presents InCoder-32B, a 32B-parameter code foundation model designed specifically for industrial engineering domains such as chip design, GPU kernel optimization, embedded systems, compiler optimization, and 3D modeling. The model uses an efficient recurrent architecture and a three-stage Code-Flow training pipeline: pre-training and annealing on curated industrial data, mid-training that expands context from 8K to 128K with synthetic industrial reasoning and agent trajectories, and post-training with execution-grounded verification. The authors reconstruct authentic simulation and execution environments (e.g., Icarus Verilog, Verilator, Yosys; CUDA/Triton; embedded firmware; CAD) to ground data generation and evaluation in real-world criteria. Across 14 general and 9 industrial benchmarks, InCoder-32B is competitive on general programming tasks (e.g., 74.8% SWE-bench Verified, 49.14% LiveCodeBench, 60.99% BFCL) while establishing strong open-source baselines in specialized industrial settings. Ablations show repository transition data, mid-training trajectory data, and multi-turn feedback-conditioned training improve robustness and out-of-distribution performance.
- 32B-parameter code LLM unifying chip design, GPU optimization, embedded systems, compiler optimization, and 3D modeling.
- Three-stage Code-Flow: curated industrial pre-training/annealing, 8K→128K progressive context extension with synthetic reasoning, and execution-grounded post-training verification.
- Industrial data synthesis includes synthetic code QA, agent trajectories, and code artifacts; evaluation grounded in real toolchains (Icarus Verilog, Verilator, Yosys; CUDA/Triton; etc.).
- Results: 74.8% on SWE-bench Verified, 49.14% on LiveCodeBench, 60.99% on BFCL; strongest open-source baselines across 9 industrial benchmarks in 4 domains.
- Key findings: repository transition data > static snapshots for planning; trajectory data and feedback-conditioned multi-turn training enhance robustness under distribution shift.