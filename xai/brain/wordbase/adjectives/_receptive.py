

#calss header
class _RECEPTIVE():
	def __init__(self,): 
		self.name = "RECEPTIVE"
		self.definitions = [u'willing to listen to and accept new ideas and suggestions: ', u'relating to the ability to understand language, rather than produce it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
