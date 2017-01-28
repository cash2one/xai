

#calss header
class _IMMATERIAL():
	def __init__(self,): 
		self.name = "IMMATERIAL"
		self.definitions = [u'not important, or not relating to the subject you are thinking about: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
