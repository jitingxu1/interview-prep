# Annotation Workflow Engine

## Problem

Annotators label data by moving through workflows. A workflow defines a set of tasks (e.g., Submission, Review, Adjudication) and how datapoints transition between them. When a task is completed with a result, the datapoint advances to its next task(s) — or reaches a terminal state.

## Format

This interview has two parts:

1. **Core workflow engine**: build the engine that moves annotators through workflows.
2. **Analytics**: add analytics on top of the engine.

The interface your code needs to implement is stubbed out in `engine/`.

A datapoint's round counts how many times its submission has been authored: it starts at 1 and goes up each time the submission is reauthored.

## Submission

When the interview ends, package up your work and send it back to us. We'll run our test suite against it.

## Questions

Feel free to ask questions at any point.
