

#calss header
class _LOYAL():
	def __init__(self,): 
		self.name = "LOYAL"
		self.definitions = [u'firm and not changing in your friendship with or support for a person or an organization, or in your belief in your principles: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
