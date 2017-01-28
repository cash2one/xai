

#calss header
class _JAMMED():
	def __init__(self,): 
		self.name = "JAMMED"
		self.definitions = [u'unable to move: ', u'full of people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
