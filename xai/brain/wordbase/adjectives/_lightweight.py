

#calss header
class _LIGHTWEIGHT():
	def __init__(self,): 
		self.name = "LIGHTWEIGHT"
		self.definitions = [u'weighing only a little or less than average: ', u'not showing deep understanding or knowledge of any subject: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
