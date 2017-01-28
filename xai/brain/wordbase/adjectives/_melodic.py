

#calss header
class _MELODIC():
	def __init__(self,): 
		self.name = "MELODIC"
		self.definitions = [u'very pleasant to listen to', u'relating to the tune in a piece of music']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
