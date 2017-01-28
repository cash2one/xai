

#calss header
class _COMMENSURATE():
	def __init__(self,): 
		self.name = "COMMENSURATE"
		self.definitions = [u'in a correct and suitable amount compared to something else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
