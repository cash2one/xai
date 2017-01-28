

#calss header
class _UNCOOPERATIVE():
	def __init__(self,): 
		self.name = "UNCOOPERATIVE"
		self.definitions = [u'not willing to work with or be helpful to other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
