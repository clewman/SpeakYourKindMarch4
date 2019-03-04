from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
from random import choice

FAKE_NAMES = ['A Smile', 'Kind Words', 'Write a Nice Note', 'Write a Thank You Note', 'Pick Up Trash',
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
class Person(AbstractUser):

    saved_scores = models.IntegerField(default=0,blank=True)

class Tile(models.Model):
    x= models.IntegerField()
    y=models.IntegerField()
    finished = models.BooleanField(default=False)
    title=models.CharField(max_length=50,blank=True,null=True)
    game=models.ForeignKey("Game",on_delete=models.CASCADE,related_name="tiles")

    def __str__(self):
        return '({}, {})'.format(self.y, self.x)

class Game(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    player = models.ForeignKey(Person,on_delete=models.PROTECT, related_name='games')
    score = models.IntegerField(default=0)
    game_finished = models.BooleanField(default=False)

    def generate_tiles(self):
        for y in range (3):
            for x in range(3):
                Tile.objects.create(x=x,y=y,game=self,title=choice(FAKE_NAMES))
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if not self.tiles.all().exists():
            self.generate_tiles()
    def check_score(self, list):
        print(list)
        for i in list:
            print(i.id)
            if not i.finished:
                return False
        return True

    def get_score(self):
        self.score = 0
        tiles = self.tiles.all()
        array = [
            [],
            [],
            [],
        ]
        for index in range(len(tiles)):
            if index in range(3):
              array[0].append(tiles[index])
            elif index in range(3, 6):
              array[1].append(tiles[index])
            elif index in range(6, 9):
              array[2].append(tiles[index])

        if self.check_score(array[0]):
            print(True)
            self.score += 1
        if self.check_score(array[1]):
            self.score += 1
        if self.check_score(array[2]):
            self.score += 1

        if self.check_score([array[0][0], array[1][0], array[2][0]]):
            self.score += 1

        if self.check_score([array[0][1], array[1][1], array[2][1]]):
            self.score += 1

        if self.check_score([array[0][2], array[1][2], array[2][2]]):
            self.score += 1

        if self.check_score([array[0][0], array[1][1], array[2][2]]):
            self.score += 1

        if self.check_score([array[0][2], array[1][1], array[2][0]]):
            self.score += 1
        return array

     #
     # #Player get a star if they complete a row or a column or diagonal
     #    stars = [
     #        [0, 1, 2],  # Across top
     #        [3, 4, 5],  # Across middle
     #        [6, 7, 8],  # Across bottom
     #        [0, 3, 6],  # Down left
     #        [1, 4, 7],  # Down middle
     #        [2, 5, 8],  # Down right
     #        [0, 4, 8],  # Diagonal ltr
     #        [2, 4, 6],  # Diagonal rtl
     #    ]
     #


class Winner(models.Model):
    highest_level = models.ForeignKey(Game, on_delete=models.PROTECT)


    def __str__(self):
        return self.current_winner.name

