

#calss header
class _MANOEUVRABLE():
	def __init__(self,): 
		self.name = "MANOEUVRABLE"
		self.definitions = [u'easy to move and direct: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
