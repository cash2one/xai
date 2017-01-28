

#calss header
class _SLIMY():
	def __init__(self,): 
		self.name = "SLIMY"
		self.definitions = [u'covered in slime: ', u'If you describe a person or their manner as slimy, you mean that they appear to be friendly but in a way that you find unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
