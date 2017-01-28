

#calss header
class _CREATIVE():
	def __init__(self,): 
		self.name = "CREATIVE"
		self.definitions = [u'producing or using original and unusual ideas: ', u'describing or explaining things in unusual ways in order to deceive or give a false impression: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
