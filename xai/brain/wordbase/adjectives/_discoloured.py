

#calss header
class _DISCOLOURED():
	def __init__(self,): 
		self.name = "DISCOLOURED"
		self.definitions = [u'Something that is discoloured has become a less attractive colour than it was originally: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
