

#calss header
class _PRONE():
	def __init__(self,): 
		self.name = "PRONE"
		self.definitions = [u'likely to suffer from an illness or show a particular negative characteristic: ', u'lying face down: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
