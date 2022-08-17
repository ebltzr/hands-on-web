def subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases):
	# print title
	print("Welcome to the Ada+ Account Dashboard")
	print() # print blank line

	# declare a dictionary to store the data
	subscribers = {}

	# do initial calculations
	for i in range(len(months_subscribed)):
		subscriber = {}
		subscriber['base_cost'] = (18 * (months_subscribed[i] // 3)) + (7 * (months_subscribed[i] % 3))
		subscriber['ad_free_cost'] = 2 * ad_free_months[i]
		subscriber['on_demand_cost'] = 27.99 * video_on_demand_purchases[i]
		subscriber['total'] = subscriber['base_cost'] + subscriber['ad_free_cost'] + subscriber['on_demand_cost']

		# print individual account details
		print(f"Account {i+1} made ${subscriber['total']}")
		print(f">>> ${subscriber['base_cost']} from month subscription")
		print(f">>> ${subscriber['ad_free_cost']} from Ad-free upgrades")
		print(f">>> ${subscriber['ad_free_cost']} from Video on Demand purchases")
		print() # print blank line

		# save data in dictionary
		subscribers[i] = subscriber

	# calculate overall stats
	total_account_amount = 0
	total_premium_amount = 0

	max_amount_earned = 0 # tracking who made the most
	highest_earner = 0 # saving the position of who made the most

	for i in range(len(months_subscribed)):
		total_account_amount += subscribers[i]['total']
		total_premium_amount += subscribers[i]['ad_free_cost'] + subscribers[i]['on_demand_cost']
		# update who made the most
		if(subscribers[i]['total'] > max_amount_earned):
			max_amount_earned = subscribers[i]['total']
			highest_earner = i # set the highest earner to the current person (this is whoever 'i' is right now)

	# print overall stats
	print(f"Combined all accounts made ${total_account_amount} total")
	print(f"Premium content (Ad-free-watching and Video on Demand) made ${total_premium_amount} total")
	print() # print blank line

	print(f"${max_amount_earned} was the most earned by any single account")
	print(f"The accounts that earned the most were: #{highest_earner + 1}")
