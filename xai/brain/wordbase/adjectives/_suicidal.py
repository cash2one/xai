

#calss header
class _SUICIDAL():
	def __init__(self,): 
		self.name = "SUICIDAL"
		self.definitions = [u'People who are suicidal want to kill themselves or are in a mental state in which it is likely that they will try to do so: ', u'Suicidal behaviour is likely to result in death: ', u'causing your own defeat or failure: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
