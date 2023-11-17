```python
import json

def ai_ethics():
    # Load AI ethics guidelines
    with open('ai_ethics_guidelines.json', 'r') as file:
        guidelines = json.load(file)

    # Check if the AI's actions are ethical
    def is_ethical(action):
        for guideline in guidelines:
            if not guideline['condition'](action):
                return False
        return True

    # Function to enforce AI ethics
    def enforce_ethics(ai_actions):
        for action in ai_actions:
            if not is_ethical(action):
                raise Exception(f'Unethical AI action detected: {action}')
        return True

    return enforce_ethics
```