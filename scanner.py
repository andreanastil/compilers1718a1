def getchar(words,pos):
	""" returns char at pos of words, or None if out of bounds """

	if pos<0 or pos>=len(words): return None

	if ord(text[pos])>=ord('0') and ord(text[pos])<=ord('1'):
		return 'zero-one'

	elif ord(text[pos])==ord('2'):
		return 'two'

	elif ord(text[pos])==ord('.') or ord(text[pos])==ord(':'):
		return 'seperator'	

	elif ord(text[pos])==ord('3'):
		return 'three'	

	elif ord(text[pos])==ord('4'):
		return 'four'

	elif ord(text[pos])==ord('5'):
		return 'five'	
		
	elif ord(text[pos])>=ord('6') and ord(text[pos])<=ord('9'):
		return 'six-nine'	

	else:
		return 'error'	

	return words[pos]
	

def scan(text,transition_table,accept_states):
	""" Scans `text` while transitions exist in 'transition_table'.
	After that, if in a state belonging to `accept_states`,
	returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	pos = 0
	state = 'q0'
	
	while True:
		
		c = getchar(text,pos)	# get next char
		
		if state in transition_table and c in transition_table[state]:
		
			state = transition_table[state][c]	# set new state
			pos += 1	# advance to next char
			
		else:	# no transition found

			# check if current state is accepting
			if state in accept_states:
				return accept_states[state],pos

			# current state is not accepting
			return 'ERROR_TOKEN',pos
			
	
# the transition table, as a dictionary

td = { 'q0':{ 'zero-one':'q1','two':'q4','three':'q2','four':'q2','five':'q2','six-nine':'q2'},
       'q1':{ 'zero-one':'q2','two':'q2','three':'q2','four':'q2','five':'q2','six-nine':'q2','seperator':'q3'},
       'q2':{ 'seperator':'q3'},
       'q3':{ 'zero-one':'q5','two':'q5','three':'q5','four':'q5','five':'q5'},
       'q4':{ 'zero-one':'q2','two':'q2','three':'q2','seperator':'q3'},
       'q5':{ 'zero-one':'q6','two':'q6','three':'q6','four':'q6','five':'q6','six-nine':'q6'}
     }  

# the dictionary of accepting states and their
# corresponding token

ad = { 'q6':'TIME_TOKEN'}  


# get a string from input
text = input('check your time>')

# scan text until no more input
while text:	# that is, while len(text)>0
	
	# get next token and position after last char recognized
	token,position = scan(text,td,ad)
	
	if token=='ERROR_TOKEN':
		print('unrecognized input at pos',position+1,'of',text)
		break
	
	print("token:",token,"string:",text[:position])
	
	# remaining text for next scan
	text = text[position:]
