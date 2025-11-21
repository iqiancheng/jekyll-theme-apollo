---
title: "Tech Tutorial: Mermaid Diagrams & Code Blocks"
layout: post
date: 2024-11-21 09:00:00
tags: [Code, Tutorial]
---

This post demonstrates how to use **Mermaid** diagrams and syntax highlighting for various programming languages.

## Mermaid Diagrams

Here is a flowchart generated using Mermaid:

<div class="mermaid">
graph TD;
    A[Start] --> B{Is it working?};
    B -- Yes --> C[Great!];
    B -- No --> D[Debug];
    D --> B;
</div>

And a sequence diagram:

<div class="mermaid">
sequenceDiagram
    participant Alice
    participant Bob
    Alice->>John: Hello John, how are you?
    loop Healthcheck
        John->>John: Fight against hypochondria
    end
    Note right of John: Rational thoughts <br/>prevail!
    John-->>Alice: Great!
    John->>Bob: How about you?
    Bob-->>John: Jolly good!
</div>

## Code Blocks

### Python

```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
```

### JavaScript

```javascript
const greet = (name) => {
    console.log(`Hello, ${name}!`);
}

greet('World');
```

### Go

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, Go!")
}
```

### Rust

```rust
fn main() {
    println!("Hello, Rust!");
}
```

## Conclusion

This theme supports rich content rendering!
