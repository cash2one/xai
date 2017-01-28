

#calss header
class _REARMOST():
	def __init__(self,): 
		self.name = "REARMOST"
		self.definitions = [u'furthest to the back or the last in a row: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
