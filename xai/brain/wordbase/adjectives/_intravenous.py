

#calss header
class _INTRAVENOUS():
	def __init__(self,): 
		self.name = "INTRAVENOUS"
		self.definitions = [u'into or connected to a vein: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
