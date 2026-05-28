# Gemini Assistant

AMPLbot is a specialized custom Gem designed to act as your expert consultant for Mathematical Optimization and the AMPL modeling ecosystem directly within Google Gemini. 

Engineered with advanced domain expertise, this Gem assists operations research analysts, developers, and engineers in formulating, implementing, and debugging optimization models with high precision and technical rigor.

Try it here: [AMPLbot on Gemini](https://gemini.google.com/gem/1u6aK9nY_4HUERmBtPSH58WJiFQfR7uLa?usp=sharing).

## Key Capabilities

Use AMPLbot to enhance and accelerate your mathematical programming workflows:

- **Python-First Integration:** Develop production-ready optimization apps by prioritizing `amplpy` implementation for all model workflows.
- **Formulation & Translation:** Convert complex natural-language business descriptions and mathematical formulations into clean, executable code.
- **Rigorous Debugging:** Diagnose infeasible or unbounded models, resolve script syntax issues, and optimize solver configurations for performance.
- **Style & Best Practices:** Refine model architecture following official style guidelines to ensure scalability, readability, and efficient presolve operations.
- **Grounded Optimization Theory:** Gain deep insights into underlying mathematical concepts (linear programming, integer programming, network flows, etc.) aligned with the core literature.

## Why Use This Gem Over General LLMs?

Unlike standard language models, AMPLbot operates under strict domain-specific constraints and architectural principles:

- **Source Grounding:** Prioritizes technical guidance explicitly derived from the AMPL Book, reference manuals, official FAQs, `amplpy` documentation, among other sources.
- **Verifiable References:** Relates answers back to specific chapters and subsections of the authoritative AMPL literature when providing structural solutions.
- **Strict Compliance Reporting:** Explicitly flags when an inquiry falls outside the scope of official documentation, ensuring transparency before offering broader AI insights.
- **Algorithmic Precision:** Enforces professional operations research standards, using concise technical language and verifying optimization parameters prior to model implementation.

## Typical Prompts

- *"Help me formulate a multi-period capacity planning model using amplpy from this description."*
- *"I am encountering an evaluation error in my constraint. How should I debug this based on the style guide?"*
- *"Can you explain the mathematical difference between these two formulations and implement the more efficient one in Python?"*
- *"Which chapter of the AMPL Book covers piecewise-linear objectives, and how do I declare them via amplpy?"*

## Operational Notes

- **Code Validation:** AMPLbot excels at generating, optimizing, and explaining code structures but does not execute optimization scripts or interact with live solvers. Always run and validate the code within your own local or cloud environment.
- **Clarification Loop:** To maintain extreme precision, the Gem may ask clarifying questions regarding your objective functions, constraint sets, or data layouts before proposing a definitive formulation.
