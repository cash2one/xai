

#calss header
class _DEDICATED():
	def __init__(self,): 
		self.name = "DEDICATED"
		self.definitions = [u'believing that something is very important and giving a lot of time and energy to it: ', u'designed to be used for one particular purpose: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
