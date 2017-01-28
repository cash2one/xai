

#calss header
class _LOCOMOTIVE():
	def __init__(self,): 
		self.name = "LOCOMOTIVE"
		self.definitions = [u'relating to movement or the ability to move']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
