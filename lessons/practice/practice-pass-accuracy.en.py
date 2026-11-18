# Pass completion rates and grades
# The learner selected the second entry with index 1 and confirmed 70.0 percent for 42 of 60.
# For the final loop, take one completed-pass count per iteration. Divide by 60 and multiply by 100.
# Check the higher threshold first. The lower threshold includes 60.
# A loop without an indented body raises IndentationError. Printing after a nonempty loop prints once.
# The example uses illustrative training thresholds.

completed_passes = [48, 36, 30]
for passes in completed_passes:
    accuracy_passes = passes / 60 * 100
    print(accuracy_passes)
    if accuracy_passes >= 80:
        print('우수')
    elif accuracy_passes >= 60:
        print('보통')
    else:
        print('개선 필요')
