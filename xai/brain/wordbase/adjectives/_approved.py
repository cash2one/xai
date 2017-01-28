

#calss header
class _APPROVED():
	def __init__(self,): 
		self.name = "APPROVED"
		self.definitions = [u'used to refer to something that is generally or officially accepted as being correct or satisfactory: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
