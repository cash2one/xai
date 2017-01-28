

#calss header
class _INCONTINENT():
	def __init__(self,): 
		self.name = "INCONTINENT"
		self.definitions = [u'unable to control the excretion of urine or the contents of the bowels: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
