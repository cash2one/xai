

#calss header
class _CHRONIC():
	def __init__(self,): 
		self.name = "CHRONIC"
		self.definitions = [u'(especially of a disease or something bad) continuing for a long time: ', u'very bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
