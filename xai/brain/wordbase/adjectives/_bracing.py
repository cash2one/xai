

#calss header
class _BRACING():
	def __init__(self,): 
		self.name = "BRACING"
		self.definitions = [u'(of weather) cold and perhaps windy; (of an activity) making you feel full of energy because it is done outside when the weather is cold and perhaps windy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
