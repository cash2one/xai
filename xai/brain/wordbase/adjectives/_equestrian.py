

#calss header
class _EQUESTRIAN():
	def __init__(self,): 
		self.name = "EQUESTRIAN"
		self.definitions = [u'connected with the riding of horses: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
