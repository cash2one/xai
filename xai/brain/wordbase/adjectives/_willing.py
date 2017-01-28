

#calss header
class _WILLING():
	def __init__(self,): 
		self.name = "WILLING"
		self.definitions = [u'to be happy to do something if it is needed: ', u'A willing person does their work energetically and enthusiastically: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
