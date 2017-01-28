

#calss header
class _DEMENTED():
	def __init__(self,): 
		self.name = "DEMENTED"
		self.definitions = [u'unable to think or act clearly because you are extremely worried, angry, or excited by something: ', u'crazy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
