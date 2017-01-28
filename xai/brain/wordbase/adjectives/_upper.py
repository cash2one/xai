

#calss header
class _UPPER():
	def __init__(self,): 
		self.name = "UPPER"
		self.definitions = [u'at a higher position or level than something else, or being the top part of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
