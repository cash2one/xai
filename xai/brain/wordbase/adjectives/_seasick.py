

#calss header
class _SEASICK():
	def __init__(self,): 
		self.name = "SEASICK"
		self.definitions = [u'vomiting or having the feeling you will vomit because of the movement of the ship you are travelling in: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
