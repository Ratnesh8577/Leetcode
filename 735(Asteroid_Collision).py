"""class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for a in asteroids:
            # If positive asteroid, just push it
            if a > 0:
                stack.append(a)
            else:
                # For negative asteroid, collide with stack's positive asteroids
                while stack and stack[-1] > 0 and stack[-1] < abs(a):
                    stack.pop()
                if stack and stack[-1] == abs(a):
                    stack.pop()  # both destroyed
                elif not stack or stack[-1] < 0:
                    stack.append(a)
                # else: the negative asteroid is destroyed (do nothing)
        return stack
"""

class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for a in asteroids:
            destroyed = False
            # Only possible collisions when current asteroid is moving left (<0)
            # and top of stack asteroid is moving right (>0)
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    stack.pop()  # top asteroid destroyed, continue checking
                    continue
                elif stack[-1] == -a:
                    stack.pop()  # both destroyed
                destroyed = True
                break
            if not destroyed:
                stack.append(a)
        return stack
