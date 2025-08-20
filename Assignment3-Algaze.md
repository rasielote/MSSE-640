##  Configuration
How do you set your Git name and email? Should it be global or just in one repo? Why?  
If you want Git to use your name and email for every repo on your computer, use global. But if you're working on a project for someone else, you can change it just in that repo (local).
### Set your Git username and email globally:
```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### Set them locally for a specific repo:
```
git config user.name "Other Name"
git config user.email "other@example.com"
```

### Set the core editor (example: VS Code):
```
git config --global core.editor "code --wait"
```

### View your config settings:
```
git config --global --list
git config --local --list
```

---

##  Working with a Local Repo

### Create a new local repository:
```
mkdir my-repo
cd my-repo
git init
```

### Clone an existing repository:
```
git clone https://github.com/user/repo.git
```

### Check the status of your repo:
```
git status
```

### Stage changes:
```
git add file.txt     # Stages one file
git add .            # Stages everything
```

### Commit changes:
```
git commit -m "Your message here"
```

### Example `.gitignore` file:
```
# .gitignore
*.log
node_modules/
.env
```

### Delete a file with Git:
```
git rm filename.txt
git commit -m "Remove file"
```

---

##  Working with a Remote

### View the remote repo:
```
git remote -v
```

### Fetch updates from the remote:
```
git fetch
```

### Pull updates and merge them:
```
git pull
```

### Push local changes to the remote:
```
git add .
git commit -m "Update something"
git push origin main
```

---

## Branches

### View local and remote branches:
```
git branch      # Local
git branch -r   # Remote
git branch -a   # All
```

### Create a new branch:
```
git branch new-feature
```

### Switch to a different branch:
```
git switch new-feature
# or
git checkout new-feature
```

### Delete a local branch:
```
git branch -d new-feature
git branch   # To confirm it's gone

```
##
# Advanced Exercises
## Examples of “Simple” Questions That Trip Up LLMs
### Basic Arithmetic Beyond Small Numbers 
Example: “What is 17,438 × 56?” LLMs often provide a confident but incorrect answer since they are not calculators.

### Common sense Temporal Reasoning 
Example:  “If I put my ice cream in the oven and turn it on, what happens?” Models sometimes misinterpret simple physical cause-and-effect.

### Trick Questions with Ambiguity 
Example:  “How many eyes does the sun have?” Instead of recognizing it as nonsense, some LLMs attempt to provide literal answers.

## Why These Problems Are Hard for LLMs
These problems are difficult for LLMs because their design is fundamentally probabilistic rather than deterministic. A model like GPT is optimized to predict the most likely sequence of words given a context, not to perform calculations or strict logical inference. Arithmetic, spatial transformations, and causal reasoning require rule-based systems, whereas LLMs rely on statistical associations learned from text. Furthermore, LLMs lack grounding in physical reality. Humans learn about heat melting ice cream or how shapes rotate through direct sensory and embodied experience, but LLMs can only infer such knowledge from patterns in training data. This leads to brittleness in cases that require common sense, multi-step reasoning, or the ability to filter nonsense.

## What This Tells Us About LLM Capacities
These limitations highlight both the strengths and weaknesses of current large language models. Today, LLMs are excellent at producing fluent, human-like language that is contextually appropriate, but they remain unreliable when correctness is required in domains such as mathematics, law, or science. Their value lies in amplifying knowledge and providing generative creativity rather than serving as factually precise or logically consistent systems. Looking ahead, hybrid approaches that combine LLMs with external tools like calculators, databases, or reasoning engines may help overcome these shortcomings. Research into multimodal grounding—linking language models to vision, robotics, and real-world sensor data—also holds promise, as it would provide models with experiential anchors beyond text. This suggests that while today’s LLMs are not yet capable of human-like reasoning, their future capacity may expand significantly through tool integration and grounded AI development.

## References
- Marcus, G., & Davis, E. (2020). *Rebooting AI: Building Artificial Intelligence We Can Trust*. Vintage.
- Bender, E. M., & Koller, A. (2020). Climbing towards NLU: On meaning, form, and understanding in the age of data. ACL Anthology. [https://doi.org/10.18653/v1/2020.acl-main.463](https://doi.org/10.18653/v1/2020.acl-main.463)
- OpenAI. (2023). GPT-4 Technical Report. *arXiv preprint* arXiv:2303.08774.
- Mitchell, M. (2023). Why AI is Harder Than We Think. *AI Magazine*,