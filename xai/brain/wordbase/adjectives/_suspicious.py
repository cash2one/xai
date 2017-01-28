

#calss header
class _SUSPICIOUS():
	def __init__(self,): 
		self.name = "SUSPICIOUS"
		self.definitions = [u'making you feel that something illegal is happening or that something is wrong: ', u'feeling doubt or no trust in someone or something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
