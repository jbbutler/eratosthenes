---
title: Another File
exports:
  - format: pdf
    output: exports/another-file.pdf
---

# Another File

Here's some text!

```{figure} https://github.com/rowanc1/pics/blob/main/sunset.png?raw=true
:label: figure1
:alt: Sunset at the beach
:align: center

An image at the beach...
```
An equation
```{math}
:label: equation1
w_{t+1} = (1 + r_{t+1}) s(w_t) + y_{t+1}
```

I am referencing [](#equation1). Look also at Figure [](#figure1).


:::{important}
An important message I have!
:::

I am citing [this reading](https://doi.org/10.1371/journal.pcbi.1002802) from last week.
