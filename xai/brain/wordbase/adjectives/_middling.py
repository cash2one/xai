

#calss header
class _MIDDLING():
	def __init__(self,): 
		self.name = "MIDDLING"
		self.definitions = [u'medium or average; neither very good nor very bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
