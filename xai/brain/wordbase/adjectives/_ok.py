

#calss header
class _OK():
	def __init__(self,): 
		self.name = "OK"
		self.definitions = [u'agreed or acceptable: ', u'in a satisfactory state or of a satisfactory quality: ', u'not bad but certainly not good: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
