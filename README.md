# **Logic Puzzle: Fox, Goose, & Grain**

### **The Illusion of Reasoning: LLMs as Pattern Matchers**
A fundamental concept that every AI-assisted developer must understand is that not all LLMs are true reasoning engines. Most do not "understand" logic, physics, or causality in the human sense. At their core, they are highly sophisticated probabilistic models trained to predict the next most likely sequence of tokens (words or code) based on the patterns they have learned from vast datasets of text and code. This is why they excel at tasks for which numerous examples exist in their training data, such as writing a web server or translating between programming languages. Conversely, they often fail at novel problems that require strict, step-by-step logical deduction and state management, as these tasks cannot be solved by pattern matching alone.

To demonstrate this , you will use various models in GitHub Copilot to solve the classic river crossing puzzle:

> A farmer needs to transport a fox, a goose, and a bag of grain across a river using a boat that can only hold the farmer and one other item. The fox cannot be left alone with the goose, and the goose cannot be left alone with the grain. The objective is to find a sequence of moves that successfully transports all three items to the other side.

### Activity:
1. Ensure the VS Code Copilot Agent is set to Ask mode.
2. You will run this simulation two or three times with difference models and compare results. Decide which models you want to test.
3. Select your first Model. Give it the above text and (if needed) prompt it to write a program to solve this puzzle in the language of your choice. 
4. Read through the proposed code. What works? What is lacking? What could be better? 
5. Try again with another Model and review in the same manner.
