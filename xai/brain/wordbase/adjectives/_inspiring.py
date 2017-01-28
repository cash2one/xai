

#calss header
class _INSPIRING():
	def __init__(self,): 
		self.name = "INSPIRING"
		self.definitions = [u'encouraging, or making you feel you want to do something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
