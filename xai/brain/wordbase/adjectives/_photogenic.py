

#calss header
class _PHOTOGENIC():
	def __init__(self,): 
		self.name = "PHOTOGENIC"
		self.definitions = [u'having a face that looks attractive in photographs']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
