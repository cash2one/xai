

#calss header
class _PORTRAIT():
	def __init__(self,): 
		self.name = "PORTRAIT"
		self.definitions = [u'A portrait computer document is to be printed with the shorter side of the paper at the top and bottom.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
