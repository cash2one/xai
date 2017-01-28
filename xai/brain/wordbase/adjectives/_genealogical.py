

#calss header
class _GENEALOGICAL():
	def __init__(self,): 
		self.name = "GENEALOGICAL"
		self.definitions = [u'related to the history of the past and present members of a family or families']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
