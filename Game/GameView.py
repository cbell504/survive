from Generic.View import View

class GameView(View):
	
	def startView(self):
		try:
			print("Possible Actions:\n")
			print("(1)  Check Stats")
			print("(2)  Check Inventory")
			print("(3)  Use Item")
			print("(4)  Gather Wood")
			print("(5)  Craft A New Item")
			print("(6)  Go Hunting")
			print("(10) Clear Screen")
			print("(0)  To Quit\n")
		except:
			raise