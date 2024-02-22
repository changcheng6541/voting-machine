def on_button_pressed_a():
    global First_persons_vote
    First_persons_vote += 1
    print("First person's vote is " + ("" + ("" + ("" + ("" + str(First_persons_vote))))) + " and " + "second person's vote is " + ("" + ("" + ("" + ("" + str(second_persons_vote))))))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    print(People_has_the_most_vote)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    print("First person's vote is " + ("" + ("" + ("" + ("" + str(First_persons_vote))))) + " and " + "second person's vote is " + ("" + ("" + ("" + ("" + str(second_persons_vote))))))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global second_persons_vote
    second_persons_vote += 1
    print("First person's vote is " + ("" + ("" + ("" + ("" + str(First_persons_vote))))) + " and " + "second person's vote is " + ("" + ("" + ("" + ("" + str(second_persons_vote))))))
input.on_button_pressed(Button.B, on_button_pressed_b)

second_persons_vote = 0
People_has_the_most_vote = ""
First_persons_vote = 0
print("Script created by Cheng, edited by Ray, and tested by Lucas Chen")

def on_forever():
    global People_has_the_most_vote
    if First_persons_vote > second_persons_vote:
        People_has_the_most_vote = "First person has the most vote"
    elif First_persons_vote < second_persons_vote:
        People_has_the_most_vote = "Second person has the most vote"
    else:
        People_has_the_most_vote = "The vote's are the same"
basic.forever(on_forever)
