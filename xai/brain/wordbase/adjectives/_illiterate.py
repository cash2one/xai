

#calss header
class _ILLITERATE():
	def __init__(self,): 
		self.name = "ILLITERATE"
		self.definitions = [u'unable to read and write: ', u'knowing little or nothing about a particular subject: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
