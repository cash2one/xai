

#calss header
class _BINDING():
	def __init__(self,): 
		self.name = "BINDING"
		self.definitions = [u'(especially of an agreement) that cannot be legally avoided or stopped: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
