

#calss header
class _CAROTID():
	def __init__(self,): 
		self.name = "CAROTID"
		self.definitions = [u'relating to the two main arteries that carry blood to the head and neck']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
