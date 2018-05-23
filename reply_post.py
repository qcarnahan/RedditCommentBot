import praw
import pdb
import re
import os
import time

 # FILTERED WORDS BELOW








FILTEREDWORDS = ['nigger','fuck','damn','bitch','whore','slut','cunt','ass','asshole','damnit','dick', 'heck']
MODREASON = ["You have violated rule #1 no swearing!"]







def run_bot(r):
	if not os.path.isfile("posts_replied_to.txt") or not os.path.isfile("comments_replied_to.txt"):
		print("creating posts_replied_to")
		print("creating comments_replied_to")
		posts_replied_to = []
		comments_replied_to = []
	else:
		with open("posts_replied_to.txt", "r") as f:
			posts_replied_to = f.read()
			posts_replied_to = posts_replied_to.split("\n")
			posts_replied_to = list(filter(None, posts_replied_to))
		with open("comments_replied_to.txt", "r") as c:
			comments_replied_to = c.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = list(filter(None, comments_replied_to))


	
	for submission in subreddit.hot(limit=25):
		process_submission(submission)

			# if re.search("communist", submission.title, re.IGNORECASE):
			# 	submission.reply("TEST BOT says: COMMIE!")
			# 	print("Bot replying to : ", submission.title)
			# 	posts_replied_to.append(submission.id)
			# 	with open("posts_replied_to.txt", "w") as f:
		 #    				for post_id in posts_replied_to:
		 #    					f.write(post_id + "\n")




def process_submission(submission):
#	if submission.id not in posts_replied_to:
	normalized_title = submission.title.lower()
	for word in FILTEREDWORDS:
		if word in normalized_title:
			submission.mod.remove()
			posts_replied_to.append(submission.id)
	submission.comments.replace_more(limit=None)
	for comment in submission.comments.list():
#				if comment.id not in comments_replied_to:
		
		for word in FILTEREDWORDS:
			if word in comment.body.lower():
				comment.mod.remove()
				author = comment.author
				print("Banning ", author)
				subreddit.banned.add(author, params={"duration": 7, "note": MODREASON[0], "ban_message": "TEST"})
				# comment_replied_to.append(comment.id)


r = praw.Reddit('bot1')
subreddit = r.subreddit('dank_APEuro')
run_bot(r)