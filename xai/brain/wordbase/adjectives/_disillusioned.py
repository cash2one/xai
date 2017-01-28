

#calss header
class _DISILLUSIONED():
	def __init__(self,): 
		self.name = "DISILLUSIONED"
		self.definitions = [u'disappointed and unhappy because of discovering the truth about something or someone that you liked or respected: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
