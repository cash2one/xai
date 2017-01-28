

#calss header
class _EVOLUTIONARY():
	def __init__(self,): 
		self.name = "EVOLUTIONARY"
		self.definitions = [u'relating to the way in which living things develop over millions of years', u'involving a gradual process of change and development: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
