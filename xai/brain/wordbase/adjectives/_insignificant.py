

#calss header
class _INSIGNIFICANT():
	def __init__(self,): 
		self.name = "INSIGNIFICANT"
		self.definitions = [u'small or not noticeable, and therefore not considered important : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
