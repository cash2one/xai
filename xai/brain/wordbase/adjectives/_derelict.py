

#calss header
class _DERELICT():
	def __init__(self,): 
		self.name = "DERELICT"
		self.definitions = [u'Derelict buildings or places are not cared for and are in bad condition: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
