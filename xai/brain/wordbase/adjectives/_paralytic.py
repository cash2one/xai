

#calss header
class _PARALYTIC():
	def __init__(self,): 
		self.name = "PARALYTIC"
		self.definitions = [u'extremely drunk', u'related to or connected with paralysis: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
