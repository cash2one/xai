

#calss header
class _SYMPTOMATIC():
	def __init__(self,): 
		self.name = "SYMPTOMATIC"
		self.definitions = [u'If something bad is symptomatic of something else, it is caused by the other thing and is proof that it exists: ', u'showing symptoms of a particular disease: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
