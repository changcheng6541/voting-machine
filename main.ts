input.onButtonPressed(Button.A, function () {
    First_persons_vote += 1
    console.log("First person's vote is " + ("" + ("" + ("" + ("" + First_persons_vote)))) + " and " + "second person's vote is " + ("" + ("" + ("" + ("" + second_persons_vote)))))
})
input.onGesture(Gesture.Shake, function () {
    console.log(People_has_the_most_vote)
})
input.onButtonPressed(Button.AB, function () {
    console.log("First person's vote is " + ("" + ("" + ("" + ("" + First_persons_vote)))) + " and " + "second person's vote is " + ("" + ("" + ("" + ("" + second_persons_vote)))))
})
input.onButtonPressed(Button.B, function () {
    second_persons_vote += 1
    console.log("First person's vote is " + ("" + ("" + ("" + ("" + First_persons_vote)))) + " and " + "second person's vote is " + ("" + ("" + ("" + ("" + second_persons_vote)))))
})
let second_persons_vote = 0
let People_has_the_most_vote = ""
let First_persons_vote = 0
console.log("Script created by Cheng, edited by Ray, and tested by Lucas Chen")
basic.forever(function () {
    if (First_persons_vote > second_persons_vote) {
        People_has_the_most_vote = "First person has the most vote"
    } else if (First_persons_vote < second_persons_vote) {
        People_has_the_most_vote = "Second person has the most vote"
    } else {
        People_has_the_most_vote = "The vote's are the same"
    }
})
