---
title: "Building a Responsive Navbar: A Frontend Guide"
layout: post
date: 2025-04-20 10:00:00
tags: [Frontend, CSS, JavaScript, Tutorial]
---

I'm a frontend developer who loves clean UI. This theme resonates with me because it practices what I preach: simplicity and responsiveness. Let's dive into how we can document UI components using **Mermaid** flowcharts and **CSS** snippets.

## The Logic Flow

Before writing code, I always map out the interaction logic. Here is how the mobile menu toggle works:

<div class="mermaid">
graph TD
    A[User Clicks Hamburger] --> B{Is Menu Open?};
    B -- Yes --> C[Remove .active class];
    B -- Yes --> D[Slide Up Menu];
    B -- No --> E[Add .active class];
    B -- No --> F[Slide Down Menu];
</div>

## The Styling

I prefer using SCSS for nesting. Here is the core logic for the hamburger icon:

```scss
.hamburger {
    display: none;
    cursor: pointer;
    
    @media (max-width: 768px) {
        display: block;
        position: absolute;
        right: 20px;
        top: 20px;
    }
    
    span {
        display: block;
        width: 25px;
        height: 3px;
        margin: 5px auto;
        background-color: #333;
        transition: all 0.3s ease-in-out;
    }
}
```

## The Result

A smooth, accessible navigation experience.

![Web Design](https://loremflickr.com/800/400/webdesign,interface)

This theme handles code blocks beautifully, making it easy for me to share my knowledge with the community.
