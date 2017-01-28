

#calss header
class _INHIBITED():
	def __init__(self,): 
		self.name = "INHIBITED"
		self.definitions = [u'not confident enough to say or do what you want: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
