

#calss header
class _TANTAMOUNT():
	def __init__(self,): 
		self.name = "TANTAMOUNT"
		self.definitions = [u'being almost the same or having the same effect as something, usually something bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
