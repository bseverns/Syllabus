# AI Systems Flow Reference

This is the course's plain-language map of how AI systems usually work in practice.

There is no single fully canonical diagram for all AI. This version intentionally combines three durable reference threads:
- Microsoft Learn fundamentals language
- the OECD idea of an AI system and lifecycle
- the NIST AI RMF view that risk has to be managed across design, use, and evaluation

## The shortest honest model

Most AI-supported work can be understood as:

`task -> data/context -> model/tool -> output -> verification -> action -> monitoring`

If a student can explain those seven parts clearly, they are usually on solid ground.

## Stage-by-stage

| Stage | What is happening | Common failure | Student question |
| --- | --- | --- | --- |
| Task | A person or organization defines the job to be done. | The goal is vague, unrealistic, or unsafe. | What problem am I actually trying to solve? |
| Data / context | The system receives source material, retrieved facts, instructions, examples, or user input. | Missing context, bad data, stale information, or private data is included. | What information is this system using, and should it be using it? |
| Model / tool | A model or software system processes the input. This might be search, classification, prediction, generation, or automation. | The wrong tool is chosen for the job. | Is this a search task, a rules task, a prediction task, or a generation task? |
| Output | The system returns text, labels, scores, summaries, recommendations, or actions. | The output looks polished but is incomplete, biased, or wrong. | What exactly did the system produce? |
| Verification | A human checks the output against sources, audience, safety, tone, and accuracy. | People skip checking because the result sounds confident. | What do I need to confirm before this is used? |
| Action | Someone decides whether to send, save, publish, escalate, or reject the result. | No clear human owner exists. | Who is responsible for the final use of this output? |
| Monitoring | People notice what happened next and adjust the workflow, prompt, source set, or policy. | Mistakes repeat because nothing was documented or improved. | What should change next time? |

## Different systems, different logic

Not every digital tool is doing the same kind of work.

- `Traditional software`: follows explicit rules written by people. Same inputs usually produce the same outputs.
- `Search / retrieval`: finds documents or passages that already exist and ranks them.
- `Machine learning prediction`: detects patterns in data and predicts labels, scores, or likely outcomes.
- `Generative AI`: predicts likely next tokens or content patterns to produce new text, images, audio, or code.
- `Automation / orchestration`: connects tools and steps so that one output triggers another action.

## Where failure enters the system

Students should not only ask whether the model is "good." They should ask where the breakdown happened.

- The task may be framed badly.
- The source data may be weak, biased, missing, or private.
- The wrong tool may be used for the job.
- The prompt or instructions may be underspecified.
- The output may be fluent but false.
- The human check may be rushed or skipped.
- The organization may have unclear rules about privacy, authority, or escalation.

## A practical workplace rule

When the stakes are real, do not ask only:
- What did the AI say?

Also ask:
- What was the task?
- What data or source material shaped the result?
- What kind of system produced it?
- What did I verify?
- Who approves final use?
- What should be documented for next time?

## Use this reference in the course

- `Session 03`: compare software, search, automation, and generative tools
- `Session 09`: explain machine learning without mysticism
- `Session 12`: locate privacy, bias, and escalation points
- `Capstone`: describe one full workflow from task to checked result

## Reference anchors

- Microsoft Learn, "Introduction to AI concepts": https://learn.microsoft.com/en-us/training/modules/fundamentals-azure-ai-services/
- Microsoft Learn, "Explore internet search and beyond": https://learn.microsoft.com/en-us/training/modules/explore-internet-search-beyond/
- Microsoft Learn, "Introduction to large language models": https://learn.microsoft.com/en-us/training/modules/introduction-large-language-models/
- OECD AI Principles overview: https://oecd.ai/en/ai-principles/
- NIST AI RMF 1.0: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10
