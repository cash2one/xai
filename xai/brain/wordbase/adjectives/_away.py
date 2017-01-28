

#calss header
class _AWAY():
	def __init__(self,): 
		self.name = "AWAY"
		self.definitions = [u"An away match or game is played at an opposing team's sports ground: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
