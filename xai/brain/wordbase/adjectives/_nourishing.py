

#calss header
class _NOURISHING():
	def __init__(self,): 
		self.name = "NOURISHING"
		self.definitions = [u'A nourishing drink or food makes you healthy and strong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
