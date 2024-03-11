## Overview

Este código aplica conceitos essenciais de Inteligência Artificial, como a predição por meio de uma linha de regressão linear. Ele também calcula o Coeficiente de Determinação (R²), que indica a proporção da variância dos dados explicada pelo modelo, e o Erro Quadrático Médio (EQM), que mede a média dos quadrados dos erros entre valores observados e predições. Além disso, o código aborda a organização de conjuntos de dados para treinamento utilizando o método Hold-out, que separa uma parte dos dados para teste e avaliação do modelo.

This code applies essential concepts of Artificial Intelligence, such as prediction through a linear regression line. It also calculates the Coefficient of Determination (R²), which indicates the proportion of data variance explained by the model, and the Mean Squared Error (MSE), which measures the average of the squares of the errors between observed values and predictions. Furthermore, the code addresses the organization of datasets for training using the Hold-out method, which separates a portion of the data for testing and model evaluation.

### Instruction

- [ ] Fork this repository

 - [ ] Clone your forked repository

 - [ ] Add your scripts

 - [ ] Commit and push

 - [ ] Celebrate your first project in android development

#### Commit Patterns

The project uses the Conventional Commits standards, so we will use the following commit structure:

```!type(?scope): !subject```

The types can be as follows:

* ```feat``` - Feat type commits indicate that your code snippet is including a new feature (related to the MINOR in semantic versioning).
* ```fix``` - Fix type commits indicate that your committed code snippet is solving a problem (bug fix), (related to the PATCH in semantic versioning).
* ```docs``` - Docs type commits indicate that there have been changes in the documentation, such as in the Readme of your repository. (Does not include code changes).
* ```perf``` - Perf type commits are used to identify any code changes related to performance.
* ```style``` - Style type commits indicate that there have been changes related to code formatting, semicolons, trailing spaces, lint… (Does not include code changes).
* ```refactor``` - Refactor type commits refer to changes due to refactorings that do not alter their functionality, such as a change in the format in which a certain part of the screen is processed, but which maintained the same functionality, or performance improvements due to a code review.
* ```enhancement``` - Enhancement type commits indicate improvements to a feature, that is, something to be added to an existing resource, such as an improvement in the layout of a button.
* ```chore``` - Change outside the runtime environment - Update something without impacting the code (e.g., readme update, CI/CD update…).

The scope refers to the issue id, for example, if there is a ODPR001 issue with a bugfix commit, it should be written following the standard:


```git commit -m "fix(DOCF001): fix to r person"```

Subject refers to a brief description of what was done in that commit, in the case above it would be “add padding in button on login page”

Note: The commits must be in English.

Thank :)))