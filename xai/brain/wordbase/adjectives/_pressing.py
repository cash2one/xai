

#calss header
class _PRESSING():
	def __init__(self,): 
		self.name = "PRESSING"
		self.definitions = [u'urgent or needing to be dealt with immediately: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
