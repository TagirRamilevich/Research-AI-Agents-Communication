# Communication of AI Agents

This repository contains the code and data for the research project "Communication of AI Agents". The project investigates the communication strategies of AI agents using Reinforcement Learning in the multi-armed bandit problem.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Experiments](#experiments)
- [Results](#results)
- [Research Results](#research-results)
- [Contributing](#contributing)
- [License](#license)
- [References](#references)
- [Contacts](#contacts)

## Introduction

This research focuses on analyzing the communication strategies of AI agents in a multi-agent system using large language models like GPT-4. The core problem tackled is the multi-armed bandit, where agents must choose between different options to maximize their rewards. The project explores several scenarios, including communication between agents, deception, and the cost of communication.

## Project Structure

- `Code/`: Contains all the source code used in the experiments.
- `Data/`: Includes the datasets generated from the experiments.

## Usage
To run the experiments, use the provided scripts in the `Code/` directory.  

## Experiments

The experiments are designed to evaluate different communication strategies among AI agents. Each experiment is run for a fixed number of rounds, and the results are recorded for analysis. The primary modes include:  

* No Communication: Agents act independently without any interaction.  
* Communication: Agents can freely communicate to share information and strategies.  
* Deception: Includes scenarios where the agent might receive false information.  
* Paid Questions: Agents must pay a cost for each question they ask, simulating the real-world cost of communication.   

## Results

The results of the experiments are stored in the `Results/` directory. They include data on total rewards, regret, average rewards, and the probability of selecting the optimal option. Detailed analysis can be found in the Jupyter notebooks within the `Notebooks/` directory.  

## Research Results

The agents were tested under various conditions to observe the effects of communication strategies and the introduction of deceptive elements in communication. The key findings include:  

* Impact of direct and restricted communication on agent learning and decision-making.  
* Consequences of deceptive communication and its impact on agent behavior.  
* The role of communication cost in strategy formulation and execution.  

Detailed results and data visualizations are available in the paper.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue. To contribute code, fork the repository and submit a pull request.  

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/TagirRamilevich/research-ai-agents-communication/blob/main/LICENSE) file for details.  

## References  

* Agrawal, R. (1995). Sample mean based index policies with O(log n) regret for the multi-armed bandit problem. Advances in Applied Probability, 27, 1054-1078.  
* Auer, P., Cesa-Bianchi, N., & Fischer, P. (2002). Finite-time Analysis of the Multiarmed Bandit Problem. Machine Learning, 47, 235-256.  
* Gorodetski, V. I. (2012). Self-organization and multiagent systems: I. Models of multiagent self-organization. Izvestiya Rossiiskoi Akademii Nauk. Teoriya i Sistemy Upravleniya, 2, 92-120.  
* Littman, M. L. (1994). Markov games as a framework for multi-agent reinforcement learning. Proceedings of the Eleventh International Conference on Machine Learning, 157-163.  
* Zhuge, M., et al. (2023). Mindstorms in Natural Language-Based Societies of Mind. arXiv.

For more information, please visit the [project repository](https://github.com/TagirRamilevich/research-ai-agents-communication/).

## Contacts  

* Telegram: [@travelwithtagir](https://t.me/travelwithtagir/)  
* Data Blog: [@tagir_analyzes](https://t.me/tagir_analyzes/)  
* LinkedIn: [Tagir Khairutdinov](https://linkedin.com/in/tagir-data-analyst/)  

