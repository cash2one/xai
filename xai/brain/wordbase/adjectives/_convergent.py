

#calss header
class _CONVERGENT():
	def __init__(self,): 
		self.name = "CONVERGENT"
		self.definitions = [u'coming closer together: ', u'becoming more similar: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
