

#calss header
class _UNEQUIVOCAL():
	def __init__(self,): 
		self.name = "UNEQUIVOCAL"
		self.definitions = [u'total, or expressed in a clear and certain way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
