# Overview

This is a self-learning Flappy Bird game implementation using Python, Pygame, and the NEAT (NeuroEvolution of Augmenting Topologies) machine learning library. The project demonstrates neuroevolution where AI agents learn to play Flappy Bird through genetic algorithms and neural networks. The implementation includes both a standard playable version and an AI-trained version that evolves over generations to improve gameplay performance.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Game Engine Architecture

**Problem**: Need a visual game environment for both human players and AI agents to interact with.

**Solution**: Pygame-based game loop architecture with object-oriented design.

The core game components are implemented as classes:
- **Bird class**: Handles bird physics (gravity, rotation, animation), movement, and collision detection
- **Pipe class** (implied): Manages obstacle generation and scrolling
- **Base class** (implied): Handles ground/floor scrolling animation

**Design Pattern**: The implementation uses a standard game loop pattern with:
- Event handling
- Game state updates
- Rendering/drawing
- Frame rate control

**Pros**: 
- Clear separation of concerns
- Easy to extend and modify game mechanics
- Works well with both manual and AI control

**Cons**:
- Pygame has performance limitations for very complex simulations
- Single-threaded architecture may limit parallel evolution

## AI Training Architecture

**Problem**: Need to evolve neural networks that can learn to play Flappy Bird without manual programming of game strategies.

**Solution**: NEAT (NeuroEvolution of Augmenting Topologies) algorithm for evolving neural network topologies and weights.

**Key Architectural Decisions**:

1. **Neural Network Input Layer** (3 inputs):
   - Bird's vertical position
   - Distance to next pipe
   - Gap position information

2. **Neural Network Output Layer** (1 output):
   - Jump/don't jump decision

3. **Fitness Function**: Based on distance traveled and survival time
   - Fitness threshold: 1000
   - Population size: 100 birds per generation
   - Criterion: Maximize fitness

4. **Evolution Parameters**:
   - Mutation rates for connections (50% add/delete probability)
   - Node mutations (20% add/delete probability)
   - No hidden layers initially (NEAT adds them through evolution)
   - Tanh activation function

**Alternatives Considered**: 
- Deep Q-Learning (DQN) would require more computational resources
- Genetic algorithms without topology evolution would be less adaptive

**Pros**:
- NEAT automatically evolves both network structure and weights
- No need to predetermine network architecture
- Fast convergence for simple games like Flappy Bird

**Cons**:
- Can get stuck in local optima
- Requires tuning of many hyperparameters

## Model Persistence

**Problem**: Need to save trained AI agents for reuse without retraining.

**Solution**: Python pickle serialization for genome storage.

The best-performing bird genome is serialized to `best_bird_genome.pkl`, allowing:
- Quick loading of trained models
- Demonstration mode without training
- Transfer learning potential

## Multi-Mode Architecture

**Problem**: Support both training mode and demonstration/play mode.

**Solution**: Command-line argument parsing (argparse) to switch between modes:
- Training mode: Runs NEAT evolution across generations
- Demo mode: Loads pre-trained genome and displays AI playing

This allows the same codebase to serve multiple purposes without code duplication.

# External Dependencies

## Core Libraries

1. **Pygame**: Graphics rendering, window management, event handling, and game loop control
   - Used for all visual elements and game mechanics
   - Handles sprite animation and collision detection

2. **NEAT-Python**: Neural network evolution library
   - Implements the NEAT algorithm for evolving neural networks
   - Configuration loaded from `config-feedforward.txt`
   - Manages population, reproduction, and speciation

3. **Pickle**: Python's built-in serialization library
   - Saves/loads trained neural network genomes
   - Enables model persistence between sessions

## Assets

**Image Resources** (located in `imgs/` directory):
- Bird sprite sheets (bird1.png, bird2.png, bird3.png) for animation
- Pipe graphics (pipe.png)
- Background image (bg.png)
- Base/ground image (base.png)

All images are loaded and scaled using Pygame's image loading utilities with alpha channel support for transparency.

## Configuration

**NEAT Configuration File** (`config-feedforward.txt`):
- Defines neural network architecture parameters
- Sets evolution hyperparameters
- Specifies fitness criteria and population settings
- Feed-forward network topology with full direct initial connections

No external databases, APIs, or web services are used. The application is entirely self-contained and runs locally.