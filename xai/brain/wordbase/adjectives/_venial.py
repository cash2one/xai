

#calss header
class _VENIAL():
	def __init__(self,): 
		self.name = "VENIAL"
		self.definitions = [u'If a wrong action is venial, it is not serious and therefore easy to forgive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
