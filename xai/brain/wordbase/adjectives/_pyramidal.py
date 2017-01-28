

#calss header
class _PYRAMIDAL():
	def __init__(self,): 
		self.name = "PYRAMIDAL"
		self.definitions = [u'shaped like a pyramid', u'relating to the path of groups of nerve fibres in the brain called the pyramidal tract']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
