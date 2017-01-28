

#calss header
class _IMPARTIAL():
	def __init__(self,): 
		self.name = "IMPARTIAL"
		self.definitions = [u'not supporting any of the sides involved in an argument: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
