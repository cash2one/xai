

#calss header
class _PERFUNCTORY():
	def __init__(self,): 
		self.name = "PERFUNCTORY"
		self.definitions = [u'done quickly, without taking care or interest: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
