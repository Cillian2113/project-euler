def coinSums():
	#make 200 with varying amounts of 1,2,5,10,20,50,100,200
	ways = 1 #for just a two pound coin
	for pound in range(3):
		for fifty in range(5):
			if pound*100+fifty*50 > 200: continue
			for twenty in range(11):
				if pound*100+fifty*50+twenty*20 > 200: continue
				for ten in range(21):
					if pound*100+fifty*50+twenty*20+ten*10 > 200: continue
					for five in range(41):
						if pound*100+fifty*50+twenty*20+ten*10+five*5 > 200: continue
						for two in range(101):
							if pound*100+fifty*50+twenty*20+ten*10+five*5+two*2 > 200: continue
							for one in range(201):
								if pound*100+fifty*50+twenty*20+ten*10+five*5+two*2+one == 200:
									ways += 1
	return ways

print(coinSums())
