

#calss header
class _EGOTISTIC():
	def __init__(self,): 
		self.name = "EGOTISTIC"
		self.definitions = [u'considering yourself to be better or more important than other people']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
