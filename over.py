"""
3. In cricket, an over consists of six deliveries a bowler bowls from one end. Create a
function that takes the number of balls bowled by a bowler and calculates the
number of overs and balls bowled by him/her. Return the value as a float, in the
format overs.balls.
"""

"""def balls(num):
    total_over=num/6
    return total_over
num=int(input("Enter the balls :-"))
result=balls(num)
print(result)"""

def calculate_overs(balls):
    overs = balls // 6
    # Calculate remaining balls
    remaining_balls = balls % 6
    # Return the result in the format overs.balls
    return float(f"{overs}.{remaining_balls}")

# Example usage:
balls_bowled = int(input("Enter the number of balls bowled: "))
result = calculate_overs(balls_bowled)
print(f"Bowler has bowled: {result} overs")
