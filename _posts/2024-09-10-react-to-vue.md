---
title: "Migrating from React to Vue 3: A Practical Guide"
layout: post
date: 2024-09-10 10:00:00
tags: [Tech, Vue, React, Frontend]
---

I recently migrated a medium-sized project from React to Vue 3 (Composition API). Here are my takeaways and some code comparisons.

## Why Switch?

React is great, but I found Vue's reactivity system to be more intuitive for this specific project. The `ref` and `reactive` primitives in Vue 3 make state management incredibly simple.

## Component Comparison

Let's look at a simple counter component.

### React (Hooks)

```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
}
```

### Vue 3 (Composition API)

```vue
<script setup>
import { ref } from 'vue';

const count = ref(0);

function increment() {
  count.value++;
}
</script>

<template>
  <div>
    <p>Count: {{ count }}</p>
    <button @click="increment">
      Increment
    </button>
  </div>
</template>
```

## Key Differences

1.  **Reactivity**: In React, you use `useState` and setters. In Vue, you mutate the `.value` of a ref directly (or use reactive objects).
2.  **Templating**: React uses JSX. Vue uses an HTML-based template syntax (though it supports JSX too).
3.  **Lifecycle**: `useEffect` vs `onMounted`, `onUpdated`, `watchEffect`.

## Performance

In my benchmarks, Vue 3 performed slightly better in terms of memory usage for this specific dashboard application.

![Performance Chart](https://loremflickr.com/800/300/chart,graph)

## Final Thoughts

Both frameworks are excellent. Choose the one that fits your team's mental model best.
