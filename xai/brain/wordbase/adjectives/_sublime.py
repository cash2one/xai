

#calss header
class _SUBLIME():
	def __init__(self,): 
		self.name = "SUBLIME"
		self.definitions = [u'extremely good, beautiful, or enjoyable: ', u'very great: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
