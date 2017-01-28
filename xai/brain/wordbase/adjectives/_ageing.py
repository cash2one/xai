

#calss header
class _AGEING():
	def __init__(self,): 
		self.name = "AGEING"
		self.definitions = [u'relating to getting older: ', u'used to describe a person or thing that is getting old: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
