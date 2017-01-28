

#calss header
class _TERRACED():
	def __init__(self,): 
		self.name = "TERRACED"
		self.definitions = [u'built as or belonging to a row of often small houses joined together along their side walls: ', u'(of land, fields, etc.) built in step-like terraces on a slope']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
