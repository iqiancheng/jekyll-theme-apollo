---
title: 图片占位符服务速查指南
layout: post
date: 2025-11-21 00:00:00 +0800
tags: [前端, 工具, 性能优化]
---

在开发过程中，图片占位符服务能显著提升原型设计和开发效率。本文整理了全球可用、国内可访问的主流占位符服务（含多种风格头像生成），并直接展示其 **Markdown 渲染效果**，方便你直接复制使用。

## 服务对比

| 服务 | 类型 | 适用场景 | 核心特性 |
| :--- | :--- | :--- | :--- |
| **Placehold.co** | 纯色占位 | 线框图、文本占位 | SVG 默认、自定义文本/字体、Retina 支持 |
| **Lorem Picsum** | 真实照片 | 逼真效果展示 | 随机/固定 ID、灰度/模糊、种子稳定 |
| **DummyImage** | 纯色占位 | 快速简单场景 | 背景/前景色、极简配置 |
| **DiceBear** | 头像生成 | 多风格头像 | 像素画/现代风、种子确定性、可自托管 |
| **RoboHash** | 头像生成 | 趣味/机器人 | 机器人/怪兽/外星人、URL 简单 |

## 实时演示与用法

### 1. Placehold.co - 纯色占位 + 可定制文本

支持 SVG（加载快）、自定义颜色和文本。

**用法：**

```markdown
![Placehold.co](https://placehold.co/600x200/orange/white/svg?text=Hello+World&font=roboto)
```

**效果预览：**

![Placehold.co](https://placehold.co/1500x500/orange/white/svg?text=Hello+World&font=roboto)

---

### 2. Lorem Picsum - 随机真实照片

提供高质量的随机摄影图片。

**用法（指定 ID 和模糊）：**

```markdown
![Lorem Picsum](https://picsum.photos/id/237/600/300?blur=2)
```

**效果预览：**

![Lorem Picsum](https://picsum.photos/id/237/600/300?blur=2)

---

### 3. DummyImage - 极简纯色占位

最简单的纯色块，URL 规则非常直观：`尺寸/背景色/前景色`。

**用法：**

```markdown
![DummyImage](https://dummyimage.com/600x200/000/fff)
```

**效果预览：**

![DummyImage](https://dummyimage.com/600x200/000/fff)

---

### 4. 头像生成专题 (Avatars)

#### 4.1 DiceBear - 像素画 & 现代风 (推荐)

功能最强大的头像生成器，支持多种风格。其中 `pixel-art` 非常适合复古/马赛克需求。

**用法（像素风 & 现代风）：**

```markdown
![DiceBear Pixel](https://api.dicebear.com/9.x/pixel-art/svg?seed=pengyai&size=128)
![DiceBear Modern](https://api.dicebear.com/9.x/avataaars/svg?seed=pengyai&size=128)
```

**效果预览：**

![DiceBear Pixel](https://api.dicebear.com/9.x/pixel-art/svg?seed=pengyai&size=128)
![DiceBear Modern](https://api.dicebear.com/9.x/avataaars/svg?seed=pengyai&size=128)

#### 4.2 Gravatar Retro - 经典回退

如果你使用 Gravatar，可以通过 `d` 参数指定回退样式。

**用法（Retro & Identicon）：**

```markdown
![Gravatar Retro](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=retro&f=y&s=128)
![Gravatar Identicon](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=identicon&f=y&s=128)
```

**效果预览：**

![Gravatar Retro](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=retro&f=y&s=128)
![Gravatar Identicon](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=identicon&f=y&s=128)

## 性能优化建议

1.  **优先使用 SVG**：DiceBear 和 Placehold.co 均原生支持 SVG，体积小且清晰。
2.  **指定 WebP 格式**：如果使用照片（Picsum），尽量在 URL 后加 `.webp`。
3.  **国内加速**：
    *   DiceBear 推荐自托管部署（官方提供 Docker 镜像）。
    *   RoboHash 在国内通常可访问，但建议生产环境做本地缓存。

## 总结

- **画原型**：Placehold.co
- **填内容**：Lorem Picsum
- **复古/像素头像**：DiceBear (pixel-art) / Gravatar Retro
