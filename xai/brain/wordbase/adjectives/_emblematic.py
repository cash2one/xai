

#calss header
class _EMBLEMATIC():
	def __init__(self,): 
		self.name = "EMBLEMATIC"
		self.definitions = [u'representing a particular person, group, or idea: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
