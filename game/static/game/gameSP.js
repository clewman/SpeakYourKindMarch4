let points = 0;
//document.querySelector('table').style.display = 'none';
//document.getElementById('current_score').style.display = 'none';



let easy = ['A Smile', 'Kind Words', 'Write a Nice Note', 'Write a Thank You Note', 'Pick Up Trash',
'Support Your Co-Workers', 'Leave a Great Tip', 'Conduct an Act of Service in Your Home',
'Leave Hidden Money', 'Start a Convo w/ a Stranger', 'Thank a Service Member', 'Thank a Police Officer',
'Open the Door for Someone', 'Bring Someone a Treat', 'Really Listen to Someone',
'Leave an Encouraging Note', 'Hold Your Partner\'s Hand', 'Surprise Someone w/ a Gift',
'Send a Text to Someone You Love', 'Honor a Teacher', 'Give a Hug', 'Give a High 5',
'Tell a Joke', 'Do a Chore for Someone', 'Return Someone\'s Cart', 'Feed the Birds',
'Let Someone go Ahead in Line', 'Thank You Note to the Mailperson', 'Help Make Dinner',
'Give Yourself 5 Compliments', 'Give up a Parking Spot', 'Help Someone Take a Photo',
'Give Directions'
]

//not sure i need this anymore
let easyIndex = Math.floor(Math.random() * 32);


function shuffle(array) {
  var currentIndex = array.length, temporaryValue, randomIndex;
  while (0 !== currentIndex) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }
  return array;
}

function loginButton() {
  document.querySelector('flex-container').style.display = 'block';

}

function newGameButton() {
  document.querySelector('table').style.display = 'table';
  easy = shuffle(easy);
  for (let textContent = 0; textContent < 9; textContent++){
    document.getElementById("square" + textContent).innerHTML = shuffle(easy[textContent]);
  }

  var btn = document.createElement("button");
  var t = document.createTextNode("Save Game");
  btn.appendChild(t);
  document.querySelector('.flex-container').appendChild(btn);
}

// function saveGameButton() {
// }


for (let square_index = 0; square_index < 9; square_index++){
  let square = document.querySelector('#square'+square_index)
  square.onclick = function (e) {
    square.onclick = null
    square.style.backgroundImage = 'linear-gradient(45deg, lime, lime, lime)'
    square.style.color = 'white';
    square.innerHTML = '<i class="fas fa-check"></i>'
    points += 10;
    document.getElementById('current_score').style.display = 'block';
    document.getElementById('current_score').innerHTML = 'Current Score: ' + points
    // alert("You earned " + points + ' points!');
    rowComplete();
  }
}
// function currentScore() {
//   document.getElementById('current_score').innerHTML = 'Current Score: ' + points
// }

function totalScore() {

}

// this needs to be per row, not just by points
function rowComplete() {
  if (points >= 30) {
    alert('You\'ve completed a row')
  }
}
