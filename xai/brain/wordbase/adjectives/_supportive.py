

#calss header
class _SUPPORTIVE():
	def __init__(self,): 
		self.name = "SUPPORTIVE"
		self.definitions = [u'showing agreement and giving encouragement: ', u'giving help and encouragement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
