

#calss header
class _RUDIMENTARY():
	def __init__(self,): 
		self.name = "RUDIMENTARY"
		self.definitions = [u'basic: ', u'Rudimentary methods, equipment, systems, or body parts are simple and not very well developed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
