

#calss header
class _PATHOGENIC():
	def __init__(self,): 
		self.name = "PATHOGENIC"
		self.definitions = [u'able to cause disease']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
