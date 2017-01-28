

#calss header
class _BROODING():
	def __init__(self,): 
		self.name = "BROODING"
		self.definitions = [u'making you feel uncomfortable or worried, as if something bad is going to happen: ', u'feeling sad, worried, or angry for a long time']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
