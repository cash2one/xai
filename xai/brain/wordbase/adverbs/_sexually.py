

#calss header
class _SEXUALLY():
	def __init__(self,): 
		self.name = "SEXUALLY"
		self.definitions = [u'to do with sexual activity: ', u'to do with being male or female: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
