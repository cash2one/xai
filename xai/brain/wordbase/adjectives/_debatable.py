

#calss header
class _DEBATABLE():
	def __init__(self,): 
		self.name = "DEBATABLE"
		self.definitions = [u'not clear or certain because different people may have different opinions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
