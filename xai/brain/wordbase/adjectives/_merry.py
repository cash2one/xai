

#calss header
class _MERRY():
	def __init__(self,): 
		self.name = "MERRY"
		self.definitions = [u'happy or showing enjoyment: ', u'UK polite word for slightly drunk: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
