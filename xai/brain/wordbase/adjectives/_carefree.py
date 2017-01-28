

#calss header
class _CAREFREE():
	def __init__(self,): 
		self.name = "CAREFREE"
		self.definitions = [u'having no problems or not being worried about anything: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
