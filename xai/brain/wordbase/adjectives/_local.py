

#calss header
class _LOCAL():
	def __init__(self,): 
		self.name = "LOCAL"
		self.definitions = [u'from, existing in, serving, or responsible for a small area, especially of a country: ', u'limited to a particular part of the body: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
