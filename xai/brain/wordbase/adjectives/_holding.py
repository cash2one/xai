

#calss header
class _HOLDING():
	def __init__(self,): 
		self.name = "HOLDING"
		self.definitions = [u"In football, if a midfield player has a holding role, their main job is to help the defence rather than attack an opponent's goal: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
