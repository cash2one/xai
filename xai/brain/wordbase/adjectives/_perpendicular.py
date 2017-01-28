

#calss header
class _PERPENDICULAR():
	def __init__(self,): 
		self.name = "PERPENDICULAR"
		self.definitions = [u'at an angle of 90\xb0 to a horizontal line or surface: ', u'at an angle of 90\xb0 to another line or surface: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
