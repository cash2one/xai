

#calss header
class _POWDERED():
	def __init__(self,): 
		self.name = "POWDERED"
		self.definitions = [u'in the form of a powder or covered with a powder: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
