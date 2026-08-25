Math and Algorithm Drills
=========================
These are explanation-first drills. Add numeric examples after you can explain each concept verbally.

1. Matrix order
   Task: Given a model point p, explain the difference between T*R*p and R*T*p. Describe the visual effect without calculating numbers.
   Check: answer should include variables, geometric meaning, and where it appears in the pipeline.

2. Homogeneous point vs direction
   Task: Write a short explanation for why a point can have w=1 and a direction can have w=0, and what translation does to each.
   Check: answer should include variables, geometric meaning, and where it appears in the pipeline.

3. Perspective divide
   Task: Explain what happens when clip coordinates (x, y, z, w) are divided by w. Why is this essential for perspective?
   Check: answer should include variables, geometric meaning, and where it appears in the pipeline.

4. Barycentric interpolation
   Task: Given weights alpha, beta, gamma with alpha+beta+gamma=1, explain how to interpolate depth or color across a triangle.
   Check: answer should include variables, geometric meaning, and where it appears in the pipeline.

5. Depth test
   Task: Given old depth 0.4 and incoming depth 0.6 under a 'less' depth test, decide whether the fragment survives and explain why.
   Check: answer should include variables, geometric meaning, and where it appears in the pipeline.

6. Diffuse lighting
   Task: Explain qualitatively why max(0, dot(n, l)) appears in a diffuse lighting term.
   Check: answer should include variables, geometric meaning, and where it appears in the pipeline.

7. Texture minification
   Task: Explain why sampling a high-frequency texture far away can alias and how mipmapping helps.
   Check: answer should include variables, geometric meaning, and where it appears in the pipeline.

8. Shadow comparison
   Task: Explain the comparison between fragment light-space depth and the stored shadow-map depth.
   Check: answer should include variables, geometric meaning, and where it appears in the pipeline.
