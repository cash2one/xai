

#calss header
class _ESTIMABLE():
	def __init__(self,): 
		self.name = "ESTIMABLE"
		self.definitions = [u'of a person or their behaviour , considered to be very good or deserving praise: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
