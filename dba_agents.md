
# DBA Agents

| Framework / Tool | Core Concept & Approach | Key Features |
| --- | --- | --- |
| **D-Bot (LLM as DBA)** | **Multi-Agent Collaboration.** Divides tasks between a *Chief DBA* (coordination), *CPU Agent*, *Memory Agent*, and *I/O Agent*. | Tree-of-Thought (ToT) reasoning; continuous knowledge extraction from textual sources. |
| **DBA-Bench** | **Production-Fidelity Benchmark.** A standard dataset used to test agent reliability across 7 operational domains. | Tests agents on live PostgreSQL environments with active, noisy workloads. |
| **AskDB** | **Unified Data & Admin Co-Pilot.** Built to bridge the gap between simple text-to-SQL analytics and hard administrative operations. | Dynamic schema-aware prompting; multi-step task decomposition using Gemini. |
| **Xata Agent / Playbooks** | **Commercial Sandbox Architecture.** Converts traditional Ansible automation and cron schedules into agentic workflows. | Safety-first sandboxing; requires explicit human approval for high-risk actions. |


