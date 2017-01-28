

#calss header
class _CORROSIVE():
	def __init__(self,): 
		self.name = "CORROSIVE"
		self.definitions = [u'A corrosive substance causes damage by chemical action: ', u'harmful and causing bad feelings: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
