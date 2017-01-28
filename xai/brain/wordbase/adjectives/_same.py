

#calss header
class _SAME():
	def __init__(self,): 
		self.name = "SAME"
		self.definitions = [u'exactly like another or each other: ', u'not another different place, time, situation, person, or thing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
