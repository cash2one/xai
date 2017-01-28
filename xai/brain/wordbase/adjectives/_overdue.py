

#calss header
class _OVERDUE():
	def __init__(self,): 
		self.name = "OVERDUE"
		self.definitions = [u'not done or happening when expected or when needed; late: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
