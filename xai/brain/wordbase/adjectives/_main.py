

#calss header
class _MAIN():
	def __init__(self,): 
		self.name = "MAIN"
		self.definitions = [u'larger, more important, or having more influence than others of the same type: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
