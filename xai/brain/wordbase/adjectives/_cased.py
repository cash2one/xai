

#calss header
class _CASED():
	def __init__(self,): 
		self.name = "CASED"
		self.definitions = [u'covered in a tight case (= container or covering): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
