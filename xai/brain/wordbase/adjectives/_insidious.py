

#calss header
class _INSIDIOUS():
	def __init__(self,): 
		self.name = "INSIDIOUS"
		self.definitions = [u'(of something unpleasant or dangerous) gradually and secretly causing harm: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
