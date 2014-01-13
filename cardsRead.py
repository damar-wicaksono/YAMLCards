#!/usr/bin/env python

import yaml

# Read the Cards in YAML format
stream = file('vessel.yaml', 'r')
cards = yaml.load(stream)

# Print the cards with pretty formatting
for i in cards.keys():
   if not cards[i][0]['General']['Skipped']: 
   # Check if the card is used at all

      if cards[i][0]['General']['Type'] == 'Scalar':
      # Check if it is a scalar card
         # Make the title of a scalar cards into a list
         y = [ cards[i][j].keys()[0] for j in range(1,len(cards[i])) ]
         z = [ cards[i][j][cards[i][j].keys()[0]]['Value'] 
                        for j in range(1, len(cards[i])) ]
         if i == 1:
            print '*******' + ''.join(['%12s' %y[k] for k in range(len(y))])
         else:
            print ''.join(['%12s' %y[k] for k in range(len(y))]).replace(' ', '*', 1)
         # Check if the card is the 1st card
         if i == 1:
            print z[0] + ''.join(['%20s' %z[k] for k in range(1, len(z))])
         else:
            print ''.join(['%12s' %z[k] for k in range(len(z))])

      elif cards[i][0]['General']['Type'] == 'Array':
      # Check if it is an array card
         y = cards[i][1].keys()[0]
         z = eval(cards[i][1][y])
         str = '%12s' %y
         str = str.replace(' ', '*', 1)
         str = str + ' *' 
         ll = 0            # Lower count limit
         if len(z) < 5:    # Upper count limit
            ul = len(z)
         else:
            ul = 5
         if len(z)%5 == 0:
            count = len(z)/5
         else:
            count = len(z)/5 + 1
         for j in range(count):
            if ul != len(z):
               str1 = str + ''.join([ '%10s' %z[k] for k in range(ll,ul) ]) + 's'
            else:
               str1 = str + ''.join([ '%10s' %z[k] for k in range(ll,ul) ]) + 'e'
            ll = (j + 1) * 5
            if len(z) - (j + 1) * 5 < 5:
               ul = len(z)
            else:
               ul = 5  + (j + 1) * 5
            
            print str1
            str1 = '' 
        


   
