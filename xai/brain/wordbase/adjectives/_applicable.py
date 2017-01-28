

#calss header
class _APPLICABLE():
	def __init__(self,): 
		self.name = "APPLICABLE"
		self.definitions = [u'affecting or relating to a person or thing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
