

#calss header
class _THEREIN():
	def __init__(self,): 
		self.name = "THEREIN"
		self.definitions = [u'in or into a particular place, thing, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
